from setuptools import setup, find_packages

setup(
    name="hoangecg",  # Tên package trên PyPI
    version="0.1.2",  # Phiên bản đầu tiên
    packages=find_packages(),  # Tự động tìm các package bên trong
    install_requires=[
        "requests",  # Nếu module của bạn dùng requests
    ],
    author="hoangecg",
    author_email="hoangecg@gmail.com",
    description="Module remote vMix, Resolume, Chrworks, TC1",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HoangECG",  # Link đến GitHub (nếu có)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
