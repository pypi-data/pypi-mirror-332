
from sklearn.preprocessing import LabelEncoder
import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.palettes import Category20
from sklearn.preprocessing import LabelEncoder
from lifelines import CoxPHFitter


def prepare_nomogram_data_logistic(data, categorical_columns, event_column, variable_columns):
    """Prepare data for nomogram plotting by encoding categorical variables, 
    computing the linear model parameters, and calculating the score data."""
    data_label = data.loc[:, variable_columns]
    data_onehot = pd.get_dummies(data_label, columns=categorical_columns, drop_first=True, dtype=int)
    updated_variable_columns = data_onehot.columns.tolist()

    event_label_encoder = LabelEncoder()
    data_onehot[event_column] = event_label_encoder.fit_transform(data[event_column])
    formula = event_column + '~' + '+'.join(updated_variable_columns)
    model_logit = smf.logit(formula, data_onehot).fit()
    model_logit_params = model_logit.params
    print(model_logit_params)

    params = model_logit_params.values
    columns = model_logit_params.index.tolist()

    meta_df = data_onehot.loc[:, columns[1:]]
    meta_df['Intercept'] = np.repeat(1, meta_df.shape[0])

    for col, beta in zip(columns, params):
        meta_df[col] = [x * beta for x in meta_df[col]]

    max_distance = np.max((meta_df[columns].max() - meta_df[columns].min()).values)
    score_df = meta_df.copy()[columns]
    for col in columns:
        score_df[col] = (meta_df[col] - meta_df[col].min()) * 100 / max_distance

    params_df = pd.DataFrame(params, index=columns, columns=['coefficient'])
    params_df['min_xbeta'] = meta_df[columns].min()
    params_df['max_distance'] = np.repeat(max_distance, params_df.shape[0])

    return data_label, meta_df, score_df, params_df



def prepare_nomogram_data_cox(data, categorical_columns, event_column, time_column, variable_columns):
    """
    Prepare data for nomogram plotting by encoding categorical variables, 
    computing the Cox model parameters, and calculating the score data.
    
    :param data: 输入的DataFrame数据
    :param categorical_columns: 分类变量列名列表
    :param time_column: 生存时间列名
    :param event_column: 事件发生列名
    :param variable_columns: 自变量列名列表
    :return: 处理后的数据和参数
    """
    # 提取自变量数据
    data_label = data.loc[:, variable_columns]
    # 对分类变量进行独热编码
    data_onehot = pd.get_dummies(data_label, columns=categorical_columns, drop_first=True, dtype=int)
    updated_variable_columns = data_onehot.columns.tolist()

    # 添加生存时间和事件发生列
    data_onehot[time_column] = data[time_column]
    data_onehot[event_column] = data[event_column]

    # 拟合Cox比例风险回归模型
    cph = CoxPHFitter()
    cph.fit(data_onehot, duration_col=time_column, event_col=event_column)
    model_cox_params = cph.params_
    print(model_cox_params)

    params = model_cox_params.values
    columns = model_cox_params.index.tolist()
    
    
    data_onehot=data_onehot.loc[:,columns]
    meta_df = data_onehot.loc[:, columns]
    # meta_df['Intercept'] = np.repeat(1, meta_df.shape[0])

    # 计算每个变量的线性组合值
    for col, beta in zip(columns, params):
        meta_df[col] = [x * beta for x in meta_df[col]]

    # 计算最大距离
    max_distance = np.max((meta_df[columns].max() - meta_df[columns].min()).values)
    score_df = meta_df.copy()[columns]

    # 计算得分
    for col in columns:
        score_df[col] = (meta_df[col] - meta_df[col].min()) * 100 / max_distance

    # 创建参数DataFrame
    params_df = pd.DataFrame(params, index=columns, columns=['coefficient'])
    params_df['min_xbeta'] = meta_df[columns].min()
    params_df['max_distance'] = np.repeat(max_distance, params_df.shape[0])

    return data_label, meta_df, score_df, params_df, cph, data_onehot

