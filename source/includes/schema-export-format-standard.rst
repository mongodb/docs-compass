Standard format schema objects contain the following fields:

.. list-table::
   :header-rows: 1
   :widths: 35 25 40
 
   * - Property
     - Data type
     - Description

   * - ``type``
     - string or array
     - |bson| type of this data type. For details, see the `official JSON 
       docs <https://json-schema.org/draft/2020-12/json-schema-validation#name-type>`_.

   * - ``required``
     - string or array
     - Fields that must appear in the schema. For details, see the 
       `official JSON docs <https://json-schema.org/draft/2020-12/json-schema-validation#name-required>`_.

   * - ``properties``
     - document
     - Properties for each field, such as ``type`` and ``description``.
       For details, see the `official JSON docs 
       <https://json-schema.org/draft/2020-12/json-schema-core#section-10.3.2.1>`_.
 
   * - ``properties.<field>.type``
     - string
     - The data type of the ``<field>``.

   * - ``properties.<field>.description``
     - string
     - Human-readable description of the ``<field>``. 

   * - ``properties.<field>.items``
     - document
     - Types of elements in array fields. For details, see the `official
       JSON docs <https://json-schema.org/draft/2020-12/json-schema-core#section-10.3.1.2>`_.

