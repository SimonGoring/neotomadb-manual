Publication Related Tables
-------------------------------------------

.. _PublicationAuthors:

PublicationAuthors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table lists authors as their names are given in publications. Only the initials are stored for authors’ given names. The ContactID links to the author’s full name and contact data in the :ref:`Contacts` table. Thus, for a bibliographic entry, Charles Robert Darwin is listed as C. R. Darwin, or as C. Darwin if the publication did not include his middle name. Book editors are also stored in this table if the entire book is cited. However, if a book chapter or section is cited, authors are stored in this table, but the book editors are stored in the :ref:`PublicationEditors` table. Thus, for the following reference, G. C. Frison is stored in the :ref:`PublicationAuthors` table.

    Frison, G. C., editor. 1996. The Mill Iron site. University of New Mexico Press, Albuquerque, New Mexico, USA.

Whereas for the following publication, L. S. Cummings is listed in the PublicationAuthors table, and G. C. Frison is listed in the :ref:`PublicationEditors` table.

    Cummings, L. S. 1996. Paleoenvironmental interpretations for the Mill Iron site: stratigraphic pollen and phyrolith analysis. Pages 177-193 in G. C. Frison, editor. The Mill Iron site. University of New Mexico Press, Albuquerque, New Mexico, USA.

+---------------------------------+----------------+------+----------------+
| **Table: PublicationAuthors**                                            |
+---------------------------------+----------------+------+----------------+
| AuthorID                        | Long Integer   | PK   |                |
+---------------------------------+----------------+------+----------------+
| PublicationID                   | Long Integer   | FK   | Publications   |
+---------------------------------+----------------+------+----------------+
| AuthorOrder                     | Long Integer   |      |                |
+---------------------------------+----------------+------+----------------+
| FamilyName                      | Text           |      |                |
+---------------------------------+----------------+------+----------------+
| Initials                        | Text           |      |                |
+---------------------------------+----------------+------+----------------+
| Suffix                          | Text           |      |                |
+---------------------------------+----------------+------+----------------+
| ContactID                       | Long Integer   | FK   | Contacts       |
+---------------------------------+----------------+------+----------------+

**AuthorID (Primary Key)** 
  An arbitrary Author identification number.

**PublicationID (Foreign Key)** 
  Publication identification number. Field links to the :ref:`Publications` table.

**AuthorOrder** 
  Ordinal number for the position in which the author's name appears in the publication’s author list.

**FamilyName** 
  Family name of author

**Initials**
  Initials of author’s given names

**Suffix**
  Authors suffix (e.g. «Jr.»)

**ContactID (Foreign Key)**
  Contact identification number. Field links to the :ref:`Contacts` table.

