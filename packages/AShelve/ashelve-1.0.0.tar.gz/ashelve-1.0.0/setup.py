from setuptools import setup, find_packages

setup(
    name="AShelve",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["asyncio"],
    author='XelXen',  
    author_email='xelxen@duck.com',
    description='A simple async wrapper for the built-in shelve module',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    readme = "README.md"
)
