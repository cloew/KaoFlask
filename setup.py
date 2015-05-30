from distutils.core import setup

setup(name='kao_flask',
      version='0.1',
      description='Python Flask Wrapper',
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      #url='http://www.python.org/sigs/distutils-sig/',
      packages=['kao_flask', 'kao_flask.controllers', 'kao_flask.ext', 
                'kao_flask.ext.sqlalchemy', 'kao_flask.ext.stormpath'],
     )