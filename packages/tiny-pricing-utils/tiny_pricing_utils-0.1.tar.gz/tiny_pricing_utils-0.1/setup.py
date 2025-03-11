from setuptools import setup, find_packages

setup(
    name="tiny_pricing_utils",  # Package name
    version="0.1",    # Version of the package
    packages=find_packages(),  # This automatically finds your 'my_utils' directory
    description="A set of utility functions for my project",
    long_description=open('README.md').read(),  # Read your README file
    long_description_content_type="text/markdown",  # The format of your README
    author="Your Name",
    author_email="michael.carlo@outlook.it",
    license="MIT",  # License type
    classifiers=[    # This is useful for PyPI classification
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
