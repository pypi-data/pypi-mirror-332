from setuptools import setup, find_packages

setup(
    name="hypertune-param", 
    version="0.1.1",  
    author="Arcoson",  
    author_email="hylendust@gmail.com",  
    description="A custom library for hyperparameter optimization using Grid Search, Random Search, and Bayesian Optimization.", 
    long_description=open('README.md').read(), 
    long_description_content_type="text/markdown",  
    url="https://github.com/Arcoson/hypertune",  
    packages=find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    install_requires=[
        "scikit-learn==1.2.2",
        "hyperopt==0.2.7",
        "numpy==1.24.3",
        "pandas==1.5.3",
        "matplotlib==3.7.1",
    ], 
    python_requires='>=3.6',
)
