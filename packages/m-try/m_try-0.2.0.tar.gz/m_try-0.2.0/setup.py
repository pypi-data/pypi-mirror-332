from setuptools import setup, find_packages

setup(
    name="m_try",
    version="0.2.0",
    author="你的名字",
    author_email="dickyzzx@gmail.com",
    description="一个数学计算的 Python 库",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/你的github/m_try",
    packages=["m_try"],  # 直接指定 m_try 目录
    package_dir={"m_try": "m_try"},  # 明确指定 m_try 目录的位置
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)