from setuptools import setup, find_packages

setup(
    name="fastapi-loadbalancer",  
    version="0.1.0",  
    packages=find_packages(), 
    install_requires=[
        "fastapi>=0.100.0",
        "uvicorn>=0.27.0",
        "requests>=2.31.0",
    ],
    description="A simple load balancer for FastAPI applications.",
    long_description=open("README.md",encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Shubham Uparkar",  
    author_email="uparkarshubham9@gmail.com",  
    url="https://github.com/shubham31121999/FastAPI-LOADBALANCER",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  
)
