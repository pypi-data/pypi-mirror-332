from setuptools import setup, find_packages

setup(
    name="fair_kmeans_aravind",  # Package name
    version="0.1.0",  # Initial version
    packages=find_packages(),  # Automatically find packages
    install_requires=[],  # Dependencies (if any)
    author="Ashwin Ram Venkataraman",
    author_email="ashwinram232@gmail.com",
    description="FAIR K-MEANS",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)