SQL Example
`````````````````````````````

The following query lists the PublicationID and complete author names for the publication of . Note that because is a name likely to be duplicated in the database, the name is given with a wild card ending and the GeoPolitical tables are linked in. The citation for this publication is:

.. code-block:: sql
   :linenos:

   SELECT PublicationAuthors.PublicationID, Contacts.ContactName
   
   FROM GeoPoliticalUnits INNER JOIN ((Contacts INNER JOIN ((Publications
   INNER JOIN (((Sites INNER JOIN CollectionUnits ON Sites.SiteID =
   CollectionUnits.SiteID) INNER JOIN Datasets ON
   CollectionUnits.CollectionUnitID = Datasets.CollectionUnitID) INNER JOIN
   DatasetPublications ON Datasets.DatasetID =
   DatasetPublications.DatasetID) ON Publications.PublicationID =
   DatasetPublications.PublicationID) INNER JOIN PublicationAuthors ON
   Publications.PublicationID = PublicationAuthors.PublicationID) ON
   Contacts.ContactID = PublicationAuthors.ContactID) INNER JOIN
   SiteGeoPolitical ON Sites.SiteID = SiteGeoPolitical.SiteID) ON
   GeoPoliticalUnits.GeoPoliticalID = SiteGeoPolitical.GeoPoliticalID

   WHERE (((Sites.SiteName) Like " \*") AND
   ((GeoPoliticalUnits.GeoPoliticalName)=""));

Result:

+---------------------+------------------------+
| **PublicationID**   | **ContactName**        |
+---------------------+------------------------+
| 202                 | Baker, Richard G.      |
+---------------------+------------------------+
| 202                 | Maher, Louis J., Jr.   |
+---------------------+------------------------+
| 202                 | L.                     |
+---------------------+------------------------+
| 202                 | Chumbley, Craig A.     |
+---------------------+------------------------+

The citation for PublicationID is:

Baker, R. G., L. J. Maher, Jr., C. A. Chumbley, and K. L. Van Zant. 1992. Patterns of Holocene environmental change in the midwestern United States. Quaternary Research 37:379-389.

.. _PublicationEditors:

PublicationEditors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores the editors of publications for which chapters or sections are the primary bibliographic entries. Chapter authors are stored in the PublicatonAuthors table, where they are linked to the :ref:`Contacts` table. However, publication editors are not cross-referenced in the :ref:`Contacts` table, because chapter authors are the principal citation.

+---------------------------------+----------------+------+----------------+
| **Table: PublicationEditors**                                            |
+---------------------------------+----------------+------+----------------+
| EditorID                        | Long Integer   | PK   |                |
+---------------------------------+----------------+------+----------------+
| PublicationID                   | Long Integer   | FK   | Publications   |
+---------------------------------+----------------+------+----------------+
| EditorOrder                     | Long Integer   |      |                |
+---------------------------------+----------------+------+----------------+
| FamilyName                      | Text           |      |                |
+---------------------------------+----------------+------+----------------+
| Initials                        | Text           |      |                |
+---------------------------------+----------------+------+----------------+
| Suffix                          | Text           |      |                |
+---------------------------------+----------------+------+----------------+

**EditorID (Primary Key)**
  An arbitrary Editor identification number.

**PublicationID (Foreign Key)**
  Publication identification number. Field links to the :ref:`Publications` table.

**EditorOrder**
  Ordinal number for the position in which the editor’s name appears in the publication’s author list.

**FamilyName**
  Family name of editor

**Initials**
  Initials of editor’s given names

**Suffix**
	Authors suffix (e.g. «Jr.»)

.. _Publications:

Publications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores publication or bibliographic data. The table is designed with fields for bibliographic data so that bibliographies can be formatted in different styles and potentially exported to bibliographic software such EndNote®. In the constituent databases that were originally merged into Neotoma, bibliographic entries were not parsed into separate fields, but rather were stored as free-form text.

Because complete parsing of these thousands of legacy bibliographic entries into individual fields would have been prohibitively time consuming, the existing bibliographic data were ingested “as is” with a PubTypeID = Other. However, for legacy publications, the year of publication was added to the Year field, and authors were parsed into the :ref:`PublicationAuthors` table and added to the :ref:`Contacts` table. In addition, some global changes were made. For example, «Pp.» was changed to «Pages», «Ed.» to «Editor», and «Eds.» to «Editors». Also for FAUNMAP entries, abbreviated journal names were changed to fully spelled out names.

The merged databases used different bibliographic styles, and data entry personnel working on the same database sometimes followed different conventions. Consequently, the current bibliographic entries are not stylistically uniform. Eventually, the legacy bibliographic data will be parsed into separate fields.

The Publications table has fields to accommodate a number of different types of publications. Some fields contain different kinds of data for different kinds of publications. For example, the BookTitle field stores the titles of books, but stores the journal name for journal articles. The Publisher field stores the name of the publisher for books, but the name of the university for theses and dissertations.

Authors are stored in the :ref:`PublicationAuthors` table. Editors are also stored in the :ref:`PublicationAuthors` table if the entire publication is cited. The :ref:`PublicationAuthors` table has a ContactID field, which links to the :ref:`Contacts` table, where full names and contact information is stored for authors and editors. The PubTypeID «Authored Book» or «Edited Book» indicates whether the PublicationAuathors records are authors or editors. If a book chapter or section is the primary bibliographic entry, then the book editors are stored in the :ref:`PublicationEditors` table, which does not have a ContactID field.

+---------------------------+----------------+------+--------------------+
| **Table: Publications**                                                |
+---------------------------+----------------+------+--------------------+
| PublicationID             | Long Integer   | PK   | Publications       |
+---------------------------+----------------+------+--------------------+
| PubTypeID                 | Long Integer   | FK   | PublicationTypes   |
+---------------------------+----------------+------+--------------------+
| Year                      | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| Citation                  | Memo           |      |                    |
+---------------------------+----------------+------+--------------------+
| ArticleTitle              | Memo           |      |                    |
+---------------------------+----------------+------+--------------------+
| BookTitle                 | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| Volume                    | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| Issue                     | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| Pages                     | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| CitationNumber            | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| DOI                       | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| NumVolumes                | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| Edition                   | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| VolumeTitle               | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| SeriesTitle               | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| SeriesVolume              | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| Publisher                 | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| City                      | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| State                     | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| Country                   | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| OriginalLanguage          | Text           |      |                    |
+---------------------------+----------------+------+--------------------+
| Notes                     | Memo           |      |                    |
+---------------------------+----------------+------+--------------------+

**PublicationID (Primary Key)**
  An arbitrary Publication identification number.

**PubTypeID (Foreign Key)**
  Publication type. Field links to the :ref:`PublicationTypes` lookup table.

**Year**
  Year of publication.

**Citation**
  The complete citation in a standard style. For Legacy citations inherited from other databases, this field holds the citation as ingested from the other databases.

**ArticleTitle**
  The title of a journal or book chapter article.

**BookTitle**
  The title of a book or journal

**Volume**
  The volume number of a journal or the volume number of a book in a set. A set of books is comprised of a fixed number of volumes and normally have ISBN numbers, not ISSN numbers. Book sets are often published simultaneously, but not necessarily. For instance, many floras, such as *The* *Flora of North America north of* and *Flora Europaea*, consist of a set number of volumes planned in advance but published over a period of years.

**Issue**
  Journal issue number, normally included only if issues are independently paginated.

**Pages**
  Page numbers for journal or book chapter articles, or the number of pages in theses, dissertations, and reports.

**CitationNumber**
  A citation or article number used in lieu of page numbers for digital or online publications, typically used in conjunction with the DOI. For example, journals published by the American Geophysical Union since 1999 use citation numbers rather than page numbers.

**DOI**
  Digital Object Identifier. A unique identifier assigned to digital publications. The DOI consists of a prefix and suffix separated by a slash. The portion before the slash stands for the publisher and is assigned by the International DOI Foundation. For example, 10.1029 is the prefix for the American Geophysical Union. The suffix is assigned by the publisher according to their protocols. For example, the DOI 10.1029/2002PA000768 is for an article submitted to *Paleoceanography* in 2002 and is article number 768 submitted since the system was installed. An example of CitationNumber and DOI:

    Barron, J. A., L. Heusser, T. Herbert, and M. Lyle. 2003.
    High-resolution climatic evolution of coastal northern during the
    past 16,000 years, Paleoceanography 18(1):\ **1020.
    DOI:10.1029/2002PA000768.**

**NumVolumes**
	Number of volumes in a set of books. Used when the entire set is referenced. An example of NumVolumes and Edition:

    Wilson, D. E., and D. M. Reeder. 2005. Mammal species of the world:
    a taxonomic and geographic reference. **Third edition. 2 volumes**.
    The Johns Hopkins University Press, Baltimore, Maryland, USA.

**Edition**
	Edition of a publication.

**VolumeTitle**
	Title of a book volume in a set. Used if the individual volume is referenced. Example of Volume and VolumeTitle:

    Flora of North America Editorial Committee. 2002. Flora of North America north of . **Volume 26**. **Magnoliophyta: Liliidae: Liliales and Orchidales**. Oxford University Press, New York, New York, USA.

**SeriesTitle**
	Title of a book series. Book series consist of a series of books, typically published at irregular intervals on sometimes
related but different topics. The number of volumes in a series is typically open ended. Book series are often assigned ISSN numbers as well as ISBN numbers. However, in contrast to most serials, book series have individual titles and authors or editors. Citation practices for book series vary; sometimes they are cited as books, other times as journals. The default citation for Neotoma includes all information. An example of SeriesTitle and SeriesVolume:

    Curtis, J. H., and D. A. Hodell. 1993. An isotopic and trace element study of ostracods from , : A 10,500 year record of paleosalinity and paleotemperature changes in the . Pages 135-152 in P. K. Swart, K. C. Lohmann, J. McKensie, and S. Savin, editors. Climate change in continental isotopic records. **Geophysical Monograph 78**. American Geophysical Union, Washington, D.C., USA.

**SeriesVolume**
	Volume number in a series.

**Publisher**
	Publisher, including commercial publishing houses, university presses, government agencies, and non-governmental organizations, generally the owner of the copyright.

**City**
	City in which the publication was published. The first city if a list is given.

**State**
	State or province in which the publication was published. Used for the and , not used for many countries.

**Country**
	Country in which the publication was published, generally the complete country name, but «» for the .

**OriginalLanguage**
	The original language if the publication or bibliographic citation is translated from another language or transliterated from a non-Latin character set. Field not needed for non-translated publications in languages using the Latin character set. In the following example, the ArticleTitle is translated from Russian to English and the BookTitle (journal name) is transliterated from Russian:

    Tarasov, P.E. 1991. Late Holocene features of the Kokchetav Highland. Vestnik Moskovskogo Universiteta. Series 5. Geography **6**:54-60 [in **Russian**].

**Notes**
	Free form notes or comments about the publication, which may be added parenthetically to the citation.

.. _PublicationTypes:

PublicationTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Publication Types. This table is referenced by the :ref:`Publications` table.

+-------------------------------+----------------+------+-----+
| **Table: PublicationTypes**                                 |
+-------------------------------+----------------+------+-----+
| PubTypeID                     | Long Integer   | PK   |     |
+-------------------------------+----------------+------+-----+
| PubType                       | Text           |      |     |
+-------------------------------+----------------+------+-----+

**PubTypeID**
	An arbitrary Publication Type identification number.

**PubType**
	Publication Type. The database has the following types:

-  Legacy Legacy citation ingested from another database and not parsed
       into separate fields

-  Journal Article Article in a journal

-  Book Chapter Chapter or section in an edited book

-  Authored Book An authored book

-  Edited Book An edited book

-  Master's Thesis A Master's thesis

-  Doctoral Dissertation A doctoral dissertation or Ph.D. thesis

-  Authored Report An authored report

-  Edited Report An edited report

-  Other Authored An authored publication not fitting in any other
       category (e.g. web sites, maps)

-  Other Edited A edited publication not fitting into any other category

Examples of the different Publication Types are given in the following sections. Shown for each Publication Type are the fields in the :ref:`Publications` table that may be filled for that type, with the exception that OriginalLanguage and Notes are not shown unless used.

Legacy Publication
`````````````````````````````

