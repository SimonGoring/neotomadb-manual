Site Related Tables
----------------------------------------------------

SiteImages
~~~~~~~~~~~~~~~~~~~

This table stores hyperlinks to jpeg images of sites.

+-------------------------+----------------+------+-------------------+
| **SiteImages**                                                      |
+-------------------------+----------------+------+-------------------+
| SiteImageID             | Long Integer   | PK   |                   |
+-------------------------+----------------+------+-------------------+
| SiteID                  | Long Integer   | FK   | :ref:`Sites`      |
+-------------------------+----------------+------+-------------------+
| ContactID               | Long Integer   | FK   | :ref:`Contacts`   |
+-------------------------+----------------+------+-------------------+
| Caption                 | Memo           |      |                   |
+-------------------------+----------------+------+-------------------+
| Credit                  | Text           |      |                   |
+-------------------------+----------------+------+-------------------+
| Date                    | Date/Time      |      |                   |
+-------------------------+----------------+------+-------------------+
| SiteImage               | Hyperlink      |      |                   |
+-------------------------+----------------+------+-------------------+

**SiteImageID (Primary Key)** An arbitrary Site Image identification
number.

**SiteID (Foreign Key)** Site identification number. Field links to the
:ref:`Sites` table.

**ContactID (Foreign Key)** Contact identification number for image
attribution from the :ref:`Contacts` table.

**Caption** Caption for the image.

**Credit** Credit for the image. If null, the credit is formed from the
ContactID.

**Date** Date of photograph or image.

**SiteImage** Hyperlink to a URL for the image.

Sites
~~~~~~~~~~~~~~~~~~~

The Sites table stores information about sites or localities, including
name, geographic coordinates, and description. Sites generally have an
areal extent and can be circumscribed by a latitude-longitude box.
However, site data ingested from legacy databases have included only
point locations. The lat-long box can be used either to circumscribe the
areal extent of a site or to provide purposeful imprecision to the site
location. Site location may be imprecise because of the original
description was vague, e.g. «a gravel bar 5 miles east of town», or
because the investigators, land owner, or land management agency may not
want the exact location made public, perhaps to prevent looting and
vandalism. In the first case, the lat-long box can be made sufficiently
large to encompass the true location and in the second case to prevent
exact location.

+--------------------+----------------+------+-----+
| **Sites**                                        |
+--------------------+----------------+------+-----+
| SiteID             | Long Integer   | PK   |     |
+--------------------+----------------+------+-----+
| SiteName           | Text           |      |     |
+--------------------+----------------+------+-----+
| LongitudeEast      | Double         |      |     |
+--------------------+----------------+------+-----+
| LatitudeNorth      | Double         |      |     |
+--------------------+----------------+------+-----+
| LongitudeWest      | Double         |      |     |
+--------------------+----------------+------+-----+
| LatitudeSouth      | Double         |      |     |
+--------------------+----------------+------+-----+
| Altitude           | Long Integer   |      |     |
+--------------------+----------------+------+-----+
| Area               | Double         |      |     |
+--------------------+----------------+------+-----+
| SiteDescription    | Memo           |      |     |
+--------------------+----------------+------+-----+
| Notes              | Memo           |      |     |
+--------------------+----------------+------+-----+

**SiteID (Primary Key)** An arbitrary Site identification number.

**SiteName** Name of the site. Alternative names, including
archaeological site numbers, are placed in square brackets, for example:

-  New #4 [Lloyd's Rock Hole]

-  Modoc Rock Shelter [11RA501]

    A search of the SiteName field for any of the alternative names or
    for the archaeological site number will find the site. Some
    archaeological sites are known only by their site number.

    Modifiers to site names are placed in parentheses. Authors are added
    for generic sites names, especially for surface samples, that are
    duplicated in the database, for example:

-  Site 1 (Heusser 1978)

-  Site 1 (Delcourt et al. 1983)

