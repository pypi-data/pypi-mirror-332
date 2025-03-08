import os
import setuptools
import sys

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    print("publish")
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as requeriments:
    REQUIREMENTS = requeriments.readlines()

setuptools.setup(
    name="notbank",
    version="1.0.0",
    packages=[
        'notbank'
    ],
    include_package_data=True,
    description="Notbank API client library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['api', 'notbank', 'bitcoin', 'ethereum'],
    # url="https://github.com/notbank/notbank-python",
    install_requires=REQUIREMENTS,
    author="Notbank",
    python_requires='>=3.7',
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
