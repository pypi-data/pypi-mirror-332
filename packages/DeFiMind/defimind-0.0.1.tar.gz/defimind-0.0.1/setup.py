from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='DeFiMind',
      version='0.0.1',
      description='DeFiMind',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/defimind-ai/defimind',
      author = "icmoore",
      author_email = "defimind.agent@gmail.com",
      license='MIT',
      package_dir = {"defimind": "python/prod"},
      packages=[
          'defimind',
          'defimind.erc'
      ],   
      zip_safe=False)
