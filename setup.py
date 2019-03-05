"""Setup file for markive."""

import setuptools

with open("README.md", 'r') as desc:
    LONG_DESC = desc.read()

setuptools.setup(
    name="markive",
    version="0.1.0",
    author="Madelyn Eriksen",
    author_email="hello@madelyneriksen.com",
    description="Personal journal and archiving tool",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    url="https://github.com/madelyneriksen/markive",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "Click",
    ],
    scripts=[
        'scripts/markive',
    ]
)
