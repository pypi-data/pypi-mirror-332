from setuptools import setup, find_packages

setup(
    name="fair_kmeans_uchicago",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "openai",
    ],
    author="Ashwin Ram Venkataraman",
    author_email="ashwinram232@gmail.com",
    description="A Fair K-Means clustering algorithm with fairness constraints.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fair_kmeans",  # Update with your GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)