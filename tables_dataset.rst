Dataset & Collection Related Tables
-----------------------------------

.. _AggregateDatasets:

AggregateDatasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aggregate Datasets are aggregates of samples of a particular datatype. Some examples:

  * Plant macrofossil samples from a group of packrat middens collected from a particular valley, mountain range, or other similarly defined geographic area. Each midden is from a different Site or Collection Unit, but they are grouped into time series for that area and are published as single dataset.

  * Samples collected from 32 cutbanks along several kms of road.  Each sample is from a different site, but they form a time series from 0 -- 12,510 :sup:`14`\ C yr BP, and pollen, plant macrofossils, and beetles were published and graphed as if from a single site.

  * A set of pollen surface samples from particular region or study that were published and analyzed as a single dataset and submitted to the database as a single dataset.

  * The examples above are datasets predefined in the database. New aggregate datasets could be assembled for particular studies, for example all the pollen samples for a given time slice for a given geographic region.

+--------------------------------+-----------------+------+-----------------------+
| **AggregateDatasets**                                                           |
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
  Aggregate Order Type identification number. Field links to the :ref:`AggregateOrderTypes` lookup table.

**Notes**
  Free form notes about the Aggregate Order Type.

.. _AggregateOrderTypes:

AggregateOrderTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table for Aggregate Order Types. Table is referenced by the :ref:`AggregateDatasets` table.

+----------------------------------+----------------+------+-----+
| **AggregateOrderTypes**                                        |
+----------------------------------+----------------+------+-----+
| AggregateOrderTypeID             | int            | PK   |     |
+----------------------------------+----------------+------+-----+
| AggregateOrderType               | nvarchar(60)   |      |     |
+----------------------------------+----------------+------+-----+
| Notes                            | ntext          |      |     |
+----------------------------------+----------------+------+-----+

**AggregateOrderTypeID (Primary Key)**
  An arbitrary Aggregate Order Type identification number.

**AggregateOrderType**
  The Aggregate Order Type.

**Notes**
  Free form notes or comments about the Aggregate Order Type.

