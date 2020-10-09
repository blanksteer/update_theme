import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="update_theme-pkg-blanksteer", # Replace with your own username
    version="0.0.1",
    author="blanksteer",
    author_email="ubiqfree@protonmail.ch",
    description="Update UX stuff",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blanksteer/update_theme",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)