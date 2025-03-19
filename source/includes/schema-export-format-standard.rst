Standard format schema objects contain the following fields:

.. list-table::
   :header-rows: 1
   :widths: 35 25 40
 
   * - Property
     - Data type
     - Description

   * - ``type``
     - string or array
     - JSON type of this data type. For details, see the `official JSON 
       docs <https://json-schema.org/draft/2020-12/json-schema-validation#name-type>`_.

   * - ``required``
     - array of strings
     - Fields that must appear in the schema. For details, see the 
       `official JSON docs <https://json-schema.org/draft/2020-12/json-schema-validation#name-required>`_.

   * - ``properties``
     - document
     - Properties for each field. Each subdocument may contain fields 
       like ``type``. For details, see the `official JSON docs 
       <https://json-schema.org/draft/2020-12/json-schema-core#section-10.3.2.1>`_.
 
   * - ``items``
     - document
     - Metadata about elements in array fields. Each subdocument may contain
       fields like ``type``. For details, see the `official
       JSON docs <https://json-schema.org/draft/2020-12/json-schema-core#section-10.3.1.2>`_.