-  Site 1 (Elliot-Fisk et al. 1982)

-  Site 1 (Whitehead and Jackson 1990)

    For actual site names duplicated in the database, the name is
    followed by the 2-letter country code and state or province, for
    example:

-  (US:)

-  (CA:)

-  (US:)

-  (US:)

**LongitudeEast** East bounding longitude for a site.

**LatitudeNorth** North bounding latitude for a site.

**LongitudeWest**: West bounding longitude for a site.

**LatitudeSouth** South bounding latitude for a site.

**Altitude** Altitude of a site in meters.

**Area** Area of a site in hectares.

**SiteDescription** Free form description of a site, including such
information as physiography and vegetation around the site.

**Notes** Free form notes or comments about the site.

SiteGeoPolitical
~~~~~~~~~~~~~~~~~~~

This table lists the GeoPolitical units in which sites occur.

+-------------------------------+----------------+------+---------------------+
| **SiteGeoPolitical**                                                        |
+-------------------------------+----------------+------+---------------------+
| SiteGeoPoliticalID            | Long Integer   | PK   |                     |
+-------------------------------+----------------+------+---------------------+
| SiteID                        | Long Integer   | FK   | :ref:`Sites`        |
+-------------------------------+----------------+------+---------------------+
| GeoPoliticalID                | Long Integer   | FK   | :ref:`GeoPoliticalUnits` |
+-------------------------------+----------------+------+---------------------+

**SiteGeoPoliticalID (Primary Key)** An arbitrary Site GeoPolitical
identification number.

**SiteID (Foreign Key)** Site identification number. Field links to the
`Sites <#_Table:_Sites_1>`__ table.

**GeoPoliticalID (Foreign Key)** GeoPolitical identification number.
Field links to the `GeoPoliticalUnits <#_Table:_GeoPoliticalUnits>`__
lookup table.

SQL Example
`````````````````````````````

The query in Example 2.8.1 lists the GeoPoliticalUnits for «», one unit
to a record. This query lists them in a single record.

.. code-block:: sql
   :linenos:

   SELECT Sites.SiteName, GeoPoliticalUnits.GeoPoliticalName,
   GeoPoliticalUnits\_1.GeoPoliticalName,
   GeoPoliticalUnits\_2.GeoPoliticalName

   FROM GeoPoliticalUnits AS GeoPoliticalUnits\_2 INNER JOIN
   (SiteGeoPolitical AS SiteGeoPolitical\_2 INNER JOIN ((SiteGeoPolitical
   AS SiteGeoPolitical\_1 INNER JOIN (GeoPoliticalUnits INNER JOIN (Sites
   INNER JOIN SiteGeoPolitical ON Sites.SiteID = SiteGeoPolitical.SiteID)
   ON GeoPoliticalUnits.GeoPoliticalID = SiteGeoPolitical.GeoPoliticalID)
   ON SiteGeoPolitical\_1.SiteID = Sites.SiteID) INNER JOIN
   GeoPoliticalUnits AS GeoPoliticalUnits\_1 ON
   SiteGeoPolitical\_1.GeoPoliticalID =
   GeoPoliticalUnits\_1.GeoPoliticalID) ON SiteGeoPolitical\_2.SiteID =
   Sites.SiteID) ON GeoPoliticalUnits\_2.GeoPoliticalID =
   SiteGeoPolitical\_2.GeoPoliticalID

   WHERE (((Sites.SiteName)="") AND ((GeoPoliticalUnits.Rank)=1) AND
   ((GeoPoliticalUnits\_1.Rank)=2) AND ((GeoPoliticalUnits\_2.Rank)=3));

Result:

+----------------+------------------------------------------+---------------------------------------------+---------------------------------------------+
| **SiteName**   | **GeoPoliticalUnits.GeoPoliticalName**   | **GeoPoliticalUnits\_1.GeoPoliticalName**   | **GeoPoliticalUnits\_2.GeoPoliticalName**   |
+----------------+------------------------------------------+---------------------------------------------+---------------------------------------------+
|                |                                          |                                             | Hennepin                                    |
+----------------+------------------------------------------+---------------------------------------------+---------------------------------------------+

 SQL Example
`````````````````````````````

