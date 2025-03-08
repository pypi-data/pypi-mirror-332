
from setuptools import setup, find_packages

setup(
    name="climeon",
    packages=find_packages(),
    version="2.1.1",
    license="MIT",
    description="Climeon API client",
    long_description="Climeon API client",
    author="Emil Hjelm",
    author_email="emil.hjelm@climeon.com",
    keywords=["climeon", "REST", "API"],
    python_requires=">=3.9",
    install_requires=[
        "plotly",
        "plotly-resampler",
        "msal",
        "pandas",
        "requests",
        "dateparser"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Operating System :: OS Independent"
    ]
)