+--------------------------+------------------------------------------------------------------------------------------+
| **PubTypeID = Legacy**                                                                                              |
+--------------------------+------------------------------------------------------------------------------------------+
| Authors                  | Each author a record in the :ref:`PublicationAuthors` table   |
+--------------------------+------------------------------------------------------------------------------------------+
| Year                     | Year published                                                                           |
+--------------------------+------------------------------------------------------------------------------------------+
| Citation                 | Complete citation as imported                                                            |
+--------------------------+------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Legacy Example: Imported from the North American Pollen Database**                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Baker, R. G. 1983. Holocene vegetational history of the western . Pages 109-127 in H.E. Wright, Jr., editor. Late-Quaternary environments of the . Volume 2. The Holocene. Press. .   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Authors                                                                                                                                                                               | R. G. Baker                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Year                                                                                                                                                                                  | 1979                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Citation                                                                                                                                                                              | Baker, R.G. 1983. Holocene vegetational history of the western . Pages 109-127 in H.E. Wright, Jr., editor. Late-Quaternary environments of the . Volume 2. the Holocene. Press. .   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Legacy Example: Imported from FAUNMAP**                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Semken, H. A., Jr. 1983. Holocene mammalian biogeography and climatic change in the eastern and central . Pp. 182-207 in Late-Quaternary environments of the , Volume 2: The Holocene (H. E. Wright, Jr., ed.), of , .   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Authors                                                                                                                                                                                                                  | H. A. Semken, Jr.                                                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Year                                                                                                                                                                                                                     | 1983                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Citation                                                                                                                                                                                                                 | Semken, H. A., Jr. 1983. Holocene mammalian biogeography and climatic change in the eastern and central . Pages 182-207 in Late-Quaternary environments of the , Volume 2: The Holocene (H. E. Wright, Jr., editor), of , .   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Journal Article
`````````````````````````````

+---------------------------+------------------------------------------------------------------------------------------+
| **PubTypeID = Journal**                                                                                              |
+---------------------------+------------------------------------------------------------------------------------------+
| Authors                   | Each author a record in the :ref:`PublicationAuthors` table   |
+---------------------------+------------------------------------------------------------------------------------------+
| Year                      | Year published                                                                           |
+---------------------------+------------------------------------------------------------------------------------------+
| ArticleTitle              | Article title                                                                            |
+---------------------------+------------------------------------------------------------------------------------------+
| BookTitle                 | Journal name                                                                             |
+---------------------------+------------------------------------------------------------------------------------------+
| Volume                    | Volume                                                                                   |
+---------------------------+------------------------------------------------------------------------------------------+
| Issue                     | Issue                                                                                    |
+---------------------------+------------------------------------------------------------------------------------------+
| Pages                     | Pages                                                                                    |
+---------------------------+------------------------------------------------------------------------------------------+
| CitationNumber            | Citation number                                                                          |
+---------------------------+------------------------------------------------------------------------------------------+
| DOI                       | Digital Object Identifier                                                                |
+---------------------------+------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| **Journal Example: Page numbers**                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Wright, H.E., Jr., T.C. Winter, and H.L. Patten. 1963. Two pollen diagrams from southeastern : problems in the regional late-glacial and postglacial vegetational history. Geological Society of Bulletin 74:1371-1396.   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Authors                                                                                                                                                                                                                   | H. E. Wright Jr.                                                                                                     |
|                                                                                                                                                                                                                           |                                                                                                                      |
|                                                                                                                                                                                                                           | T. C. Winter                                                                                                         |
|                                                                                                                                                                                                                           |                                                                                                                      |
|                                                                                                                                                                                                                           | H. L. Patten                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Year                                                                                                                                                                                                                      | 1963                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ArticleTitle                                                                                                                                                                                                              | Two pollen diagrams from southeastern : problems in the regional late-glacial and postglacial vegetational history   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| BookTitle                                                                                                                                                                                                                 | Geological Society of Bulletin                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Volume                                                                                                                                                                                                                    | 74                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Issue                                                                                                                                                                                                                     |                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Pages                                                                                                                                                                                                                     | 1371-1396                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| CitationNumber                                                                                                                                                                                                            |                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| DOI                                                                                                                                                                                                                       |                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| **Journal Example: Page numbers, article in French, OriginalLanguage not needed**                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Richard, P .J. H. 1979. Contribution à l'histoire postglaciaire de la végétation au nord-est de la Jamésie, Nouveau-Québec. Géographie physique et Quaternaire 33:93-112.   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Authors                                                                                                                                                                     | Richard, P. J. H.                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Year                                                                                                                                                                        | 1979                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ArticleTitle                                                                                                                                                                | Contribution à l'histoire postglaciaire de la végétation au nord-est de la Jamésie, Nouveau-Québec   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| BookTitle                                                                                                                                                                   | Géographie physique et Quaternaire                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Volume                                                                                                                                                                      | 33                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Issue                                                                                                                                                                       |                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Pages                                                                                                                                                                       | 93-112                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| CitationNumber                                                                                                                                                              |                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| DOI                                                                                                                                                                         |                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| **Journal Example: Citation number and DOI**                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Barron, J. A., L. Heusser, T. Herbert, and M. Lyle. 2003. High-resolution climatic evolution of coastal northern during the past 16,000 years, Paleoceanography 18(1):1020. DOI:10.1029/2002PA000768.   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Authors                                                                                                                                                                                                 | J. A. Barron                                                                          |
|                                                                                                                                                                                                         |                                                                                       |
|                                                                                                                                                                                                         | L. Heusser                                                                            |
|                                                                                                                                                                                                         |                                                                                       |
|                                                                                                                                                                                                         | T. Herbert                                                                            |
|                                                                                                                                                                                                         |                                                                                       |
|                                                                                                                                                                                                         | M. Lyle                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Year                                                                                                                                                                                                    | 2003                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ArticleTitle                                                                                                                                                                                            | High-resolution climatic evolution of coastal northern during the past 16,000 years   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| BookTitle                                                                                                                                                                                               | Paleoceanography                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Volume                                                                                                                                                                                                  | 18                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Issue                                                                                                                                                                                                   | 1                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Pages                                                                                                                                                                                                   |                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| CitationNumber                                                                                                                                                                                          | 1020                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| DOI                                                                                                                                                                                                     | 10.1029/2002PA000768                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| **Journal Example: Translated and transliterated from Russian**                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Tarasov, P.E. 1991. Late Holocene features of the Kokchetav Highland. Vestnik Moskovskogo Universiteta. Series 5. Geography 6:54-60 [in Russian].   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Authors                                                                                                                                             | P. E. Tarasov                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Year                                                                                                                                                | 1991                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| ArticleTitle                                                                                                                                        | Late Holocene features of the Kokchetav Highland        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| BookTitle                                                                                                                                           | Vestnik Moskovskogo Universiteta. Series 5. Geography   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Volume                                                                                                                                              | 6                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Issue                                                                                                                                               |                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Pages                                                                                                                                               | 54-60                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| CitationNumber                                                                                                                                      |                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| DOI                                                                                                                                                 |                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| OriginalLanguage                                                                                                                                    | Russian                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+

Book Chapter
`````````````````````````````

