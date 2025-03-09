#!/usr/bin/env python
"""
Setup script for edger package.
"""
from setuptools import setup, find_packages

setup(
    name="edger",
    version="0.1.3",
    description="Redirect Microsoft Edge to your preferred browser",
    long_description="""
        Edger is a lightweight Windows utility that runs in your system tray and 
        automatically redirects Microsoft Edge browser windows to your default browser.
        It's designed for users who prefer their browser of choice but find Edge being 
        forced upon them in various contexts.
    """,
    long_description_content_type="text/markdown",
    author="Daniel Agans",
    author_email="phwelo@qwe.rip",
    url="https://github.com/phwelo/edger",
    packages=["edger", "edger.data"],
    package_data={
        "edger": ["config.ini", "data/*.ico"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    license="MIT",
    python_requires=">=3.6",
    install_requires=[
        "pystray>=0.17.0",
        "Pillow>=8.0.0",
        "pywin32>=300",
        "psutil>=5.9.0",
        "pyautogui>=0.9.53",
        "pyperclip>=1.8.2",
        "configparser>=5.2.0",
    ],
    entry_points={
        "console_scripts": [
            "edger=edger:main",
        ],
    },
) 