Neotoma Tables
=============================

The Neotoma Database contains more than 100 tables and as new proxy types get added, or new metadata is stored, the number of tables may increase or decrease.  As a result, this manual should not be considered the final authority, but it should provide nearly complete coverage of the database and its structure.  In particular, we divide tables into logical groupings, Chronology & Chronology related tables, Site related tables, Contact tables, Sample tables and so on.

Chronology & Age Related Tables
-----------------------------

AgeTypes, AggregateChronologies, ChronControls, Chronologies, AggregateSampleAges, Geochronology, GeochronPublications, GeochronTypes, RelativeAgePublications, RelativeAges, RadiocarbonCalibration, RelativeAgeScales, RelativeAgeUnits, RelativeChronology


Dataset & Collection Related Tables
-----------------------------------

AggregateDatasets

Sample & Sample Related Tables
---------------------------





DepEnvtTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Depostional Environment Types. Table is referenced by
the `CollectionUnits`__ table.

+---------------------------+----------------+------+--------------------------+
| **DepEnvtTypes**                                                             |
+---------------------------+----------------+------+--------------------------+
| DepEnvtID                 | Long Integer   | PK   |                          |
+---------------------------+----------------+------+--------------------------+
| DepEnvt                   | Text           |      |                          |
+---------------------------+----------------+------+--------------------------+
| DepEnvtHigherID           | Long Integer   | FK   | DepEnvtTypes:DepEnvtID   |
+---------------------------+----------------+------+--------------------------+

**DepEnvtID (Primary Key)** An arbitrary Depositional Environment Type
identification number.

**DepEnvt** Depositional Environment.

**DepEnvtHigherID** The Depositional Environment Types are
hierarchical. DepEnvtHigherID is the DepEnvtID of the higher ranked
Depositional Environment. See following table gives some examples.

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

This following query gives a list of the second level «Terrestrial»
Depositional Environment Types.
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

FaciesTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Facies Types. Table is referenced by the
`AnalysisUnits <#_Table:_AnalysisUnits>`__ table.

+--------------------------+----------------+------+-----+
| **FaciesTypes**                                 |
+--------------------------+----------------+------+-----+
| FaciesID                 | Long Integer   | PK   |     |
+--------------------------+----------------+------+-----+
| Facies                   | Text           |      |     |
+--------------------------+----------------+------+-----+

**FaciesID (Primary Key)** An arbitrary Facies identification number.

**Facies** Short Facies description.

 Table: Keywords
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Keywords referenced by the
`SampleKeywords <#_Table:_SampleKeywords>`__ table. The table provides a
means to identify samples sharing a common attribute. For example, the
keyword «modern sample» identifies modern surface samples in the
database. These samples include individual surface samples, as well as
core tops. Although not implemented, a «pre-European settlement» keyword
would be a means to identify samples just predating European settlement.

+-----------------------+----------------+------+-----+
| **Table: Keywords**   |
+-----------------------+----------------+------+-----+
| KeywordID             | Long Integer   | PK   |     |
+-----------------------+----------------+------+-----+
| Keyword               | Text           |      |     |
+-----------------------+----------------+------+-----+

**KeywordID (Primary Key)** An arbitrary Keyword identification number.

**Keyword** A keyword for identifying samples sharing a common
attribute.

Table: Lithology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores the lithologic descriptions of Collection Units.

+------------------------+----------------+------+--------------------+
| **Table: Lithology**   |
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

**LithologyID (Primary Key)** An arbitrary identification number for a
lithologic unit.

**CollectionUnitID (Foreign Key)** Collection Unit identification
number. Field links to the
`CollectionUnits <#_Table:_CollectionUnits>`__ table.

**DepthTop** Depth of the top of the lithologic unit in cm.

**DepthBottom** Depth of the bottom of the lithologic unit in cm.

**LowerBoundary** Description of the nature of the lower boundary of
the lithologic unit, e.g. «gradual, over ca. 10 cm».

**Description** Description of the lithologic unit. These can be quite
detailed, with Munsell color or Troels-Smith descriptions. Some
examples:

-  interbedded gray silt and peat

-  marly fine-detritus copropel

-  humified sedge and Sphagnum peat

-  sedge peat 5YR 5/4

-  gray sandy loam with mammoth and other animal bones

-  grey-green gyttja, oxidizing to gray-brown

