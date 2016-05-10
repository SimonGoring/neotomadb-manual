Sample Related Tables
-------------------------------

.. _AnalysisUnits:

AnalysisUnits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores the data for Analysis Units.

+----------------------------+----------------+------+-------------------+
| Column Name                | Type           | Key  | Table Reference   |
+----------------------------+----------------+------+-------------------+
| AnalysisUnitID             | int            | PK   |                   |
+----------------------------+----------------+------+-------------------+
| CollectionUnitID           | int            | FK   | CollectionUnits   |
+----------------------------+----------------+------+-------------------+
| AnalysisUnitName           | nvarchar(80)   |      |                   |
+----------------------------+----------------+------+-------------------+
| Depth                      | float          |      |                   |
+----------------------------+----------------+------+-------------------+
| Thickness                  | float          |      |                   |
+----------------------------+----------------+------+-------------------+
| FaciesID                   | int            | FK   |                   |
+----------------------------+----------------+------+-------------------+
| Mixed                      | bit            |      |                   |
+----------------------------+----------------+------+-------------------+
| IGSN                       | nvarchar(40)   |      |                   |
+----------------------------+----------------+------+-------------------+
| Notes                      | ntext          |      |                   |
+----------------------------+----------------+------+-------------------+

**AnalysisUnitID (Primary Key)** 
  An arbitrary Analysis Unit identification number.

**CollectionUnitID (Foreign Key)** 
  Collection Unit ID number. Field links to :ref:`CollectionUnits` table. Every Analysis Unit belongs to a Collection Unit.

**AnalysisUnitName** 
  Optional name for an Analysis Unit. Analysis Units are usually designated with either a depth or a name, sometimes both.

**Depth** 
  Optional depth of the Analysis Unit in cm. Depths are typically designated for Analysis Units from cores and for Analysis Units excavated in arbitrary (e.g. 10 cm) levels. Depths are normally the midpoints of arbitrary levels. For example, for a level excavated from 10 to 20 cm or for a core section from 10 to 15 cm, the depth is 15. Designating depths as midpoints and thicknesses facilitates calculation of ages from age models that utilize single midpoint depths for Analysis Units rather than top and bottom depths. Of course, top and bottom depths can be calculated from midpoint depths and thicknesses. 
  For many microfossil core samples, only the midpoint depths are known or published; the diameter or width of the sampling device is often not given.

**Thickness** 
  Optional thickness of the Analysis Unit in cm. For many microfossil core samples, the depths are treated as points, and the thicknesses are not given in the publications, although 0.5 to 1.0 cm would be typical.

**FaciesID**
  Sedimentary facies of the Analysis Unit. Field links to the :ref:`FaciesTypes` table.

**Mixed**
  Indicates whether specimens in the Analysis Unit are of mixed ages, for example Pleistocene fossils occurring with late Holocene fossils. Although Analysis Units may be mixed, samples from the Analysis Unit may not be, for example individually radiocarbon dated specimens.

**IGSN** 
  International Geo Sample Number. The IGSN is a unique identifier for a Geoscience sample. They are assigned by the SESAR, the System for Earth Sample Registration (`www.geosamples.org <http://www.geosamples.org>`__), which is a registry that provides and administers the unique identifiers. IGSN’s may be assigned to all types of geoscience samples, including cores, rocks, minerals, and even fluids. Their purpose is to facilitate sharing and correlation of samples and sample-based data. For data in Neotoma, their primary value would be for correlation various samples from the same Analysis Units, for example pollen, charcoal, diatoms, and geochemical analyses. Conceivably, the AnalysisUnitID could be used for this purpose; however, IGSN’s could be assigned by projects before their data are submitted to the database. Moreover, AnalysisUnitID’s are intended to be internal to the database. Although IGSN’s could be assigned to Neotoma Collection Units and Samples, their primary value lies in their assignment to Analysis Units. IGSN’s are not yet assigned to Neotoma Analysis Units; however, that may change after consultation with SESAR.

**Notes** 
  Free form notes or comments about the Analysis Unit.

.. _Data:

Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The primary data table in the database. Each occurrence of a Variable in a sample comprises a record in the Data table.

