from setuptools import setup, find_packages

setup(
    name="encode-decode-shahed",  # The new unique package name
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="MD Shahed Rahman",
    author_email="shahedrahmanltd@gmail.com",
    description="A simple encoding and decoding package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shahedltd/encode_decode",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
