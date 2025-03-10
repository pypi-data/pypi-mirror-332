from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="catchttp",
    version="1.0.0",
    author="Nikolai Timofeev",
    author_email="timofeevnik41@gmail.com",
    description="HTTP request capture and mock library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/timofeev41/catchttp",
    packages=["request_catcher"],
    install_requires=[
        "httpx>=0.23.0",
        "requests>=2.26.0",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.7",
) 