+--------------------------------+------------------------------------------------------------------------------------------+
| **PubTypeID = Book Chapter**                                                                                              |
+--------------------------------+------------------------------------------------------------------------------------------+
| Authors                        | Each author a record in the :ref:`PublicationAuthors` table   |
+--------------------------------+------------------------------------------------------------------------------------------+
| Year                           | Year published                                                                           |
+--------------------------------+------------------------------------------------------------------------------------------+
| ArticleTitle                   | Article title                                                                            |
+--------------------------------+------------------------------------------------------------------------------------------+
| Editors                        | Table PublicatonAuthors: AuthorTypeID =Editor                                            |
+--------------------------------+------------------------------------------------------------------------------------------+
| Volume                         | Volume in set                                                                            |
+--------------------------------+------------------------------------------------------------------------------------------+
| Pages                          | Article pages                                                                            |
+--------------------------------+------------------------------------------------------------------------------------------+
| BookTitle                      | Book title                                                                               |
+--------------------------------+------------------------------------------------------------------------------------------+
| Edition                        | Edition                                                                                  |
+--------------------------------+------------------------------------------------------------------------------------------+
| VolumeTitle                    | Title of volume in multivolume set                                                       |
+--------------------------------+------------------------------------------------------------------------------------------+
| SeriesTitle                    | Series title                                                                             |
+--------------------------------+------------------------------------------------------------------------------------------+
| SeriesVolume                   | Volume in series                                                                         |
+--------------------------------+------------------------------------------------------------------------------------------+
| Publisher                      | Publisher                                                                                |
+--------------------------------+------------------------------------------------------------------------------------------+
| City                           | City where published                                                                     |
+--------------------------------+------------------------------------------------------------------------------------------+
| State                          | State or province where published                                                        |
+--------------------------------+------------------------------------------------------------------------------------------+
| Country                        | Country where published                                                                  |
+--------------------------------+------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| **Book Chapter Example: Volume in a set**                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| Lundelius, E. L., Jr., R. W. Graham, E. Anderson, J. Guilday, J. A. Holman, D. W. Steadman, and S. D. Webb. 1983. Terrestrial vertebrate faunas. Pages 311-353 in S. C. Porter, editor. Late-Quaternary environments of the . Volume 1. The late Pleistocene. of Press, .   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| Authors                                                                                                                                                                                                                                                                     | E. L. Lundelius Jr.                   |
|                                                                                                                                                                                                                                                                             |                                       |
|                                                                                                                                                                                                                                                                             | R. W. Graham                          |
|                                                                                                                                                                                                                                                                             |                                       |
|                                                                                                                                                                                                                                                                             | J. Guilday                            |
|                                                                                                                                                                                                                                                                             |                                       |
|                                                                                                                                                                                                                                                                             | J. A. Holman                          |
|                                                                                                                                                                                                                                                                             |                                       |
|                                                                                                                                                                                                                                                                             | D. W. Steadman                        |
|                                                                                                                                                                                                                                                                             |                                       |
|                                                                                                                                                                                                                                                                             | S. D. Webb                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| Year                                                                                                                                                                                                                                                                        | 1983                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| ArticleTitle                                                                                                                                                                                                                                                                | Terrestrial vertebrate faunas         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| Editors                                                                                                                                                                                                                                                                     | S. C. Porter                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| Volume                                                                                                                                                                                                                                                                      | 1                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| Pages                                                                                                                                                                                                                                                                       | 311-353                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| BookTitle                                                                                                                                                                                                                                                                   | Late-Quaternary environments of the   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| Edition                                                                                                                                                                                                                                                                     |                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| VolumeTitle                                                                                                                                                                                                                                                                 | The late Pleistocene                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| SeriesTitle                                                                                                                                                                                                                                                                 |                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| SeriesVolume                                                                                                                                                                                                                                                                |                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| Publisher                                                                                                                                                                                                                                                                   | Press                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| City                                                                                                                                                                                                                                                                        |                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| State                                                                                                                                                                                                                                                                       |                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| Country                                                                                                                                                                                                                                                                     |                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| **Book Chapter Example: Volume in a series**                                                                                                                                                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Curtis, J. H., and D. A. Hodell. 1993. An isotopic and trace element study of ostracods from , : A 10,500 year record of paleosalinity and paleotemperature changes in the . Pages 135-152 in P. K. Swart, K. C. Lohmann, J. McKensie, and S. Savin, editors. Climate change in continental isotopic records. Geophysical Monograph 78. American Geophysical Union, .   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Authors                                                                                                                                                                                                                                                                                                                                                                 | J. H. Curtis                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                         | D. A. Hodell                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Year                                                                                                                                                                                                                                                                                                                                                                    | 1993                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ArticleTitle                                                                                                                                                                                                                                                                                                                                                            | An isotopic and trace element study of ostracods from , : A 10,500 year record of paleosalinity and paleotemperature changes in the   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Editors                                                                                                                                                                                                                                                                                                                                                                 | P. K. Swart                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                         | K. C. Lohmann                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                         | J. McKensie                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                         | S. Savin                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Volume                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Pages                                                                                                                                                                                                                                                                                                                                                                   | 135-152                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| BookTitle                                                                                                                                                                                                                                                                                                                                                               | Climate change in continental isotopic records                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Edition                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| VolumeTitle                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| SeriesTitle                                                                                                                                                                                                                                                                                                                                                             | Geophysical Monograph                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| SeriesVolume                                                                                                                                                                                                                                                                                                                                                            | 78                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Publisher                                                                                                                                                                                                                                                                                                                                                               | American Geophysical                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| City                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| State                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Country                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| **Book Chapter Example: Chapter in an edited technical report**                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Gust, S. 1990. Faunal. Pages 112-113 in J. G. Maniery, editor. Northern Pomo prehistory: archaeological test excavations at CA-MEN 2138, . Technical Report 1. PAR Environmental Services, Inc.,   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Authors                                                                                                                                                                                            | S. Gust                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Year                                                                                                                                                                                               | 1990                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| ArticleTitle                                                                                                                                                                                       | Faunal                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Editors                                                                                                                                                                                            | J. G. Maniery                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Volume                                                                                                                                                                                             |                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Pages                                                                                                                                                                                              | 112-113                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| BookTitle                                                                                                                                                                                          | Northern Pomo prehistory: archaeological test excavations at CA-MEN 2138,   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Edition                                                                                                                                                                                            |                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| VolumeTitle                                                                                                                                                                                        |                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| SeriesTitle                                                                                                                                                                                        | Technical Report                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| SeriesVolume                                                                                                                                                                                       | 71                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Publisher                                                                                                                                                                                          | PAR Environmental Services, Inc.                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| City                                                                                                                                                                                               |                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| State                                                                                                                                                                                              |                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Country                                                                                                                                                                                            |                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

