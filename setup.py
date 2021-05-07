import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tb-helper",
    version="0.0.1",
    author="Mohammad Farid Azampour",
    author_email="mf.azampur@tum.de",
    description="A helper package for better viewing results on tensorboard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/mfazampour/tensorboard-helper",
    project_urls={
        "Bug Tracker": "https://github.com/mfazampour/tensorboard-helper/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
            'torch>=1.0',
            'numpy>=1.0',
            'matplotlib>=3'
      ],
    python_requires=">=3.6",
)