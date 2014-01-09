from setuptools import setup, find_packages

setup(name='pyflwor',
      version='1.0',
      description=(
        'A object query system for arbitrary python objects..'
      ),
      author='Tim Henderson',
      author_email='tim.tadh@gmail.com',
      url='https://www.github.com/timtadh/pyflwor',
      license='BSD',
      packages=find_packages(),
      install_requires=[
        'ply',
      ],
      tests_require=[
        'nose'
      ],
      test_suite='pyflwor.tests',
      extras_require = {
        'repl':  ['getline']
      },
      dependency_links = [
        'https://github.com/timtadh/getline/tarball/master#egg=getline',
    ]
)
