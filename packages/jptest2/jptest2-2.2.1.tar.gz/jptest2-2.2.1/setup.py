# configuration
libs = [
    'jupyter',
    'aiofiles==24.1.0'
]

sqlite_libs = [
    'aiosqlite==0.21.0'
]

demo_libs = [
    'watchfiles==1.0.4'
]

version = '2.2.1'

# package setup
if __name__ == '__main__':
    with open('README.md', 'r', encoding='utf-8') as file:
        long_description = file.read()

    from setuptools import setup, find_packages
    setup(
        name='jptest2',
        version=version,
        author='Eric Tröbs',
        author_email='eric.troebs@tu-ilmenau.de',
        description='write graded unit tests for Jupyter Notebooks in a few lines of code',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/erictroebs/jptest',
        project_urls={
            'Bug Tracker': 'https://github.com/erictroebs/jptest/issues',
        },
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        package_dir={'': 'src'},
        packages=find_packages(where='src'),
        python_requires='>=3.9',
        install_requires=libs,
        extras_require={
            'sqlite': sqlite_libs,
            'demo': demo_libs,
        }
    )
