from setuptools import setup, find_packages

setup(
    name="scope-emd",
    version="0.1.0",
    description="scope is the Python-based package for detecting oscillatory \
                 signals in observational or experimental time series with the \
                EMD technique and assessing their statistical significance vs. \
                power-law distributed background noise.",
    author="Dmitrii Kolotkov, Weijie Gu, Sergey Belov, Valery Nakariakov",
    author_email="Sergey.Belov@warwick.ac.uk",
    readme = "README.md",
    packages=find_packages(),
    install_requires=[
       'colorednoise>=2.2.0',
       'emd>=0.7.0',
       'numpy>=1.26.4',
       'lmfit>=1.3.2'
    ],
    python_requires=">=3.8",
    Homepage = "https://github.com/Warwick-Solar/scope"
)