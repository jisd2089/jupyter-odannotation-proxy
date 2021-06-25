import setuptools
from os import path


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="jupyter-odannotation-proxy",
    version='0.1.0',
    url="https://github.com/jisd2089/jupyter-odannotation-proxy",
    author="jisd2089",
    description="jisd09042333@126.com",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
	keywords=['jupyter', 'Odannotation IDE', 'jupyterhub'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy>=1.5.0'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'odannotation = jupyter_odannotation_proxy:setup_odannotation',
        ]
    },
    package_data={
        'jupyter_odannotation_proxy': ['icons/example: foo.svg'],
    },
)
