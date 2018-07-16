How did I do that?
**************************

.. _Anaconda: https://www.anaconda.com/download

Here, we will explain how to set up Sphinx for a code written in Python. Here are the steps:

1. Go to Anaconda_, and select the Python version for you.

2. Type: 

    .. code-block:: bash
        
        $ pip install sphinx

    in your terminal. This will install sphinx for you.

3. Clone your repository from Github. I assume here that you have some directory with all of your Python code (at least, all of the Python code you want to document) in a single directory. In this example I have used `src` as my directory holding my Python code.

4. Type:

    .. code-block:: bash

        $ sphinx-quickstart

   Here is what I used:

    .. code-block:: none

        Welcome to the Sphinx 1.6.6 quickstart utility.

        Please enter values for the following settings (just press Enter to
        accept a default value, if one is given in brackets).

        Enter the root path for documentation.
        > Root path for the documentation [.]: 

        You have two options for placing the build directory for Sphinx output.
        Either, you use a directory "_build" within the root path, or you separate
        "source" and "build" directories within the root path.
        > Separate source and build directories (y/n) [n]: y

        Inside the root directory, two more directories will be created; "_templates"
        for custom HTML templates and "_static" for custom stylesheets and other static
        files. You can enter another prefix (such as ".") to replace the underscore.
        > Name prefix for templates and static dir [_]: 

        The project name will occur in several places in the built documentation.
        > Project name: Documentation
        > Author name(s): Kevin Ryczko

        Sphinx has the notion of a "version" and a "release" for the
        software. Each version can have multiple releases. For example, for
        Python the version is something like 2.5 or 3.0, while the release is
        something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
        just set both to the same value.
        > Project version []: 0.0.1
        > Project release [0.0.1]: 

        If the documents are to be written in a language other than English,
        you can select a language here by its language code. Sphinx will then
        translate text that it generates into that language.

        For a list of supported codes, see
        http://sphinx-doc.org/config.html#confval-language.
        > Project language [en]: 

        The file name suffix for source files. Commonly, this is either ".txt"
        or ".rst".  Only files with this suffix are considered documents.
        > Source file suffix [.rst]: 

        One document is special in that it is considered the top node of the
        "contents tree", that is, it is the root of the hierarchical structure
        of the documents. Normally, this is "index", but if your "index"
        document is a custom template, you can also set this to another filename.
        > Name of your master document (without suffix) [index]: 

        Sphinx can also add configuration for epub output:
        > Do you want to use the epub builder (y/n) [n]: 

        Please indicate if you want to use one of the following Sphinx extensions:
        > autodoc: automatically insert docstrings from modules (y/n) [n]: y
        > doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
        > intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
        > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
        > coverage: checks for documentation coverage (y/n) [n]: y
        > imgmath: include math, rendered as PNG or SVG images (y/n) [n]: n
        > mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
        > ifconfig: conditional inclusion of content based on config values (y/n) [n]: y
        > viewcode: include links to the source code of documented Python objects (y/n) [n]: y
        > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: y

        A Makefile and a Windows command file can be generated for you so that you
        only have to run e.g. `make html' instead of invoking sphinx-build
        directly.
        > Create Makefile? (y/n) [y]: y
        > Create Windows command file? (y/n) [y]: n

        Creating file ./source/conf.py.
        Creating file ./source/index.rst.
        Creating file ./Makefile.

        Finished: An initial directory structure has been created.

        You should now populate your master file ./source/index.rst and create other documentation
        source files. Use the Makefile to build the docs, like so:
           make builder
        where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

5. Now, edit the file `conf.py` and make the following changes:

.. code-block:: python

    import os
    import sys
    sys.path.insert(0, os.path.abspath('../src'))

This will be commented out. So you must uncomment it and change the path (i.e. `../src`) to whatever directory you have your source code in.

Also, add `numpydoc` like so:

.. code-block:: python

    extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'numpydoc']

6. Go to your code, and add docstrings where ever you would like to document your code. An example is the following:

.. code-block:: python

    class Something:
        """
        This is the doc string for something, here you should explain what this class does.
        Why is this class useful. You can even give examples of how you would use it here.

        Arguments
        ---------
        file_name : A string which is the file name of some file I would like to open.
        """
        def __init__(self, file_name):
            self.file_name = file_name

        def openFile(self):
            """
            This function opens the file that is passed into the class.

            Arguments
            ---------
            None

            Returns
            -------
            A file object.
            """

            return open(self.file_name, 'r')

6. Now we would like to create documentation from the docstrings that we have entered here. What we're going to do is now look at our directory tree. Our files should be in a folder, which is called the package name. In this case it is something. Along with this, there must be a file called "__init__.py". Make sure you type:

.. code-block:: bash

    $ touch ../src/__init__.py

Along with this, we will create a file called something.rst which is in the same directory as "index.rst". This file will have the following:

.. code-block:: rst
    
    Something class
    **************************

    .. automodule:: something.Something
        :members:

This is including the file "something.py" and saying we want to document the class "Something". The "automodule" and ":members:" handles collecting all of the documentented functions inside the class. We then want to modify the file "index.rst" as such:

.. code-block:: rst

    .. Documentation documentation master file, created by
   sphinx-quickstart on Mon Jul 16 14:30:52 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


    Welcome to Documentation's documentation!
    =========================================

    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       something

    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`

All I did here is add the keyword "something" underneath the Contents.

7. We now want to modify our Makefile as such:

.. code-block:: bash

    # Minimal makefile for Sphinx documentation
    #

    # You can set these variables from the command line.
    SPHINXOPTS    =
    SPHINXBUILD   = sphinx-build
    SPHINXPROJ    = Documentation
    SOURCEDIR     = .
    BUILDDIR      = ../../docs-build

    # Put it first so that "make" without argument is like "make help".
    help:
            @$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

    .PHONY: help Makefile

    # Catch-all target: route all unknown targets to Sphinx using the new
    # "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
    %: Makefile
            @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

All I did here was modify the "BUILDDIR" variable. The rest is identical to the generated Makefile.

8. Now run:

.. code-block:: bash

    $ make html

build the website which will contain all of the documentation. 
