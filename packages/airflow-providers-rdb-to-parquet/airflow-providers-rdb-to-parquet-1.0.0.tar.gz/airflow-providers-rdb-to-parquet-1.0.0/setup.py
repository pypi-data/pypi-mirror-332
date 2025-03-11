from setuptools import find_packages, setup

setup(
    name="airflow-providers-rdb-to-parquet",
    version="1.0.0",
    author="Hazel Liu",
    author_email="hazel.liu@crypto.com",
    description="Custom Airflow Operator to extract data from PostgreSQL, convert it to Parquet format, and upload to S3.",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "pyarrow",
        "apache-airflow",
        "boto3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Apache Airflow",
        "License :: OSI Approved :: MIT License",
    ],
)
