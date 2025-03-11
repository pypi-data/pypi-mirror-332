from setuptools import setup, find_packages

setup(
    name='sparkxgb',
    version='0.2',
    description='sparkxgb module',
    url='',
    author='unk',
    author_email='unk@gmail.com',
    liscence='unk',
    packages=['sparkxgb'],
    zip_safe=False,
    install_requires=[
        'pyspark==3.5.4',
    ]
)
