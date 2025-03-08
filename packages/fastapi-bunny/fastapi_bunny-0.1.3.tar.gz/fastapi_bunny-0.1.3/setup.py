from setuptools import setup, find_packages

setup(
    name="fastapi_bunny",
    version="0.1.3",  # Incremented version
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "pymongo",
        "pydantic",
        "uvicorn[standard]"  # Added for running FastAPI
    ],
    entry_points={
        "console_scripts": [
            "fastapi_bunny=fastapi_bunny.generate:create_boilerplate",
        ],
    },
    author="Pranay Vartak",
    author_email="iamvartak@gmail.com",
    description="A package to generate FastAPI boilerplate based on user input",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pranayvartak/fastapi_bunny",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
