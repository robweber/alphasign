import setuptools
setuptools.setup(
  name = 'alphasign',
  version = '1.1',
  packages = setuptools.find_packages(),

  install_requires = ['pyserial>=3.5', 'pyusb>=1.2.1', 'pyyaml>=5.1'],

  author = 'Matt Sparks',
  author_email = 'ms@quadpoint.org',
  description = 'Implementation of the Alpha Sign Communications Protocol',
  long_description = ('Implementation of the Alpha Sign Communications '
                      'Protocol, which is used by many commercial LED signs, '
                      'including the Betabrite.'),
  url = 'https://github.com/robweber/alphasign',
  license = 'BSD',
)
