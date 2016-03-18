===============================
setup logging for me
===============================

.. image:: https://img.shields.io/pypi/v/setup_logging_for_me.svg
        :target: https://pypi.python.org/pypi/setup_logging_for_me

.. image:: https://img.shields.io/travis/jmansilla/setup_logging_for_me.svg
        :target: https://travis-ci.org/jmansilla/setup_logging_for_me

.. image:: https://readthedocs.org/projects/setup_logging_for_me/badge/?version=latest
        :target: https://readthedocs.org/projects/setup_logging_for_me/?badge=latest
        :alt: Documentation Status


I never remember how to do python logging basic config. Do you?


* Free software: ISC license
* Documentation: https://setup_logging_for_me.readthedocs.org.

Features
--------

.. code-block:: python
    import setup_logging_for_me

    ...

    if __name__ == '__main__':
        setup_logging_for_me.basicConfig()

Which does nothing more than calling to

.. code-block:: python
    logging.basicConfig(level=logging.INFO,
                        format="%(name)s %(levelname)s %(asctime)s - %(message)s)


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
