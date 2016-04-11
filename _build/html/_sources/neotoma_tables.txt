Neotoma Tables
=============================

The Neotoma Database contains more than 100 tables and as new proxy types get added, or new metadata is stored, the number of tables may increase or decrease.  As a result, this manual should not be considered the final authority, but it should provide nearly complete coverage of the database and its structure.  In particular, we divide tables into logical groupings, Chronology & Chronology related tables, Site related tables, Contact tables, Sample tables and so on.

Chronology & Age Related Tables
-----------------------------

AgeTypes, AggregateChronologies, ChronControls, Chronologies, AggregateSampleAges, Geochronology, GeochronPublications, GeochronTypes, RelativeAgePublications, RelativeAges, RadiocarbonCalibration, RelativeAgeScales, RelativeAgeUnits, RelativeChronology


Dataset & Collection Related Tables
-----------------------------------

AggregateDatasets

Sample Related Tables
---------------------------

Site Related Tables
---------------------------

Taxonomy Related Tables
---------------------------

Tables related to taxonomic information, phylogenetic information and ecological classifications.  These tables also include hierarchy based on morphological or phylogenetic relationships.

  :ref:`EcolGroups`, :ref:`EcolGroupTypes`, :ref:`EcolSetTypes`, :ref:`Synonyms`, :ref:`SynonymTypes`, :ref:`Taxa`, :ref:`TaxaGroupTypes`, :ref:`Variables`, :ref:`VariableContexts`, :ref:`VariableElements`, :ref:`VariableModifications`, :ref:`VariableUnits`.


Individual Related Tables
---------------------------

Publication Related Tables
---------------------------






RepositoryInstitutions
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

RepositorySpecimens
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

SpecimenDates
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

