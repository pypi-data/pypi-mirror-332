from setuptools import setup, find_packages

setup(
    name="tamil_stemmer-advanced-0.1.2",  # Package name
    version="0.1.2",  # Increment version
    description="A simple Tamil word stemmer",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Pavithra Harini Sivakumar",
    author_email="pavitra040604@gmail.com",
    packages=["tamil_stemmer"],  # Explicitly specify the package
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Tamil",
    ],
    python_requires=">=3.6",
)
