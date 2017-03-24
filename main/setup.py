from distutils.core import setup
setup(name='cs-academic-fair',
      version='17.03.24',
      py_modules=['jeopardy-tk'],
	  package_data={'academic-fair': ['data/*.dat']},
      )
