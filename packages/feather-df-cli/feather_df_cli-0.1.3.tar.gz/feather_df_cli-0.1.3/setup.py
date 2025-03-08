from setuptools import setup, find_packages

setup(
    name="feather-df-cli",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[
        "pyarrow>=12.0.1",
        "tabulate>=0.9.0"
    ],
    entry_points={
        'console_scripts': [
            'feather-cli=feather_df_cli.cli:main',
        ],
    },
    python_requires='>=3.6',
    author="villadora",
    description="A CLI tool for reading and displaying Feather data format files",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/villadora/feather-df-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
