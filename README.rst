octoAPy
=======

**Python wrapper for Github API**

Easy to use methods for using Github API in your favourite language python!

Let's start!
------------

.. code-block:: python

    >>> from octopy import octopy
    >>> apiobj = octopy("mbad0la","$password")
    >>> apiobj.me()
    {u'disk_usage': 11046, u'private_gists': 0, u'public_repos': 34, ...}


Similar easy the use methods to  fulfill your requirements.

You need to get Client ID and Client secret to use authentication in your app. Read more about it `here <https://developer.github.com/v3/oauth/>`_.

Contributing
------------

As a lot of API endpoints are yet uncovered, any contribution to include more endpoints is much appreciated. It would be appreciated if pull requests follow the coding practices used in the project. It would allow me to merge your requests quicker and maintain code readability.
