from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name='teraboxdl',
    version='0.2',
    packages=find_packages(),
    url='https://github.com/TG-BOTSNETWORK/teraboxdl',
    author='Santhosh',
    author_email='telegramsanthu@gmail.com',
    description='A package for downloading from Terabox',
    install_requires=[
       'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
