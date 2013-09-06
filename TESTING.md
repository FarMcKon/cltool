# Testing
This doc covers some testing topics when trying to make a python distributable, and especially when trying to make a python distributable that delivers a command line tool.

## Testing Locally
For quick and dirty testing you can run two lines to see how things work.

    python setup.py sdist bdist_egg # build your egg, and your standard distribution
    python setup.py develop #do a developer install on your local machine 

That will install the tool in your local machine. Beware that the install will 'leak' to new terminal windows

## Testing using pypitest
Python Package Index (pypi) is the place pip or easy_install goes to fetch packages by name.   There is a test site for it called pypitest which is rather a pain to use.  This will walk you through using pypitest for testing your package.

## Example pypirc
To get your machine to talk to the pypitest server, you will need to make a sever configuration for the pypirc server.  You can just use a basic config included below.  Just save that (cut and paste your username, 'natch) as ~/.pypirc and keep rolling.
 
    [distutils]
    index-servers =
        pypi
        pypitest

    [pypi]
    username:FarMcKon

    [pypitest]
    repository: http://testpypi.python.org/pypi
    username:FarMcKon

### Build and send your module to pypitest server
Add more info on this here

    python setup.py register -r pypitest sdist bdist_egg upload -r pypitest

### Setup a virtualenv to test your pip install
Virtual Environments (virtualenv) is the best way to test installs, by putting them in a sandbox to see if they work. There are [some great virtualenv tutorials](http://iamzed.com/2009/05/07/a-primer-on-virtualenv/) and a quick reminder of how to fire up a virtualenv is below

    virtualenv --no-site-packages testmyproject
    cd testmyproject
    source bin/activate

### Test your pip install from pypitest with verbose info and debugging 
Add more info on the pip install options here

    pip install --upgrade --verbose --index-url http://testpypi.python.org/pypi/ cltool
