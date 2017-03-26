from distutils.core import setup
setup(name='jeopardy',
      version='17.03.26',
      py_modules=['jeopardy-tk'],
	  package_data={'jeopardy': ['data/*.dat']},
      )
