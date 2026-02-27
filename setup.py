from setuptools import setup, find_packages

setup(
    name="csv-reader",
    version="0.1.0",
    description="A simple CSV reader",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "csv-reader=csv_reader.reader:main"
        ]
    },
    python_requires=">=3.7",
)
