from setuptools import setup, find_packages

setup(
    name="andrey_misis-mlops2024",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        line.strip() for line in open("requirements.txt").readlines() if not line.startswith("#")
    ],
    author="Andrey Laptev",
    author_email="alaptev@gmail.com",
    description="MLOps course project",
    keywords="mlops, machine learning",
    python_requires=">=3.12",
)