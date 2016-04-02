Sample Related Tables
-------------------------------

SampleAges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores sample ages. Ages are assigned to a Chronology.
Because there may be more than one Chronology for a Collection Unit,
samples may be assigned different ages for different Chronologies. A
simple example is one sample age in radiocarbon years and another in
calibrated radiocarbon years. The age units are an attribute of the
Chronology.

+-------------------------+----------------+------+----------------+
| **Table: SampleAges**                                            |
+-------------------------+----------------+------+----------------+
| SampleAgeID             | Long Integer   | PK   |                |
+-------------------------+----------------+------+----------------+
| SampleID                | Long Integer   | FK   | Samples        |
+-------------------------+----------------+------+----------------+
| ChronologyID            | Long Integer   | FK   | Chronologies   |
+-------------------------+----------------+------+----------------+
| Age                     | Double         |      |                |
+-------------------------+----------------+------+----------------+
| AgeYounger              | Double         |      |                |
+-------------------------+----------------+------+----------------+
| AgeOlder                | Double         |      |                |
+-------------------------+----------------+------+----------------+

**SampleAgeID (Primary Key)** An arbitrary Sample Age identification
number.

**SampleID (Foreign Key)** Sample identification number. Field links to
the `Samples <#_Table:_Samples>`__ table.

**ChronologyID (Foreign Key)** Chronology identification number. Field
links to the `Chronologies <#_Table:_Chronologies>`__ table.

**Age** Age of the sample

**AgeYounger** Younger error estimate of the age. The definition of
this estimate is an attribute of the Chronology. Many ages do not have
explicit error estimates assigned.

**AgeOlder** Older error estimate of the age.

SQL Example
`````````````````````````````

This query lists the Sample Ages for the default Chronologies for «».
The CollectionUnit.Handle indicates that there is only one Collection
Unit from this site. There are two default Chronologies, one in
«Radiocarbon years BP» and the other in «Calibrated radiocarbon years
BP».

.. code-block:: sql
   :linenos:

   SELECT Sites.SiteName, CollectionUnits.Handle, SampleAges.Age,
   AgeTypes.AgeType

   FROM AgeTypes INNER JOIN (((Sites INNER JOIN CollectionUnits ON
   Sites.SiteID = CollectionUnits.SiteID) INNER JOIN Chronologies ON
   CollectionUnits.CollectionUnitID = Chronologies.CollectionUnitID) INNER
   JOIN SampleAges ON Chronologies.ChronologyID = SampleAges.ChronologyID)
   ON AgeTypes.AgeTypeId = Chronologies.AgeTypeID

   WHERE (((Sites.SiteName)="Muskox Lake") AND
   ((Chronologies.IsDefault)=True));

The first five lines of the result for each Age Type:

+----------------+--------------+-----------+-----------------------------------+
| **SiteName**   | **Handle**   | **Age**   | **AgeType**                       |
+----------------+--------------+-----------+-----------------------------------+
|                | MUSKOX       | -50       | Radiocarbon years BP              |
+----------------+--------------+-----------+-----------------------------------+
|                | MUSKOX       | 538       | Radiocarbon years BP              |
+----------------+--------------+-----------+-----------------------------------+
|                | MUSKOX       | 1125      | Radiocarbon years BP              |
+----------------+--------------+-----------+-----------------------------------+
|                | MUSKOX       | 1712      | Radiocarbon years BP              |
+----------------+--------------+-----------+-----------------------------------+
|                | MUSKOX       | 2300      | Radiocarbon years BP              |
+----------------+--------------+-----------+-----------------------------------+
|                | MUSKOX       | -50       | Calibrated radiocarbon years BP   |
+----------------+--------------+-----------+-----------------------------------+
|                | MUSKOX       | 604       | Calibrated radiocarbon years BP   |
+----------------+--------------+-----------+-----------------------------------+
|                | MUSKOX       | 1258      | Calibrated radiocarbon years BP   |
+----------------+--------------+-----------+-----------------------------------+
|                | MUSKOX       | 1912      | Calibrated radiocarbon years BP   |
+----------------+--------------+-----------+-----------------------------------+
|                | MUSKOX       | 2567      | Calibrated radiocarbon years BP   |
+----------------+--------------+-----------+-----------------------------------+

