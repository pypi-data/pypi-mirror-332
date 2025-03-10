import os
from setuptools import setup, find_packages

# Get version from environment variable or use '0.0.0'
version = os.getenv("CI_COMMIT_TAG", "2025.1.3.1")

setup(
    name="fast_bi_dbt_runner",
    version=version,  # Dynamically set version
    author="Fast.Bi",
    author_email="support@fast.bi",
    maintainer="Fast.Bi",
    maintainer_email="administrator@fast.bi",
    description="Private Python library who provides managing for set up DBT DAGs.",
    url="https://gitlab.fast.bi/infrastructure/bi-platform-pypi-packages/fast_bi_dbt_runner",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    setup_requires=["setuptools"],
)