The Aggregate Order Types are:

  * **Latitude**: AggregateDataset samples are ordered by, in order of priority, either (1) :ref:`CollectionUnits`.GPSLatitude or (2) the mean of :ref:`Sites`.LatitudeNorth and :ref:`Sites`.LatitudeSouth.

  * **Longitude** AggregateDataset samples are ordered by, in order of priority, either (1) :ref:`CollectionUnits`.GPSLongitude or (2) the mean of :ref:`Sites`.LongitudeWest and :ref:`Sites`.LongitudeEast.

  * **Altitude** AggregateDataset samples are ordered by :ref:`Sites`.Altitude`.

  * **Age** AggregateDataset samples are ordered by :ref:`SampleAges`.Age, where :ref:`SampleAges`.SampleAgeID is from :ref:`AggregateSampleAges`.SampleAgeID.

  * **Alphabetical by site name** AggregateDataset samples are ordered alphabetically by :ref:`Sites`.SiteName.

  * **Alphabetical by collection unit name** AggregateDataset samples are ordered alphabetically by :ref:`CollectionUnits`.CollUnitName.

  * **Alphabetical by collection units handle** AggregateDataset samples are ordered alphabetically by :ref:`CollectionUnits`.Handle.

.. _CollectionTypes:

CollectionTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table is a lookup table of for types of Collection Units, or Collection Types. Table is referenced by the :ref:`CollectionUnits` table.

+------------------------------+----------------+------+-----+
| **CollectionTypes**          | Variable Type  | Key  |     |
+------------------------------+----------------+------+-----+
| CollTypeID                   | int            | PK   |     |
+------------------------------+----------------+------+-----+
| CollType                     | nvarchar(50)   |      |     |
+------------------------------+----------------+------+-----+

**CollTypeID (Primary Key)** 
  An arbitrary Collection Type identification number.

**Colltype**
  The Collection Type. Types include cores, sections, excavations, and animal middens. Collection Units may be modern collections, surface float, or isolated specimens. Composite Collections Units include different kinds of Analysis Units, for example a modern surface sample for ostracodes and an associated water sample.

.. _CollectionUnits:

CollectionUnits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores data for Collection Units.

+------------------------------+-----------------+------+-------------------+
| **CollectionUnits**          | Variable Type   | Key  | Table Reference   |
+------------------------------+-----------------+------+-------------------+
| CollectionUnitID             | int             | PK   |                   |
+------------------------------+-----------------+------+-------------------+
| Handle                       | nvarchar(10)    |      |                   |
+------------------------------+-----------------+------+-------------------+
| SiteID                       | int             | FK   | Sites             |
+------------------------------+-----------------+------+-------------------+
| CollTypeID                   | int             | FK   | CollectionTypes   |
+------------------------------+-----------------+------+-------------------+
| DepEnvtID                    | int             | FK   | DepEnvtTypes      |
+------------------------------+-----------------+------+-------------------+
| CollUnitName                 | nvarchar(255)   |      |                   |
+------------------------------+-----------------+------+-------------------+
| CollDate                     | datetime        |      |                   |
+------------------------------+-----------------+------+-------------------+
| CollDevice                   | nvarchar(255)   |      |                   |
+------------------------------+-----------------+------+-------------------+
| GPSLatitude                  | float           |      |                   |
+------------------------------+-----------------+------+-------------------+
| GPSLongitude                 | float           |      |                   |
+------------------------------+-----------------+------+-------------------+
| GPSAltitude                  | float           |      |                   |
+------------------------------+-----------------+------+-------------------+
| GPSError                     | float           |      |                   |
+------------------------------+-----------------+------+-------------------+
| WaterDepth                   | float           |      |                   |
+------------------------------+-----------------+------+-------------------+
| SubstrateID                  | int             | FK   | Substrates        |
+------------------------------+-----------------+------+-------------------+
| SlopeAspect                  | int             |      |                   |
+------------------------------+-----------------+------+-------------------+
| SlopeAngle                   | int             |      |                   |
+------------------------------+-----------------+------+-------------------+
| Location                     | nvarchar(255)   |      |                   |
+------------------------------+-----------------+------+-------------------+
| Notes                        | ntext           |      |                   |
+------------------------------+-----------------+------+-------------------+

**CollectionUnitID (Primary Key)** 
  An arbitrary Collection Unit identification number.

**SiteID (Foreign Key)** 
  Site where CollectionUnit was located. Field links to :ref:`Sites` table.

**CollTypeID (Foreign Key)** 
  Type of Collection Unit. Field links to the :ref:`CollectionTypes` table.

**DepEnvtID (Foreign Key)** 
  Depositional environment of the CollectionUnit. Normally, this key refers to the modern environment. For example, the site may be located on a colluvial slope, in which case the Depositional Environment may be Colluvium or Colluvial Fan. However, an excavation may extend into alluvial sediments, which represent a different depositional environment. These are accounted for by the Facies of the AnalysisUnit. Field links to the :ref:`DepEnvtTypes` table.

**Handle**
  Code name for the Collection Unit. This code may be up to 10 characters, but an effort is made to keep these to 8 characters or less. Data are frequently distributed by Collection Unit, and the Handle is used for file names.

**CollUnitName** 
  Name of the Collection Unit. Examples: Core BPT82A, Structure 9, P4A Test 57. If faunal data are reported from a site or locality without explicit Collection Units, then data are assigned to a single Collection Unit with the name «Locality».

**CollDate**
  Date Collection Unit was collected.

**CollDevice**
  Device used for obtain Collection Unit. This field applies primarily to cores, for example «Wright square-rod piston corer (5 cm)».

**GPSLatitude**
  Precise latitude of the Collection Unit, typically taken with a GPS, although may be precisely measured from a map.

**GPSLongitude**
  Precise longitude of the Collection Unit, typically taken with a GPS, although may be precisely measured from a map.

**GPSAltitude**
  Precise altitude of the Collection Unit, typically taken with a GPS or precisely obtained from a map.

**GPSError**
  Error in the horizontal GPS coordinates, if known.

**WaterDepth**
  Depth of water at the Collection Unit location. This field applies mainly to Collection Units from lakes.

**SubstrateID (Foreign Key)**
  Substrate or rock type on which the Collection Unit lies. Field links to the RockTypes table. This field is especially used for rodent middens.

**SlopeAspect**
  For Collection Units on slopes, the horizontal direction to which a slope faces measured in degrees clockwise from north. This field is especially used for rodent middens.

**SlopeAngle**
  For Collection Units on slopes, the angle of slope from horizontal. field is especially used for rodent middens.

**Location** 
  Short description of the location of the Collection Unit within the site.

**Notes**
  Free form notes or comments about the Collection Unit.

.. _DatasetPublications:

DatasetPublications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table lists the publications for datasets.

+----------------------------------+-------+----------+----------------+
| **DatasetPublications**                                              |
+----------------------------------+-------+----------+----------------+
| DatasetID                        | int   | PK, FK   | Datasets       |
+----------------------------------+-------+----------+----------------+
| PublicationID                    | int   | PK, FK   | Publications   |
+----------------------------------+-------+----------+----------------+
| PrimaryPub                       | bit   |          |                |
+----------------------------------+-------+----------+----------------+

**DatasetID (Primary Key, Foreign Key)** 
  Dataset identification number. Field links to :ref:`Datasets` table.

**PublicationID (Primary Key, Foreign Key)** 
  Publication identification number. Field links to :ref:`Publications` table.

**PrimaryPub** 
  Is «True» if the publication is the primary publication for the dataset.

.. _Datasets:

Datasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores the data for Datasets. A Dataset is the set of samples for a particular data type from a Collection Unit. A Collection Unit may have multiple Datasets for different data types, for example one dataset for pollen and another for plant macrofossils. Every Sample is assigned to a Dataset, and every Dataset is assigned to a Collection Unit. Samples from different Collection Units cannot be assigned to the same Dataset (although they may be assigned to :ref:`AggregateDatasets`).

+-----------------------+----------------+------+-------------------+
| **Datasets**                                                      |
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

**DatasetID (Primary Key)** 
  An arbitrary Dataset identification number.

**CollectionUnitID (Foreign Key)** 
  Collection Unit identification number. Field links to the :ref:`CollectionUnits` table.

**DatasetTypeID (Foreign Key)** 
  Dataset Type identification number. Field links to the :ref:`DatasetTypes` lookup table.

**DatasetName** 
  Optional name for the Dataset.

**Notes** 
  Free form notes or comments about the Dataset.

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

This query lists the plant macrofossils identified at site «Bear River No. 3».

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


.. _DatasetSubmissions:

DatasetSubmissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Submissions to the database are of Datasets. Submissions may be original
submissions, resubmissions, compilations from other databases, or
recompilations. See the description of the
:ref:`DatasetSubmissionTypes` table.

+---------------------------------+----------------+------+--------------------------+
| **DatasetSubmissions**                                                             |
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
  Dataset identification number. Field links to the :ref:`Datasets` table. Datasets may occur multiple times in this table (e.g. once for the original compilation into a different database and a second time for the recompilation into Neotoma).

**ProjectID (Foreign Key)**
  Database project responsible for the submission or compilation.

**ContactID (Foreign Key)**
  Contact identification number. Field links to the :ref:`Contacts` table. The Contact is the person who submitted, resubmitted, compiled, or recompiled the data. This person is not necessarily the Dataset PI; it is the person who submitted the data or compiled the data from the literature.

**SubmissionDate**
  Date of the submission, resubmission, compilation, or recompilation.

**SubmissionTypeID (Foreign Key)**
  Submission Type identification number. Field links to the :ref:`DatasetSubmissionTypes` table.

**Notes**
  Free form notes or comments about the submission.

.. _DatasetSubmissionTypes:

DatasetSubmissionTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Dataset Submission Types. Table is referenced by the :ref:`DatasetSubmissions` table.

+-------------------------------------+----------------+------+-----+
| **DatasetSubmissionTypes**                                        |
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

  -  Recompilation into or revisions to Neotoma:  The initial development of Neotoma involved merging the data from several existing databases, including FAUNMAP, the Global Pollen Database, and the North American Plant Macrofossil Database. Thus original compilation of Datasets was into one of these databases, which were then recompiled into Neotoma. The original compilation and the recompilation into Neotoma are separate submissions.

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

.. _DatasetTypes:

DatasetTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table for Dataset Types. Table is referenced by the :ref:`Datasets` table.

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

.. _DatasetPIs:

DatasetPIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table lists the Principle Investigators for Datasets.

+-------------------------+----------------+----------+------------+
| **DatasetPIs**                                                   |
+-------------------------+----------------+----------+------------+
| DatasetID               | Long Integer   | PK, FK   | Datasets   |
+-------------------------+----------------+----------+------------+
| ContactID               | Long Integer   | PK, FK   | Contacts   |
+-------------------------+----------------+----------+------------+
| PIOrder                 | Long Integer   |          |            |
+-------------------------+----------------+----------+------------+

**DatasetID (Primary Key, Foreign Key)** 
  Dataset identification number. Field links to Dataset table.

**ContactID (Primary Key, Foreign Key)** 
  Contact identification number. Field links to :ref:`Contacts` table.

**PIOrder** 
  Order in which PIs are listed.

.. _DepEnvtTypes:

DepEnvtTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Depostional Environment Types. Table is referenced by
the :ref:`CollectionUnits` table.

+---------------------------+----------------+------+--------------------------+
| **DepEnvtTypes**                                                             |
+---------------------------+----------------+------+--------------------------+
| DepEnvtID                 | Long Integer   | PK   |                          |
+---------------------------+----------------+------+--------------------------+
| DepEnvt                   | Text           |      |                          |
+---------------------------+----------------+------+--------------------------+
| DepEnvtHigherID           | Long Integer   | FK   | DepEnvtTypes:DepEnvtID   |
+---------------------------+----------------+------+--------------------------+

**DepEnvtID (Primary Key)** 
  An arbitrary Depositional Environment Type identification number.

**DepEnvt** 
  Depositional Environment.

**DepEnvtHigherID** 
  The Depositional Environment Types are hierarchical. DepEnvtHigherID is the DepEnvtID of the higher ranked Depositional Environment. See following table gives some examples.

+---------------------+---------------+-----------------------+
|     **DepEnvtID**   | **DepEnvt**   | **DepEnvtHigherID**   |
+---------------------+---------------+-----------------------+
|     19              | Lacustrine    | 19                    |
+---------------------+---------------+-----------------------+
|     24              |               | 19                    |
+---------------------+---------------+-----------------------+
|     29              | Glacial       | 24                    |
+---------------------+---------------+-----------------------+
|     30              |               | 29                    |
+---------------------+---------------+-----------------------+
|     33              |               | 29                    |
+---------------------+---------------+-----------------------+
|     59              | Palustrine    | 59                    |
+---------------------+---------------+-----------------------+
|     61              | Mire          | 59                    |
+---------------------+---------------+-----------------------+
|     62              | Bog           | 61                    |
+---------------------+---------------+-----------------------+
|     63              | Blanket Bog   | 62                    |
+---------------------+---------------+-----------------------+
|     64              | Raised Bog    | 62                    |
+---------------------+---------------+-----------------------+

SQL Example
`````````````````````````````

