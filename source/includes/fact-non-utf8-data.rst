If Compass encounters data display issues when querying your data 
with the error message: ``Invalid UTF-8 string in BSON document``. You 
can disable UTF8 validation by setting the ``enableUtf8Validation`` 
URI option to false. 

The following URI disables UTF8 validation:

.. code-block:: javascript

      mongodb://localhost:27017/?enableUtf8Validation=false

.. note::

   You can also disable this option in the 
   :guilabel:`Advanced Connection Options` by 
   selecting the key :guilabel:`enableUtf8Validation` and entering 
   the value ``false``.
