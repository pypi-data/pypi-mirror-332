from setuptools import setup, find_packages

setup(
    name='shankskit', 
    version='0.1.0',
    author='Shashank Rao',
    author_email='your.email@example.com',
    description='A brief description of your library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ShashankRaoCoding/shankskit',
    packages=find_packages(),
    license = "LGPL-3.0-or-later" , 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
