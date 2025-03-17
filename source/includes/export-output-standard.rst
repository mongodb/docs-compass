.. code-block:: json
   :linenos:
   :copyable: false
   
   {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "type": "object", 
      "required": ["title", "year"],
      "properties": {
          "_id": {
            "type": "string",
            "description": "MongoDB's ObjectId"
          }, 
          "title": {
            "type": "string" 
   		  }, 
          "year": { 
            "type": "number"
   		  },
          "genres": {
            "type": "array",
            "items": {
              "type": "string"
          }
       },
     }
   }