The problem with the query above is that if a site has less than three
GeoPolitical Names, the result will return empty. For example, «» has no
GeoPoliticalUnit with Rank = 3, and will return an empty result with the
above query. A solution to this problem is to create and save separate
queries for the three ranks:

Query GeoPol1:

.. code-block:: sql
   :linenos:

   SELECT Sites.SiteName, GeoPoliticalUnits.GeoPoliticalName

   FROM Sites INNER JOIN (GeoPoliticalUnits INNER JOIN SiteGeoPolitical ON
   GeoPoliticalUnits.GeoPoliticalID = SiteGeoPolitical.GeoPoliticalID) ON
   Sites.SiteID = SiteGeoPolitical.SiteID

   WHERE (((GeoPoliticalUnits.Rank)=1));

Query GeoPol2:

.. code-block:: sql
   :linenos:

   SELECT Sites.SiteName, GeoPoliticalUnits.GeoPoliticalName

   FROM Sites INNER JOIN (GeoPoliticalUnits INNER JOIN SiteGeoPolitical ON
   GeoPoliticalUnits.GeoPoliticalID = SiteGeoPolitical.GeoPoliticalID) ON
   Sites.SiteID = SiteGeoPolitical.SiteID

   WHERE (((GeoPoliticalUnits.Rank)=2));

Query GeoPol3:

.. code-block:: sql
   :linenos:

   SELECT Sites.SiteName, GeoPoliticalUnits.GeoPoliticalName

   FROM Sites INNER JOIN (GeoPoliticalUnits INNER JOIN SiteGeoPolitical ON
   GeoPoliticalUnits.GeoPoliticalID = SiteGeoPolitical.GeoPoliticalID) ON
   Sites.SiteID = SiteGeoPolitical.SiteID

   WHERE (((GeoPoliticalUnits.Rank)=3));

These three queries can now be combined in a new query with left joins,
and the GeoPolitical Names will be returned even if there are less than
three.

.. code-block:: sql
   :linenos:

   SELECT GeoPol1.SiteName, GeoPol1.GeoPoliticalName,
   GeoPol2.GeoPoliticalName, GeoPol3.GeoPoliticalName

   FROM (GeoPol1 LEFT JOIN GeoPol2 ON GeoPol1.SiteName = GeoPol2.SiteName)
   LEFT JOIN GeoPol3 ON GeoPol2.SiteName = GeoPol3.SiteName

   WHERE (((GeoPol1.SiteName)="Lofty "));

Result:

+----------------+--------------------------------+--------------------------------+--------------------------------+
| **SiteName**   | **GeoPol1.GeoPoliticalName**   | **GeoPol2.GeoPoliticalName**   | **GeoPol3.GeoPoliticalName**   |
+----------------+--------------------------------+--------------------------------+--------------------------------+
| Lofty          |                                |                                |                                |
+----------------+--------------------------------+--------------------------------+--------------------------------+

