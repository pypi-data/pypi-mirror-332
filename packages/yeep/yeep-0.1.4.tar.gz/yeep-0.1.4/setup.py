from setuptools import setup, find_packages
import os


def readme():
  """Read README.md and return its contents."""
  with open('README.md', encoding='utf-8') as f:
    return f.read()


setup(
  name='yeep',
  version='0.1.4',
  description='Простая и мощная библиотека для работы с PostgreSQL',
  long_description=readme(),
  long_description_content_type='text/markdown',
  author='Tima Yeep',
  author_email='timik277@gmail.com',
  url='https://github.com/Timok277/yeep',
  packages=find_packages(),
  install_requires=[
    'psycopg2-binary>=2.9.0',
    'python-dotenv>=0.19.0'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Database',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ],
  python_requires='>=3.7',
  keywords='postgresql database orm sql',
)