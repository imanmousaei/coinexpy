from distutils.core import setup

setup(
    name='coinexpy',
    packages=['coinexpy'],
    version='0.1',
    license='MIT',
    description='Python wrapper for Coinex APIs',
    author='Iman Mousaei',
    author_email='imanmousaei1379@gmail.com',
    url='https://github.com/user/reponame',  # Provide either the link to your github or to your website
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',  # I explain this later on
    keywords=['coinex', 'api', 'wrapper', 'trade'],
    install_requires=[
        'hashlib',
        'json',
        'urllib3'
    ],
    classifiers=[
        # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Development Status :: 3 - Alpha',

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
