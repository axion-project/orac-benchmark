#!/usr/bin/env python3

from setuptools import setup, find_packages
import pathlib

# Read README for long description
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text(encoding='utf-8')

# Read requirements
def read_requirements():
    with open('requirements.txt', 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="orac-benchmark",
    version="2.0.0",
    author="ORAC Team",
    author_email="orac@yourorg.com",
    description="A comprehensive, next-generation benchmarking framework for system performance evaluation",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/orac-benchmark",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/orac-benchmark/issues",
        "Documentation": "https://github.com/yourusername/orac-benchmark/wiki",
        "Source Code": "https://github.com/yourusername/orac-benchmark",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Benchmark",
        "Topic :: System :: Systems Administration",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.20.0", 
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=0.991",
        ],
        "cloud": [
            "boto3>=1.24.0",
            "google-cloud-monitoring>=2.11.0", 
            "azure-monitor-query>=1.1.0",
        ],
        "containers": [
            "docker>=6.0.0",
            "kubernetes>=24.2.0",
        ],
        "visualization": [
            "matplotlib>=3.5.0",
            "plotly>=5.10.0",
            "dash>=2.6.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "orac-bench=orac_bench:main",
            "orac-monitor=orac_bench:monitor_mode",
        ],
    },
    include_package_data=True,
    package_data={
        "orac_benchmark": [
            "config/*.yaml",
            "templates/*.json",
            "dashboards/*.json",
        ],
    },
    keywords="benchmark performance testing monitoring latency memory security scaling energy",
    zip_safe=False,
)
