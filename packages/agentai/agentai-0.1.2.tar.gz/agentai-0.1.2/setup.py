from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agentai",
    version="0.1.2",
    author="Andrei Oprisan",
    author_email="andrei@agent.ai",
    description="A Python client for the Agent.ai API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OnStartups/python_sdk",
    packages=find_packages(where='agentai'),
    package_dir={'': 'agentai'},
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)
