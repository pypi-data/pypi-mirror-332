from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="example_package_clarenceh",  # Replace with your package name
    version="0.1.0",
    author="Clarence Ho",  # Replace with your name
    author_email="ho.clarence@gmail.com",  # Replace with your email
    description="A simple example Python SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-simple-sdk",  # Replace with your GitHub URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choose a license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',  # Specify minimum Python version
)
