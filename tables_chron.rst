Chronology & Age Related Tables
-----------------------------

.. _AgeTypes:

AgeTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Age Types or units. This table is referenced by the
:ref:`Chronologies` and
:ref:`Geochronology` tables.

+-----------------------+----------------+------+-----+
| **AgeTypes**                                        |
+-----------------------+----------------+------+-----+
| AgeTypeID             | int            | PK   |     |
+-----------------------+----------------+------+-----+
| AgeType               | nvarchar(64)   |      |     |
+-----------------------+----------------+------+-----+

**AgeTypeID (Primary Key)**
  An arbitrary Age Type identification number.

**AgeType** 
  Age type or units. Includes the following:

  * Calendar years AD/BC

  * Calendar years BP

  * Calibrated radiocarbon years BP

  * Radiocarbon years BP

  * Varve years BP

.. _AggregateChronologies:

AggregateChronologies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores metadata for Aggregate Chronologies. An Aggregate Chronology refers to an explicit chronology assigned to a sample Aggregate. The individual Aggregate Samples have ages assigned in the :ref:`AggregateSampleAges` table. An Aggregate Chronology would be used, for example, for a set of packrat middens assigned to an :ref:`AggregateDataset`. The Aggregate Chronology is analsgous to the Chronology assigned to samples from a single Collection Unit.

An Aggregate may have more than one Aggregate Chronology, for example one in radiocarbon years and another in calibrated radiocarbon years. One Aggreagate Chronology per Age Type may be designated the default, which is the Aggregate Chronology currently preferred by the database stewards.

+------------------------------------+-----------------+------+---------------------+
| **AggregateChronologies**                                                         |
+------------------------------------+-----------------+------+---------------------+
| AggregateChronID                   | int             | PK   |                     |
+------------------------------------+-----------------+------+---------------------+
| AggregateDatasetID                 | int             | FK   | AggregateDatasets   |
+------------------------------------+-----------------+------+---------------------+
| AgeTypeID                          | int             | FK   | AgeTypes            |
+------------------------------------+-----------------+------+---------------------+
| IsDefault                          | bit             |      |                     |
+------------------------------------+-----------------+------+---------------------+
| ChronologyName                     | nvarchar(80)    |      |                     |
+------------------------------------+-----------------+------+---------------------+
| AgeBoundYounger                    | int             |      |                     |
+------------------------------------+-----------------+------+---------------------+
| AgeBoundOlder                      | int             |      |                     |
+------------------------------------+-----------------+------+---------------------+
| Notes                              | nvarchar(MAX)   |      |                     |
+------------------------------------+-----------------+------+---------------------+

**AggregateChronID (Primary Key)** 
  An arbitrary Aggregate Chronology identification number.

**AggregateDatasetID (Foreign Key)**
  Dataset to which the Aggregate Chronology applies. Field links to the :ref:`AggregateDatasets` table.

**AgeTypeID (Foreign Key)**
  Age type or units. Field links to the :ref:`AgeTypes` table.

**IsDefault**
  Indicates whether the Aggregate Chronology is a default or not. Default status is determined by a Neotoma data steward.  Aggregate Datasets may have more than one default Aggregate Chronology, but may have only one default Aggregate Chronology per Age Type.

**ChronologyName** 
  Optional name for the Chronology.

**AgeBoundYounger**
  The younger reliable age bound for the Aggregate Chronology. Younger ages may be assigned to samples, but are not regarded as reliable. If the entire Chronology is considered reliable, AgeBoundYounger is assigned the youngest sample age rounded down to the nearest 10. Thus, for 72 BP, AgeBoundYounger = 70 BP; for -45 BP, AgeBoundYounger = -50 BP.

**AgeBoundOlder** 
  The older reliable age bound for the Aggregate Chronology. Ages older than AgeOlderBound may be assigned to samples, but are not regarded as reliable. This situation is particularly true for ages extrapolated beyond the oldest Chron Control. . If the entire Chronology is considered reliable, AgeBoundOlder is assigned the oldest sample age rounded up to the nearest 10. Thus, for 12564 BP, AgeBoundOlder is 12570.

**Notes**
  Free form notes or comments about the Aggregate Chronology.

.. _ChronControls:

ChronControls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores data for Chronology Controls, which are the age-depth control points used for age models. These controls may be geophysical controls, such as radiocarbon dates, but include many other kinds of age controls, such as biostratigraphic controls, archaeological cultural associations, and volcanic tephras. In the case of radiocarbon dates, a Chronology Control may not simply be the raw radiocarbon date reported by the laboratory, but perhaps a radiocarbon date corrected for an old carbon reservoir, a calibrated radiocarbon date, or an average of several radiocarbon dates from the same level. A common control for lake-sediment cores is the age of the top of the core, which may be the year the core was taken or perhaps an estimate of 0 BP if a few cm of surficial sediment were lost.

