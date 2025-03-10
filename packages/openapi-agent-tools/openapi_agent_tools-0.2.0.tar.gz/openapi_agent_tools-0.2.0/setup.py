from setuptools import setup, find_packages

setup(
    name="openapi_agent_tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyYAML>=5.4.0",
        "ruamel.yaml>=0.17.0"
    ],
)
