from setuptools import setup

setup(
    name="anyfox",
    version="0.0.0",
    author="zetaloop",
    author_email="zetaloop@outlook.com",
    description="This fox is very different than anyfox else.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zetaloop/anyfox",
    packages=["anyfox"],
    package_data={"anyfox": ["../anyfox.pth"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Natural Language :: Chinese (Simplified)",
    ],
    python_requires=">=3.8",
)