+----------------------------+---------+------+---------------------+
| **ChronControls**          |                                      |
+----------------------------+---------+------+---------------------+
| ChronControlID             | int     | PK   |                     |
+----------------------------+---------+------+---------------------+
| ChronologyID               | int     | FK   | Chronologies        |
+----------------------------+---------+------+---------------------+
| ChronControlTypeID         | int     | FK   | ChronControlTypes   |
+----------------------------+---------+------+---------------------+
| Depth                      | float   |      |                     |
+----------------------------+---------+------+---------------------+
| Thickness                  | float   |      |                     |
+----------------------------+---------+------+---------------------+
| Age                        | float   |      |                     |
+----------------------------+---------+------+---------------------+
| AgeLimitYounger            | float   |      |                     |
+----------------------------+---------+------+---------------------+
| AgeLimitOlder              | float   |      |                     |
+----------------------------+---------+------+---------------------+
| Notes                      | ntext   |      |                     |
+----------------------------+---------+------+---------------------+

**ChronControlID (Primary Key)**
  An arbitrary Chronology Control identification number.

**ChronologyID (Foreign Key)**
  Chronology to which the ChronControl belongs. Field links to the Chronolgies table.

**ChronControlTypeID (Foreign Key)** 
  The type of Chronology Control. Field links to the :ref:`ChronControlTypes` table.

**Depth**
  Depth of the Chronology Control in cm.

**Thickness**
  Thickness of the Chronology Control in cm.

**Age**
  Age of the Chronology Control.

**AgeLimitYounger**
  The younger age limit of a Chronology Control. This limit may be explicitly defined, for example the younger of the 2-sigma range limits of a calibrated radiocarbon date, or it may be more loosely defined, for example the younger limit on the range of dates for a biostratigraphic horizon.

**AgeLimitOlder**
  The older age limit of a Chronology Control.

**Notes**
  Free form notes or comments about the Chronology Control.

.. _ChronControlTypes:

ChronControlTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Chronology Control Types. This table is referenced by
the :ref:`ChronControls` table.

+--------------------------------+----------------+------+-----+
| **ChronControlTypes**          |                             |
+--------------------------------+----------------+------+-----+
| ChronControlTypeID             | int            | PK   |     |
+--------------------------------+----------------+------+-----+
| ChronControlType               | nvarchar(50)   |      |     |
+--------------------------------+----------------+------+-----+

**ChronControlTypeID (Primary Key)**
  An arbitrary Chronology Control Type identification number.

**ChronControlType**
  The Chronology Control Type. Chronology Controls include such geophysical controls as radiocarbon dates, calibrated radiocarbon dates, averages of several radiocarbon dates, potassium-argon dates, and thermoluminescence dates, as well as biostratigraphic controls, sediment stratigraphic contols, volcanic tephras, archaeological cultural associations, and any other types of age controls.

.. _Chronologies:

Chronologies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores Chronology data. A Chronology refers to an explicit chronology assigned to a Collection Unit. A Chronology has Chronology Controls, the actual age-depth control points, which are stored in the `ChronControls` table. A Chronology is also based on an Age Model, which may be a numerical method that fits a curve to a set of age-depth control points or may simply be individually dated Analysis Units.

A Collection Unit may have more than one Chronology, for example one in radiocarbon years and another in calibrated radiocarbon years. There may be a Chronology developed by the original author and another developed by a later research project. Chronologies may be stored for archival reasons, even though they are now believed to have problems, if they were used for an important research project. One Chronology per Age Type may be designated the default Chronology, which is the Chronology currently preferred by the database stewards.

Based upon the Chronology, which includes the Age Model and the Chron Controls, ages are assigned to individual samples, which are stored in the :ref:`SampleAges` table. 

A younger and older age bounds are assigned to the Chronology. Within these bounds the Chronology is regarded as reliable. Ages may be assigned to samples beyond the reliable age bounds, but these are not considered reliable.

+---------------------------+----------------+------+-------------------+
| **Chronologies**          |                                           |
+---------------------------+----------------+------+-------------------+
| ChronologyID              | int            | PK   |                   |
+---------------------------+----------------+------+-------------------+
| CollectionUnitID          | int            | FK   | CollectionUnits   |
+---------------------------+----------------+------+-------------------+
| AgeTypeID                 | int            | FK   | AgeTypes          |
+---------------------------+----------------+------+-------------------+
| ContactID                 | int            | FK   | Contacts          |
+---------------------------+----------------+------+-------------------+
| IsDefault                 | bit            |      |                   |
+---------------------------+----------------+------+-------------------+
| ChronologyName            | nvarchar(80)   |      |                   |
+---------------------------+----------------+------+-------------------+
| DatePrepared              | datetime       |      |                   |
+---------------------------+----------------+------+-------------------+
| AgeModel                  | nvarchar(80)   |      |                   |
+---------------------------+----------------+------+-------------------+
| AgeBoundYounger           | int            |      |                   |
+---------------------------+----------------+------+-------------------+
| AgeBoundOlder             | int            |      |                   |
+---------------------------+----------------+------+-------------------+
| Notes                     | ntext          |      |                   |
+---------------------------+----------------+------+-------------------+

**ChronologyID (Primary Key)**
  An arbitrary Chronology identification number.

**CollectionUnitID (Foreign Key)**
  Collection Unit to which the Chronology applies. Field links to the :ref:`CollectionUnits` table.

**AgeTypeID (Foreign Key)**
  Age type or units. Field links to the :ref:`AgeTypes` table.

**ContactID (Foreign Key)** 
  Person who developed the Age Model. Field links to the :ref:`Contacts` table.

