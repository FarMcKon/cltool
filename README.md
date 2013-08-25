#cltool

An Example of how to build a command line tool that can be installed using easy_install or pip.

This builds a tiny module that installs a few test command tools, *cltool1*, *cltool2*, and *cltool3*. cltool is a command line tool that uses raw bash, cltool2 is a python script that can be run as a command line tool. This project was written to teach myself how to do this, and due to the dearth of good tutorials. 

## Installing cltool 
To install cltool,  you can simply run 

    pip install cltool

Once that is done, cltool package will be installed, and the commands *cltool1*, *cltool2* and *cltool3* will be avaliable from your command line. If you want to see exactly which cltool or cltool2 was installed, you can simply run:
    
    which cltool1
    which cltoo2
    which cltool3

### cltool1 is:
An example raw bash script that you can run from the command line, to print out a hello world

### cltool2 is:
An example python file that is launched by bash script that you can run from the command line, to print out a hello world

### cltool3 is:
An easy_install/pip generated command line script that launches directly to a function in a python package.

## Some of the Nifty Stuff in setup.py

### use the future but avoid unicode 
The __future__ import block is to make forward compatiblity with Python3 easier. Usually it looks like: 

    from __future__ import ( unicode_literals, print_function, with_statement, absolute_import )

Howerver in our installer it is

    from __future__ import ( print_function, with_statement, absolute_import )

When building an installer, unicode_literals has some bugs related to the fact that zip file format (and many zip tools) don't process unicode filenames well. In installers, it's ofter quicker to remove that line then to fight the errors. 

### Try to use distrbute, but fallback if you need to 
The initial try block is trying to use new distribute_setup rather than the older setuptools.  I am not entirely sure of the diference, but I've seen several things on the internet suggesting it's the way to do things.

### Version can be tricky
The version search assumes version is saved as __version__ (some older packages use VERSION) in the init file of the project.  It aslo assomes version is an outright variable, not built from some other value or object. Double check where and how version is used before using it. Some people import the project to get the version number, but I've encountered some weird bugs trying that.  Although it's a hack, I suggest the file-search version of getting the module version.

###Use 'where' for package search readability
For clarity, I always set 'where' in find_packages. It makes clearer reading for people new to your project/system.

### scripts, the magic
The setup value 'scripts' is where the magic is for *os specific tools*  That simple line does the work of grabbing those scripts, and adding them to the path on the installed system when the install happens.  Sadly, this is not very cross-platform. Your scripts need to be OS specific, and you can not load directly into endpoints in your program.  So, for example, .exe wrappers are not created for windows.  For cross platform magic, see the entry_points info below, which is better.

### entry_points, even moar magic!
The setup value 'entry_points' is even more magical. Entry_points in general is used to give other packages info on where to connect to your module.  The'console_scripts' value in entry_points is the most magic, and **as your module installs, the host OS will build what it needs to run that at the commandline*. Magic!!!1!! The entry is in the form of :

    entry_points = { 'console_scripts': ['cmdline_tool_name= package:function_to_run',] } 

For my example app, that line is:

    entry_points = {'console_scripts': [ 'cltool3= cltool:command_line_runner',]  }

On windows you will get a proper .exe created and added to your path. On *nix you get a small script that launches that entry point. In both cases, the installing host handles the problem of how to make sure the console tool works.


# Testing
Testing a distributed package can be tough. I have a separate file called [TESTING.md](TESTING.md) which covers how to test a new package in full.  For quick and dirty testing you can run two lines to see how things work.

    python setup.py sdist bdist_egg # build your egg, and your standard distribution
    python setup.py develop #do a developer install in that console window

As always *python setup.py develop --help* will give you some great commands and semi-clear notes on what they do.  If you want to use pypitest to test the module before releasing, see the [TESTING.md](TESTING.md) doc for more info.

# Releasing
Once you have tweaked, tested, and are sure your module (mostly) works, you can publish your module to PyPi so that other users can run *pip install <module>* and use it.  I recommend reading [RELEASING.md](RELEASING.md for more info on how to release.  But if you just want to release it quick and dirty, you can do that [by registering at PyP](http://pypi.python.org/pypi?%3Aaction=register_form) and then running: 

    python setup.py register sdist bdist_egg upload 

##See Also: 
- http://parijatmishra.wordpress.com/2008/10/13/python-packaging-custom-scripts/
- http://peak.telecommunity.com/DevCenter/setuptools#non-package-data-files


Happy Hacking,
- (Far McKon)[http://FarMcKon.net]