+-------------------+----------------+----------+-------------+
| **Table: Data**                                             |
+-------------------+----------------+----------+-------------+
| SampleID          | Long Integer   | PK, FK   | Samples     |
+-------------------+----------------+----------+-------------+
| VariableID        | Long Integer   | PK, FK   | Variables   |
+-------------------+----------------+----------+-------------+
| Value             | Double         |          |             |
+-------------------+----------------+----------+-------------+

**SampleID (Primary Key, Foreign Key)**
  Sample identification number. Field links to :ref:`Samples` table.

**VariableID (Primary Key, Foreign Key)**
  Variable identification number. Field links to :ref:`Variables` table.

**Value**
  The value of the variable.

SQL Example
`````````````````````````````

The following SQL example gives a list of vertebrate taxa by
Analysis Unit for all sites. Also listed are Variable Measurement Units and Values.

.. code-block:: sql
     :linenos:

     SELECT
       AnalysisUnits.AnalysisUnitName,
       Taxa.TaxonName,
       VariableUnits.VariableUnits,
       `Data.Value`

     FROM
       VariableUnits
     INNER JOIN (
       AnalysisUnits
       INNER JOIN (
         DatasetTypes
         INNER JOIN (
           Taxa
           INNER JOIN (
             `Variables`
             INNER JOIN (
               (
                 (
                   (
                     Sites
                     INNER JOIN CollectionUnits ON Sites.SiteID = CollectionUnits.SiteID
                   )
                   INNER JOIN Datasets ON CollectionUnits.CollectionUnitID = Datasets.CollectionUnitID
                 )
                 INNER JOIN Samples ON Datasets.DatasetID = Samples.DatasetID
               )
               INNER JOIN `Data` ON Samples.SampleID = `Data.SampleID`
             ) ON `Variables.VariableID` = `Data.VariableID`
           ) ON Taxa.TaxonID = `Variables.TaxonID`
         ) ON DatasetTypes.DatasetTypeID = Datasets.DatasetTypeID
         AND (DatasetTypes.DatasetType) = "vertebrate fauna"
       ) ON (
         CollectionUnits.CollectionUnitID = AnalysisUnits.CollectionUnitID
       )
       AND (
         AnalysisUnits.AnalysisUnitID = Samples.AnalysisUnitID
       )
     ) ON VariableUnits.VariableUnitsID = `Variables.VariableUnitsID`

     LIMIT 5;

The first few lines of the result:

+------------------------+-------------------------+---------------------+-------------+
| **AnalysisUnitName**   | **TaxonName**           | **VariableUnits**   | **Value**   |
+------------------------+-------------------------+---------------------+-------------+
| Level 10 prov. 1-3     | Clethrionomys gapperi   | NISP                | 2           |
+------------------------+-------------------------+---------------------+-------------+
| Level 10 prov. 1-3     | Cricetidae              | NISP                | 29          |
+------------------------+-------------------------+---------------------+-------------+
| Level 10 prov. 1-3     | Dicrostonyx torquatus   | NISP                | 5           |
+------------------------+-------------------------+---------------------+-------------+
| Level 10 prov. 1-3     | Lemmus sibiricus        | NISP                | 12          |
+------------------------+-------------------------+---------------------+-------------+
| Level 10 prov. 1-3     | Marmota caligata        | NISP                | 38          |
+------------------------+-------------------------+---------------------+-------------+
| Level 10 prov. 1-3     | Martes                  | NISP                | 2           |
+------------------------+-------------------------+---------------------+-------------+

.. _DepAgents:

DepAgents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deposition Agents for Analysis Units. Individual Analysis Units may be listed multiple times with different Deposition Agents.

+------------------------+----------------+----------+------------------+
| **DepAgents**                                                         |
+------------------------+----------------+----------+------------------+
| AnalysisUnitID         | Long Integer   | PK, FK   |  AnalysisUnits   |
+------------------------+----------------+----------+------------------+
| DepAgentID             | Long Integer   | PK, FK   |  DepAgentTypes   |
+------------------------+----------------+----------+------------------+

**AnalysisUnitID (Primary Key)**
  Analysis Unit identification number. Field links to :ref:`AnalysisUnits` table.

**DepAgentID**
  Deposition Agent identification number. Field links to :ref:`DepAgentTypes` table.

.. _DepAgentTypes:

DepAgentTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Depositional Agents. Table is referenced by the :ref:`DepAgents` table.

+----------------------------+----------------+------+-----+
| **DepAgentTypes**                                        |
+----------------------------+----------------+------+-----+
| DepAgentID                 | Long Integer   | PK   |     |
+----------------------------+----------------+------+-----+
| DepAgent                   | Text           |      |     |
+----------------------------+----------------+------+-----+

**DepAgentID (Primary Key)**
   An arbitrary Depositional Agent identification number.

**DepAgent** 
   Depostional Agent.

.. _SampleAges:

SampleAges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores sample ages. Ages are assigned to a Chronology. Because there may be more than one Chronology for a Collection Unit, samples may be assigned different ages for different Chronologies. A simple example is one sample age in radiocarbon years and another in calibrated radiocarbon years. The age units are an attribute of the Chronology.

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

**SampleAgeID (Primary Key)** 
   An arbitrary Sample Age identification number.

**SampleID (Foreign Key)** 
   Sample identification number. Field links to the :ref:`Samples` table.

**ChronologyID (Foreign Key)** 
   Chronology identification number. Field links to the :ref:`Chronologies` table.

**Age** 
   Age of the sample

**AgeYounger** 
   Younger error estimate of the age. The definition of this estimate is an attribute of the Chronology. Many ages do not have explicit error estimates assigned.

**AgeOlder**
   Older error estimate of the age.

SQL Example
`````````````````````````````