def calculate_case_score(params_df, case_data=None,ununion_cols=None,reunion_cols=None,cox=False,cox_model=None,specific_times=None):
    if case_data is None:
        case_data = {'age': 20, 'bmi': 25, 'sex_Female': 1, 'hypertension_Yes': 1, 'ejection_Fair': 0, 'ejection_Poor': 1}
    if cox:
        case_data_df=pd.DataFrame(case_data,index=[0])
        params_df['case_value'] = [case_data.get(col, 0) for col in params_df.index]
        params_df['case_xbeta'] = params_df['coefficient'] * params_df['case_value']
        params_df['case_score'] = (params_df['case_xbeta'] - params_df['min_xbeta']) * 100 / params_df['max_distance']
        if ununion_cols is not None:
            params_df= _reunite_categorical_columns(params_df.T,ununion_cols,reunion_cols).T
        case_data['total_xbeta'] =  params_df['case_xbeta'].sum()
        case_data['total_score'] = params_df['case_score'].sum()
        for time in specific_times:
            case_data['risk_prob_{}'.format(time)] = cox_model.predict_cumulative_hazard(case_data_df, times=time).T.values[0][0]
            case_data['surivival_prob_{}'.format(time)] = cox_model.predict_survival_function(case_data_df, times=time).T.values[0][0]
    else:
    # Ensure the intercept term is included
        case_data['Intercept'] = 1

        # Calculate xbeta and score for each parameter
        params_df['case_value'] = [case_data.get(col, 0) for col in params_df.index]
        params_df['case_xbeta'] = params_df['coefficient'] * params_df['case_value']
        params_df['case_score'] = (params_df['case_xbeta'] - params_df['min_xbeta']) * 100 / params_df['max_distance']
        if ununion_cols is not None:
            params_df= _reunite_categorical_columns(params_df.T,ununion_cols,reunion_cols).T
        # Calculate total xbeta, total score, and probability
        case_data['total_xbeta'] = params_df['case_xbeta'].sum()
        case_data['total_score'] = params_df['case_score'].sum()
        case_data['probability'] = 1 / (1 + np.exp(-case_data['total_xbeta']))

    return params_df, case_data

def _reunite_categorical_columns(df, ununion_cols, reunion_cols):
    """
    Reunite categorical columns by summing them up.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame.
    ununion_cols : list of lists
        List of lists, where each inner list contains categorical columns that
        should be summed up into one column.
    reunion_cols : list
        List of column names for the reunited categorical columns.

    Returns
    -------
    df_reunion : pandas.DataFrame
        Output DataFrame with reunited categorical columns.
    """
    for i, ununion_col in enumerate(ununion_cols):
        if len(ununion_col) > 1:
            df[reunion_cols[i]] = df[ununion_col].sum(axis=1)
        else:
            df[reunion_cols[i]] = df[ununion_col[0]]
    ununion_cols_flat = [col for group in ununion_cols for col in group]
    df_reunion = df.drop(ununion_cols_flat, axis=1)

    return df_reunion

