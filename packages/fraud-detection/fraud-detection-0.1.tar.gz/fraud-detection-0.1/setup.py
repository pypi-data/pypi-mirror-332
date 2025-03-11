from setuptools import setup, find_packages

setup(
    name="fraud-detection",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scikit-learn",
        "joblib",
    ],
    author="Trần Minh Tâm",
    author_email="tam.ming.zhan@gmail.com",
    description="AI phát hiện gian lận kế toán",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Trantamming/accounting_fraud_detection",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
