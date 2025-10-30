from setuptools import setup, find_packages

setup(
    name="proyecto_integrador",
    version="0.0.1",
    author="Andres Callejas",
    author_email="andres.callejas@iudigital.edu.co",
    description="Proyecto integrador",
    py_modules=["proyecto_integrador"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4",
        "matplotlib",
        "kagglehub[pandas-datasets]>=0.3.8",
        "seaborn",
        "pyarrow"
    ]
)