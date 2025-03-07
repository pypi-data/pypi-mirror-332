from setuptools import setup, find_packages

setup(
    name="dind3",  
    version="0.1",
    packages=find_packages(),
    install_requires=["numpy", "pandas","matplotlib"],
    author="owlpharoah",
    author_email="sreeharirathish128@gmail.com",
    description="library to import popular data librabries",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/owlpharoah/dind",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

