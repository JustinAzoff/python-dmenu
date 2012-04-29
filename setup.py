from setuptools import setup

setup(name="dmenu",
    version="0.1",
    description="Wrapper for dmenu",
    license='MIT',
    classifiers=[
    ],
    keywords='dmenu onscreen menu',
    author="Justin Azoff",
    author_email="justin@bouncybouncy.net",
    py_modules = ["dmenu"], 
    setup_requires=[
    ],
    test_suite='nose.collector',
)
