from setuptools import setup, find_packages

setup(
    name="jopilot-api",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
    ],
    author="JoPilot",
    author_email="developers@jopilot.net",
    description="Python wrapper for the JoPilot API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://jopilot.net/",
    project_urls={
        "Homepage": "https://jopilot.net/",
        "Documentation": "https://api.jopilot.net/swagger/index.html",
        "Source Code": "https://github.com/jopilot-net/JoPilotAPI-python",
        "Bug Tracker": "https://github.com/jopilot-net/JoPilotAPI-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)