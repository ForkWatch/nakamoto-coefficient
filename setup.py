from setuptools import setup

setup(name='nakamoto',
      version='0.1',
      description='generate nakamoto coefficient of cryptocurrency',
      author='Yaz Khoury',
      email='yaz.khoury@gmail.com',
      license='MIT',
      packages=['nakamoto'],
      install_requires=[
          'markdown',
      ],
      zip_safe=False
)
