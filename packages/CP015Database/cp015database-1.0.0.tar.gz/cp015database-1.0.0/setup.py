from setuptools import setup, find_packages

setup(
    name="CP015Database",
    version="1.0.0",  # Change this when updating
    packages=find_packages(),
    install_requires=[
        "mysql-connector-python",
    ],
    author="Muhammad Aiman",
    description="A simple database handler package for CP015 Matriculation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