-  Ag 3, Ga 1, medium gray, firm, elastic

-  nig3, strf0, elas2, sicc0; Th2 T12 Tb+

-  Ld°4, , Dg+, Dh+

   1. .. rubric:: Table: Projects
         :name: table-projects

This table stores a list of database projects that have supplied data to
Neotoma. These include the databases that were merged in the initial
development of Neotoma as well as other independent projects that
continue to assemble data for a particular region or data type. Some of
these projects have developed relational databases, whereas others have
compiled data in flat files. This table is referenced by the
DatabaseSubmissions table.

+-----------------------+----------------+------+------------+
| **Table: Projects**   |
+-----------------------+----------------+------+------------+
| ProjectID             | Long Integer   | PK   |            |
+-----------------------+----------------+------+------------+
| ProjectName           | Text           |      |            |
+-----------------------+----------------+------+------------+
| ContactID             | Long Integer   | FK   | Contacts   |
+-----------------------+----------------+------+------------+
| URL                   | Text           |      |            |
+-----------------------+----------------+------+------------+

**ProjectID (Primary Key)** An arbitrary Project identification number.

**ProjectName** Name of the Project, e.g. «Cooperative Holocene Mapping
Project», «North American Pollen Database», «FAUNMAP».

**ContactID (Foreign Key)** Contact person for the project. Field links
to the `Contacts <#_Table:_Contacts>`__ table.

**URL** Web site address for the project.

Table: RepositoryInstitutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A lookup table of institutions that are repositories for fossil
specimens. Table is referenced by the
`RepositorySpecimens <#_Table:_RepositorySpecimens>`__ table.

+-------------------------------------+----------------+------+-----+
| **Table: RepositoryInstitutions**                                 |
+-------------------------------------+----------------+------+-----+
| RepositoryID                        | Long Integer   | PK   |     |
+-------------------------------------+----------------+------+-----+
| Acronym                             | Text           |      |     |
+-------------------------------------+----------------+------+-----+
| Repository                          | Text           |      |     |
+-------------------------------------+----------------+------+-----+
| Notes                               | Memo           |      |     |
+-------------------------------------+----------------+------+-----+

**RepositoryID (PrimaryKey)** An arbitrary Repository identification
number. Repositories include museums, university departments, and
various governmental agencies.

**Acronym** A unique acronym for the repository. Many repositories have
well-established acronyms (e.g. AMNH = of Natural History); however,
there is no official list. Various acronyms have been used for some
institutions, and in some cases the same acronym has been used for
different institutions. Consequently, the database acronym may differ
from the acronym used in some publications. For example, «CMNH» has been
used for the Carnegie Museum of Natural History, the Cleveland Museum of
Natural History, and the Cincinnati Museum of Natural History. In
Neotoma, two of these institutions were assigned different acronyms,
ones that have been used for them in other publications: CM – Carnegie
Museum of Natural History, CLM – Cleveland Museum of Natural History.

**Repository** The full name of the repository.

**Notes** Free form notes or comments about the repository, especially
notes about name changes, closures, and specimen transfers. In some
cases, it is known that the specimens were transferred, but their
current disposition may be uncertain.

Table: RepositorySpecimens
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table lists the repositories in which fossil specimens have been
accessioned or reposited. The inventory in Neotoma is by Dataset, which
is the collection of specimens from a Collection Unit. Occasionally,
specimens from a single Collection Unit have been reposited at different
institutions, in which case multiple records for that Dataset occur in
the table.

+----------------------------------+----------------+----------+---------------------------+
| **Table: RepositorySpecimens**                                                           |
+----------------------------------+----------------+----------+---------------------------+
| DatasetID                        | Long Integer   | PK, FK   |  Datasets                 |
+----------------------------------+----------------+----------+---------------------------+
| RepositoryID                     | Long Integer   | PK, FK   |  RepositoryInstitutions   |
+----------------------------------+----------------+----------+---------------------------+
| Notes                            | Memo           |          |                           |
+----------------------------------+----------------+----------+---------------------------+

**DatasetID (Primary Key, Foreign Key)** Dataset identification number.
Field links to the `Datasets <#table-datasets>`__ table.

**RepositoryID (Primary Key, Foreign Key)** Repository identification
number. Field links to the
`RepositoryInstitutions <#_Table:_RepositoryInstitutions>`__ lookup
table.

