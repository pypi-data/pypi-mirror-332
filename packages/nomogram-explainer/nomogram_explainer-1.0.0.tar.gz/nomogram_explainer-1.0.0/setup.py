from setuptools import setup, find_packages

# 读取 requirements.txt 文件获取依赖项
with open('requirements.txt', 'r', encoding='utf-8') as f:
    install_requires = f.read().splitlines()

# 读取 README.md 文件作为长描述
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nomogram-explainer',
    version='1.0.0',
    author='Jeffery Liu',
    description='Drawing the nomogram with python, and explain the model with nomogram-drived data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email='liuyp2080@gmail.com',
    url='https://github.com/liuyp2080/pynomogram-explainer',
    license='MIT',
    include_package_data=True,
    package_dir={},  # 当代码在项目根目录时，设置为空字典
    packages=find_packages(),  # 不指定 where 参数，默认从当前目录查找包
    install_requires=install_requires,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    python_requires=">=3.10"
)