This query lists the Sample Ages for the default Chronologies for «». The CollectionUnit.Handle indicates that there is only one Collection Unit from this site. There are two default Chronologies, one in «Radiocarbon years BP» and the other in «Calibrated radiocarbon years BP».

.. code-block:: sql
   :linenos:

   SELECT
      s.SiteName,
      -- From the Sites table
      c.Handle,
      -- From the CollectionUnits table
      sa.Age,
      -- From the SampleAges table
      a.AgeType -- From the AgeTypes table
   FROM
      AgeTypes AS a
   INNER JOIN (
      (
         (
            Sites AS s
            INNER JOIN CollectionUnits AS c ON s.SiteID = c.SiteID
         )
         INNER JOIN Chronologies AS ch ON c.CollectionUnitID = ch.CollectionUnitID
      )
      INNER JOIN SampleAges AS sa ON ch.ChronologyID = sa.ChronologyID
   ) ON a.AgeTypeId = ch.AgeTypeID
   WHERE
      (s.SiteName) = "Muskox Lake"
   AND (ch.IsDefault) = TRUE;

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

.. _SampleAnalysts:

SampleAnalysts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table lists the Sample Analysts.

+-----------------------------+----------------+------+------------+
| **Table: SampleAnalysts**                                        |
+-----------------------------+----------------+------+------------+
| AnalystID                   | Long Integer   | PK   |            |
+-----------------------------+----------------+------+------------+
| SampleID                    | Long Integer   | FK   | Samples    |
+-----------------------------+----------------+------+------------+
| ContactID                   | Long Integer   | FK   | Contacts   |
+-----------------------------+----------------+------+------------+
| AnalystOrder                | Long Integer   |      |            |
+-----------------------------+----------------+------+------------+

**AnalystID (Primary Key)**
   An arbitrary Sample Analyst identification number.

**SampleID (Foreign Key)** 
   Sample identification number. Field links to the :ref:`Samples` table.

**ContactID (Foreign Key)** 
   Contact identification number. Field links to the :ref:`Contacts` table.

**AnalystOrder**
   Order in which Sample Analysts are listed if more than one (rare).

.. _SampleKeywords:

SampleKeywords
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table links keywords to samples. For example, it identifies modern pollen surface samples.

+-----------------------------+----------------+----------+------------+
| **Table: SampleKeywords**   |                                        |
+-----------------------------+----------------+----------+------------+
| SampleID                    | Long Integer   | PK, FK   | Samples    |
+-----------------------------+----------------+----------+------------+
| KeywordID                   | Long Integer   | PK, FK   | Keywords   |
+-----------------------------+----------------+----------+------------+

**SampleID (Primary Key, Foreign Key)** 
   Sample identification number. Field links to the :ref:`Samples` table.