SQL Example
`````````````````````````````

The saved queries from the example above can be linked with tables in a
more complicated query. This query lists all the pollen sites in the
adjacent states of «» in the «» and «» in «».

.. code-block:: sql
   :linenos:

   SELECT GeoPol1.SiteName, GeoPol1.GeoPoliticalName,
   GeoPol2.GeoPoliticalName, GeoPol3.GeoPoliticalName,
   DatasetTypes.DatasetType

   FROM (DatasetTypes INNER JOIN ((Sites INNER JOIN CollectionUnits ON
   Sites.SiteID = CollectionUnits.SiteID) INNER JOIN Datasets ON
   CollectionUnits.CollectionUnitID = Datasets.CollectionUnitID) ON
   DatasetTypes.DatasetTypeID = Datasets.DatasetTypeID) INNER JOIN
   ((GeoPol1 LEFT JOIN GeoPol2 ON GeoPol1.SiteName = GeoPol2.SiteName) LEFT
   JOIN GeoPol3 ON GeoPol2.SiteName = GeoPol3.SiteName) ON Sites.SiteName =
   GeoPol1.SiteName

   GROUP BY GeoPol1.SiteName, GeoPol1.GeoPoliticalName,
   GeoPol2.GeoPoliticalName, GeoPol3.GeoPoliticalName,
   DatasetTypes.DatasetType

   HAVING (((GeoPol1.GeoPoliticalName)="" Or (GeoPol1.GeoPoliticalName)="")
   AND ((GeoPol2.GeoPoliticalName)="" Or (GeoPol2.GeoPoliticalName)="") AND
   ((DatasetTypes.DatasetType)="pollen"))

   ORDER BY GeoPol1.GeoPoliticalName, GeoPol2.GeoPoliticalName,
   GeoPol3.GeoPoliticalName, DatasetTypes.DatasetType;

Result:

+------------------+--------------------------------+--------------------------------+--------------------------------+-------------------+
| **SiteName**     | **GeoPol1.GeoPoliticalName**   | **GeoPol2.GeoPoliticalName**   | **GeoPol3.GeoPoliticalName**   | **DatasetType**   |
+------------------+--------------------------------+--------------------------------+--------------------------------+-------------------+
| Sierra Bacha     |                                |                                |                                | pollen            |
+------------------+--------------------------------+--------------------------------+--------------------------------+-------------------+
| Sierra Bacha 3   |                                |                                |                                | pollen            |
+------------------+--------------------------------+--------------------------------+--------------------------------+-------------------+
|                  |                                |                                | Apache                         | pollen            |
+------------------+--------------------------------+--------------------------------+--------------------------------+-------------------+
|                  |                                |                                | Coconino                       | pollen            |
+------------------+--------------------------------+--------------------------------+--------------------------------+-------------------+
|                  |                                |                                | Coconino                       | pollen            |
+------------------+--------------------------------+--------------------------------+--------------------------------+-------------------+
|                  |                                |                                | Coconino                       | pollen            |
+------------------+--------------------------------+--------------------------------+--------------------------------+-------------------+
| Montezuma Well   |                                |                                | Yavapai                        | pollen            |
+------------------+--------------------------------+--------------------------------+--------------------------------+-------------------+

GeoPoliticalUnits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of GeoPoliticalUnits. Table is referenced by the
`SiteGeoPolitical <#_Table:_SiteGeoPolitical>`__ table. These are
countries and various subdivisions. Countries and subdivisions were
acquired from the U.S. Central Intelligence Agency World Factbook [8]_
and the ISO 3166-1 and ISO 3166-2 databases [9]_.

Each GeoPolitical Unit has a rank. GeoPolitical Units with Rank 1 are
generally countries. There are a few exceptions, including Antarctica
and island territories, such as , which although a Danish territory, is
geographically separate and distinct. Rank 2 units are generally
secondary political divisions with various designations: e.g. states in
the , provinces in , and regions in . For some countries, the secondary
divisions are not political but rather distinct geographic entities,
such as islands. The secondary divisions of some island nations include
either groups of islands or sections of more highly populated islands;
however, the actual island on which a site is located is more important
information. Some countries also have Rank 3 units, e.g. counties in the
and metropolitan departments in . In addition to purely political units,
various other administrative regions and geographic entities can be
contained in this table. Examples of administrative regions are National
Parks and Forests. It might be quite useful, for example, to have a
record of all the sites in . These additional units are Rank 4, and they
can be added to the database as warranted.

