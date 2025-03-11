from setuptools import find_packages
from setuptools import setup


def find_required() -> list[str]:
    with open("requirements.txt") as f:
        return f.read().splitlines()


def find_dev_required() -> list[str]:
    with open("requirements-dev.txt") as f:
        return f.read().splitlines()


def get_version(filename='flakyzavr/version') -> str:
    return open(filename, "r").read().strip()


setup(
    name="flakyzavr",
    version=get_version(),
    description="vedro.io plugin for reporting about flaky tests into jira "
                "(with plugin enabled in flaky check runs)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Yuriy Sagitov",
    author_email="pro100.ko10ok@gmail.com",
    python_requires=">=3.7",
    url="https://github.com/ko10ok/flakyzavr",
    license="Apache-2.0",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=find_required(),
    tests_require=find_dev_required(),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
    ],
    package_data={
        'flakyzavr': ['version', 'py.typed'],
    },
)
