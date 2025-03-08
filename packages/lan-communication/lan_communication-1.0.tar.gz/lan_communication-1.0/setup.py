from setuptools import setup, find_packages

setup(
    name="lan_communication",
    version="1.0",
    author="Hakim Adiche",
    author_email="adiche@kfupm.edu.sa",
    description="A Python package for enabling communication between two hosts using sockets.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
)
