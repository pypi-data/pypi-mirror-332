import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uzbek-stopwords",
    version="0.0.1",
    author="Nurbek Suvonov",
    author_email="nurbekkmu@gmail.com",
    description="A list of Uzbek stopwords for the Uzbek language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nurbekkmu/uzbek_stopwords",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
