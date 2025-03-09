from setuptools import setup

setup(
    name="elonadl",
    version="0.1.7",
    author="vichmartins",
    packages=["elonadl"],
    description="ElonaPlusCGXDownload",
    long_description="Quick script to download and setup Elona+CGX",
    python_requires='>=3.10',
    install_requires=['pywin32', 'requests', 'winshell']
)
