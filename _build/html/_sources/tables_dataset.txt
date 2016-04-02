Dataset & Collection Related Tables
-----------------------------------

AggregateDatasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aggregate Datasets are aggregates of samples of a particular datatype.
Some examples:

-  Plant macrofossil samples from a group of packrat middens collected
   from a particular valley, mountain range, or other similarly defined
   geographic area. Each midden is from a different Site or Collection
   Unit, but they are grouped into time series for that area and are
   published as single dataset.

-  Samples collected from 32 cutbanks along several km of , northeast .
   Each sample is from a different site, but they form a time series
   from 0-12,510 :sup:`14`\ C yr BP, and pollen, plant macrofossils, and
   beetles were published and graphed as if from a single site.

-  A set of pollen surface samples from particular region or study that
   were published and analyzed as a single dataset and submitted to the
   database as a single dataset.

The examples above are datasets predefined in the database. New
aggregate datasets could be assembled for particular studies, for
example all the pollen samples for a given time slice for a given
geographic region.

+--------------------------------+-----------------+------+-----------------------+
| **AggregateDatasets**   |
+--------------------------------+-----------------+------+-----------------------+
| AggregateDatasetID             | int             | PK   |                       |
+--------------------------------+-----------------+------+-----------------------+
| AggregateDatasetName           | nvarchar(255)   |      |                       |
+--------------------------------+-----------------+------+-----------------------+
| AggregateOrderTypeID           | int             | FK   | AggregateOrderTypes   |
+--------------------------------+-----------------+------+-----------------------+
| Notes                          | nvarchar(MAX)   |      |                       |
+--------------------------------+-----------------+------+-----------------------+

**AggregateDatasetID (Primary Key)** 
  An arbitrary Aggregate Dataset identification number.

**AggregateDatasetName** 
  Name of Aggregate Dataset.

**AggregateOrderTypeID (Foreign Key)**
  Aggregate Order Type identification number. Field links to the `AggregateOrderTypes <#_Table:_AggregateOrderTypes>`__ lookup table.

**Notes**
  Free form notes about the Aggregate Order Type.

DatasetPublications
--------------------------

This table lists the publications for datasets.

+----------------------------------+-------+----------+----------------+
| **DatasetPublications**   |
+----------------------------------+-------+----------+----------------+
| DatasetID                        | int   | PK, FK   | Datasets       |
+----------------------------------+-------+----------+----------------+
| PublicationID                    | int   | PK, FK   | Publications   |
+----------------------------------+-------+----------+----------------+
| PrimaryPub                       | bit   |          |                |
+----------------------------------+-------+----------+----------------+

**DatasetID (Primary Key, Foreign Key)** Dataset identification number.
Field links to Dataset table.

**PublicationID (Primary Key, Foreign Key)** Publication identification
number. Field links to `Publications <#_Table:_Publications>`__ table.

**PrimaryPub** Is «True» if the publication is the primary publication
for the dataset.

 Datasets
----------------

This table stores the data for Datasets. A Dataset is the set of samples
for a particular data type from a Collection Unit. A Collection Unit may
have multiple Datasets for different data types, for example one dataset
for pollen and another for plant macrofossils. Every Sample is assigned
to a Dataset, and every Dataset is assigned to a Collection Unit.
Samples from different Collection Units cannot be assigned to the same
Dataset (although they may be assigned to `Aggregate
Datasets <#_Table:_AggregateDatasets>`__).

+-----------------------+----------------+------+-------------------+
| **Datasets**   |
+-----------------------+----------------+------+-------------------+
| DatasetID             | Long Integer   | PK   |                   |
+-----------------------+----------------+------+-------------------+
| CollectionUnitID      | Long Integer   | FK   | CollectionUnits   |
+-----------------------+----------------+------+-------------------+
| DatasetTypeID         | Long Integer   | FK   | DatasetTypes      |
+-----------------------+----------------+------+-------------------+
| DatasetName           | Text           |      |                   |
+-----------------------+----------------+------+-------------------+
| Notes                 | Memo           |      |                   |
+-----------------------+----------------+------+-------------------+

**DatasetID (Primary Key)** An arbitrary Dataset identification number.

**CollectionUnitID (Foreign Key)** Collection Unit identification
number. Field links to the
`CollectionUnits <#_Table:_CollectionUnits>`__ table.

**DatasetTypeID (Foreign Key);** Dataset Type identification number.
Field links to the `DatasetTypes <#_Table:_DatasetTypes>`__ lookup
table.

**DatasetName** Optional name for the Dataset.

**Notes** Free form notes or comments about the Dataset.

