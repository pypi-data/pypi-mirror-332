from setuptools import setup, find_packages

setup(
    name="JsonCreatoor",
    version="0.0.1",
    author="Gennadiy",
    author_email="genkaprostotak@gmail.com",
    description="Json library creator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.10.0",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "hatchling",
    ],
)
