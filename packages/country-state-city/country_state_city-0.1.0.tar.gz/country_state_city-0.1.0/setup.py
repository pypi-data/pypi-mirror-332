from setuptools import setup, find_packages

setup(
    name="country_state_city",
    version="0.1.0",
    author="Raymond Lucke",
    author_email="ray@raylucke.com",
    description="A Python library to get countries, states, and cities data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rwl4/country_state_city",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    package_data={
        "country_state_city": ["data/*.json"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    test_suite="tests",
)