SQL Example
`````````````````````````````

The following query lists the Dataset Types for the site «».

.. code-block:: sql
   :linenos:

   SELECT Sites.SiteName, DatasetTypes.DatasetType

   FROM DatasetTypes INNER JOIN ((Sites INNER JOIN CollectionUnits ON
   Sites.SiteID = CollectionUnits.SiteID) INNER JOIN Datasets ON
   CollectionUnits.CollectionUnitID = Datasets.CollectionUnitID) ON
   DatasetTypes.DatasetTypeID = Datasets.DatasetTypeID

   WHERE (((Sites.SiteName)=""));

Result:

+----------------+--------------------+
| **SiteName**   | **DatasetType**    |
+----------------+--------------------+
|                | Loss-on-ignition   |
+----------------+--------------------+
|                | pollen             |
+----------------+--------------------+
|                | geochronologic     |
+----------------+--------------------+

SQL Example
`````````````````````````````

This query lists the plant macrofossils identified at site «Bear River
No. 3».

.. code-block:: sql
   :linenos:
   SELECT Sites.SiteName, Taxa.TaxonName

   FROM DatasetTypes INNER JOIN (Taxa INNER JOIN (Variables INNER JOIN
   ((((Sites INNER JOIN CollectionUnits ON Sites.SiteID =
   CollectionUnits.SiteID) INNER JOIN Datasets ON
   CollectionUnits.CollectionUnitID = Datasets.CollectionUnitID) INNER JOIN
   Samples ON Datasets.DatasetID = Samples.DatasetID) INNER JOIN Data ON
   Samples.SampleID = Data.SampleID) ON Variables.VariableID =
   Data.VariableID) ON Taxa.TaxonID = Variables.TaxonID) ON
   DatasetTypes.DatasetTypeID = Datasets.DatasetTypeID

   GROUP BY Sites.SiteName, DatasetTypes.DatasetType, Taxa.TaxonName

   HAVING (((Sites.SiteName)="Bear River No. 3") AND
   ((DatasetTypes.DatasetType)="plant macrofossils"));

Result:

+--------------------+--------------------------------------------+
| **SiteName**       | **TaxonName**                              |
+--------------------+--------------------------------------------+
| Bear River No. 3   | Bolboschoenus maritimus subsp. paludosus   |
+--------------------+--------------------------------------------+
| Bear River No. 3   | Zea mays                                   |
+--------------------+--------------------------------------------+

DatasetSubmissions
-------------------------

Submissions to the database are of Datasets. Submissions may be original
submissions, resubmissions, compilations from other databases, or
recompilations. See the description of the
`DatasetSubmissionTypes <#_Table:_DatasetSubmissionTypes>`__ table.

+---------------------------------+----------------+------+--------------------------+
| **DatasetSubmissions**   |
+---------------------------------+----------------+------+--------------------------+
| SubmissionID                    | Long Integer   | PK   |                          |
+---------------------------------+----------------+------+--------------------------+
| DatasetID                       | Long Integer   | FK   | Datasets                 |
+---------------------------------+----------------+------+--------------------------+
| ProjectID                       | Long Integer   | FK   | Projects                 |
+---------------------------------+----------------+------+--------------------------+
| ContactID                       | Long Integer   | FK   | Contacts                 |
+---------------------------------+----------------+------+--------------------------+
| SubmissionTypeID                | Long Integer   | FK   | DatasetSubmissionTypes   |
+---------------------------------+----------------+------+--------------------------+
| SubmissionDate                  | Date/Time      |      |                          |
+---------------------------------+----------------+------+--------------------------+
| Notes                           | Memo           |      |                          |
+---------------------------------+----------------+------+--------------------------+

**SubmissionID (Primary Key)**
  An arbitrary submission identification number.

**DatasetID (Foreign Key)** 
  Dataset identification number. Field links to the `Datasets <#table-datasets>`__ table. Datasets may occur multiple times in this table (e.g. once for the original compilation into a different database and a second time for the recompilation into Neotoma).

**ProjectID (Foreign Key)**
  Database project responsible for the submission or compilation.

**ContactID (Foreign Key)**
  Contact identification number. Field links to the `Contacts <#_Table:_Contacts>`__ table. The Contact is the person who submitted, resubmitted, compiled, or recompiled the data. This person is not necessarily the Dataset PI; it is the person who submitted the data or compiled the data from the literature.

**SubmissionDate**
  Date of the submission, resubmission, compilation, or recompilation.

**SubmissionTypeID (Foreign Key)**
  Submission Type identification number. Field links to the DatasetSubmissionsType table.

**Notes**
  Free form notes or comments about the submission.

DatasetSubmissionTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Dataset Submission Types. Table is referenced by the
`DatasetSubmissions <#_Table:_DatasetSubmissions>`__ table.

