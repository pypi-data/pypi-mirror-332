from setuptools import setup, find_packages

setup(
    name="mycomputelib", #package_name_must_be_unique on PyPI
    version="0.1.0", # package version
    author_email="neerajww@gmail.com",
    description="A simple computation library",
    long_description=open("README.md").read(),
    packages=find_packages(),
    classifier=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">3.8",
)
