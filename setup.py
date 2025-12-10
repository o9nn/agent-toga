"""
Agent-Toga Setup Configuration
Himiko Toga AI Personality - Cheerful Chaos Meets Cognitive Architecture
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="agent-toga",
    version="1.0.0",
    author="o9nn",
    description="Himiko Toga AI Personality with Security Testing & Code Absorption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/o9nn/agent-toga",
    packages=find_packages(include=["python", "python.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        # No external dependencies - pure Python implementation!
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.yaml", "*.md"],
    },
    keywords="ai personality himiko-toga security-testing penetration-testing red-team agent-neuro",
    project_urls={
        "Documentation": "https://github.com/o9nn/agent-toga/blob/main/README.md",
        "Source": "https://github.com/o9nn/agent-toga",
        "Tracker": "https://github.com/o9nn/agent-toga/issues",
    },
)
