from setuptools import setup

version = '0.4'

setup(
    name='coinexpy',
    packages=['coinexpy'],
    version=version,
    license='MIT',
    description='Python wrapper for Coinex APIs',
    long_description_content_type='text/markdown',
    long_description=open('README.md', 'rt').read(),
    author='Iman Mousaei',
    author_email='imanmousaei1379@gmail.com',
    url='https://github.com/imanmousaei/coinexpy',
    download_url=f'https://github.com/imanmousaei/coinexpy/archive/refs/tags/v{version}.tar.gz',
    keywords=['coinex', 'api', 'wrapper', 'trade', 'crypto', 'bitcoin'],
    install_requires=[
        'urllib3'
    ],
    classifiers=[
        # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
