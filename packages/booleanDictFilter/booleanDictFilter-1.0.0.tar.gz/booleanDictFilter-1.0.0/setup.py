from setuptools import setup, find_packages

setup(
    name="booleanDictFilter",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    author="Sean Hummel",
    description="Library for applying a boolean filter string to a dictionary, allowing for searches of keyvalue pairs.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mrmessagewriter/BooleanDictFilter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)
