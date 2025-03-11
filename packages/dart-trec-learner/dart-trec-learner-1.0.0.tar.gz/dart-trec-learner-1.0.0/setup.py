from setuptools import setup, find_packages
from datetime import datetime
import os


def remove_prefix(self, prefix):
    if self.startswith(prefix):
        return self[len(prefix):]
    else:
        return self[:]


with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    req = f.read().split("\n")

version = remove_prefix(os.getenv("VERSION", "v1.0.0"), "v")

if version == 'nightly':
    version = datetime.today().strftime('%Y%m%d')

setup(
    name="dart-trec-learner",
    version=version,
    author="SIDIA",
    author_email="sidia@sidia.com",
    description="T-REC learner libs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.sec.samsung.net/SOL/dart-trec-learner",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires="~=3.7",
    install_requires=req,
    dependency_links=[
        'https://bart.sec.samsung.net/artifactory/api/pypi/trec-pypi/simple'
    ],
)