**Notes** Free form notes or comments about the disposition of the
specimens.

SQL Example
`````````````````````````````

This query lists the repositories for specimens from the Kimmswick site.

.. code-block:: sql
   :linenos:

   SELECT Sites.SiteName, CollectionUnits.CollUnitName,
   RepositoryInstitutions.Repository

   FROM RepositoryInstitutions INNER JOIN (((Sites INNER JOIN
   CollectionUnits ON Sites.SiteID = CollectionUnits.SiteID) INNER JOIN
   Datasets ON CollectionUnits.CollectionUnitID =
   Datasets.CollectionUnitID) INNER JOIN RepositorySpecimens ON
   Datasets.DatasetID = RepositorySpecimens.DatasetID) ON
   RepositoryInstitutions.RepositoryID = RepositorySpecimens.RepositoryID

   WHERE (((Sites.SiteName)="Kimmswick"));

Result:

+----------------+--------------------+------------------+
| **SiteName**   | **CollUnitName**   | **Repository**   |
+----------------+--------------------+------------------+
| Kimmswick      | Locality           |                  |
+----------------+--------------------+------------------+
| Kimmswick      | Locality           |                  |
+----------------+--------------------+------------------+

Table: SpecimenDates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table enables queries for dated specimens of indivual taxa.
Although the MaterialDated field in the Geochronology table may list the
taxa dated, this protocol is not enforced, and the field is not linked
to the taxa table.

+-----------------------+---------+------+--------------------+
| **Table: Synonyms**                                         |
+-----------------------+---------+------+--------------------+
| SpecimenDateID        | int     | PK   |                    |
+-----------------------+---------+------+--------------------+
| GeochronID            | int     | FK   | Geochronology      |
+-----------------------+---------+------+--------------------+
| TaxonID               | int     | FK   | Taxa               |
+-----------------------+---------+------+--------------------+
| VariableElementID     | int     | FK   | VariableElements   |
+-----------------------+---------+------+--------------------+
| SampleID              | int     | FK   | Samples            |
+-----------------------+---------+------+--------------------+
| Notes                 | ntext   |      |                    |
+-----------------------+---------+------+--------------------+

**SpecimenDateID (Primary Key)** An arbitrary specicimen date
ID

**GeochronID (Foreign Key)** Geochronologic identification number.
Field links to the `Geochronology <#_Table:_Geochronology>`__ table.

**TaxonID (Foreign Key)** Accepted name in Neotoma. Field links to
`Taxa <#_Table:_Taxa>`__ table.

**VariableElementID (Foreign Key)** Variable Element identification
number. Field links to the
`VariableElements <#_Table:_VariableElements>`__ lookup table.

**SampleID (Primary Key, Foreign Key)** Sample ID number. Field links
to the `Samples <#_Table:_Samples>`__ table.

**Notes** Free form notes or comments about dated specimen.

Table: Tephrachronology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores tephrachronologic data. The table relates Analysis
Units with dated tephras in the `Tephras <#_Table:_Tephras>`__ table.
These are tephras with established ages that are used form a chronology.
The tephras are typically not directly dated at the Site of the Analysis
Unit, but have been dated at other sites. A directly dated tephra, e.g.
an argon-argon date, belongs in the
`Geochronology <#_Table:_Geochronology>`__ table.

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

**TephrachronID (Primary Key)** An arbitrary Tephrachronology
identification number.

**AnalysisUnitID (Foreign Key)** Analysis Unit identification number.
Field links to the ` <#_Table:_AnalysisUnits>`__ table. The tephra may
be contained within the AnalysisUnit, especially in excavations, or the
AnalysisUnit may be assigned specifically to the tephra, particulary
with cores.

**TephraID (Foreign Key)** Tephra identification number. Field links to
the `Tephras <#_Table:_Tephras>`__ table.

**Notes** Free form notes or comments about the tephra.

Table: Tephras
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tephras lookup table. This table stores recognized tephras with
established ages. Referenced by the
`Tephrachronology <#_Table:_Tephrachronology>`__ table.

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

Table: Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table lists Variables, which always consist of a Taxon and Units of
measurement. Variables can also have Elements, Contexts, and
Modifications. Thus, the same taxon with different measurement units
(e.g. present/absent, NISP, MNI) are different Variables.

