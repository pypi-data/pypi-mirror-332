from setuptools import setup, find_packages

setup(
    name="face-gest-loader",  # Package name
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas"
    ],
    author="Yaseen/Sonain amil",
    author_email="yaseen@sju.ac.kr",
    description="Loading FaceGest dataset",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yaseen21khan/FaceGest_Repo",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
