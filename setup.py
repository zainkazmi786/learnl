from setuptools import setup, find_packages

setup(
    name="learnl",
    version="0.1.0",
    description="Your AI command assistant for Linux terminal",
    author="Asim - Zain",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
        "prompt-toolkit>=3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "learnl=learnl.main:main",  # Assuming main.py contains a main() function
        ]
    }
)
