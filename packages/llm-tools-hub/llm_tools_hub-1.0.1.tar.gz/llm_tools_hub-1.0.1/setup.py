from setuptools import setup, find_packages

setup(
    name="llm-tools-hub",
    version="1.0.1",
    author="Ronivaldo Sampaio",
    author_email="ronivaldo@gmail.com",
    description="Instant integration of external tools into LLM applications via automatic function calling.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ronivaldo/llm-tools-hub",
    packages=find_packages(),
    install_requires=[
        "openai==0.28",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)