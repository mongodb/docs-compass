.. procedure:: 
   :style: normal 

   .. step:: Paste your connection string. 

      If you have the connection string for your deployment available, you can 
      paste the string directly into the dialog box. You can use either the 
      :manual:`Standard Connection String Format 
      </reference/connection-string/#connections-standard-connection-string-format>`
      or the :manual:`DNS Seedlist Connection Format 
      </reference/connection-string/#connections-dns-seedlist>`. 
      
      To obtain the connection string for an |service| cluster: 
      
      a. Navigate to your |service| :guilabel:`Clusters` view.
            
      #. Click :guilabel:`Connect` for your desired cluster.
            
      #. Click :guilabel:`Connect with MongoDB Compass`.
            
      #. Copy the provided connection string.

      .. include:: /includes/fact-hide-connection-string-password.rst
            
      To learn how to format the connection string for a deployment that is not 
      hosted on |service|, see :manual:`Connection String URI Format </reference/connection-string>`.

   .. step:: Connect to your cluster.

      Click :guilabel:`Connect` or :guilabel:`Save & Connect` to navigate to the 
      |compass-short| :doc:`Home Page </instance>`. 
      
      The :guilabel:`Save & Connect` button prompts you to save your connection 
      string as a :ref:`Favorite Connection <favorite-connections>` and then 
      navigates to the home page. 

      .. important:: Required Access
        
        Once you are connected to your MongoDB deployment, you may require 
        specific :manual:`user roles <reference/built-in-roles/>` to access 
        various |compass-short| features. For more information on the required 
        roles for |compass-short| features, see :ref:`required-access`.
