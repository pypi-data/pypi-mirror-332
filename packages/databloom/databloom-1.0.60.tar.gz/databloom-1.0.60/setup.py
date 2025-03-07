from setuptools import setup, find_packages
# with open("README.md", "r") as fh:
#     long_description = fh.read()

version = "1.0.60"

setup(
    name="databloom",
    version=version,
    author="gada121982",
    author_email="gada121982@gmail.com",
    description="A small example package",
    long_description="In progress",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'v1': ["v1/*"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pandas>=2.2.3",
        "psycopg2-binary>=2.9.10",
        "mysql-connector-python>=9.2.0",
        "mysqlclient>=2.2.7",
        "sqlalchemy>=2.0.38",
        "trino>=0.333.0",
        "pyspark>=3.5.1"
    ]
)
