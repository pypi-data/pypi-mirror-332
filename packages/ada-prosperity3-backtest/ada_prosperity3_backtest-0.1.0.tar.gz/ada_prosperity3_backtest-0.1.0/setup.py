from setuptools import setup, find_packages

setup(
    name="ada-prosperity3-backtest",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pandas"],
    entry_points={
        "console_scripts": [
            "ada-prosperity3-backtest = ada_prosperity3_backtest.cli:main",
        ],
    },
)
