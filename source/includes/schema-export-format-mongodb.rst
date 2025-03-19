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
     - Properties for each field, such as ``bsonType``.

   * - ``items``
     - document
     - Metadata about elements in array fields.
