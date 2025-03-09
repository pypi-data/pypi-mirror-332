from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import numpy

with open("README.md","r", encoding = 'utf-8') as fp:
	readme = fp.read()

# Define the Cython extension
extensions = [
    Extension(
        name = "gmimtools.gmim",
        sources = ["gmimtools/gmim.pyx"],
        include_dirs = [numpy.get_include()],
    )
]

# Call setup
setup(
	name="gmimtools",
	version="0.2.0",
	license='MIT',
    
	description="A suite of ground motion intensity measure tools.",
	author="A. Renmin Pretell Ductram",
	author_email='rpretell@unr.edu',
	url="https://github.com/RPretellD/gmimtools",
    
    long_description_content_type="text/markdown",
    long_description=readme,
    
    packages=find_packages(),

	include_package_data=True,
    ext_modules=cythonize(extensions),
    python_requires	= ">=3.7",
    install_requires=[
            "numpy",
            "Cython"
    ],

	keywords='gmim',
	classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Cython",
        "Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
	],    
)