**KeywordID (Primary Key, Foreign Key)** 
   Keyword identification number. Field links to the :ref:`Keywords` lookup table.

SQL Example
`````````````````````````````

This query provides a list of modern pollen surface samples from «».
Listed are the Site Name, Collection Type, Contact person, and
Depositional Environment.

.. code-block:: sql
   :linenos:

   SELECT Samples.SampleID, Sites.SiteName, CollectionTypes.CollType,
   Contacts.ContactName, DepEnvtTypes.DepEnvt

   FROM DepEnvtTypes INNER JOIN (Contacts INNER JOIN ((CollectionTypes
   INNER JOIN (GeoPoliticalUnits INNER JOIN ((Sites INNER JOIN
   (CollectionUnits INNER JOIN (DatasetTypes INNER JOIN (Datasets INNER
   JOIN (Samples INNER JOIN (Keywords INNER JOIN SampleKeywords ON
   Keywords.KeywordID = SampleKeywords.KeywordID) ON Samples.SampleID =
   SampleKeywords.SampleID) ON Datasets.DatasetID = Samples.DatasetID) ON
   DatasetTypes.DatasetTypeID = Datasets.DatasetTypeID) ON
   CollectionUnits.CollectionUnitID = Datasets.CollectionUnitID) ON
   Sites.SiteID = CollectionUnits.SiteID) INNER JOIN SiteGeoPolitical ON
   Sites.SiteID = SiteGeoPolitical.SiteID) ON
   GeoPoliticalUnits.GeoPoliticalID = SiteGeoPolitical.GeoPoliticalID) ON
   CollectionTypes.CollTypeID = CollectionUnits.CollTypeID) INNER JOIN
   DatasetPIs ON Datasets.DatasetID = DatasetPIs.DatasetID) ON
   Contacts.ContactID = DatasetPIs.ContactID) ON DepEnvtTypes.DepEnvtID =
   CollectionUnits.DepEnvtID

   WHERE (((Keywords.Keyword)="modern sample") AND
   ((DatasetTypes.DatasetType)="pollen") AND
   ((GeoPoliticalUnits.GeoPoliticalName)=""))

   ORDER BY CollectionTypes.CollType;

Result:

+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| **SampleID**   | **SiteName**                         | **CollType**   | **ContactName**           | **DepEnvt**        |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 60536          |                                      | Core           | Radle, Nancy Jean         | Glacial            |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 11153          | (US:)                                | Core           | Grimm, Eric Christopher   | Glacial            |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 61194          | (US:)                                | Core           | Watts, William A.         | Glacial            |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 24780          | JHMS31 (McAndrews and Wright 1969)   | Modern         | McAndrews, John H.        | Organic Detritus   |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 24771          | JHMS23 (McAndrews and Wright 1969)   | Modern         | McAndrews, John H.        | Organic Detritus   |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 24772          | JHMS24 (McAndrews and Wright 1969)   | Modern         | McAndrews, John H.        | Organic Detritus   |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 24773          | JHMS25 (McAndrews and Wright 1969)   | Modern         | McAndrews, John H.        | Organic Detritus   |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 24774          | JHMS26 (McAndrews and Wright 1969)   | Modern         | McAndrews, John H.        | Organic Detritus   |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 24775          | JHMS27 (McAndrews and Wright 1969)   | Modern         | McAndrews, John H.        | Organic Detritus   |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 24776          | JHMS28 (McAndrews and Wright 1969)   | Modern         | McAndrews, John H.        | Organic Detritus   |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 24777          | JHMS28 (McAndrews and Wright 1969)   | Modern         | McAndrews, John H.        | Cattle Tank        |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 3173           | Site 1 (Hansen unpublished)          | Modern         | Hansen, Barbara C. S.     | Unknown            |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 24779          | JHMS30 (McAndrews and Wright 1969)   | Modern         | McAndrews, John H.        | Organic Detritus   |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 24781          | JHMS32 (McAndrews and Wright 1969)   | Modern         | McAndrews, John H.        | Organic Detritus   |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 24782          | JHMS32 (McAndrews and Wright 1969)   | Modern         | McAndrews, John H.        | Cattle Tank        |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 24783          | JHMS33 (McAndrews and Wright 1969)   | Modern         | McAndrews, John H.        | Organic Detritus   |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 45068          | K11 (Kapp 1965]                      | Modern         | Kapp, Ronald O.           | Stock Pond         |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 55819          | Rose 1a (Watts and Wright 1966)      | Modern         | Watts, William A.         | Stock Pond         |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 55819          | Rose 1a (Watts and Wright 1966)      | Modern         | Wright, Herbert E., Jr.   | Stock Pond         |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 55820          | Rose 1b (Watts and Wright 1966)      | Modern         | Watts, William A.         | Stock Pond         |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 55820          | Rose 1b (Watts and Wright 1966)      | Modern         | Wright, Herbert E., Jr.   | Stock Pond         |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+
| 24778          | JHMS29 (McAndrews and Wright 1969)   | Modern         | McAndrews, John H.        | Organic Detritus   |
+----------------+--------------------------------------+----------------+---------------------------+--------------------+

.. _Samples:

Samples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores sample data. Samples belong to Analysis Units, which belong to Collection Units, which belong to Sites. Samples also belong to a Dataset, and the Dataset determines the type of sample. Thus, there could be two different samples from the same Analysis Unit, one belonging to a pollen dataset, the other to a plant macrofossil dataset.

+----------------------+----------------+------+-----------------+
| **Table: Samples**                                             |
+----------------------+----------------+------+-----------------+
| SampleID             | Long Integer   | PK   |                 |
+----------------------+----------------+------+-----------------+
| AnalysisUnitID       | Long Integer   | FK   | AnalysisUnits   |
+----------------------+----------------+------+-----------------+
| DatasetID            | Long Integer   | FK   | Datasets        |
+----------------------+----------------+------+-----------------+
| SampleName           | Text           |      |                 |
+----------------------+----------------+------+-----------------+
| AnalysisDate         | Date/Time      |      |                 |
+----------------------+----------------+------+-----------------+
| LabNumber            | Text           |      |                 |
+----------------------+----------------+------+-----------------+
| PreparationMethod    | Memo           |      |                 |
+----------------------+----------------+------+-----------------+
| Notes                | Memo           |      |                 |
+----------------------+----------------+------+-----------------+

**SampleID (Primary Key)**
   An arbitrary Sample identification number.

**AnalysisUnitID (Foreign Key)**
   Analysis Unit identification number. Field links to the :ref:`AnalysisUnits` table.

**DatasetID (Foreign Key)** 
   Dataset identification number. Field links to the :ref:`Datasets` table.

**SampleName**
   Sample name if any.

**AnalysisDate**
   Date of analysis.

**LabNumber**
   Laboratory number for the sample. A special case regards geochronologic samples, for which the LabNumber is the number, if any, assigned by the submitter, not the number assigned by the radiocarbon laboratory, which is in the :ref:`Geochronology` table.

**PreparationMethod** 
   Description, notes, or comments on preparation methods. For faunal samples, notes on screening methods or screen size are stored here.

**Notes**
   Free form note or comments about the sample.

SQL Example
`````````````````````````````

