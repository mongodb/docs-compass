.. note:: Large Integer Limitations
    To use a query filter that finds integers over the JavaScript maximum integer size, you must wrap the number value in string characters.

    For example, to find all documents with an integer value of 507550989629521900, use the
    following query filter:

    .. code-block:: javascript

        { "number": "507550989629521900" }