+--------------------------------+----------------+------+------------------------------------+
| **Table: GeoPoliticalUnits**                                                                |
+--------------------------------+----------------+------+------------------------------------+
| GeoPoliticalID                 | Long Integer   | PK   |                                    |
+--------------------------------+----------------+------+------------------------------------+
| GeoPoliticalName               | Text           |      |                                    |
+--------------------------------+----------------+------+------------------------------------+
| GeoPoliticalUnit               | Text           |      |                                    |
+--------------------------------+----------------+------+------------------------------------+
| Rank                           | Long Integer   |      |                                    |
+--------------------------------+----------------+------+------------------------------------+
| HigherGeoPoliticalID           | Long Integer   | FK   | GeoPoliticalUnits:GeoPoliticalID   |
+--------------------------------+----------------+------+------------------------------------+

**GeoPoliticalID (Primary Key)** An arbitrary GeoPolitical
identification number.

**GeoPoliticalName** Name of the GeoPolitical Unit, e.g. , .

**GeoPoliticalUnit** The name of the unit, e.g. country, state, county,
island, governorate, oblast.

**Rank** The rank of the unit.

**HigherGeoPoliticalID** The GeoPoliticalUnit with higher rank, e.g.
the country in which a state lies.

SQL Example
`````````````````````````````

The following query lists all the political subdivisions of in the .

.. code-block:: sql
   :linenos:

   SELECT GeoPoliticalUnits\_2.Rank, GeoPoliticalUnits\_2.GeoPoliticalUnit,
   GeoPoliticalUnits\_2.GeoPoliticalName

   FROM (GeoPoliticalUnits AS GeoPoliticalUnits\_2 RIGHT JOIN
   (GeoPoliticalUnits AS GeoPoliticalUnits\_1 RIGHT JOIN GeoPoliticalUnits
   ON GeoPoliticalUnits\_1.HigherGeoPoliticalID =
   GeoPoliticalUnits.GeoPoliticalID) ON
   GeoPoliticalUnits\_2.HigherGeoPoliticalID =
   GeoPoliticalUnits\_1.GeoPoliticalID) LEFT JOIN GeoPoliticalUnits AS
   GeoPoliticalUnits\_3 ON GeoPoliticalUnits\_2.GeoPoliticalID =
   GeoPoliticalUnits\_3.HigherGeoPoliticalID

   WHERE (((GeoPoliticalUnits.GeoPoliticalName)="") AND
   ((GeoPoliticalUnits\_1.GeoPoliticalName)=""));

The first 17 records of the result:

+------------+------------------------+------------------------+
| **Rank**   | **GeoPoliticalUnit**   | **GeoPoliticalName**   |
+------------+------------------------+------------------------+
| 3          | district               | Omagh                  |
+------------+------------------------+------------------------+
| 3          | district               | North Down             |
+------------+------------------------+------------------------+
| 3          | district               | Strabane               |
+------------+------------------------+------------------------+
| 3          | district               | Newry and Mourne       |
+------------+------------------------+------------------------+
| 3          | district               | Moyle                  |
+------------+------------------------+------------------------+
| 3          | district               | Magherafelt            |
+------------+------------------------+------------------------+
| 3          | district               |                        |
+------------+------------------------+------------------------+
| 4          | historical county      |                        |
+------------+------------------------+------------------------+
| 4          | historical county      |                        |
+------------+------------------------+------------------------+
| 4          | historical county      |                        |
+------------+------------------------+------------------------+
| 4          | historical county      |                        |
+------------+------------------------+------------------------+
| 4          | historical county      |                        |
+------------+------------------------+------------------------+
| 3          | district               | Banbridge              |
+------------+------------------------+------------------------+
| 3          | district               | Lisburn                |
+------------+------------------------+------------------------+
| 4          | historical county      |                        |
+------------+------------------------+------------------------+
| 3          | district               | Ballymoney             |
+------------+------------------------+------------------------+
| 3          | district               | Carrickfergus          |
+------------+------------------------+------------------------+

