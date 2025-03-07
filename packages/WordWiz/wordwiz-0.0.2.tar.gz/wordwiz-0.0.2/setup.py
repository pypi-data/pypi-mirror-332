from setuptools import setup, find_packages

def readme_read():
    with open("README.md", "r") as f:
        return f.read()
    
def license_read():
    with open("LICENSE.txt", "r") as f:
        return f.read()

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9"
]

setup(
    name="WordWiz",
    version="0.0.2",
    description="A word API for definitions, synonyms and antonyms.",
    long_description=readme_read(),
    long_description_content_type="text/markdown",
    url="https://github.com/devs-des1re/WordWiz/",
    project_urls={
        "Bug Reporter": "https://github.com/devs-des1re/WordWiz/issues",
        "Repository": "https://github.com/devs-des1re/WordWiz"
    },
    author="devs_des1re",
    author_email="arjunbrij8811@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords="words",
    packages=find_packages(),
    install_requires=[
        "bs4",
        "requests"
    ],
)