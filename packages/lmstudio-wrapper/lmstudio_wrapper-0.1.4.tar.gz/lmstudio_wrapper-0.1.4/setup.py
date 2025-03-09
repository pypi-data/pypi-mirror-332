from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lmstudio-wrapper',  
    version='0.1.4',  
    author='Harshit',
    author_email='harshitkumar9030@gmail.com',
    description='A client library for interacting with the LM Studio API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/harshitkumar9030/lmstudio-client',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests>=2.25.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
)