from setuptools import setup, find_packages

setup(
    name="django-generic-model-fields",
    version="2.0.0",
    description="Sensible Django model fields for easy migrations and database portability",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="WaAWsUPQpGcRLcLcEkthyDyhX",
    author_email="molding_exact_6i@icloud.com",
    url="https://github.com/iBfuRsiFUBbfzPdnJhXUfFFkk/django-generic-model-fields",
    packages=find_packages(),
    install_requires=[
        "django==5.1.7",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
