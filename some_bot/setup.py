from setuptools import setup, find_namespace_packages

setup(name='some_bot',
      version='1.5',
      description='Bot which works with phone book and calendar',
      url='',
      author='Oshmarin Sergii',
      author_email='sergiioshmarin@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['somebot=some_bot.somebot:main']})