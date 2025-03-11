from setuptools import setup, find_packages

setup(
    name="eamcvd",
    version="1.3",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author="The EAMCVD Team",
    author_email="info@axiom-mc.org",
    description="A library to fetch EAMCVD(elefant ai mod comp. and vulnerabilities database) incompatibility reports",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://axiom-mc.org/eamcvd",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