+--------------------------+----------------+------+-------------------------+
| **Table: Variables**     |
+--------------------------+----------------+------+-------------------------+
| VariableID               | Long Integer   | PK   |                         |
+--------------------------+----------------+------+-------------------------+
| TaxonID                  | Long Integer   | FK   | Taxa                    |
+--------------------------+----------------+------+-------------------------+
| VariableElementID        | Long Integer   | FK   | VariableElements        |
+--------------------------+----------------+------+-------------------------+
| VaribleUnitsID           | Long Integer   | FK   | VariableUnits           |
+--------------------------+----------------+------+-------------------------+
| VariableContextID        | Long Integer   | FK   | VariableContexts        |
+--------------------------+----------------+------+-------------------------+
| VariableModificationID   | Long Integer   | FK   | VariableModifications   |
+--------------------------+----------------+------+-------------------------+

**VariableID (Primary Key)** An arbitrary Variable identification
number.

**TaxonID (Foreign Key)** Taxon identification number. Field links to
the ` <#_Table:_Taxa>`__ table.

**VariableElementID (Foreign Key)** Variable Element identification
number. Field links to the
`VariableElements <#_Table:_VariableElements>`__ lookup table.

**VariableUnitsID (Foreign Key)** Variable Units identification number.
Field links to the `VariableUnits <#_Table:_VariableUnits>`__ lookup
table.

**VariableContextID (Foreign Key)** Variable Context identification
number. Field links to the
`VariableContexts <#_Table:_VariableContexts>`__ lookup table.

**VarialbeModificationID (Foreign Key)** Variable Modification
identification number. Field links to the
`VariableModifications <#_Table:_VariableModifications>`__ lookup table.

SQL Example
`````````````````````````````

This query lists the Variables for «\ *Zea mays*\ » with elements and
measurement units.

.. code-block:: sql
   :linenos:

   SELECT Taxa.TaxonName, VariableElements.VariableElement,
   VariableUnits.VariableUnits

   FROM VariableUnits INNER JOIN (VariableElements INNER JOIN (Taxa INNER
   JOIN Variables ON Taxa.TaxonID = Variables.TaxonID) ON
   VariableElements.VariableElementID = Variables.VariableElementID) ON
   VariableUnits.VariableUnitsID = Variables.VariableUnitsID

   GROUP BY Taxa.TaxonName, VariableElements.VariableElement,
   VariableUnits.VariableUnits

   HAVING (((Taxa.TaxonName)="Zea mays"));

Result:

+-----------------+-----------------------+---------------------+
| **TaxonName**   | **VariableElement**   | **VariableUnits**   |
+-----------------+-----------------------+---------------------+
| Zea mays        | cob                   | NISP                |
+-----------------+-----------------------+---------------------+
| Zea mays        | glume                 | NISP                |
+-----------------+-----------------------+---------------------+
| Zea mays        | kernel                | NISP                |
+-----------------+-----------------------+---------------------+
| Zea mays        | pollen                | NISP                |
+-----------------+-----------------------+---------------------+
| Zea mays        | stalk fiber           | present/absent      |
+-----------------+-----------------------+---------------------+

SQL Example
`````````````````````````````

This query lists all sites with *Zea mays* pollen by designating the
VariableElement as «pollen».

.. code-block:: sql
   :linenos:

   SELECT Taxa.TaxonName, VariableElements.VariableElement, Sites.SiteName

   FROM VariableElements INNER JOIN (Sites INNER JOIN (CollectionUnits
   INNER JOIN (Datasets INNER JOIN (Samples INNER JOIN ((Taxa INNER JOIN
   Variables ON Taxa.TaxonID = Variables.TaxonID) INNER JOIN Data ON
   Variables.VariableID = Data.VariableID) ON Samples.SampleID =
   Data.SampleID) ON Datasets.DatasetID = Samples.DatasetID) ON
   CollectionUnits.CollectionUnitID = Datasets.CollectionUnitID) ON
   Sites.SiteID = CollectionUnits.SiteID) ON
   VariableElements.VariableElementID = Variables.VariableElementID

   GROUP BY Taxa.TaxonName, VariableElements.VariableElement,
   Sites.SiteName

   HAVING (((Taxa.TaxonName)="Zea mays") AND
   ((VariableElements.VariableElement)="pollen"));

The first few lines of the result:

