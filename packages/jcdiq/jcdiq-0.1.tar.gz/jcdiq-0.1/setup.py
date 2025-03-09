from setuptools import setup, find_packages

setup(
    name='jcdiq',  # 项目名称
    version='0.1',      # 版本号
    package_dir={'': 'src'},  # 指定包的根目录为 src
    packages=find_packages(where='src'),  # 从 src 目录查找包
    install_requires=[  # 依赖项
        'requests>=2.25.1',
    ],
    author='jiacheng',
    author_email='libo@jiachengnet.com',
    description='jcdiq project for python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://jiachengnet.com/example',  # 项目主页
    license='Commercial',  # 商业许可
    python_requires='>=3.6',  # Python 版本要求
)