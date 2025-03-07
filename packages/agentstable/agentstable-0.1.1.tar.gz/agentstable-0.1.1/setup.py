"""
Setup script for the AgentStable SDK.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agentstable",
    version="0.1.1",
    author="AgentStable Team",
    author_email="info@agentstable.ai",
    description="A Python SDK for integrating with the AgentStable Search Action Service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clayton-dcruze/agentstable-sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=21.5b2",
            "isort>=5.9.1",
            "mypy>=0.910",
            "build>=0.10.0",
            "twine>=4.0.2",
        ],
        "openai": [
            "openai>=1.0.0",
        ],
        "anthropic": [
            "anthropic>=0.5.0",
        ],
        "redis": [
            "redis>=4.5.0",
        ],
        "all": [
            "openai>=1.0.0",
            "anthropic>=0.5.0",
            "redis>=4.5.0",
        ],
    },
) 