Authored Book
`````````````````````````````

+-----------------------------------+------------------------------------------------------------------------------------------+
| \ **PubTypeID = Authored Book**   |
+-----------------------------------+------------------------------------------------------------------------------------------+
| Authors                           | Each author a record in the :ref:`PublicationAuthors` table   |
+-----------------------------------+------------------------------------------------------------------------------------------+
| Year                              | Year published                                                                           |
+-----------------------------------+------------------------------------------------------------------------------------------+
| Volume                            | Volume in set                                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------+
| BookTitle                         | Book title                                                                               |
+-----------------------------------+------------------------------------------------------------------------------------------+
| Edition                           | Edition                                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------+
| NumVolumes                        | Number of volumes in set. Use only if Volume not specified.                              |
+-----------------------------------+------------------------------------------------------------------------------------------+
| VolumeTitle                       | Title of volume in multivolume set                                                       |
+-----------------------------------+------------------------------------------------------------------------------------------+
| SeriesTitle                       | Series title                                                                             |
+-----------------------------------+------------------------------------------------------------------------------------------+
| SeriesVolume                      | Series volume                                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------+
| Publisher                         | Publisher                                                                                |
+-----------------------------------+------------------------------------------------------------------------------------------+
| City                              | City where published                                                                     |
+-----------------------------------+------------------------------------------------------------------------------------------+
| State                             | State or province where published                                                        |
+-----------------------------------+------------------------------------------------------------------------------------------+
| Country                           | Country where published                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------+

+-------------------------------------------------------------+-----------------------------+
| **Authored Book Example**                                   |
+-------------------------------------------------------------+-----------------------------+
| Ritchie, J. C. 1987. Postglacial vegetation of . Press, .   |
+-------------------------------------------------------------+-----------------------------+
| Authors                                                     | J. C. Ritchie               |
+-------------------------------------------------------------+-----------------------------+
| Year                                                        | 1987                        |
+-------------------------------------------------------------+-----------------------------+
| Volume                                                      |                             |
+-------------------------------------------------------------+-----------------------------+
| BookTitle                                                   | Postglacial vegetation of   |
+-------------------------------------------------------------+-----------------------------+
| Edition                                                     |                             |
+-------------------------------------------------------------+-----------------------------+
| NumVolumes                                                  |                             |
+-------------------------------------------------------------+-----------------------------+
| VolumeTitle                                                 |                             |
+-------------------------------------------------------------+-----------------------------+
| SeriesTitle                                                 |                             |
+-------------------------------------------------------------+-----------------------------+
| SeriesVolume                                                |                             |
+-------------------------------------------------------------+-----------------------------+
| Publisher                                                   | Press                       |
+-------------------------------------------------------------+-----------------------------+
| City                                                        |                             |
+-------------------------------------------------------------+-----------------------------+
| State                                                       |                             |
+-------------------------------------------------------------+-----------------------------+
| Country                                                     |                             |
+-------------------------------------------------------------+-----------------------------+

+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| **Authored Book Example: Multivolume**                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| Wilson, D. E., and D. M. Reeder. 2005. Mammal species of the world: a taxonomic and geographic reference. Third edition. 2 volumes. The Press, .   |
+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| Authors                                                                                                                                            | D. E.                                                               |
|                                                                                                                                                    |                                                                     |
|                                                                                                                                                    | D. M. Reeder                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| Year                                                                                                                                               | 2005                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| Volume                                                                                                                                             |                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| BookTitle                                                                                                                                          | Mammal species of the world: a taxonomic and geographic reference   |
+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| Edition                                                                                                                                            | Third                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| NumVolumes                                                                                                                                         | 2                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| VolumeTitle                                                                                                                                        |                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| SeriesTitle                                                                                                                                        |                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| SeriesVolume                                                                                                                                       |                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| Publisher                                                                                                                                          | The Press                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| City                                                                                                                                               |                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| State                                                                                                                                              |                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| Country                                                                                                                                            |                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| **Authored Book Example: Volume in a set**                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| Flora of Editorial Committee. 2002. Flora of North America north of . Volume 26. Magnoliophyta: Liliidae: Liliales and Orchidales. Press, .   |
+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| Authors                                                                                                                                       | Flora of Editorial Committee                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| Year                                                                                                                                          | 2002                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| Volume                                                                                                                                        | 26                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| BookTitle                                                                                                                                     | Flora of North America north of                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| Edition                                                                                                                                       |                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| NumVolumes                                                                                                                                    |                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| VolumeTitle                                                                                                                                   | Magnoliophyta: Liliidae: Liliales and Orchidales   |
+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| SeriesTitle                                                                                                                                   |                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| SeriesVolume                                                                                                                                  |                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| Publisher                                                                                                                                     | Press                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| City                                                                                                                                          |                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| State                                                                                                                                         |                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+
| Country                                                                                                                                       |                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------+

.. _Edited Book:

Edited Book
~~~~~~~~~~~

+-------------------------------+------------------------------------------------------------------------------------------+
| **PubTypeID = Edited Book**                                                                                              |
+-------------------------------+------------------------------------------------------------------------------------------+
| Authors                       | Each editor a record in the :ref:`PublicationAuthors` table   |
+-------------------------------+------------------------------------------------------------------------------------------+
| Year                          | Year published                                                                           |
+-------------------------------+------------------------------------------------------------------------------------------+
| Volume                        | Volume in set                                                                            |
+-------------------------------+------------------------------------------------------------------------------------------+
| BookTitle                     | Book title                                                                               |
+-------------------------------+------------------------------------------------------------------------------------------+
| Edition                       | Edition                                                                                  |
+-------------------------------+------------------------------------------------------------------------------------------+
| NumVolumes                    | Number of volumes in set. Use only if Volume not specified.                              |
+-------------------------------+------------------------------------------------------------------------------------------+
| VolumeTitle                   | Title of volume in multivolume set                                                       |
+-------------------------------+------------------------------------------------------------------------------------------+
| SeriesTitle                   | Series title                                                                             |
+-------------------------------+------------------------------------------------------------------------------------------+
| SeriesVolume                  | Series volume                                                                            |
+-------------------------------+------------------------------------------------------------------------------------------+
| Publisher                     | Publisher                                                                                |
+-------------------------------+------------------------------------------------------------------------------------------+
| City                          | City where published                                                                     |
+-------------------------------+------------------------------------------------------------------------------------------+
| State                         | State or province where published                                                        |
+-------------------------------+------------------------------------------------------------------------------------------+
| Country                       | Country where published                                                                  |
+-------------------------------+------------------------------------------------------------------------------------------+

+----------------------------------------------------------------+----------------------+
| **Edited Book Example**                                                               |
+----------------------------------------------------------------+----------------------+
| Frison, G. C., editor. 1996. The Mill Iron site. of Press, .                          |
+----------------------------------------------------------------+----------------------+
| Editors                                                        | G. C. Frison         |
+----------------------------------------------------------------+----------------------+
| Year                                                           | 1996                 |
+----------------------------------------------------------------+----------------------+
| Volume                                                         |                      |
+----------------------------------------------------------------+----------------------+
| BookTitle                                                      | The Mill Iron site   |
+----------------------------------------------------------------+----------------------+
| Edition                                                        |                      |
+----------------------------------------------------------------+----------------------+
| NumVolumes                                                     |                      |
+----------------------------------------------------------------+----------------------+
| VolumeTitle                                                    |                      |
+----------------------------------------------------------------+----------------------+
| SeriesTitle                                                    |                      |
+----------------------------------------------------------------+----------------------+
| SeriesVolume                                                   |                      |
+----------------------------------------------------------------+----------------------+
| Publisher                                                      | Press                |
+----------------------------------------------------------------+----------------------+
| City                                                           |                      |
+----------------------------------------------------------------+----------------------+
| State                                                          |                      |
+----------------------------------------------------------------+----------------------+
| Country                                                        |                      |
+----------------------------------------------------------------+----------------------+

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| **Edited Book Example: May also be entered as an edited report**                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Jeter, M. D., editor. 1988. The Burris site and beyond: archeological survey and testing along a pipeline corridor and excavations at a Mississippian village, northeast . Research Report 27. Archeological Survey, .   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Editors                                                                                                                                                                                                                  | M. D. Jeter                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Year                                                                                                                                                                                                                     | 1988                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Volume                                                                                                                                                                                                                   |                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| BookTitle                                                                                                                                                                                                                | The Burris site and beyond: archeological survey and testing along a pipeline corridor and excavations at a Mississippian village, northeast   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Edition                                                                                                                                                                                                                  |                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| NumVolumes                                                                                                                                                                                                               |                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| VolumeTitle                                                                                                                                                                                                              |                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| SeriesTitle                                                                                                                                                                                                              | Research Report                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| SeriesVolume                                                                                                                                                                                                             | 27                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Publisher                                                                                                                                                                                                                | Archeological Survey                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| City                                                                                                                                                                                                                     |                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| State                                                                                                                                                                                                                    |                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Country                                                                                                                                                                                                                  |                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| **Edited Book Example: Second edition of volume in a set **                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| Tutin, T. G., N. A. Burges, A. O. Chater, J. R. Edmondson, V. H. Heywood, D. M. Moore, D. H. Valentine, S. M. Walters, and D. A. Webb, editors. 1993. Flora Europaea. Volume 1. Psilotaceae to Platanaceae. Second edition. Press, .   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| Editors                                                                                                                                                                                                                                | T. G. Tutin                  |
|                                                                                                                                                                                                                                        |                              |
|                                                                                                                                                                                                                                        | N. A. Burges                 |
|                                                                                                                                                                                                                                        |                              |
|                                                                                                                                                                                                                                        | A. O. Chater                 |
|                                                                                                                                                                                                                                        |                              |
|                                                                                                                                                                                                                                        | J. R. Edmondson              |
|                                                                                                                                                                                                                                        |                              |
|                                                                                                                                                                                                                                        | V. H. Heywood                |
|                                                                                                                                                                                                                                        |                              |
|                                                                                                                                                                                                                                        | D. M. Moore                  |
|                                                                                                                                                                                                                                        |                              |
|                                                                                                                                                                                                                                        | D. H. Valentine              |
|                                                                                                                                                                                                                                        |                              |
|                                                                                                                                                                                                                                        | S. M. Walters                |
|                                                                                                                                                                                                                                        |                              |
|                                                                                                                                                                                                                                        | D. A. Webb                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| Year                                                                                                                                                                                                                                   | 1993                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| Volume                                                                                                                                                                                                                                 | 1                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| BookTitle                                                                                                                                                                                                                              | Flora Europaea               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| Edition                                                                                                                                                                                                                                | Second                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| NumVolumes                                                                                                                                                                                                                             |                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| VolumeTitle                                                                                                                                                                                                                            | Psilotaceae to Platanaceae   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| SeriesTitle                                                                                                                                                                                                                            |                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| SeriesVolume                                                                                                                                                                                                                           |                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| Publisher                                                                                                                                                                                                                              | Press                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| City                                                                                                                                                                                                                                   |                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| State                                                                                                                                                                                                                                  |                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+
| Country                                                                                                                                                                                                                                |                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+

Master’s Thesis
`````````````````````````````

