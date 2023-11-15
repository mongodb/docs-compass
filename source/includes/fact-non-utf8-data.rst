Compass can have issues displaying collections if documents within
the collection have invalid UTF8 characters.

If you attemp to query or export this data, the following error 
message displays: 

.. code-block:: none
   :copyable: false

   Invalid UTF-8 string in BSON document. 

In order to query or export this data, you can disable 
UTF8 validation by setting the ``enableUtf8Validation`` URI option to 
``false``. 

The following URI disables UTF8 validation:

.. code-block:: javascript

      mongodb://localhost:27017/?enableUtf8Validation=false

.. note::

   You can also disable this option in the 
   :guilabel:`Advanced Connection Options` by 
   selecting the key :guilabel:`enableUtf8Validation` and entering 
   the value ``false``.
