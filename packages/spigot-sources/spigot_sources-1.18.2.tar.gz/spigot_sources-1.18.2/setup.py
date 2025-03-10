from setuptools import setup, find_namespace_packages

setup(
    name='spigot-sources',
    version='1.18.2',
    author='magicmq',
    author_email='business@magicmq.dev',
    description='Translated Spigot sources for writing PySpigot scripts',
    url='https://pyspigot-docs.magicmq.dev',
    py_modules=[],
    packages=find_namespace_packages(),
    python_requires='>=3.6',
    classifiers = [
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Java Libraries',
        'License :: OSI Approved :: Apache Software License'
    ],
)
