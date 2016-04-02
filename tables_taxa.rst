Taxonomy Related Tables
--------------------------------

EcolGroups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Taxa are assigned to Sets of Ecological Groups. A taxon may be assigned
to more than one Set of Ecological Groups, representing different
schemes for organizing taxa.

+-------------------------+----------------+----------+------------------+
| **EcolGroups**                                                  |
+-------------------------+----------------+----------+------------------+
| TaxonID                 | Long Integer   | PK, FK   | Taxa             |
+-------------------------+----------------+----------+------------------+
| EcolSetID               | Long Integer   | PK, FK   | EcolSetTypes     |
+-------------------------+----------------+----------+------------------+
| EcolGroupID             | Text           | FK       | EcolGroupTypes   |
+-------------------------+----------------+----------+------------------+

**TaxonID (Primary Key, Foreign Key)** Taxon identification number.
Field links to the `Taxa <#_Table:_Taxa>`__ table.

**EcolSetID (Primary Key, Foreign Key)** Ecological Set identification
number. Field links to the `EcolSetTypes <#_Table:_EcolSetTypes>`__
table.

**EcolGroupID (Foreign Key)** A four-letter Ecological Group
identification code. Field links to the
`EcolGroupTypes <#table-ecolgrouptypes>`__ table.

SQL Example
`````````````````````````````

The following query produces a list of Ecological Groups for vascular
plants (VPL).

.. code-block:: sql
   :linenos:

   SELECT Taxa.TaxaGroupID, EcolGroups.EcolGroupID,
   EcolSetTypes.EcolSetName, EcolGroupTypes.EcolGroup

   FROM EcolSetTypes INNER JOIN (EcolGroupTypes INNER JOIN (Taxa INNER JOIN
   EcolGroups ON Taxa.TaxonID = EcolGroups.TaxonID) ON
   EcolGroupTypes.EcolGroupID = EcolGroups.EcolGroupID) ON
   EcolSetTypes.EcolSetID = EcolGroups.EcolSetID

   GROUP BY Taxa.TaxaGroupID, EcolGroups.EcolGroupID,
   EcolSetTypes.EcolSetName, EcolGroupTypes.EcolGroup

   HAVING (((Taxa.TaxaGroupID)="VPL"));

Result:

+-------------------+-------------------+-------------------+-----------------------------------+
| **TaxaGroupID**   | **EcolGroupID**   | **EcolSetName**   | **EcolGroup**                     |
+-------------------+-------------------+-------------------+-----------------------------------+
| VPL               | ANAC              | Default plant     | Anachronic                        |
+-------------------+-------------------+-------------------+-----------------------------------+
| VPL               | AQVP              | Default plant     | Aquatic Vascular Plants           |
+-------------------+-------------------+-------------------+-----------------------------------+
| VPL               | TRSH              | Default plant     | Trees and Shrubs                  |
+-------------------+-------------------+-------------------+-----------------------------------+
| VPL               | UNID              | Default plant     | Unknown and Indeterminable        |
+-------------------+-------------------+-------------------+-----------------------------------+
| VPL               | UPHE              | Default plant     | Upland Herbs                      |
+-------------------+-------------------+-------------------+-----------------------------------+
| VPL               | VACR              | Default plant     | Terrestrial Vascular Cryptogams   |
+-------------------+-------------------+-------------------+-----------------------------------+

SQL Example
`````````````````````````````

This query lists all the taxa in the Ecological Group «Sirenia».

.. code-block:: sql
   :linenos:

   SELECT EcolGroupTypes.EcolGroup, Taxa.TaxonName

   FROM EcolGroupTypes INNER JOIN (Taxa INNER JOIN EcolGroups ON
   Taxa.TaxonID = EcolGroups.TaxonID) ON EcolGroupTypes.EcolGroupID =
   EcolGroups.EcolGroupID

   WHERE (((EcolGroupTypes.EcolGroup)="Sirenia"));

Result:

+-----------------+----------------------+
| **EcolGroup**   | **TaxonName**        |
+-----------------+----------------------+
| Sirenia         | Dugongidae           |
+-----------------+----------------------+
| Sirenia         | Hydrodamalis gigas   |
+-----------------+----------------------+
| Sirenia         | Sirenia              |
+-----------------+----------------------+
| Sirenia         | Trichechidae         |
+-----------------+----------------------+
| Sirenia         | Trichechus manatus   |
+-----------------+----------------------+
| Sirenia         | Hydrodamalis         |
+-----------------+----------------------+
| Sirenia         | Trichechus           |
+-----------------+----------------------+

 EcolGroupTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Ecological Group Types. Table is referenced by the
`EcolGroups <#_Table:_EcolGroups>`__ table.

+-----------------------------+--------+------+-----+
| **EcolGroupTypes**                         |
+-----------------------------+--------+------+-----+
| EcolGroupID                 | Text   | PK   |     |
+-----------------------------+--------+------+-----+
| EcolGroup                   | Text   |      |     |
+-----------------------------+--------+------+-----+

**EcolGroupID (Primary Key)** An arbitrary Ecological Group
identification number.

**EcolGroup**: Ecological Group.

EcolSetTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Ecological Set Types. Table is referenced by the
`EcolGroups <#_Table:_EcolGroups>`__ table.

+---------------------------+----------------+------+-----+
| **EcolSetTypes**                                 |
+---------------------------+----------------+------+-----+
| EcolSetID                 | Long Integer   | PK   |     |
+---------------------------+----------------+------+-----+
| EcolSetName               | Text           |      |     |
+---------------------------+----------------+------+-----+

**EcolSetID (Primary Key)** An arbitrary Ecological Set identification
number.

**EcolSetName** Ecological Set name.

