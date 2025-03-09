from setuptools import setup, find_packages

setup(
    name="databooster",  
    version="0.1.0",  
    author="ilyanozary",
    author_email="ilyanozary.dynamic@gmail.com",
    description="A smart data augmentation tool for AI developers.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ilyanozary/data_booster",  
    packages=find_packages(),  
    install_requires=[
        "Pillow", 
        "nltk" 
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
