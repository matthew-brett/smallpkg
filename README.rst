##########################
Package for sphinx testing
##########################

::

    mkvirtualenv test
    pip install -e .
    pip install numpydoc sphinx
    cd doc
    make html
