from setuptools import setup, find_packages

setup(
    name='mysql_f',  # 包名，将在 PyPI 上显示
    version='0.1.1',  # 版本号
    description='A Python library for efficient MySQL database operations with connection pooling and optimization.',  # 包的简短描述
    long_description=open('README.md', encoding='utf-8').read(),  # 详细描述，通常从 README.md 文件中读取
    long_description_content_type='text/markdown',  # 详细描述的内容类型
    author='fjh',  # 作者名
    author_email='2449579731@qq.com',  # 作者邮箱
    url='https://github.com/cxfjh/mysql_f',  # 项目主页，通常是 GitHub 仓库
    packages=find_packages(),  # 自动查找包
    install_requires=[  # 依赖项
        'mysqlclient>=2.1.0',  # MySQLdb 的依赖
        'dbutils>=3.0.0',  # PooledDB 的依赖
    ],
    classifiers=[  # 分类器，帮助用户找到你的包
        'Development Status :: 3 - Alpha',  # 开发状态
        'Intended Audience :: Developers',  # 目标受众
        'License :: OSI Approved :: MIT License',  # 许可证
        'Programming Language :: Python :: 3',  # 支持的 Python 版本
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',  # 支持的 Python 版本范围
)