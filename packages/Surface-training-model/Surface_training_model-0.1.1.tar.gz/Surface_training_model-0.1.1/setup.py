from setuptools import setup, find_packages
setup(
    name="Surface_training_model",  # 你的包名
    version="0.1.1",    # 版本号
    author="Dongfang Fan",
    author_email="2300541001@email.szu.edu.cn",
    description="SHARAD surface echo extraction model training package based on deep learning",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),  # 自动查找包
    install_requires=[
        "numpy",  # 依赖项
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 兼容的 Python 版本
)