+-----------------+-----------------------+-----------------+
| **TaxonName**   | **VariableElement**   | **SiteName**    |
+-----------------+-----------------------+-----------------+
| Zea mays        | pollen                | Almanac Pond    |
+-----------------+-----------------------+-----------------+
| Zea mays        | pollen                | Balikh          |
+-----------------+-----------------------+-----------------+
| Zea mays        | pollen                |                 |
+-----------------+-----------------------+-----------------+
| Zea mays        | pollen                |                 |
+-----------------+-----------------------+-----------------+
| Zea mays        | pollen                | Big John Pond   |
+-----------------+-----------------------+-----------------+
| Zea mays        | pollen                | Black Pond      |
+-----------------+-----------------------+-----------------+
| Zea mays        | pollen                |                 |
+-----------------+-----------------------+-----------------+
| Zea mays        | pollen                | Bouara          |
+-----------------+-----------------------+-----------------+
| Zea mays        | pollen                |                 |
+-----------------+-----------------------+-----------------+

The same result can be obtained by designating the DatasetType as
«pollen»:

.. code-block:: sql
   :linenos:

   SELECT Taxa.TaxonName, DatasetTypes.DatasetType, Sites.SiteName

   FROM DatasetTypes INNER JOIN ((Taxa INNER JOIN Variables ON Taxa.TaxonID
   = Variables.TaxonID) INNER JOIN (Sites INNER JOIN (((CollectionUnits
   INNER JOIN Datasets ON CollectionUnits.CollectionUnitID =
   Datasets.CollectionUnitID) INNER JOIN Samples ON Datasets.DatasetID =
   Samples.DatasetID) INNER JOIN Data ON Samples.SampleID = Data.SampleID)
   ON Sites.SiteID = CollectionUnits.SiteID) ON Variables.VariableID =
   Data.VariableID) ON DatasetTypes.DatasetTypeID = Datasets.DatasetTypeID

   GROUP BY Taxa.TaxonName, DatasetTypes.DatasetType, Sites.SiteName
   HAVING (((Taxa.TaxonName)="Zea mays") AND
   ((DatasetTypes.DatasetType)="pollen"));

SQL Example
`````````````````````````````

This example gives a list of all sites with *Bison bison antiquus* bones
with human butchering.

.. code-block:: sql
   :linenos:

   SELECT Taxa.TaxonName, VariableModifications.VariableModification,
   Sites.SiteName

   FROM Sites INNER JOIN (CollectionUnits INNER JOIN (Datasets INNER JOIN
   (Samples INNER JOIN ((VariableModifications INNER JOIN (Taxa INNER JOIN
   Variables ON Taxa.TaxonID = Variables.TaxonID) ON
   VariableModifications.VariableModificationID =
   Variables.VariableModificationID) INNER JOIN Data ON
   Variables.VariableID = Data.VariableID) ON Samples.SampleID =
   Data.SampleID) ON Datasets.DatasetID = Samples.DatasetID) ON
   CollectionUnits.CollectionUnitID = Datasets.CollectionUnitID) ON
   Sites.SiteID = CollectionUnits.SiteID

   GROUP BY Taxa.TaxonName, VariableModifications.VariableModification,
   Sites.SiteName

   HAVING (((Taxa.TaxonName)="Bison bison antiquus") AND
   ((VariableModifications.VariableModification)="human butchering"));

Result:

+------------------------+----------------------------+----------------------------+
| **TaxonName**          | **VariableModification**   | **SiteName**               |
+------------------------+----------------------------+----------------------------+
| Bison bison antiquus   | human butchering           | Folsom                     |
+------------------------+----------------------------+----------------------------+
| Bison bison antiquus   | human butchering           | [41LU1]                    |
+------------------------+----------------------------+----------------------------+
| Bison bison antiquus   | human butchering           | Murray Springs [EE:8:25]   |
+------------------------+----------------------------+----------------------------+
| Bison bison antiquus   | human butchering           | San Jon                    |
+------------------------+----------------------------+----------------------------+

Table: VariableContexts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Variable Contexts lookup table. Table is referenced by the
`Variables <#_Table:_Variables>`__ table.

+-------------------------------+----------------+------+-----+
| **Table: VariableContexts**                                 |
+-------------------------------+----------------+------+-----+
| VariableContextID             | Long Integer   | PK   |     |
+-------------------------------+----------------+------+-----+
| VariableContext               | Text           |      |     |
+-------------------------------+----------------+------+-----+

