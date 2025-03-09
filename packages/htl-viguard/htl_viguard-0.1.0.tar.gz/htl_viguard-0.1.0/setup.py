from setuptools import setup, find_packages

setup(
    name="htl-viguard",  # Tên package
    version="0.1.0",  # Phiên bản
    author="Hoang Thanh Lam",
    author_email="lamkt547749@gmail.com",
    description="DATN ViGuard - Ultralytics",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
