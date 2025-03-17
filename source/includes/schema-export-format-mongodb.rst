MongoDB format schema objects contain the following fields:

.. list-table::
   :header-rows: 1
   :widths: 35 25 40
 
   * - Property
     - Data type
     - Description

   * - ``bsonType``
     - string 
     - |bson| type of this field.

   * - ``required``
     - string or array
     - Fields that must appear in the schema. 

   * - ``properties``
     - document
     - Properties for each field, such as ``bsonType`` and 
       ``description``.
 
   * - ``properties.<field>.bsonType``
     - string
     - The |bson| data type of the ``<field>``.

   * - ``properties.<field>.description``
     - string
     - Human-readable description of the ``<field>``. 

   * - ``properties.<field>.items.bsonType``
     - document
     - Type of elements in array fields. 
