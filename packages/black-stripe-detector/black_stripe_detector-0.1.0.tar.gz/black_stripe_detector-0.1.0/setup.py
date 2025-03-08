from setuptools import setup, find_packages

setup(
    name="black_stripe_detector",
    version="0.1.0",
    description="A Python package to detect black stripes in images that may indicate rendering errors.",
    author="Jer NC",
    author_email="",
    packages=find_packages(),
    install_requires=[
        "Pillow>=9.0.0",
        "numpy>=1.21.0",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)