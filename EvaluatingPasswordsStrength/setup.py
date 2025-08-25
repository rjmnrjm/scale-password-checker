from setuptools import setup, find_packages

setup(
    name="scale-password-checker",
    version="1.0.0",
    description="Password Strength Checker with GUI (Scale)",
    author="Your Name",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "scale=scale.gui:main"   # allows running `scale` from terminal
        ]
    },
)
