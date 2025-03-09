from setuptools import setup, find_packages

setup(
    name="atai-url-tool",
    version="0.0.1",
    description="A CLI tool to check a URL's content type and map it to a simplified type.",
    author="AtomGradient",
    author_email="alex@atomgradient.com",
    url="https://github.com/AtomGradient/atai-url-tool",
    packages=find_packages(),
    install_requires=[
        "playwright",
    ],
    entry_points={
        "console_scripts": [
            "atai-url-tool = atai_url_tool.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
