from setuptools import setup, find_packages

setup(
    name="mouse-movement",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List any dependencies if required
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    description="A library for controlling mouse and keyboard via ctypes on Windows",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mouse-movement",
    author="Your Name",
    author_email="your.email@example.com",
)
