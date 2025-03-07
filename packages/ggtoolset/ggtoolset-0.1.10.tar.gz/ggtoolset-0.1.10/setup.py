from setuptools import setup, find_packages

setup(
	name='ggtoolset',
	version='0.1.10',
	author='gg61021277',
	author_email='gg61021277@gmail.com',
	description='everday utilities',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	url='https://github.com/',
	packages=['ggtoolset'],
    install_requires=[
        'python-box>=5.0.0',  # Ensure the appropriate version of python-box is installed
    ],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	],
	python_requires='>=3.6',
)
