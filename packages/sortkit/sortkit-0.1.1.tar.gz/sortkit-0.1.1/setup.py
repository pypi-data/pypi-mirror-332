from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sortkit",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],
    author="Sudipta Ghosh",
    description="A Python library implementing various sorting algorithms",
    long_description=long_description,  # ✅ Add this
    long_description_content_type="text/markdown",  # ✅ Specify Markdown format
    url="https://github.com/Sudipto-tales/sortkit",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
