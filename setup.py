import setuptools

setuptools.setup(
    name='f1_data_parser',
    version='0.1.0',
    author='ryazhenkofc',
    author_email='ryazhenkofc@gmail.com',
    description='A Python library for parsing Formula 1 data from www.formula1.com',
    url='https://github.com/ryazhenkofc/f1_data_parser',
    packages=['f1_data_parser'],
    install_requires=['requests', 'beautifulsoup4', 're', 'csv'],
    license="MIT",
)
