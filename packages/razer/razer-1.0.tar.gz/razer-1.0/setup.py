from setuptools import setup, find_packages

setup(
    name="razer",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        # List any dependencies if required
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    description="A library for controlling mouse and keyboard via ctypes on Windows",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rescore9",
    author="Barzan",
    author_email="rescoregta@gmail.com",
)