This query gives a list of the top level Depostional Environment Types.

.. code-block:: sql
   :linenos:

   SELECT DepEnvtTypes.DepEnvtID, DepEnvtTypes.DepEnvt,
   DepEnvtTypes.DepEnvtHigherID

   FROM DepEnvtTypes INNER JOIN DepEnvtTypes AS DepEnvtTypes\_1 ON
   (DepEnvtTypes.DepEnvt = DepEnvtTypes\_1.DepEnvt) AND
   (DepEnvtTypes.DepEnvtHigherID = DepEnvtTypes\_1.DepEnvtID);

Result:

+-----------------+------------------+-----------------------+
| **DepEnvtID**   | **DepEnvt**      | **DepEnvtHigherID**   |
+-----------------+------------------+-----------------------+
| 1               | Archaeological   | 1                     |
+-----------------+------------------+-----------------------+
| 6               | Biological       | 6                     |
+-----------------+------------------+-----------------------+
| 16              | Estuarine        | 16                    |
+-----------------+------------------+-----------------------+
| 19              | Lacustrine       | 19                    |
+-----------------+------------------+-----------------------+
| 51              | Marine           | 51                    |
+-----------------+------------------+-----------------------+
| 59              | Palustrine       | 59                    |
+-----------------+------------------+-----------------------+
| 76              | Riverine         | 76                    |
+-----------------+------------------+-----------------------+
| 93              | Sampler          | 93                    |
+-----------------+------------------+-----------------------+
| 99              | Spring           | 99                    |
+-----------------+------------------+-----------------------+
| 103             | Terrestrial      | 103                   |
+-----------------+------------------+-----------------------+
| 136             | Other            | 136                   |
+-----------------+------------------+-----------------------+
| 137             | Unknown          | 137                   |
+-----------------+------------------+-----------------------+

