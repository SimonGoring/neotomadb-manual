Neotoma Tables
=============================

The Neotoma Database contains more than 100 tables and as new proxy types get added, or new metadata is stored, the number of tables may increase or decrease.  As a result, this manual should not be considered the final authority, but it should provide nearly complete coverage of the database and its structure.  In particular, do our best to divide tables into logical groupings: Chronology & Age related tables, Dataset related tables, Site related tables, Contact tables, Sample tables and so on.

Site Related Tables
---------------------------

:ref:`SiteImages`, :ref:`Sites`, :ref:`SiteGeoPolitical`, :ref:`GeoPoliticalUnits`


Dataset & Collection Related Tables
-----------------------------------

Tables related to complete datasets, or collections of samples.  These include Collection information, but only refer to sites, since, as described in the Design Concepts, datasets are conceptually nested within sites, even if a site contains only a single dataset.

  :ref:`AggregateDatasets`, :ref:`AggregateOrderTypes`, :ref:`CollectionTypes`, :ref:`CollectionUnits`, :ref:`DatasetPublications`, :ref:`Datasets`, :ref:`DatasetSubmissions`, :ref:`DatasetSubmissionTypes`, :ref:`DatasetTypes`, :ref:`DatasetPIs`, :ref:`DepEnvtTypes`, :ref:`Lithology`, :ref:`Projects`.

Chronology & Age Related Tables
-----------------------------

  :ref:`AgeTypes`, :ref:`AggregateChronologies`, :ref:`ChronControls`, :ref:`ChronControlTypes`, :ref:`Chronologies`, :ref:`AggregateSampleAges`, :ref:`Geochronology`, :ref:`GeochronPublications`, :ref:`GeochronTypes`, :ref:`RelativeAgePublications`, :ref:`RelativeAges`, :ref:`RadiocarbonCalibration`, :ref:`RelativeAgeScales`, :ref:`RelativeAgeUnits`, :ref:`RelativeChronology`, :ref:`Tephrachronology`, :ref:`Tephras`.

Sample Related Tables
---------------------------

Taxonomy Related Tables
---------------------------

Tables related to taxonomic information, phylogenetic information and ecological classifications.  These tables also include hierarchy based on morphological or phylogenetic relationships.

  :ref:`EcolGroups`, :ref:`EcolGroupTypes`, :ref:`EcolSetTypes`, :ref:`Synonyms`, :ref:`SynonymTypes`, :ref:`Taxa`, :ref:`TaxaGroupTypes`, :ref:`Variables`, :ref:`VariableContexts`, :ref:`VariableElements`, :ref:`VariableModifications`, :ref:`VariableUnits`.


Individual Related Tables
---------------------------

Publication Related Tables
---------------------------

