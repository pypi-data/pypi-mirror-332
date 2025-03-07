from setuptools import setup, find_packages

setup(
    name="multicoin",
    version="0.0.1",
    author="Taireru LLC",
    author_email="tairerullc@gmail.com",
    description="Multicoin is an ease-of-access Python package packed full of useful tools for developers.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TaireruLLC/gitbase",
    packages=find_packages(),
    install_requires=[
        "requests",
        "fancyutil>=0.0.1",
        "altcolor>=0.0.5",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="MIT",
)
