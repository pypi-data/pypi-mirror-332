from setuptools import setup, find_packages

setup(
    name='yathoo',
    version='0.2.0',
    packages=find_packages(),
    description='A short description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Yathartha Santosh Yadav',
    author_email='yathartha.ys@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
