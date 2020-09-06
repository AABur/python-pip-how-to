import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AABur_pip_how_to",  # Replace with your own username
    version="0.1.0",
    author="AABur",
    author_email="aabur@mail.ru",
    description="pip_how_to",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AABur/python-pip-how-to",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Natural Language :: English",
        "Topic :: Education",
    ],
    python_requires='>=3.8',
)
