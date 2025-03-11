from setuptools import setup, find_packages

setup(
    name="chacha20-utils",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["cryptography"],
    author="Sakib Salim",
    author_email="salimsakib775@yahoo.com",
    description="A simple ChaCha20 encryption/decryption utility.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SAKIB-SALIM/chacha20-utils",  # Update with your GitHub link
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
