import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="realiseven",
    version="0.1.0",
    author="Dmytro Kreiza",
    author_email="d.kreiza.dev.news@gmail.com",
    description="AI-Powered library to determine if number is even or odd.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kreiza/realiseven",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=["openai~=1.65.4", "pydantic~=2.10.6"],
)
