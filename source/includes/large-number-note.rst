.. note:: Large Integer Limitations

    To query for integers larger than the JavaScript maximum integer size,
    wrap the integer in string characters.

    For example, to find all documents with a ``number`` value of ``507550989629521900``, use
    this query filter:

    .. code-block:: javascript

        { "number": "507550989629521900" }