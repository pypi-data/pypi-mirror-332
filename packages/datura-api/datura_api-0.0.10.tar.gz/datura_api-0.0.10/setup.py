from setuptools import setup, find_packages

setup(
    name="datura_api",
    version="0.0.6",
    description="A Python SDK for interacting with the My API service.",
    author="Your Name",
    author_email="your.email@example.com",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
