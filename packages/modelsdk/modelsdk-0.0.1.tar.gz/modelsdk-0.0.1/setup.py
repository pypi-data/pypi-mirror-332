from setuptools import setup, find_packages

setup(
    name="modelsdk",
    version="0.0.1",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "numpy",
        "flask",
        "pandas",
        "db-dtypes==1.1.1",
        "gunicorn==22.0.0",
        "google-cloud-bigquery==3.10.0",
    ],
    extras_require={"dev": ["build>=0.8.0", "twine>=4.0.0"]},
    description="A flexible SDK for interacting with various models",
)
