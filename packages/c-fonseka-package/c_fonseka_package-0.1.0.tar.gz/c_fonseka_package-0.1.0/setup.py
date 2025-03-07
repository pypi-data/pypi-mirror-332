from setuptools import setup, find_packages

setup(
    name="c_fonseka_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Crosper fonseka",
    author_email="your.email@example.com",
    description="A Python package with a submodule",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/c_fonseka_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
