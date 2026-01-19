from setuptools import setup, find_packages


setup(
    name="optativa_pycicd_bdd",
    version="1.0.0",
    author="Blagovest Doukov Dimitrova",
    author_email="dandeline544@gmail.com",
    description="Proyecto de blagovest",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "flake8",
    ],
)
