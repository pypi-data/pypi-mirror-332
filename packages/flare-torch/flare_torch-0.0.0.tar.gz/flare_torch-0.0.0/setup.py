from setuptools import setup, find_packages

setup(
    name="flare-torch",
    version="0.0.0",
    packages=find_packages(include=["flare", "flare.*"]),
    description="(Not yet.) Train pytorch models with a few lines of code.",
    author="denev6",
    author_email="sungjin.code@gmail.com",
    url="https://github.com/denev6/deep-learning-codes/tree/main/flare",
    license="MIT License",
    install_requires=[
        "torch",
        "tqdm",
        "numpy",
        "scikit-learn",
    ],
    keywords=["teddynote", "teddylee777", "python datasets", "python tutorial", "pypi"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
