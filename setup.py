import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deeptrade",
    version="0.0.5",
    author="Fabio C.",
    author_email="info@deeptrade.ch",
    description="A python library to communicate with the DeepTrade API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://deeptrade.ch",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'pandas'
        ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
