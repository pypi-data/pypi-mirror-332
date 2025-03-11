import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mailinator_python_client_2",
    version="0.0.8",
    author="Marian Melnychuk",
    author_email="marian.melnychuk@gmail.com",
    description="SDK for Mailinator",
    long_description="SDK for Mailinator",
    long_description_content_type="text/markdown",
    url="https://github.com/manybrain/mailinator-python-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
    python_requires='>=3.6',
)
