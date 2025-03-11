from setuptools import setup, find_packages

setup(
    name="ieeefp",  # The name that will be used for pip install
    version="0.1.2",  # resolved minor fix
    packages=find_packages(),
    author="Sagnik Nath",
    author_email="sanath@ucsc.edu",
    description="A tool to convert floating-point numbers to IEEE 754 format",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sagniknath91/ieeefp",  # Create a GitHub repo for it
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "ieeefp=ieeefp.ieeefp:float_to_ieee754",  # Makes it executable
        ],
    },
)
