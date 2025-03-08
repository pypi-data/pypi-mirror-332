from setuptools import setup, find_packages

setup(
    name="nwlabcomm",  # Name of your package
    version="1.0",  # Version number
    author="Hakim Adiche",
    author_email="adiche@kfupm.edu.sa",
    description="Client and Server Communication",
    packages=find_packages(),  # Automatically finds packages in the directory
    install_requires=[
        "ttkbootstrap",
        "datetime",
        "pyaudio",
        "wave",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version required
)