+-----------------------------------+-------------------------------------------------------------------------------------+
| **PubTypeID = Master’s Thesis**   |
+-----------------------------------+-------------------------------------------------------------------------------------+
| Authors                           | Author a record in the :ref:`PublicationAuthors` table   |
+-----------------------------------+-------------------------------------------------------------------------------------+
| Year                              | Year published                                                                      |
+-----------------------------------+-------------------------------------------------------------------------------------+
| Pages                             | Number of pages in thesis                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------+
| BookTitle                         | Title of thesis                                                                     |
+-----------------------------------+-------------------------------------------------------------------------------------+
| Publisher                         | University where degree granted                                                     |
+-----------------------------------+-------------------------------------------------------------------------------------+
| City                              | City of university                                                                  |
+-----------------------------------+-------------------------------------------------------------------------------------+
| State                             | State or province of university                                                     |
+-----------------------------------+-------------------------------------------------------------------------------------+
| Country                           | Country of university                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------+

+----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| **Master’s Thesis Example**                                                                                          |
+----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| , N. J. 1981. Vegetation history and lake-level changes at a saline lake in northeastern . Master's thesis. of , .   |
+----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Authors                                                                                                              | N. J. Radle                                                                  |
+----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Year                                                                                                                 | 1981                                                                         |
+----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Pages                                                                                                                | 126                                                                          |
+----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| BookTitle                                                                                                            | Vegetation history and lake-level changes at a saline lake in northeastern   |
+----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Publisher                                                                                                            |                                                                              |
+----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| City                                                                                                                 |                                                                              |
+----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| State                                                                                                                |                                                                              |
+----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Country                                                                                                              |                                                                              |
+----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+