This query provides a list of samples from «». The Collection Unit Name,
Analysis Unit Name, Dataset Type, and Preparation Methods are listed.

.. code-block:: sql
   :linenos:

   SELECT CollectionUnits.CollUnitName, AnalysisUnits.AnalysisUnitName,
   DatasetTypes.DatasetType, Samples.PreparationMethod

   FROM DatasetTypes INNER JOIN ((((Sites INNER JOIN CollectionUnits ON
   Sites.SiteID = CollectionUnits.SiteID) INNER JOIN AnalysisUnits ON
   CollectionUnits.CollectionUnitID = AnalysisUnits.CollectionUnitID) INNER
   JOIN Samples ON AnalysisUnits.AnalysisUnitID = Samples.AnalysisUnitID)
   INNER JOIN (Datasets.DatasetID = Samples.DatasetID) AND
   (CollectionUnits.CollectionUnitID = Datasets.CollectionUnitID)) ON
   DatasetTypes.DatasetTypeID = Datasets.DatasetTypeID

   WHERE (((Sites.SiteName)=""))

   ORDER BY CollectionUnits.CollUnitName, AnalysisUnits.AnalysisUnitName;

Result:

+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| **CollUnitName**   | **AnalysisUnitName**      | **DatasetType**    | **PreparationMethod**                                                   |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Locality           | Assemblage                | vertebrate fauna   |                                                                         |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Locality           | Large Mammal Assemblage   | vertebrate fauna   |                                                                         |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit A             | Level 1                   | vertebrate fauna   | All excavated material was fine screened (<1/16-inch or 1.6-mm mesh).   |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit A             | Level 1                   | geochronologic     |                                                                         |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit A             | Level 1                   | geochronologic     |                                                                         |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit A             | Level 1                   | geochronologic     |                                                                         |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit A             | Level 1                   | geochronologic     |                                                                         |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit A             | Level 2                   | geochronologic     |                                                                         |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit A             | Level 2                   | vertebrate fauna   | All excavated material was fine screened (<1/16-inch or 1.6-mm mesh).   |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit A             | Level 2                   | geochronologic     |                                                                         |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit A             | Level 2                   | geochronologic     |                                                                         |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit A             | Level 2                   | geochronologic     |                                                                         |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit A/B           | Assemblage                | vertebrate fauna   | All excavated material was fine screened (<1/16-inch or 1.6-mm mesh).   |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit B             | Level 4                   | vertebrate fauna   | All excavated material was fine screened (<1/16-inch or 1.6-mm mesh).   |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit B             | Level 5                   | vertebrate fauna   | All excavated material was fine screened (<1/16-inch or 1.6-mm mesh).   |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit C             | Level 1                   | vertebrate fauna   | All excavated material was fine screened (<1/16-inch or 1.6-mm mesh).   |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit C             | Level 1                   | geochronologic     |                                                                         |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit C             | Level 2                   | vertebrate fauna   | All excavated material was fine screened (<1/16-inch or 1.6-mm mesh).   |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit C             | Level 2                   | geochronologic     |                                                                         |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit C             | Level 2                   | geochronologic     |                                                                         |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+
| Unit C             | Level 2                   | geochronologic     |                                                                         |
+--------------------+---------------------------+--------------------+-------------------------------------------------------------------------+

