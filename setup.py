from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='optimizedf',
    url='https://github.com/gbletsch/optimizedf',
    author='Guilherme Boelhouwer Letsch',
    author_email='gbletsch@gmail.com',
    # Needed to actually package something
    packages=['optimizedf'],
    # Needed for dependencies
    install_requires=['pandas'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Optimize a pandas DataFrame changing some columns dtypes.',
    long_description=open('README.md').read(),
)