Doctoral Dissertation
`````````````````````````````

+-----------------------------------------+-------------------------------------------------------------------------------------+
| **PubTypeID = Doctoral Dissertation**   |
+-----------------------------------------+-------------------------------------------------------------------------------------+
| Authors                                 | Author a record in the :ref:`PublicationAuthors` table   |
+-----------------------------------------+-------------------------------------------------------------------------------------+
| Year                                    | Year published                                                                      |
+-----------------------------------------+-------------------------------------------------------------------------------------+
| Pages                                   | Number of pages in thesis                                                           |
+-----------------------------------------+-------------------------------------------------------------------------------------+
| BookTitle                               | Title of thesis                                                                     |
+-----------------------------------------+-------------------------------------------------------------------------------------+
| Publisher                               | University where degree granted                                                     |
+-----------------------------------------+-------------------------------------------------------------------------------------+
| City                                    | City of university                                                                  |
+-----------------------------------------+-------------------------------------------------------------------------------------+
| State                                   | State or province of university                                                     |
+-----------------------------------------+-------------------------------------------------------------------------------------+
| Country                                 | Country of university                                                               |
+-----------------------------------------+-------------------------------------------------------------------------------------+

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| **Doctoral Dissertation Example**                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Ortega-Guerrero, B. 1992. Paleomagnetismo, magnetoestratifia y paleoecología del Cuaternario tardío en el Lago de Chalco, Cuenca de México. Doctoral dissertation. Universidad Nacional Autónoma de México, , Mexico.   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Authors                                                                                                                                                                                                                 | B. Ortega-Guerrero                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Year                                                                                                                                                                                                                    | 1992                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Pages                                                                                                                                                                                                                   | 161                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| BookTitle                                                                                                                                                                                                               | Paleomagnetismo, magnetoestratifia y paleoecología del Cuaternario tardío en el Lago de Chalco, Cuenca de México   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Publisher                                                                                                                                                                                                               | Universidad Nacional Autónoma de México                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| City                                                                                                                                                                                                                    |                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| State                                                                                                                                                                                                                   |                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Country                                                                                                                                                                                                                 |                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

Authored Report
`````````````````````````````

