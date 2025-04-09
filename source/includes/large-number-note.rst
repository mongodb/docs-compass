.. note:: Large Integer Limitations

    To run a query that filters for integers over the JavaScript maximum integer size,
    wrap the number value in string characters.

    For example, to find all documents with an ``number`` value of ``507550989629521900``, use
    the following query filter:

    .. code-block:: javascript

        { "number": "507550989629521900" }