def postprocess(meta_df, score_df,ununion_cols=None, reunion_cols=None,cox=False, specific_times=None,cox_model=None,data_onehot_cox=None):
    """Post-processing of meta and score DataFrames."""
    
    if cox:
        if ununion_cols is not None:
            meta_df = _reunite_categorical_columns(meta_df, ununion_cols, reunion_cols)
            score_df = _reunite_categorical_columns(score_df, ununion_cols, reunion_cols)
        meta_df['total'] = meta_df.sum(axis=1)
        score_df['total'] = score_df.sum(axis=1)
        specific_times=specific_times
        for time in specific_times:
            meta_df['risk_prob_{}'.format(time)] = cox_model.predict_cumulative_hazard(data_onehot_cox, times=time).T.values
            meta_df['surivival_prob_{}'.format(time)] = cox_model.predict_survival_function(data_onehot_cox, times=time).T.values
            score_df['risk_prob_{}'.format(time)] = meta_df['risk_prob_{}'.format(time)]
            score_df['surivival_prob_{}'.format(time)] = meta_df['surivival_prob_{}'.format(time)]

    else:
        # Reunite categorical columns
        if ununion_cols is not None:
            meta_df = _reunite_categorical_columns(meta_df, ununion_cols, reunion_cols)
            score_df = _reunite_categorical_columns(score_df, ununion_cols, reunion_cols)
        # Calculate total and probability
        meta_df['total'] = meta_df.sum(axis=1)
        meta_df['probability'] = 1 / (1 + np.exp(-meta_df['total']))
        score_df['total'] = score_df.sum(axis=1)
        score_df['probability'] = meta_df['probability']
        

    return meta_df, score_df
    

