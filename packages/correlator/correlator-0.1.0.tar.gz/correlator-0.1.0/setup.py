from setuptools import setup, find_packages

setup(
    name="correlator",
    version="0.1.0",
    author="Kasper Arfman",
    author_email="kasper.arf@gmail.com",
    description="A simple hello world package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Kasper-Arfman/kasper",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "kasper=kasper.main:hello",
        ],
    },
)
