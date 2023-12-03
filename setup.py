from setuptools import setup, find_packages

# 从 requirements.txt 读取依赖项
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='fluhp',
    version='1.0.0',
    author='Lihuirull',
    author_email='ssdx202203@163.com',
    description='A tool for predicting influenza virus hosts from sequence data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lihuirull/test2',
    packages=find_packages(),
    include_package_data=True,  # 包含 MANIFEST.in 中指定的非代码文件
    entry_points={
        'console_scripts': [
            'fluhp=fluhp.fluhp:main',  # 指向 src/fluhp/fluhp.py 中的 main 函数
        ],
    },
    package_data={
        '': ['data/*.*', 'model/*.*','tests/*.*'],  # 包含 data 和 model 目录中的文件
    },
   
    install_requires=required,
    zip_safe=False,
 
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    keywords='influenza host prediction bioinformatics',
)
