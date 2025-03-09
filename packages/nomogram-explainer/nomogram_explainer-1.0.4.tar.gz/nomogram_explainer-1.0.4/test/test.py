from sklearn.preprocessing import LabelEncoder
import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.palettes import Category20
from nomogram_explainer import *

data=pd.read_csv('data_dev_factor_cleaned_remove_space.csv')
#排在第一的label作为哑变量
data['hypertension']=pd.Categorical(data['hypertension'],categories=['No','Yes'],ordered=True)
data['ejection']=pd.Categorical(data['ejection'],categories=['Good','Fair','Poor'],ordered=True)
data['sex']=pd.Categorical(data['sex'],categories=['Male','Female'],ordered=True)
#指定变量的类型，待改进
cat_cols = ['sex', 'hypertension','ejection']
continuous_cols = ['age', 'bmi']
event_col = 'outcome'
var_cols = continuous_cols + cat_cols
ununion_cols=[['sex_Female'],['hypertension_Yes'],['ejection_Poor','ejection_Fair']]
reunion_cols=['sex','hypertension','ejection']

data_label, meta_df, score_df, params_df = prepare_nomogram_data_logistic(data, cat_cols, event_col, var_cols)
#必要的处理，转换变量和计算概率
meta_df,score_df=postprocess(meta_df,score_df,ununion_cols,reunion_cols)

params_df_case,case_data_m=calculate_case_score(params_df,case_data={'age':20,'bmi':25,'sex_Female':1,'hypertension_Yes':1,'ejection_Fair':0,'ejection_Poor':1},ununion_cols=ununion_cols,reunion_cols=reunion_cols)

#fig
fig = plot_nomogram(score_df,data_label,meta_df,params_df_case,
                    prob_range=[0.01,0.1,0.3,0.7,0.9,1],
                    continuous_step_scale={0: 3, 1: 2, 2: 1,'total': 1.5},
                    case_data=case_data_m,
                    color_theme='CNS',symbol_theme='CNS'
                    )
fig.show()


# print(case_data)
# plot_waterfall_chart(params_df,margin_right=10)
# plot_horizontal_bar_chart_of_averages(score_df.loc[:,var_cols],margin_right=10)
# print(params_df.T)



    #------------------------------------------cox-------------------------------------------------------
    #读取数据cox
    # data=pd.read_csv('heart_failure.csv')
    # #处理分类变量
    # data['anaemia']=pd.Categorical(data['anaemia'],categories=[0,1],ordered=True)
    # data['diabetes']=pd.Categorical(data['diabetes'],categories=[0,1],ordered=True)
    # data['high_blood_pressure']=pd.Categorical(data['high_blood_pressure'],categories=[0,1],ordered=True)
    # data['sex']=pd.Categorical(data['sex'],categories=[0,1],ordered=True)
    # data['smoking']=pd.Categorical(data['smoking'],categories=[0,1],ordered=True)
    # #指定需要的变量
    # cat_cols = ['sex', 'anaemia','diabetes','high_blood_pressure','smoking']
    # continuous_cols = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 'serum_creatinine', 'serum_sodium']
    # time_col = 'time'
    # event_col = 'DEATH_EVENT'
    # var_cols = continuous_cols + cat_cols
    # #计算数据
    # data_label, meta_df, score_df, params_df,cph,data_onehot = prepare_nomogram_data_cox(data, cat_cols, event_col, time_col, var_cols)
    # #后处理
    # ununion_cols=[['sex_1'],['anaemia_1'],['diabetes_1'],['high_blood_pressure_1'],['smoking_1']]
    # reunion_cols=['sex','anaemia','diabetes','high_blood_pressure','smoking']
    # meta_df,score_df=postprocess(meta_df,score_df,ununion_cols,reunion_cols,cox=True,specific_times=[30,60],cox_model=cph,data_onehot_cox=data_onehot)
    # #计算个案数据
    # case_data={'age':60,'creatinine_phosphokinase':40,'ejection_fraction':50,'serum_creatinine':1,'serum_sodium':120,'sex_1':1,'anaemia_1':1,'diabetes_1':1,'high_blood_pressure_1':1,'smoking_1':1}
    # params_df_case,case_data=calculate_case_score(params_df,case_data=case_data,ununion_cols=ununion_cols,reunion_cols=reunion_cols,cox=True,cox_model=cph,specific_times=[30,60])
    
    # #绘制列线图
    # fig = plot_nomogram(score_df,data_label,meta_df,params_df_case,
    #                     prob_range=[0.1,0.2,0.3,0.6,0.9],
    #                     cox=True,cox_model=cph,specific_times=[30,60],
    #                     continuous_step_scale={0: 3, 1: 1000, 2: 2,3:1,4:5,'total': 2},# modify the scale density of continuous variables
    #                     case_data=case_data,
    #                     color_theme='CNS',symbol_theme='CNS'
    #                     )
    # fig.show()
    # plot_horizontal_bar_chart_of_averages(meta_df[var_cols])
    # plot_horizontal_bar_chart_of_averages(score_df[var_cols],margin_right=5)

    # plot_waterfall_chart(params_df_case,type='meta',cox=True,cox_model=cph)
    # plot_waterfall_chart(params_df_case,type='score',cox=True,cox_model=cph,margin_right=15,margin_left=0.5)