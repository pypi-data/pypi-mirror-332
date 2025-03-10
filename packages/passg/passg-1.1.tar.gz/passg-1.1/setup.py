import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name="passg",
	version="1.1",
	author="Yasin Amirany",
	author_email="yasin.amirany@gmail.com",
	description="strong password generator",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/yasin1ar/passg",
	packages=setuptools.find_packages(),
	license="MIT",
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.6",
)