+-------------------------------------+----------------+------+-----+
| **DatasetSubmissionTypes**   |
+-------------------------------------+----------------+------+-----+
| SubmissionTypeID                    | Long Integer   | PK   |     |
+-------------------------------------+----------------+------+-----+
| SubmissionType                      | Text           |      |     |
+-------------------------------------+----------------+------+-----+

**SubmissionTypeID (Primary Key)**
  An arbitrary Submission Type identification number.

**SubmissionType**
  Type of submission. The database has the following types:

  -  Original submission from data contributor

  -  Resubmission or revision from data contributor

  -  Compilation into a flat file database

  -  Compilation into a another relational database

  -  Recompilation or revisions to a another relational database

  -  Compilation into Neotoma from another database

  -  Recompilation into Neotoma from another database

  -  Compilation into Neotoma from primary source

  -  Recompilation into or revisions to Neotoma
    The initial development of Neotoma involved merging the data from several existing databases, including FAUNMAP, the Global Pollen Database, and the North American Plant Macrofossil Database. Thus original compilation of Datasets was into one of these databases, which were then recompiled into Neotoma. The original compilation and the recompilation into Neotoma are separate submissions.

SQL Example
`````````````````````````````

This query gives a list of Dataset Submissions for the site «Bear River
No. 3» ordered by date.

.. code-block:: sql
   :linenos:
   
   SELECT DatasetTypes.DatasetType, Projects.ProjectName,
   DatasetSubmissions.SubmissionDate,
   DatasetSubmissionTypes.SubmissionType, DatasetSubmissions.Notes

   FROM Sites INNER JOIN (Projects INNER JOIN (DatasetTypes INNER JOIN
   (DatasetSubmissionTypes INNER JOIN ((CollectionUnits INNER JOIN Datasets
   ON CollectionUnits.CollectionUnitID = Datasets.CollectionUnitID) INNER
   JOIN DatasetSubmissions ON Datasets.DatasetID =
   DatasetSubmissions.DatasetID) ON DatasetSubmissionTypes.SubmissionTypeID
   = DatasetSubmissions.SubmissionTypeID) ON DatasetTypes.DatasetTypeID =
   Datasets.DatasetTypeID) ON Projects.ProjectID =
   DatasetSubmissions.ProjectID) ON Sites.SiteID = CollectionUnits.SiteID

   WHERE (((Sites.SiteName)="Bear River No. 3"))
   ORDER BY DatasetSubmissions.SubmissionDate;

Result:

+----------------------+-------------------+----------------------+--------------------------------------------------+------------------------------------------+
| **DatasetType**      | **ProjectName**   | **SubmissionDate**   | **SubmissionType**                               | **Notes**                                |
+----------------------+-------------------+----------------------+--------------------------------------------------+------------------------------------------+
| vertebrate fauna     | FAUNMAP           | 1/31/1992            | Compilation into a another relational database   |                                          |
+----------------------+-------------------+----------------------+--------------------------------------------------+------------------------------------------+
| vertebrate fauna     | Neotoma           | 11/24/2007           | Compilation into Neotoma from another database   | Compiled from FAUNMAP                    |
+----------------------+-------------------+----------------------+--------------------------------------------------+------------------------------------------+
| mollusks             | Neotoma           | 11/25/2007           | Compilation into Neotoma from primary source     |                                          |
+----------------------+-------------------+----------------------+--------------------------------------------------+------------------------------------------+
| plant macrofossils   | Neotoma           | 11/25/2007           | Compilation into Neotoma from primary source     |                                          |
+----------------------+-------------------+----------------------+--------------------------------------------------+------------------------------------------+
| vertebrate fauna     | Neotoma           | 11/25/2007           | Recompilation into or revisions to Neotoma       | Bison elements, fish, and birds added.   |
+----------------------+-------------------+----------------------+--------------------------------------------------+------------------------------------------+

DatasetTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table for Dataset Types. Table is referenced by the `Datasets <#table-datasets>`__ table.

+---------------------------+----------------+------+-----+
| **DatasetTypes**                                        |
+---------------------------+----------------+------+-----+
| DatasetTypeID             | Long Integer   | PK   |     |
+---------------------------+----------------+------+-----+
| DatasetType               | Text           |      |     |
+---------------------------+----------------+------+-----+

**DatasetTypeID (Primary Key)**
  An arbitrary Dataset Type identification number.

**DatasetType**
  The Dataset type, including the following:
    
    -  geochronologic
    -  loss-on-ignition
    -  pollen
    -  plant macrofossils
    -  vertebrate fauna
    -  mollusks