def plot_nomogram(score_df, data_label, meta_df, params_df_case, prob_range=None, case_data=None,cox=False, specific_times=None,cox_model=None,
                  continuous_step_scale={0: 3, 1: 2, 2: 1,'total':1.5}, space_between_lines=3,fig_width=800, fig_height=600, color_theme='classic',symbol_theme='classic'):
    # 定义不同的颜色主题
    color_themes = {
        'classic': {
            'scale': 'black',
            'variable': 'black',
            'total': 'black',
            'case': 'black'
        },
        'CNS': {
            'scale': '#0072B2',
            'variable': '#D55E00',
            'total': '#009E73',
            'case': '#CC79A7'
        },
        'dark': {
            'scale': '#2c3e50',
            'variable': '#e74c3c',
            'total': '#27ae60',
            'case': '#9b59b6'
        },
        'cool': {
            'scale': '#00FFFF',
            'variable': '#FF1493',
            'total': '#FFD700',
            'case': '#8A2BE2'
        }
    }
    
    # 定义不同的symbol主题
    symbol_themes = {
        'classic': {
            'scale': '142',
            'variable': '142',
            'total': '142',
            'case': 'star'
        },
        'CNS': {
        'scale': 'circle',
        'variable': 'square',
        'total': 'diamond',
        'case': 'star'
        },
        'cool': {
        'scale': 'hourglass',
        'variable': 'diamond-tall',
        'total': 'star-square',
        'case': 'star'
    }
    }

    # 获取所选主题的颜色和symbol
    colors = color_themes.get(color_theme, color_themes['classic'])
    symbols = symbol_themes.get(symbol_theme, symbol_themes['classic'])

    if prob_range is None:
        prob_range = [0, 0.1, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

  
    fig = go.Figure().set_subplots(rows=3, cols=2, vertical_spacing=0.01,
                                   horizontal_spacing=0.01, column_widths=[0.2, 0.8],
                                   row_heights=[0.1, 0.6, 0.2])
    fig.update_yaxes(autorange=False, visible=False)
    fig.update_xaxes(visible=False)
    fig.update_yaxes(row=1, range=[2, 4])
    fig.update_yaxes(row=2, range=[4 - data_label.columns.shape[0] * space_between_lines, 4.5])
    if specific_times is None:
        fig.update_yaxes(row=3, range=[1 - space_between_lines, 4.5])
    else:
        fig.update_yaxes(row=3, range=[1-len(specific_times)*space_between_lines, 4.5])

    fig.update_xaxes(row=1, col=2, range=[-5, 105])
    fig.update_xaxes(row=2, col=2, range=[-5, 105])
    fig.update_xaxes(row=3, col=2, range=[-5, max(score_df['total']) * 1.2])
    fig.update_layout(width=fig_width, height=fig_height, showlegend=False, paper_bgcolor="#ffffff", plot_bgcolor="#ffffff")

    # Draw the 100-point scale
    fig.add_trace(go.Scatter(mode='lines+markers', y=np.repeat(3, 21), x=np.arange(0, 105, 5),
                             marker={'symbol': symbols['scale'], "color": colors['scale'], 'size': 15}), row=1, col=2)

    # Draw minor ticks
    fig.add_trace(go.Scatter(mode='lines+markers', x=np.arange(0, 101), y=np.repeat(3, 101),
                             marker={'symbol': symbols['scale'], 'color': colors['scale']}), row=1, col=2)

    # Draw data labels
    fig.add_trace(go.Scatter(mode='text', x=np.arange(0, 105, 5), y=np.repeat(3.5, 21),
                             text=np.arange(0, 105, 5)), row=1, col=2)

    # Draw left-side label
    fig.add_trace(go.Scatter(mode='text', x=[-3], y=[3], text='Points'), row=1, col=1)

    # Variables
    for i, col in enumerate(data_label.columns):
        if data_label[col].dtype.kind in 'if':
            step = score_df[col].max() / (data_label[col].max() - data_label[col].min())
            text = [int(x) for x in np.arange(np.floor(min(data_label[col])), np.floor(max(data_label[col]) + continuous_step_scale[i]), continuous_step_scale[i])]
            if meta_df[col].min() < 0:
                text = text[::-1]
            x_range = np.arange(0, score_df[col].max() + continuous_step_scale[i] * step, continuous_step_scale[i] * step)

            fig.add_trace(go.Scatter(mode='lines+markers', y=np.repeat(3 - space_between_lines * i, len(x_range)), x=x_range,
                                     marker={'symbol': symbols['variable'], "color": colors['variable']}), row=2, col=2)

            fig.add_trace(go.Scatter(mode='text', x=x_range, y=np.repeat(3.5 - space_between_lines * i, len(x_range)), text=text),
                          row=2, col=2)

            fig.add_trace(go.Scatter(mode='text', x=[-3], y=[3 - space_between_lines * i], text=col, textfont=dict(size=10)), row=2, col=1)

            if case_data is not None:
                fig.add_trace(go.Scatter(mode='markers', y=[3 - space_between_lines * i], x=[params_df_case.T.loc['case_score'].loc[col]],
                                         marker={'symbol': symbols['case'], "color": colors['case'], 'size': 10}), row=2, col=2)

        if data_label[col].dtype.kind in 'O':
            x_range = np.unique(score_df[col])
            text = data_label[col].unique()
            if meta_df[col].min() < 0:
                text = text[::-1]

            fig.add_trace(go.Scatter(mode='lines+markers', y=np.repeat(3 - space_between_lines * i, len(x_range)), x=x_range,
                                     marker={'symbol': symbols['variable'], "color": colors['variable']}), row=2, col=2)

            fig.add_trace(go.Scatter(mode='text', x=x_range, y=np.repeat(3.5 - space_between_lines * i, len(x_range)), text=text),
                          row=2, col=2)

            fig.add_trace(go.Scatter(mode='text', x=[-3], y=[3 - space_between_lines * i], text=col, textfont=dict(size=10)), row=2, col=1)
            if case_data is not None:
                fig.add_trace(go.Scatter(mode='markers', y=[3 - space_between_lines * i], x=[params_df_case.T.loc['case_score'].loc[col]],
                                         marker={'symbol': symbols['case'], "color": colors['case'], 'size': 10}), row=2, col=2)

    # Total score
    step_total = (score_df['total'].max() - score_df['total'].min()) / 20
    x_total_range = np.arange(score_df['total'].min() * 0.8, max(score_df['total']) * 1.1, step_total*continuous_step_scale['total'])
    fig.add_trace(go.Scatter(mode='lines+markers', y=np.repeat(3, len(x_total_range)), x=x_total_range,
                             marker={'symbol': symbols['total'], "color": colors['total'], 'size': 15}), row=3, col=2)

    fig.add_trace(go.Scatter(mode='text', x=x_total_range, y=np.repeat(3.5, len(x_total_range)),
                             text=x_total_range.round(0)), row=3, col=2)

    fig.add_trace(go.Scatter(mode='text', x=[-3], y=[3], text='Total'), row=3, col=1)

    if case_data is not None:
        fig.add_trace(go.Scatter(mode='markers', y=[3], x=[case_data['total_score']],
                                 marker={'symbol': symbols['case'], "color": colors['case'], 'size': 10}), row=3, col=2)

    # Probability
    if cox:
        for i,time in enumerate(specific_times):
            x_proba_range, proba_text_label = [], []
            for p in prob_range:
                proba_closest = max(score_df[score_df[f'risk_prob_{time}'] <= p][f'risk_prob_{time}'], default=None)
                if proba_closest is not None:
                    label = round(proba_closest, 2)
                    value = score_df[score_df[f'risk_prob_{time}'] == proba_closest]['total']
                    x_proba_range.append(value)
                    proba_text_label.append(label)

            x_proba_range, proba_text_label = np.unique(x_proba_range), np.unique(proba_text_label)
            
            fig.add_trace(go.Scatter(mode='lines+markers', y=np.repeat(3-space_between_lines-space_between_lines*i, len(x_proba_range)), x=x_proba_range,
                                    marker={'symbol': symbols['total'], "color": colors['total']}), row=3, col=2)

            fig.add_trace(go.Scatter(mode='text', x=x_proba_range, y=np.repeat(3.5-space_between_lines-space_between_lines*i, len(x_proba_range)),
                                    text=proba_text_label), row=3, col=2)

            fig.add_trace(go.Scatter(mode='text', x=[-3], y=[3-space_between_lines-space_between_lines*i], text=f'risk_prob_{time}'), row=3, col=1)

            if case_data is not None:
                fig.add_trace(go.Scatter(mode='markers', y=[3-space_between_lines-space_between_lines*i], x=[case_data['total_score']],
                                        marker={'symbol': symbols['case'], "color": colors['case'], 'size': 10}), row=3, col=2)
    else:    
        x_proba_range, proba_text_label = [], []
        for p in prob_range:
            proba_closest = max(score_df[score_df['probability'] <= p]['probability'], default=None)
            if proba_closest is not None:
                label = round(proba_closest, 2)
                value = score_df[score_df['probability'] == proba_closest]['total']
                x_proba_range.append(value)
                proba_text_label.append(label)

        x_proba_range, proba_text_label = np.unique(x_proba_range), np.unique(proba_text_label)
        
        fig.add_trace(go.Scatter(mode='lines+markers', y=np.repeat(3-space_between_lines, len(x_proba_range)), x=x_proba_range,
                                marker={'symbol': symbols['total'], "color": colors['total']}), row=3, col=2)

        fig.add_trace(go.Scatter(mode='text', x=x_proba_range, y=np.repeat(1.5, len(x_proba_range)),
                                text=proba_text_label), row=3, col=2)

        fig.add_trace(go.Scatter(mode='text', x=[-3], y=[3-space_between_lines], text='Probability'), row=3, col=1)

        if case_data is not None:
            fig.add_trace(go.Scatter(mode='markers', y=[3-space_between_lines], x=[case_data['total_score']],
                                    marker={'symbol': symbols['case'], "color": colors['case'], 'size': 10}), row=3, col=2)

    return fig

def plot_waterfall_chart(params_df_case, title='Waterfall Chart', type='score',x_axis_label="数值",
                         y_axis_label="项目",width=800,cox=False,cox_model=None,margin_left=0.2,margin_right=3):
    """Plot a waterfall chart of the score changes."""
    
    if cox:
        if type == 'score':
            start_value = 0
            changes=params_df_case.loc[params_df_case.index, 'case_score'].values
        elif type == 'meta':
            start_value = cox_model.baseline_hazard_.iloc[0,0]
            changes=params_df_case.loc[params_df_case.index, 'case_xbeta'].values
        labels = params_df_case.index.tolist()
    else:
    # Get the starting value
        if type == 'score':   
            start_value = params_df_case.loc['Intercept', 'case_score']

            # Get the changes and labels, excluding 'Intercept'
            changes = params_df_case.loc[params_df_case.index != 'Intercept', 'case_score'].values
            labels = params_df_case.loc[params_df_case.index != 'Intercept', 'case_score'].index.tolist()
        elif type == 'meta':
            start_value = params_df_case.loc['Intercept', 'case_xbeta']
            changes = params_df_case.loc[params_df_case.index != 'Intercept', 'case_xbeta'].values
            labels = params_df_case.loc[params_df_case.index != 'Intercept', 'case_xbeta'].index.tolist()

    # Calculate the cumulative values
    cumulative_values = np.cumsum([start_value] + list(changes))

    # Prepare the data
    data = {
        'y': list(range(len(labels) + 2)),
        'left': [0] + list(cumulative_values[:-1]) + [0],
        'right': [start_value] + list(cumulative_values[:-1] + changes) + [cumulative_values[-1]],
        'colors': ['blue'] + ['green' if x >= 0 else'red' for x in changes] + ['blue'],
        'labels': ['起始'] + labels + ['最终'],
        'change_values': [round(start_value, 2)] + [round(x, 2) for x in changes] + [round(cumulative_values[-1], 2)]
    }

    source = ColumnDataSource(data)
    # 找到 x 轴的最大值
    max_x_value = max(data['right'])

    # Create the plot with adjusted x_range
    p = figure(title=title, x_axis_label=x_axis_label, y_axis_label=y_axis_label, width=width,
               toolbar_location="right", tools="pan,box_zoom,reset,save",
               x_range=(min(data['left'])-margin_left, max_x_value + margin_right))


    # Add the horizontal bar chart
    p.hbar(y='y', right='right', left='left', height=0.8, color='colors', source=source)

    # Add labels to display the item names
    labels = LabelSet(x='right', y='y', text='labels', level='glyph',
                      x_offset=5, y_offset=0, source=source, text_font_size='10pt')
    p.add_layout(labels)

    # Add labels to display the change values
    value_labels = LabelSet(x='right', y='y', text='change_values', level='glyph',
                            x_offset=5, y_offset=15, source=source, text_font_size='12pt', text_color='black')
    p.add_layout(value_labels)

    # Show the plot
    show(p)


def plot_horizontal_bar_chart_of_averages(data_frame, title="Important Summary",
                                          x_axis_label='Average Value',
                                          y_axis_label='Variables', width=800,
                                          sort_ascending=True,margin_left=0.1,margin_right=0.5):
 

    # Calculate the averages of the given columns
    columns_to_calculate = [column for column in data_frame.columns]
    averages = data_frame[columns_to_calculate].mean()

    # Sort the averages in the given order
    sorted_index = averages.abs().sort_values(ascending=sort_ascending).index
    averages = averages[sorted_index]

    # Prepare the data
    source = ColumnDataSource(data=dict(
        variables=averages.index.tolist(),
        averages=averages.values.round(2),
        colors=Category20[len(averages)]
    ))
    
    max_x_value = averages.max()
    min_x_value = averages.min()

    # Create the plot
    p = figure(y_range=averages.index.tolist(), title=title,
               toolbar_location="right", tools="pan,box_zoom,reset,save", width=width,
               x_axis_label=x_axis_label, y_axis_label=y_axis_label,
               x_range=(min_x_value - margin_left, max_x_value + margin_right))

    # Add the horizontal bar chart
    p.hbar(y='variables', right='averages', height=0.8, source=source,
           line_color='white', fill_color='colors')

    # Add the average values as labels
    labels = LabelSet(x='averages', y='variables', text='averages', level='glyph',
                      x_offset=5, y_offset=0, source=source, text_font_size='10pt')
    p.add_layout(labels)

    # Show the plot
    show(p)