.. _AggregateSamples:

AggregateSamples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores the samples in Aggregate Datasets.

+-------------------------------+-------+----------+---------------------+
| **AggregateSamples**          |                                        |
+-------------------------------+-------+----------+---------------------+
| AggregateDatasetID            | int   | PK, FK   | AggregateDatasets   |
+-------------------------------+-------+----------+---------------------+
| SampleID                      | int   | PK, FK   | Samples             |
+-------------------------------+-------+----------+---------------------+

**AggregateDatasetID (Primary Key, Foreign Key)** 
  An arbitrary Aggregate Dataset identification number. Field links to the :ref:`AggregateDatasets` table.

**SampleID (Primary Key, Foreign Key)**
  Sample ID number. Field links to the :ref:`Samples` table.

.. _FaciesTypes:

FaciesTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Facies Types. Table is referenced by the :ref:`AnalysisUnits` table.

+--------------------------+----------------+------+-----+
| **FaciesTypes**                                        |
+--------------------------+----------------+------+-----+
| FaciesID                 | Long Integer   | PK   |     |
+--------------------------+----------------+------+-----+
| Facies                   | Text           |      |     |
+--------------------------+----------------+------+-----+

**FaciesID (Primary Key)** 
   An arbitrary Facies identification number.

**Facies** 
   Short Facies description.

.. _Keywords:

Keywords
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Keywords referenced by the :ref:`SampleKeywords` table. The table provides a means to identify samples sharing a common attribute. For example, the
keyword «modern sample» identifies modern surface samples in the database. These samples include individual surface samples, as well as core tops. Although not implemented, a «pre-European settlement» keyword would be a means to identify samples just predating European settlement.

+-----------------------+----------------+------+-----+
| **Table: Keywords**                                 |
+-----------------------+----------------+------+-----+
| KeywordID             | Long Integer   | PK   |     |
+-----------------------+----------------+------+-----+
| Keyword               | Text           |      |     |
+-----------------------+----------------+------+-----+

**KeywordID (Primary Key)**
   An arbitrary Keyword identification number.

**Keyword**
   A keyword for identifying samples sharing a common attribute.
