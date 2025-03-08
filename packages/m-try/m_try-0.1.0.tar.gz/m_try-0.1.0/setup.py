from setuptools import setup, find_packages

setup(
    name="m_try",  # 你的包的名字（别人 `pip install m_try` 时用）
    version="0.1.0",  # 版本号
    author="你的名字",  # 你的名字
    author_email="dickyzzx@gmail.com",  # 你的邮箱
    description="一个数学计算的 Python 库",  # 介绍你的包
    long_description=open("README.md", encoding="utf-8").read(),  # 详细介绍
    long_description_content_type="text/markdown",
    url="https://github.com/你的github/m_try",  # 你的 GitHub（可选）
    packages=find_packages(),  # 自动查找所有 Python 模块
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)