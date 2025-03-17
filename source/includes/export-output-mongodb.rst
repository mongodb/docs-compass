.. code-block:: json
   :linenos:
   :copyable: false

   { 
      $jsonSchema: {
        bsonType: "object", 
        required: ["title", "year"],
        properties: {
          _id: {
            bsonType: "objectId"
          }, 
          title: { 
            bsonType: "string",
            description: "Title must be a string",
          }, 
          year: { 
            bsonType: "int",
            description: "Year must be an integer"
          },
          genres: {
            bsonType: "array",
            items: {
              bsonType: "string"
            },
            description: "Genres must be an array of strings"
          },
        }
      }
   }
