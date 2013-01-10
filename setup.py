from __future__ import ( print_function, with_statement, absolute_import )
import sys
# When possible, use distribute_setup's version of tools
try:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
except ImportError:
    from setuptools import setup, find_packages
if sys.version >= '2.3':
  import re, os, sys
  version = re.search(
        "__version__.*'(.+)'",
        open(os.path.join('cltool','__init__.py')).read()).group(1)
else:
    raise Exception("only python 2.3 or newer supported")

setup(
    name='cltool',
    version= version,
    description='Example of installing a comand line tool via pip/easy_install',
    author='Far McKon',
    author_email='FarMcKon@gmail.com',
    url='https://github.com/farmckon/cltool#cltool',
    packages=find_packages(where='.'),
    include_package_data=True,
    zip_safe=False,
    scripts=['scripts/cltool1','scripts/cltool2',],
    entry_points={
        'console_scripts': [ 'cltool3= cltool:command_line_runner',]  },
)
   
