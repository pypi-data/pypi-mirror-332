from setuptools import find_packages, setup

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name="jupyterhub-enverge-nativeauthenticator",
    version="0.0.2",
    description="JupyterHub Enverge Native Authenticator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Enverge-Labs/enverge_nativeauthenticator",
    author="Leticia Portella",
    author_email="leportella@protonmail.com",
    license="3 Clause BSD",
    packages=find_packages(),
    package_data={
        'enverge_nativeauthenticator': ['templates/*.html'],
    },
    python_requires=">=3.9",
    install_requires=[
        "jupyterhub>=4.1.6",
        "bcrypt",
        "onetimepass",
    ],
    extras_require={
        "test": [
            "notebook>=6.4.1",
            "pytest",
            "pytest-asyncio",
            "pytest-cov",
        ],
    },
    include_package_data=True,
)
