from setuptools import setup, find_packages

setup(
    name="cnki-agent",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "selenium",
    ],
    author="zstar",
    author_email="zstar1003@163.com",
    description="A Python package for scraping CNKI papers.",
    url="https://github.com/zstar1003/cnki-agent",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
