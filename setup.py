from setuptools import setup, find_packages

setup(
    name='Piltdown',
    version='0.1.1',
    author='Evans Winner',
    author_email='evans.winner@gmail.com',
    # package_dir={"":"piltdown"},
    packages=find_packages(),
    long_description_content_type='text/markdown',
    # long_description='README.md',
    url='http://github.com/evanswinner/piltdown',
    license='LICENSE',
    description='Unicode data viz for your Twitter posts.',
    long_description=open('README.md').read(),
)
