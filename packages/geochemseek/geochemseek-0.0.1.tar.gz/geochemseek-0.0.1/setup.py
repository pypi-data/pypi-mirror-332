from setuptools import setup, find_packages

setup(
    name="geochemseek",
    version="0.0.1",
    description="Placeholder package for geochemical toolkit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="QingFengMei",
    author_email="qingfengmei@foxmail.com",
    url="https://github.com/QingFengMei/geochemseek",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
)