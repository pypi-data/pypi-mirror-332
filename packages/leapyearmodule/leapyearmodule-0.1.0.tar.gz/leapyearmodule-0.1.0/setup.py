from setuptools import setup, find_packages

setup(
    name="leapyearmodule",  # Package name (must be unique on PyPI)
    version="0.1.0",  # Initial version
    packages=find_packages(),  # Automatically find package directories
    install_requires=[],  # No external dependencies for this module
    author="Om Satyawan Pathak",  # Replace with your name
    author_email="omsatyawanpathakwebdevelopment@gmail.com",  # Replace with your email
    description="A module to determine leap years and classify years as AD or BC",
    long_description=open("README.md").read(),  # Use README.md for detailed description
    long_description_content_type="text/markdown",  # Specify Markdown format
    url="https://github.com/yourusername/leapyearmodule",  # Replace with your repo URL (optional)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
)