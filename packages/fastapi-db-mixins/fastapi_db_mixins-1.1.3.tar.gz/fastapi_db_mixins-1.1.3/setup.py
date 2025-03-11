from setuptools import setup, find_packages

setup(
    name="fastapi-db-mixins",
    version="1.1.3",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy",
    ],
    description="FastAPI database mixins"
)