SQL Example
`````````````````````````````

This following query gives a list of the second level «Terrestrial» Depositional Environment Types.

.. code-block:: sql
  :linenos:

  SELECT DepEnvtTypes\_1.DepEnvtID, DepEnvtTypes\_1.DepEnvt,
  DepEnvtTypes\_1.DepEnvtHigherID

  FROM DepEnvtTypes INNER JOIN DepEnvtTypes AS DepEnvtTypes\_1 ON
  DepEnvtTypes.DepEnvtID = DepEnvtTypes\_1.DepEnvtHigherID

  WHERE (((DepEnvtTypes.DepEnvt)="Terrestrial"));


Result:

+-----------------+---------------+-----------------------+
| **DepEnvtID**   | **DepEnvt**   | **DepEnvtHigherID**   |
+-----------------+---------------+-----------------------+
| 103             | Terrestrial   | 103                   |
+-----------------+---------------+-----------------------+
| 104             | Aeolian       | 103                   |
+-----------------+---------------+-----------------------+
| 109             | Cave          | 103                   |
+-----------------+---------------+-----------------------+
| 117             | Glacial       | 103                   |
+-----------------+---------------+-----------------------+
| 122             | Gravity       | 103                   |
+-----------------+---------------+-----------------------+
| 127             | Soil          | 103                   |
+-----------------+---------------+-----------------------+
| 131             | Volcanic      | 103                   |
+-----------------+---------------+-----------------------+

.. _Lithology:

Lithology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores the lithologic descriptions of Collection Units.

+------------------------+----------------+------+--------------------+
| **Table: Lithology**                                                |
+------------------------+----------------+------+--------------------+
| LithologyID            | Long Integer   | PK   |                    |
+------------------------+----------------+------+--------------------+
| CollectionUnitID       | Long Integer   | FK   |  CollectionUnits   |
+------------------------+----------------+------+--------------------+
| DepthTop               | Double         |      |                    |
+------------------------+----------------+------+--------------------+
| DepthBottom            | Double         |      |                    |
+------------------------+----------------+------+--------------------+
| LowerBoundary          | Text           |      |                    |
+------------------------+----------------+------+--------------------+
| Description            | Memo           |      |                    |
+------------------------+----------------+------+--------------------+

**LithologyID (Primary Key)** 
  An arbitrary identification number for a lithologic unit.

**CollectionUnitID (Foreign Key)** 
  Collection Unit identification number. Field links to the :ref:`CollectionUnits` table.

**DepthTop**
  Depth of the top of the lithologic unit in cm.

**DepthBottom**
  Depth of the bottom of the lithologic unit in cm.

**LowerBoundary**
  Description of the nature of the lower boundary of the lithologic unit, e.g. «gradual, over ca. 10 cm».

**Description**
  Description of the lithologic unit. These can be quite detailed, with Munsell color or Troels-Smith descriptions. Some examples:

  -  interbedded gray silt and peat
  -  marly fine-detritus copropel
  -  humified sedge and Sphagnum peat
  -  sedge peat 5YR 5/4
  -  gray sandy loam with mammoth and other animal bones
  -  grey-green gyttja, oxidizing to gray-brown
  -  Ag 3, Ga 1, medium gray, firm, elastic
  -  nig3, strf0, elas2, sicc0; Th2 T12 Tb+
  -  Ld°4, , Dg+, Dh+

.. _Projects:

Projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores a list of database projects that have supplied data to Neotoma. These include the databases that were merged in the initial development of Neotoma as well as other independent projects that continue to assemble data for a particular region or data type. Some of these projects have developed relational databases, whereas others have compiled data in flat files. This table is referenced by the :ref:`DatasetSubmissions` table.

+------------------------------------------------------------+
| **Table: Projects**                                        |
+-----------------------+----------------+------+------------+
| ProjectID             | Long Integer   | PK   |            |
+-----------------------+----------------+------+------------+
| ProjectName           | Text           |      |            |
+-----------------------+----------------+------+------------+
| ContactID             | Long Integer   | FK   | Contacts   |
+-----------------------+----------------+------+------------+
| URL                   | Text           |      |            |
+-----------------------+----------------+------+------------+

**ProjectID (Primary Key)** 
  An arbitrary Project identification number.

**ProjectName** 
  Name of the Project, e.g. «Cooperative Holocene Mapping Project», «North American Pollen Database», «FAUNMAP».

**ContactID (Foreign Key)** 
  Contact person for the project. Field links to the :ref:`Contacts` table.

**URL** 
  Web site address for the project.
