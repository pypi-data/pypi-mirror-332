from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="telethon_router",
    version="0.1.0",
    author="Seu Nome",
    author_email="seu.email@example.com",
    description="A library for building Telegram bots using routing similar to web pages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabrielmrts/telethon_router",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "telethon",
    ],
)