from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="EbookTranslator",
    version="0.1.0",
    author="Chen",
    author_email="1421243966@qq.com",
    description="The world's highest performing e-book retention layout translation library",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/EbookTranslator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pymupdf>=1.18.0",
        "Pillow>=8.0.0",
        "pytesseract>=0.3.0",
        "deepl==1.17.0",
        "Pillow==10.2.0",
        "PyMuPDF==1.24.0",
        "pytesseract==0.3.10",
        "requests",
        "Werkzeug",
        "aiohttp",

        # 添加其他依赖
    ],
    entry_points={
        "console_scripts": [
            "EbookTranslator=EbookTranslator.cli:main",
        ],
    },
    include_package_data=True,
)
