from setuptools import setup, find_packages

setup(
    name="base-consumer",
    version="0.1",
    packages=find_packages(),
    install_requires=["confluent_kafka"],
)