+-----------------------------------+------------------------------------------------------------------------------------------+
| **PubTypeID = Authored Report**   |
+-----------------------------------+------------------------------------------------------------------------------------------+
| Authors                           | Each author a record in the :ref:`PublicationAuthors` table   |
+-----------------------------------+------------------------------------------------------------------------------------------+
| Year                              | Year published                                                                           |
+-----------------------------------+------------------------------------------------------------------------------------------+
| Pages                             | Number of pages in report                                                                |
+-----------------------------------+------------------------------------------------------------------------------------------+
| BookTitle                         | Title of report                                                                          |
+-----------------------------------+------------------------------------------------------------------------------------------+
| SeriesTitle                       | Report series or description                                                             |
+-----------------------------------+------------------------------------------------------------------------------------------+
| SeriesVolume                      | Report number if in a numbered series                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------+
| Publisher                         | Publisher, may be a government agency or non-governmental organization                   |
+-----------------------------------+------------------------------------------------------------------------------------------+
| City                              | City where published                                                                     |
+-----------------------------------+------------------------------------------------------------------------------------------+
| State                             | State where published                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------+
| Country                           | Country where published                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| **Authored Report Example: Numbered series**                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Huber, J. K. 2003. Results of a pollen and loss-on-ignition analysis of sediment from a mastodon pulp cavity, North Fork Canoe Creek, . Report 2003-1. James K. Huber Consulting, .   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Authors                                                                                                                                                                               | J. K. Huber                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Year                                                                                                                                                                                  | 2003                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Pages                                                                                                                                                                                 |                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| BookTitle                                                                                                                                                                             | Results of a pollen and loss-on-ignition analysis of sediment from a mastodon pulp cavity, North Fork Canoe Creek,   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| SeriesTitle                                                                                                                                                                           | Report                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| SeriesVolume                                                                                                                                                                          | 2003-1                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Publisher                                                                                                                                                                             | James K. Huber Consulting                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| City                                                                                                                                                                                  | Vinton                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| State                                                                                                                                                                                 |                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Country                                                                                                                                                                               |                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| **Authored Report Example: Numbered series**                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| Daugherty, R. D., J. J. Flenniken, and J. M. Welch. 1987. A data recovery study of rockshelters (45-LE-222) in Lewis County, Washington. United States Department of Agriculture, Forest Service, Region. Studies in Cultural Resource Management 8. .   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| Authors                                                                                                                                                                                                                                                  | R. D. Daugherty                                                                 |
|                                                                                                                                                                                                                                                          |                                                                                 |
|                                                                                                                                                                                                                                                          | J. J. Flenniken                                                                 |
|                                                                                                                                                                                                                                                          |                                                                                 |
|                                                                                                                                                                                                                                                          | J. M. Welch                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| Year                                                                                                                                                                                                                                                     | 1987                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| Pages                                                                                                                                                                                                                                                    |                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| BookTitle                                                                                                                                                                                                                                                | A data recovery study of rockshelters (45-LE-222) in Lewis County, Washington   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| SeriesTitle                                                                                                                                                                                                                                              | Studies in Cultural Resource Management                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| SeriesVolume                                                                                                                                                                                                                                             | 8                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| Publisher                                                                                                                                                                                                                                                | United States Department of Agriculture, Forest Service, Region                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| City                                                                                                                                                                                                                                                     |                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| State                                                                                                                                                                                                                                                    |                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| Country                                                                                                                                                                                                                                                  |                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Authored Report Example: Report series is a description**                                                                                                                                                                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Cannon, K. P. 1997. The analysis of a late Holocene bison skull from Fawn Creek, , and its implications for understanding the history and ecology of bison in the Intermountain West. Report prepared for The Department of Agriculture, United States Forest Service, Salmon-Challis National Forest, Salmon, Idaho. United States Department of Interior, National Park Service, Midwest Archeological Center, .   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Authors                                                                                                                                                                                                                                                                                                                                                                                                              | K. P. Cannon                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Year                                                                                                                                                                                                                                                                                                                                                                                                                 | 1997                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pages                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BookTitle                                                                                                                                                                                                                                                                                                                                                                                                            | The analysis of a late Holocene bison skull from Fawn Creek, , and its implications for understanding the history and ecology of bison in the Intermountain West   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SeriesTitle                                                                                                                                                                                                                                                                                                                                                                                                          | Report prepared for The Department of Agriculture, United States Forest Service, Salmon-Challis National Forest, Salmon, Idaho                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SeriesVolume                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Publisher                                                                                                                                                                                                                                                                                                                                                                                                            | United States Department of Interior, National Park Service, Archeological Center                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| City                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| State                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Country                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Edited Report
`````````````````````````````

+---------------------------------+------------------------------------------------------------------------------------------+
| **PubTypeID = Edited Report**   |
+---------------------------------+------------------------------------------------------------------------------------------+
| Authors                         | Each editor a record in the :ref:`PublicationAuthors` table   |
+---------------------------------+------------------------------------------------------------------------------------------+
| Year                            | Year published                                                                           |
+---------------------------------+------------------------------------------------------------------------------------------+
| Pages                           | Number of pages in report                                                                |
+---------------------------------+------------------------------------------------------------------------------------------+
| BookTitle                       | Title of report                                                                          |
+---------------------------------+------------------------------------------------------------------------------------------+
| SeriesTitle                     | Report series or description                                                             |
+---------------------------------+------------------------------------------------------------------------------------------+
| SeriesVolume                    | Report number if in a numbered series                                                    |
+---------------------------------+------------------------------------------------------------------------------------------+
| Publisher                       | Publisher, may be a government agency or non-governmental organization                   |
+---------------------------------+------------------------------------------------------------------------------------------+
| City                            | City where published                                                                     |
+---------------------------------+------------------------------------------------------------------------------------------+
| State                           | State where published                                                                    |
+---------------------------------+------------------------------------------------------------------------------------------+
| Country                         | Country where published                                                                  |
+---------------------------------+------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| **Edited Report Example: Numbered series**                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| Fishel, R. L., editor. 1999. Bison hunters of the western prairies: archaeological investigations at the site (13WD8), . Report 21. Office of the State Archaeologist, University of , .   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| Authors                                                                                                                                                                                    | R. L. Fishel                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| Year                                                                                                                                                                                       | 1999                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| Pages                                                                                                                                                                                      |                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| BookTitle                                                                                                                                                                                  | Bison hunters of the western prairies: archaeological investigations at the site (13WD8),   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| SeriesTitle                                                                                                                                                                                | Report                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| SeriesVolume                                                                                                                                                                               | 21                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| Publisher                                                                                                                                                                                  | Office of the State Archaeologist,                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| City                                                                                                                                                                                       |                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| State                                                                                                                                                                                      |                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| Country                                                                                                                                                                                    |                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+

Other Authored Publication
`````````````````````````````

+----------------------------------+------------------------------------------------------------------------------------------+
| **PubTypeID = Other Authored**   |
+----------------------------------+------------------------------------------------------------------------------------------+
| Authors                          | Each author a record in the :ref:`PublicationAuthors` table   |
+----------------------------------+------------------------------------------------------------------------------------------+
| Year                             | Year published                                                                           |
+----------------------------------+------------------------------------------------------------------------------------------+
| ArticleTitle                     | Rest of citation                                                                         |
+----------------------------------+------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| **Other Example: Web site**                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Stevens, P.F. 2007. Angiosperm Phylogeny Website. Version 8, June 2007. http://www.mobot.org/MOBOT/research/APweb/.   |
+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Authors                                                                                                               | P. F. Stevens                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Year                                                                                                                  | 2007                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ArticleTitle                                                                                                          | Angiosperm Phylogeny Website. Version 8, June 2007. http://www.mobot.org/MOBOT/research/APweb/.   |
+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

Other Edited Publication
`````````````````````````````

+--------------------------------+------------------------------------------------------------------------------------------+
| **PubTypeID = Other Edited**   |
+--------------------------------+------------------------------------------------------------------------------------------+
| Authors                        | Each editor a record in the :ref:`PublicationAuthors` table   |
+--------------------------------+------------------------------------------------------------------------------------------+
| Year                           | Year published                                                                           |
+--------------------------------+------------------------------------------------------------------------------------------+
| ArticleTitle                   | Rest of citation                                                                         |
+--------------------------------+------------------------------------------------------------------------------------------+

