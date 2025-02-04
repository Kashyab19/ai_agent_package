"""
Legacy Builds
"""

from setuptools import setup, find_packages

setup(
    name="ai_agent",
    version="0.1.0",
    description="An AI agent for blockchain interactions.",
    author="Kashyab",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pydantic"
    ],
)
