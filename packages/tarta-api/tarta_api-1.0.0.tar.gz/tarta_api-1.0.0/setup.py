from setuptools import setup, find_packages

setup(
    name="tarta-api",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
    ],
    author="tarta.ai",
    author_email="taras@tarta.ai",
    description="Python wrapper for the Tarta API, designed to seamlessly integrate AI-powered job search functionality into your applications.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://tarta.ai/",
    project_urls={
        "Homepage": "https://tarta.ai/",
        "Documentation": "https://api.tarta.net/swagger/index.html",
        "Source Code": "https://github.com/tarta-ai/TartaAPI-python",
        "Bug Tracker": "https://github.com/tarta-ai/TartaAPI-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)