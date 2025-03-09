from setuptools import setup, find_packages

setup(
    name="bullscatch_backtester",  # Change this to your package name
    version="0.1.0",
    author="Guru Pandey",
    author_email="guru@bullscatchsecurities.com",
    description="A package for backtesting trading strategies meant for Bullscatch Securities",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    #url="https://github.com/yourusername/my_package",  # Update with your GitHub repo
    packages=find_packages(),
    install_requires=[],  # Add dependencies here if needed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
