# Document on how to release well.

## Testing
Do testing (on TestPyPi)[./TESTING].

## Releasing
Register for (an account on PyPi)[http://pypi.python.org/pypi?%3Aaction=register_form].  Then simply run
    
    python setup.py register sdist bdist_egg upload 

of course, once that is done, you'll want to test installing it by running:

    pip install --upgrade --verbose <your_module_name>

