import setuptools

with open("README.md","r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="gltf2usd",
  version="0.0.2",
  author="Kacey Coley",
  author_email="kcoley@github.com",
  description="glTF to USD converter",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/kcoley/gltf2usd",
  packages=setuptools.find_packages(),
  install_requires=[
    "pillow==5.2.0",
    "enum34==1.1.6",
    "numpy==1.15.1"
  ],
  classifiers=[
    "Programming Language :: Python :: 2.7",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ]
)