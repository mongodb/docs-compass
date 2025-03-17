Expanded format schema objects contain the following fields:

.. list-table::
   :header-rows: 1
   :widths: 35 25 40
 
   * - Property
     - Data type
     - Description

   * - ``type``
     - string
     - Data type of the field.

   * - ``x-bsonType``
     - string or array
     - |bson| type of this field.

   * - ``x-metadata``
     - document
     - Document containing metadata about the field.

   * - ``x-metadata.hasDuplicates``
     - boolean
     - ``true`` if a single value of this data type appears multiple 
       times in the corresponding field. Otherwise ``false``.

   * - ``x-metadata.probability``
     - float
     - Probability that the value of the corresponding field is this 
       data type in a random document.

   * - ``x-metadata.count``
     - integer
     -  Number of documents sampled from the collection.

   * - ``x-sampleValues``
     - array
     - Sample values as Expanded JSON.
