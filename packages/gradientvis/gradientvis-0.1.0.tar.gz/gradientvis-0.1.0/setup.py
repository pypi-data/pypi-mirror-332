from setuptools import setup, find_packages

setup(
    name="gradientvis",  # The name of the package
    version="0.1.0",  # The version number
    description="A library for visualizing neural network gradients",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Arcoson",
    author_email="hylendust@gmail.com",
    url="https://github.com/Arcoson/gradientvis",
    packages=find_packages(),  # Automatically find packages
    install_requires=[
        "torch",  # List any required dependencies
        "numpy",
        "matplotlib",
        "scipy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
)
