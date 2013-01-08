
print "setup.py happening"
from setuptools import setup, find_packages

from distutils.core import setup
from distutils.command.build_py import build_py
from distutils.command.build_scripts import build_scripts
 
## Post install object class, extends behavior
## I could not get this to work
#from distutils.command.install_data import install_data
#class post_install(install_data):
#        def run(self):
#            print "Custom install_data created"
#            # Call parent 
#            install_data.run(self)
#            # Execute commands
#            print "Running Custom Post Install"
#        def append_to_bashrc(self):
#            print "FUUUUUUUCK yeah. Appending myself to .bashrc"
#            import pdb
#            pdb.set_trace()

setup(
    name='cltool',
    version='0.5.0.4',
    description='example of installing a comand line tool via pip/easy_install',
    #cmdclass={"install_data": post_install},
    packages=find_packages(where='.'),
    include_package_data=True,
    zip_safe=False,
    scripts=['scripts/cltool','scripts/cltool2','scripts/cltool3'],
)
   