**VariableContextID (Primary Key)** An arbitrary Variable Context
identification number.

**VariableContext** Depositional context. Examples are:

-  **anachronic** – specimen older than the primary deposit, e.g. a
   Paleozoic spore in a Holocene deposit; may be redeposited from the
   catchment or may be derived from long distance, e.g. Tertiary pollen
   grains in Quaternary sediments with no local Tertiary source. A
   Pleistocene specimen in a Holocene archaeological deposit, possibly
   resulting from aboriginal fossil collecting, would also be
   anachronic.

-  **intrusive** – specimen generally younger younger than the primary
   deposit, e.g. a domestic pig in an otherwise Pleistocene deposit in .

-  **redeposited** – specimen older than the primary deposit and assumed
   to have been redeposited from a local source by natural causes.

-  **articulated** – articulated skeleton

-  **clump** – clump, esp. of pollen grains

   1. .. rubric:: Table: VariableElements
         :name: table-variableelements

Lookup table of Variable Elements. Table is referenced by the
`Variables <#_Table:_Variables>`__ table.

+-------------------------------+----------------+------+-----+
| **Table: VariableElements**                                 |
+-------------------------------+----------------+------+-----+
| VariableElementID             | Long Integer   | PK   |     |
+-------------------------------+----------------+------+-----+
| VariableElement               | Text           |      |     |
+-------------------------------+----------------+------+-----+

**VariableElementID (Primary Key)** An arbitrary Variable Element
identification number.

**VariableElement** The element, part, or organ of the taxon
identified. For plants, these include pollen, spores, and various
macrofossil organs, such as «seed», «twig», «cone», and «cone bract».
Thus, *Betula* pollen and *Betula* seeds are two different Variables.
For mammals, Elements include the bone or tooth identified, e.g.
«tibia». «tibia, distal, left», «M2, lower, left». Some more unusual
elements are *Neotoma* fecal pellets and *Erethizon dorsata* quills. If
no element is indicated for mammalian fauna, then the genric element
«bone/tooth» is assigned. Elements were not assigned in FAUNMAP, so all
Variables ingested from FAUNMAP were assigned the «bone/tooth» element.
Physical Variables may also have elements. For example, the
Loss-on-ignition Variables have «Loss-on-ignition» as a Taxon, and
temperature of analysis as an element, e.g. «500°C», «900°C». Charcoal
Variables have the size fragments as elements, e.g. «75-100 µm»,
«100-125 µm».

Table: VariableModifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Variable Modifications. Table is referenced by the
`Variables <#_Table:_Variables>`__ table.

+------------------------------------+----------------+------+-----+
| **Table: VariableModifications**                                 |
+------------------------------------+----------------+------+-----+
| VariableModificationID             | Long Integer   | PK   |     |
+------------------------------------+----------------+------+-----+
| VariableModification               | Text           |      |     |
+------------------------------------+----------------+------+-----+

**VariableModificationID (Primary Key)** An arbitrary Variable
Modification identification number.

**VariableModification** Modification to a specimen. Examples of
modifications to bones include «carnivore gnawed», «rodent gnawed»,
«burned», «human butchering». Modifications to pollen grains include
various preservation states, e.g. «1/2 grains», «degraded», «corroded»,
«broken». Most Variables do not have a modification assigned.

Table: VariableUnits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Variable Units. Table is referenced by the
`Variables <#_Table:_Variables>`__ table.

+----------------------------+----------------+------+-----+
| **Table: VariableUnits**   |                             |
+----------------------------+----------------+------+-----+
| VariableUnitsID            | Long Integer   | PK   |     |
+----------------------------+----------------+------+-----+
| VariableUnit               | Text           |      |     |
+----------------------------+----------------+------+-----+

**VariableUnitsID (Primary Key)** An arbitrary Variable Units
identification number.

**VariableUnit** The units of measurement. For fauna, these are
«present/absent», «NISP» (Number of Individual Specimens), and «MNI»
(Minimum Number of Individals). For pollen, these are «NISP» (pollen
counts) and «percent». Units for plant macrofossils include
«present/abesnt» and «NISP», as well as a number of quantitative
concentration measurements and semi-quantitative abundance measurements
such as «1-5 scale». Examples of charcoal measurement units are
«fragments/ml» and «µm^2/ml».
