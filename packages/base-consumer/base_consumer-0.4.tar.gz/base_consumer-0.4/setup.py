from setuptools import setup, find_packages

setup(
    name="base-consumer",
    version="0.4",
    packages=find_packages(),
    install_requires=["confluent_kafka"],
)
