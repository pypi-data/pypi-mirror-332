from setuptools import setup

setup(
    name="elonadl",
    version="0.1.8",
    author="vichmartins",
    packages=["elonadl"],
    description="ElonaPlusCGXDownload",
    long_description="Installs the latest version of Elona+CGX (Windows Only Currently)",
    python_requires='>=3.10',
    install_requires=['pywin32', 'requests', 'winshell']
)
