Compass can have issues displaying collections if documents have 
invalid UTF8 characters.

If you attempt to query or export this data, the following error 
message displays: 

.. code-block:: none
   :copyable: false

   Invalid UTF-8 string in BSON document. 

In order to query or export this data, you can disable 
UTF8 validation by setting the ``enableUtf8Validation`` URI option to 
``false``. 

.. warning::

   **Editing data** with ``enableUtf8Validation=false`` can result in 
   potential loss of data. This approach is a temporary workaround to 
   query or export data only.

The following URI disables UTF8 validation:

.. code-block:: javascript

      mongodb://localhost:27017/?enableUtf8Validation=false


.. note::

   You can also disable this option in the 
   :ref:`Advanced Connection Options <advanced-connection-tab>` by 
   selecting the key :guilabel:`enableUtf8Validation` and entering 
   the value ``false``.