**IsDefault**
  Indicates whether the Chronology is a default chronology or not. Default status is determined by a Neotoma data steward. Collection Units may have more than one default Chronology, but may have only one default Chronology per Age Type. Thus, there may be a default radiocarbon year Chronology and a default calibrated radiocarbon year Chronology, but only one of each. Default Chronologies may be used by the Neotoma web site, or other web sites, for displaying default diagrams or time series of data. Default Chronologies may also be of considerable use for actual research purposes; however, users may of course choose to develop their own chronologies.

**ChronologyName**
  Optional name for the Chronology. Some examples are:

  * COHMAP chron 1 A Chronology assigned by the COHMAP project.
  * COHMAP chron 2 An alternative Chronology assigned by the COHMAP project
  * NAPD 1 A Chronology assigned by the North American Pollen Database.
  * Gajewski 1995 A Chronology assigned by Gajewski (1995).

**DatePrepared**
  Date that the Chronology was prepared.

**AgeModel**
  The age model used for the Chronology. Some examples are: linear interpolation, 3\ :sup:`rd` order polynomial, and individually dated analysis units.

**AgeBoundYounger** 
  The younger reliable age bound for the Chronology. Younger ages may be assigned to samples, but are not regarded as reliable. If the entire Chronology is considered reliable, AgeBoundYounger is assigned the youngest sample age rounded down to the nearest 10. Thus, for 72 BP, AgeBoundYounger = 70 BP; for -45 BP, AgeBoundYounger = -50 BP.

**AgeBoundOlder** 
  The older reliable age bound for the Chronology. Ages older than AgeOlderBound may be assigned to samples, but are not regarded as reliable. This situation is particularly true for ages extrapolated beyond the oldest Chron Control. . If the entire Chronology is considered reliable, AgeBoundOlder is assigned the oldest sample age rounded up to the nearest 10. Thus, for 12564 BP, AgeBoundOlder is 12570.

**Notes**
  Free form notes or comments about the Chronology.

SQL Example
````````````````````````````

The following SQL statement produces a list of Chronologies for :

.. code-block:: sql
   :linenos:

   SELECT Sites.SiteName, Chronologies.ChronologyName,
   Chronologies.IsDefault, AgeTypes.AgeType

   FROM AgeTypes INNER JOIN ((Sites INNER JOIN CollectionUnits ON
   Sites.SiteID = CollectionUnits.SiteID) INNER JOIN Chronologies ON
   CollectionUnits.CollectionUnitID = Chronologies.CollectionUnitID) ON
   AgeTypes.AgeTypeId = Chronologies.AgeTypeID

   WHERE (((Sites.SiteName)=""));

Result:

+----------------+----------------------+-----------------+-----------------------------------+
| **SiteName**   | **ChronologyName**   | **IsDefault**   | **AgeType**                       |
+----------------+----------------------+-----------------+-----------------------------------+
|                | COHMAP chron 1       | FALSE           | Radiocarbon years BP              |
+----------------+----------------------+-----------------+-----------------------------------+
|                | NAPD 1               | TRUE            | Radiocarbon years BP              |
+----------------+----------------------+-----------------+-----------------------------------+
|                | NAPD 2               | TRUE            | Calibrated radiocarbon years BP   |
+----------------+----------------------+-----------------+-----------------------------------+

SQL Example
````````````````````````````

The following statement produces a list of the ChronControls for the
Default Chronology from in Calibrated radiocarbon years BP:

.. code-block:: sql
   :linenos:

   SELECT ChronControls.Depth, ChronControls.Age,
   ChronControls.AgeLimitYounger, ChronControls.AgeLimitOlder,
   ChronControlTypes.ChronControlType

   FROM ChronControlTypes INNER JOIN ((AgeTypes INNER JOIN ((Sites INNER
   JOIN CollectionUnits ON Sites.SiteID = CollectionUnits.SiteID) INNER
   JOIN Chronologies ON CollectionUnits.CollectionUnitID =
   Chronologies.CollectionUnitID) ON AgeTypes.AgeTypeId =
   Chronologies.AgeTypeID) INNER JOIN ChronControls ON
   Chronologies.ChronologyID = ChronControls.ChronologyID) ON
   ChronControlTypes.ChronControlTypeID = ChronControls.ChronControlTypeID

   WHERE (((Sites.SiteName)="Wolsfeld Lake") AND
   ((Chronologies.IsDefault)=True) AND ((AgeTypes.AgeType)="Calibrated
   radiocarbon years BP"));

Result:

+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| **Depth**   | **Age**   | **AgeLimitYounger**   | **AgeLimitOlder**   | **ChronControlType**                     |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 650         | -25       | -25                   | -25                 | Core top                                 |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 662         | -13       | -8                    | -18                 | Interpolated, corrected for compaction   |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 670         | 0         | -5                    | 5                   | Interpolated, corrected for compaction   |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 680         | 22        | 17                    | 27                  | Interpolated, corrected for compaction   |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 690         | 46        | 41                    | 51                  | Interpolated, corrected for compaction   |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 702         | 72        | 67                    | 77                  | Interpolated, corrected for compaction   |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 715         | 100       | 80                    | 120                 | Biostratigraphic, pollen                 |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 750         | 335       | 120                   | 492                 | Radiocarbon, calibrated                  |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 785         | 433       | 310                   | 517                 | Radiocarbon, calibrated                  |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 975         | 2242      | 2063                  | 2433                | Radiocarbon, calibrated                  |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 1065        | 3402      | 3261                  | 3556                | Radiocarbon, calibrated                  |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 1135        | 3776      | 3585                  | 3973                | Radiocarbon, calibrated                  |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 1345        | 5836      | 5662                  | 5992                | Radiocarbon, calibrated                  |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 1415        | 6910      | 6730                  | 7160                | Radiocarbon, calibrated                  |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 1520        | 8268      | 8022                  | 8443                | Radiocarbon, calibrated                  |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 1640        | 11636     | 11264                 | 12027               | Radiocarbon, calibrated                  |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+
| 1725        | 13864     | 13646                 | 14218               | Radiocarbon, calibrated                  |
+-------------+-----------+-----------------------+---------------------+------------------------------------------+

.. _AggregateSampleAges:

AggregateSampleAges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores the links to the ages of samples in an Aggregate Dataset. The table is necessary because samples may be from Collection Units with multiple chronologies, and this table stores the links to the sample ages desired for the Aggregate Dataset.

+----------------------------------+-------+----------+-------------------------+
| **AggregateSampleAges**                                                       |
+----------------------------------+-------+----------+-------------------------+
| AggregateDatasetID               | int   | PK, FK   | AggregateDatasets       |
+----------------------------------+-------+----------+-------------------------+
| AggregateChronID                 | int   | PK, FK   | AggregateChronologies   |
+----------------------------------+-------+----------+-------------------------+
| SampleAgeID                      | int   | PK, FK   | SampleAges              |
+----------------------------------+-------+----------+-------------------------+

**AggregateDatasetID (Primary Key, Foreign Key)**
  Aggregate Dataset identification number. Field links to the :ref:`AggregateDatasets` table.

**AggregateChronID (Primary Key, Foreign Key)**
  Aggregate Chronology identification number Field links to the :ref:`AggregateChronologies` table.

**SampleAgeID (Primary Key, Foreign Key)**
  Sample Age ID number. Field links to the :ref:`SampleAges` table.

SQL Example
``````````````````````````````````````

The following SQL statement produces a list of Sample ID numbers and ages for the Aggregate Dataset:

.. code-block:: sql
   :linenos:
   SELECT AggregateSamples.SampleID, SampleAges.Age

   FROM SampleAges INNER JOIN ((AggregateDatasets INNER JOIN
   AggregateSampleAges ON AggregateDatasets.AggregateDatasetID =
   AggregateSampleAges.AggregateDatasetID) INNER JOIN AggregateSamples ON
   AggregateDatasets.AggregateDatasetID =
   AggregateSamples.AggregateDatasetID) ON (AggregateSamples.SampleID =
   SampleAges.SampleID) AND (SampleAges.SampleAgeID =
   AggregateSampleAges.SampleAgeID)

   WHERE (((AggregateDatasets.AggregateDatasetName)=""));


SQL Example
`````````````````````````````

The AggregateSampleAges table may have multiple SampleAgeID's for Aggregate Dataset samples, for example SampleAgeID's for radiocarbon and calibrated radiocarbon chronologies. In this case, the Chronolgies table must be linked into a query to obtain the ages of Aggregate Samples, and either the AgeTypeID must be specified in the Chronolgies table or the :ref:`AgeTypes` table must also be linked with the AgeType specified. The following SQL statement produces a list of Sample ID numbers and «Radiocarbon years BP» ages for the «» Aggregate Dataset: :ref:`Samples`

.. code-block:: sql
   :linenos:

   SELECT AggregateSamples.SampleID, SampleAges.Age

   FROM AgeTypes INNER JOIN (Chronologies INNER JOIN (SampleAges INNER JOIN
   ((AggregateDatasets INNER JOIN AggregateSampleAges ON
   AggregateDatasets.AggregateDatasetID =
   AggregateSampleAges.AggregateDatasetID) INNER JOIN AggregateSamples ON
   AggregateDatasets.AggregateDatasetID =
   AggregateSamples.AggregateDatasetID) ON (AggregateSamples.SampleID =
   SampleAges.SampleID) AND (SampleAges.SampleAgeID =
   AggregateSampleAges.SampleAgeID)) ON Chronologies.ChronologyID =
   SampleAges.ChronologyID) ON AgeTypes.AgeTypeId = Chronologies.AgeTypeID

   WHERE (((AggregateDatasets.AggregateDatasetName)="") AND
   ((AgeTypes.AgeType)="Radiocarbon years BP"));

.. _Geochronology:

Geochronology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores geochronologic data. Geochronologic measurements are from geochronologic samples, which are from Analysis Units, which may have a depth and thickness. Geochronologic measurments may be from the same or different Analysis Units as fossils. In the case of faunal excavations, geochronologic samples are typically from the same Analysis Units as the fossils, and there may be multiple geochronologic samples from a single Analysis Unit. In the case of cores used for microfossil analyses, geochronologic samples are often from separate Analysis Units; dated core sections are often thicker than microfossil Analysis Units.

+----------------------------+----------------+------+-----------------+
| **Geochronology**                                                    |
+----------------------------+----------------+------+-----------------+
| GeochronID                 | Long Integer   | PK   |                 |
+----------------------------+----------------+------+-----------------+
| SampleID                   | Long Integer   | FK   | Samples         |
+----------------------------+----------------+------+-----------------+
| GeochronTypeID             | Long Integer   | FK   | GeochronTypes   |
+----------------------------+----------------+------+-----------------+
| AgeTypeID                  | Long Integer   | FK   | AgeTypes        |
+----------------------------+----------------+------+-----------------+
| Age                        | Double         |      |                 |
+----------------------------+----------------+------+-----------------+
| ErrorOlder                 | Double         |      |                 |
+----------------------------+----------------+------+-----------------+
| ErrorYounger               | Double         |      |                 |
+----------------------------+----------------+------+-----------------+
| Infinite                   | Yes/No         |      |                 |
+----------------------------+----------------+------+-----------------+
| Delta13C                   | Double         |      |                 |
+----------------------------+----------------+------+-----------------+
| LabNumber                  | Text           |      |                 |
+----------------------------+----------------+------+-----------------+
| MaterialDated              | Text           |      |                 |
+----------------------------+----------------+------+-----------------+
| Notes                      | Memo           |      |                 |
+----------------------------+----------------+------+-----------------+

**GeochronID (Primary Key)** 
  An arbitrary Geochronologic identificantion number.

**SampleID (Foreign Key)**
  Sample identification number. Field links to :ref:`Samples` table.

**GeochronTypeID (Foreign Key)**
  Identification number for the type of Geochronologic analysis, e.g. «Carbon-14», «Thermoluminescence». Field links to the :ref:`GeochronTypes` table.

**AgeTypeID (Foreign Key)**
  Identification number for the age units, e.g. «Radiocarbon years BP», «Calibrated radiocarbon years BP».

**Age** 
  Reported age value of the geochronologic measurement.

**ErrorOlder**
  The older error limit of the age value. For a date reported with ±1 SD or σ, the ErrorOlder and ErrorYounger values are this value.

**ErrorYounger** 
  The younger error limit of the age value.

**Infinite** 
  Is «True» for and infinite or “greater than” geochronologic measurement, otherwise is «False».

**Delta13C**
  The measured or assumed δ\ :sup:`13`\ C value for radiocarbon dates, if provided. Radiocarbon dates are assumed to be normalized to δ\ :sup:`13`\ C, and if uncorrected and normalized ages are reported, the normalized age should be entered in the database.

**LabNumber**
  Lab number for the geochronologic measurement.

**Material Dated**
  Material analyzed for a geochronologic measurement.

**Notes**
  Free form notes or comments about the geochronologic measurement.

SQL Example
`````````````````````````````

This query lists the geochronologic data for Montezuma Well.

.. code-block:: sql
   :linenos:

   SELECT AnalysisUnits.Depth, AnalysisUnits.Thickness, 
   GeochronTypes.GeochronType, Geochronology.Age, Geochronology.ErrorOlder,
   Geochronology.ErrorYounger, Geochronology.Delta13C,
   Geochronology.LabNumber, Geochronology.MaterialDated,
   Geochronology.Notes

   FROM GeochronTypes INNER JOIN ((((Sites INNER JOIN CollectionUnits ON
   Sites.SiteID = CollectionUnits.SiteID) INNER JOIN AnalysisUnits ON
   CollectionUnits.CollectionUnitID = AnalysisUnits.CollectionUnitID) INNER
   JOIN Samples ON AnalysisUnits.AnalysisUnitID = Samples.AnalysisUnitID)
   INNER JOIN Geochronology ON Samples.SampleID = Geochronology.SampleID)
   ON GeochronTypes.GeochronTypeID = Geochronology.GeochronTypeID

   WHERE (((Sites.SiteName)="Montezuma Well"));

Result:

+-------------+---------------+--------------------------------------------+-----------+-------------------+---------------------+----------------+------------------+---------------------+----------------------------------------------+
| **Depth**   | **Thick..**   | **GeochronType**                           | **Age**   | **Error Older**   | **Error Younger**   | **Delta13C**   | **Lab Number**   | **MaterialDated**   | **Notes**                                    |
+-------------+---------------+--------------------------------------------+-----------+-------------------+---------------------+----------------+------------------+---------------------+----------------------------------------------+
| 1015        | 1             | Carbon-14: accelerator mass spectrometry   | 10975     | 95                | 95                  |                | AA-4694          | Juniperus twig      |                                              |
+-------------+---------------+--------------------------------------------+-----------+-------------------+---------------------+----------------+------------------+---------------------+----------------------------------------------+
| 225         | 10            | Carbon-14: accelerator mass spectrometry   | 1526      | 50                | 50                  |                | AA-2450          | charcoal, wood      |                                              |
+-------------+---------------+--------------------------------------------+-----------+-------------------+---------------------+----------------+------------------+---------------------+----------------------------------------------+
| 330         | 10            | Carbon-14: accelerator mass spectrometry   | 2885      | 60                | 60                  |                | AA-2451          | charcoal, wood      |                                              |
+-------------+---------------+--------------------------------------------+-----------+-------------------+---------------------+----------------+------------------+---------------------+----------------------------------------------+
| 395         | 10            | Carbon-14: accelerator mass spectrometry   | 5540      | 60                | 60                  |                | AA-4693          | charcoal, wood      |                                              |
+-------------+---------------+--------------------------------------------+-----------+-------------------+---------------------+----------------+------------------+---------------------+----------------------------------------------+
| 465         | 10            | Carbon-14: accelerator mass spectrometry   | 8003      | 70                | 70                  |                | AA-2452          | Scirpus achenes     |                                              |
+-------------+---------------+--------------------------------------------+-----------+-------------------+---------------------+----------------+------------------+---------------------+----------------------------------------------+
| 535         | 10            | Carbon-14: proportional gas counting       | 14950     | 350               | 320                 | -26.7          | A-4732           | bark                | Davis and Shafer (1992) reject as too old.   |
+-------------+---------------+--------------------------------------------+-----------+-------------------+---------------------+----------------+------------------+---------------------+----------------------------------------------+
| 887         | 1             | Carbon-14: proportional gas counting       | 9520      | 200               | 200                 | -25.3          | A-4733           | wood                |                                              |
+-------------+---------------+--------------------------------------------+-----------+-------------------+---------------------+----------------+------------------+---------------------+----------------------------------------------+
| 887         | 1             | Carbon-14: accelerator mass spectrometry   | 24910     | 370               | 370                 |                | AA-5053          | wood                | Davis and Shafer (1992) reject as too old.   |
+-------------+---------------+--------------------------------------------+-----------+-------------------+---------------------+----------------+------------------+---------------------+----------------------------------------------+

.. _GeochronPublications:

GeochronPublications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Publications in which Geochronologic measurements are reported. Many older radiocarbon dates are reported in the journal *Radiocarbon*. Dates may be reported in multiple publications. The "publication" could be a database such as the online Canadian Archaeological Radiocarbon Database.

+-----------------------------------+----------------+----------+-----------------+
| **GeochronPublications**                                                        |
+-----------------------------------+----------------+----------+-----------------+
| GeochronID                        | Long Integer   | PK, FK   | Geochronology   |
+-----------------------------------+----------------+----------+-----------------+
| PublicationID                     | Long Integer   | PK, FK   | Publications    |
+-----------------------------------+----------------+----------+-----------------+

**GeochronID (Primary Key, Foreign Key)** 
  Geochronologic identification number. Field links to the :ref:`Geochronology` table.

**PublicationID (Primary Key, Foreign Key)**
  Publication identification number. Field links to the :ref:`Publications` table.

.. _GeochronTypes:

GeochronTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table for Geochronology Types. Table is referenced by the
:ref:`Geochronology` table.

+----------------------------+----------------+------+-----+
| **GeochronTypes**                                        |
+----------------------------+----------------+------+-----+
| GeochronTypeID             | Long Integer   | PK   |     |
+----------------------------+----------------+------+-----+
| GeochronType               | Text           |      |     |
+----------------------------+----------------+------+-----+

**GeochronTypeID (Primary Key)**
  Geochronology Type identification number.

**GeochronType**
  Type of Geochronologic measurement.

.. _RelativeAgePublications:

RelativeAgePublications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores Publications in which Relative Ages are reported for CollectionUnits.

+--------------------------------------+----------------+----------+----------------+
| **RelativeAgePublications**                                                       |
+--------------------------------------+----------------+----------+----------------+
| RelativeAgeID                        | Long Integer   | PK, FK   | RelativeAges   |
+--------------------------------------+----------------+----------+----------------+
| PublicationID                        | Long Integer   | PK, FK   | Publications   |
+--------------------------------------+----------------+----------+----------------+

**RelativeAgeID (Primary Key, Foreign Key)** 
  Relative Ages identification number. Field links to the :ref:`RelativeAges` table.

**PublicationID (Primary Key, Foreign Key)**
  Publication identification number. Field links to :ref:`Publications` table.

.. _RelativeAges:

RelativeAges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of RelativeAges. Table is referenced by the :ref:`RelativeChronology` table.

+---------------------------+----------------+------+---------------------+
| **RelativeAges**                                                        |
+---------------------------+----------------+------+---------------------+
| RelativeAgeID             | Long Integer   | PK   |                     |
+---------------------------+----------------+------+---------------------+
| RelativeAgeUnitID         | Long Integer   | FK   | RelativeAgeUnits    |
+---------------------------+----------------+------+---------------------+
| RelativeAgeScaleID        | Long Integer   | FK   | RelativeAgeScales   |
+---------------------------+----------------+------+---------------------+
| RelativeAge               | Text           |      |                     |
+---------------------------+----------------+------+---------------------+
| C14AgeYounger             | Double         |      |                     |
+---------------------------+----------------+------+---------------------+
| C14AgeOlder               | Double         |      |                     |
+---------------------------+----------------+------+---------------------+
| CalAgeYounger             | Double         |      |                     |
+---------------------------+----------------+------+---------------------+
| CalAgeOlder               | Double         |      |                     |
+---------------------------+----------------+------+---------------------+
| Notes                     | Memo           |      |                     |
+---------------------------+----------------+------+---------------------+

**RelativeAgeID (Primary Key)** 
  An arbitrary Relative Age identification number.

**RelativeAgeUnitID (Foreign Key)**
  Relative Age Unit (e.g. «Marine isotope stage», «Land mammal age»). Field links to the :ref:`RelativeAgeUnits` lookup table.

**RelativeAgeScaleID (Foreign Key)**
  Relative Age Scale (e.g. «Geologic time scale», «Marine isotope stages»). Field links to the :ref:`RelativeAgeScales` lookup table.

**RelativeAge**
  Relative Age (e.g. «Rancholabrean», a land mammal age; «MIS 11», marine isotope stage 11).

**C14AgeYounger**
  Younger age of the Relative Age unit in :sup:`14`\ C yr B.P. Applies only to Relative Age units within the radiocarbon time scale.

**C14AgeOlder**
  Older age of the Relative Age unit in :sup:`14`\ C yr B.P. Applies only to Relative Age units within the radiocarbon time scale.

**CalAgeYounger**
  Younger age of the Relative Age unit in calendar years.

**CalAgeOlder**
  Older age of the Relative age unit in calendar years.

**Notes**
  Free form notes or comments about Relative Age unit.

SQL Example
``````````````````````````````````

The following query gives the Relative Ages for the «North American land
mammal ages». The Relative Age Unit for each of these is «Land mammal
age». Commas were added to the ages in the query result to make them
more readable.

.. code-block:: sql
   :linenos:

   SELECT RelativeAges.RelativeAge, RelativeAges.CalAgeYounger,
   RelativeAges.CalAgeOlder

   FROM RelativeAgeScales INNER JOIN RelativeAges ON
   RelativeAgeScales.RelativeAgeScaleID = RelativeAges.RelativeAgeScaleID

   WHERE (((RelativeAgeScales.RelativeAgeScale)="North American land mammal ages"));

Result:

+--------------------+---------------------+-------------------+
| **RelativeAge**    | **CalAgeYounger**   | **CalAgeOlder**   |
+--------------------+---------------------+-------------------+
| Rancholabrean      | 11,800              | 150,000           |
+--------------------+---------------------+-------------------+
| Irvingtonian       | 150,000             | 1,900,000         |
+--------------------+---------------------+-------------------+
| Irvingtonian I     | 850,000             | 1,900,000         |
+--------------------+---------------------+-------------------+
| Irvingtonian II    | 400,000             | 850,000           |
+--------------------+---------------------+-------------------+
| Irvingtonian III   | 150,000             | 400,000           |
+--------------------+---------------------+-------------------+
| Blancan            | 1,900,000           | 4,900,000         |
+--------------------+---------------------+-------------------+
| Blancan I          | 4,620,000           | 4,900,000         |
+--------------------+---------------------+-------------------+
| Blancan II         | 4,100,000           | 4,620,000         |
+--------------------+---------------------+-------------------+
| Blancan III        | 3,000,000           | 4,100,000         |
+--------------------+---------------------+-------------------+
| Blancan IV         | 2,500,000           | 3,000,000         |
+--------------------+---------------------+-------------------+
| Blancan V          | 1,900,000           | 2,500,000         |
+--------------------+---------------------+-------------------+

.. _RadiocarbonCalibration:

RadiocarbonCalibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Radiocarbon calibraton table. This table is intended for quick calibraton of age-model radiocarbon dates. These calibrated dates are for perusal and data exploration only. Please see Section *2.5* for a full discussion.

+-------------------------------------+----------------+------+-----+
| **RadiocarbonCalibration**                                        |
+-------------------------------------+----------------+------+-----+
| C14yrBP                             | Long Integer   | PK   |     |
+-------------------------------------+----------------+------+-----+
| CalyrBP                             | Long Integer   |      |     |
+-------------------------------------+----------------+------+-----+

**C14yrBP**
  Age in radiocarbon years BP. The range is -100 to 45,000 by 1-year increments.

**CalyrBP**
  Age in calibrated radiocarbon years BP.

.. _RelativeAgeScales:

RelativeAgeScales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Relative Age Scales. Table is referenced by the
:ref:`RelativeAges` table.

+--------------------------------+----------------+------+-----+
| **RelativeAgeScales**                                        |
+--------------------------------+----------------+------+-----+
| RelativeAgeScaleID             | Long Integer   | PK   |     |
+--------------------------------+----------------+------+-----+
| RelativeAgeScale               | Text           |      |     |
+--------------------------------+----------------+------+-----+

**RelativeAgeScaleID (Primary Key)**
  An arbitrary Relative Age Scale identification number.

**RelativeAgeScale** 
  Relative Age Scale. The table stores the following Relative Age Scales:

  * Archaeological time scale
  * Geologic time scale
  * Geomagnetic polarity time scale
  * Marine isotope stages
  * North American land mammal ages
  * Quaternary event classification

.. _RelativeAgeUnits:

RelativeAgeUnits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of RelativeAgeUnits. Table is referenced by the
:ref:`RelativeAges` table.

+-------------------------------+----------------+------+-----+
| **RelativeAgeUnits**                                        |
+-------------------------------+----------------+------+-----+
| RelativeAgeUnitID             | Long Integer   | PK   |     |
+-------------------------------+----------------+------+-----+
| RelativeAgeUnit               | Text           |      |     |
+-------------------------------+----------------+------+-----+

**RelativeAgeUnitID (Primary Key)** 
  An arbitrary Relative Age Unit identification number.

**RelativeAgeUnit** 
  Relative Age Unit. Below are the Relative Age Units for the «Geologic time scale» with an example Relative Age.

+---------------------------+---------------------------+
| **Geologic time scale**                               |
+---------------------------+---------------------------+
| **RelativeAgeUnit**       | **RelativeAge Example**   |
+---------------------------+---------------------------+
| Period                    | Quaternary                |
+---------------------------+---------------------------+
| Epoch                     | Pleistocene               |
+---------------------------+---------------------------+
| Stage                     | Middle Pleistocene        |
+---------------------------+---------------------------+
| Informal stage            | Middle Holocene           |
+---------------------------+---------------------------+

«Period», «Epoch», and «Stage» are defined by the International Commission on Statigraphy. An «Informal stage» is defined in Neotoma.

.. _RelativeChronology:

RelativeChronology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores relative chronologic data. Relative Ages are assigned to Analysis Units, The Relative Age data along with any possible :ref:`Geochronology` and :ref:`Tephrachronology` data are used to create a chronology.

+---------------------------------+----------------+------+-----------------+
| RelativeChronology**                                                      |
+---------------------------------+----------------+------+-----------------+
| RelativeChronID                 | Long Integer   | PK   |                 |
+---------------------------------+----------------+------+-----------------+
| AnalysisUnitID                  | Long Integer   | FK   | AnalysisUnits   |
+---------------------------------+----------------+------+-----------------+
| RelativeAgeID                   | Long Integer   | FK   | RelativeAges    |
+---------------------------------+----------------+------+-----------------+
| Notes                           | Memo           |      |                 |
+---------------------------------+----------------+------+-----------------+

**RelativeChronID (Primary Key)**
  An arbitrary Relative Chronology identification number.

**AnalysisUnitID (Foreign Key)**
  Analysis Unit identification number. Field links to the :ref:`AnalysisUnits` table.

**RelativeAgeID (Foreign Key)**
  Relative Age identification number. Field links to the :ref:`RelativeAges` lookup table.

**Notes**
  Free form notes or comments.

.. _Tephrachronology:

Tephrachronology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores tephrachronologic data. The table relates Analysis Units with dated tephras in the :ref:`Tephras` table.
These are tephras with established ages that are used form a chronology.  The tephras are typically not directly dated at the Site of the Analysis Unit, but have been dated at other sites. A directly dated tephra, e.g. an argon-argon date, belongs in the :ref:`Geochronology` table.

+-------------------------------+----------------+------+-----------------+
| **Table: Tephrachronology**   |
+-------------------------------+----------------+------+-----------------+
| TephrachronID                 | Long Integer   | PK   |                 |
+-------------------------------+----------------+------+-----------------+
| AnalysisUnitID                | Long Integer   | FK   | AnalysisUnits   |
+-------------------------------+----------------+------+-----------------+
| TephraID                      | Long Integer   | FK   | Tephras         |
+-------------------------------+----------------+------+-----------------+
| Notes                         | Memo           |      |                 |
+-------------------------------+----------------+------+-----------------+

**TephrachronID (Primary Key)** An arbitrary Tephrachronology identification number.

**AnalysisUnitID (Foreign Key)** Analysis Unit identification number. Field links to the :ref:`AnalysisUnits` table. The tephra may be contained within the AnalysisUnit, especially in excavations, or the AnalysisUnit may be assigned specifically to the tephra, particulary with cores.

**TephraID (Foreign Key)** Tephra identification number. Field links to the :ref:`Tephras` table.

**Notes** Free form notes or comments about the tephra.

.. _Tephras:

Tephras
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tephras lookup table. This table stores recognized tephras with
established ages. Referenced by the
`Tephrachronology` table.

+----------------------+----------------+------+-----+
| **Table: Tephras**   |
+----------------------+----------------+------+-----+
| TephraID             | Long Integer   | PK   |     |
+----------------------+----------------+------+-----+
| TephraName           | Text           |      |     |
+----------------------+----------------+------+-----+
| C14Age               | Double         |      |     |
+----------------------+----------------+------+-----+
| C14AgeYounger        | Double         |      |     |
+----------------------+----------------+------+-----+
| C14AgeOlder          | Double         |      |     |
+----------------------+----------------+------+-----+
| CalAge               | Double         |      |     |
+----------------------+----------------+------+-----+
| CalAgeYounger        | Double         |      |     |
+----------------------+----------------+------+-----+
| CalAgeOlder          | Double         |      |     |
+----------------------+----------------+------+-----+
| Notes                | Memo           |      |     |
+----------------------+----------------+------+-----+

**TephraID (Primary Key)** An arbitrary Tephra identification number.

**TephraName** Name of the tephra, e.g. «Mazama».

**C14Age** Age of the tephra in :sup:`14`\ C yr BP. For example,
Hallett et al. (1997) provide an estimate of the age of the Mazama
tephra based on radiocarbon dating of plant macrofossils in lake
sediments encasing the tephra.

**C14AgeYounger** Younger age estimate of the tephra in :sup:`14`\ C yr
BP.

**C14AgeOlder** Older age estimate of the tephra in :sup:`14`\ C yr BP.

**CalAge** Age of the tephra in cal yr BP, either calibrated
radiocarbon years or estimated calendar years derived from another
dating method. For example, Zdanowicz et al. (1999) identified the
Mazama tephra in the GISP2 ice core and estimated the age from layer
counts.

**CalAgeYounger** Younger age estimate of the tephra in cal yr BP.

**CalAgeOlder** Older age estimate of the tephra in cal yr BP.

**Notes** Free form notes or comments about the tephra.

