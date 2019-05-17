from setuptools import setup
setup(name='poloniex',
      version='0.5.0',
      description='Poloniex API wrapper for Python 2.7 and 3',
      url='https://github.com/s4w3d0ff/python-poloniex',
      author='s4w3d0ff',
      license='GPL v2',
      packages=['poloniex'],
      install_requires=['requests', 'websocket_client'],
      zip_safe=False)
