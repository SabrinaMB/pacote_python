from setuptools import setup

setup(name='dev_aberto_sabrinamb',
      version='0.1',
      author="Sabrina",
      packages=['dev_aberto'],
      install_requires=['requests'],
      scripts=['scripts/hello.py'],
      license="MIT",
      classifiers=[
	  "License :: OSI Approved :: MIT License",
  	  "Programming Language :: Python :: 3",
  	  "Programming Language :: Python :: 3.7",
      ],
      )
