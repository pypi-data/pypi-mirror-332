from setuptools import setup, find_packages

setup(
    name="infoweb",
    version="1.4",
    author="Golden",
    author_email="GoldenWebr5@gmail.com",
    description="A Python package to check website status, extract links, and audit websites.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["requests","pytz","cloudscraper",],
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Operating System :: OS Independent",],
    python_requires=">=3.6",
)