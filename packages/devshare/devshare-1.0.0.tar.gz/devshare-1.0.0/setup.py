from setuptools import setup, find_packages

setup(
    name="devshare",
    version="1.0.0",
    packages=find_packages(),
    py_modules=["devshare"],
    install_requires=[
        "fastapi",
        "uvicorn",
        "websockets",
        "cryptography",
        "requests",
        "tqdm",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "devshare=cli.devshare:main"
        ]
    },
    author="Zayan Khan",
    author_email="khanzayan_123@hotmail.com",
    description="Secure peer-to-peer file transfer CLI with encryption.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ZayanKhan-12",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
