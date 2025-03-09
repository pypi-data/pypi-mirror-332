from setuptools import setup, find_packages

setup(
    name="Pairs_Package2",
    version="0.1.7",
    packages=find_packages(),
    py_modules=['Pairs_Package2'],
    install_requires=[
        'pandas',
        'pandas_datareader',
        'alpaca-trade-api',
        'numpy',
        'python-dotenv',
        'setuptools',
        'statsmodels', 
    ],
    description='Pairs Trading strategy, trades executed with Alpaca',
    author='Mihai Posea',
    author_email='pose4408@mylaurier.ca',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
)


