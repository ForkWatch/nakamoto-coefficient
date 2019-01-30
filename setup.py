from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="nakamoto",
      version="0.1.3",
      author="Yaz Khoury",
      author_email="yaz.khoury@gmail.com",
      description="Python Library to Generate Nakamoto Coefficient",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/YazzyYaz/nakamoto-coefficient",
      license="MIT",
      packages=find_packages(),
      install_requires=[
          "numpy",
          "pandas",
          "requests",
          "plotly",
          "PyGithub",
          "requests_html"
      ],
      zip_safe=False
)
