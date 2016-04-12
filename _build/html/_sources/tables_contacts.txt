Contact and Individual Related Tables
----------------------------------------------------

.. _Collectors:

Collectors
~~~~~~~~~~~~~~~~~~~

The Collectors table lists the people who collected Collection Units.

+-------------------------+----------------+------+-------------------+
| **Collectors**                                                      |
+-------------------------+----------------+------+-------------------+
| CollectorID             | Long Integer   | PK   |                   |
+-------------------------+----------------+------+-------------------+
| CollectionUnitID        | Long Integer   | FK   | CollectionUnits   |
+-------------------------+----------------+------+-------------------+
| ContactID               | Long Integer   | FK   | Contacts          |
+-------------------------+----------------+------+-------------------+
| CollectorOrder          | Long Integer   |      |                   |
+-------------------------+----------------+------+-------------------+

**CollectorID (Primary Key)**
  An arbitrary Collector identification number.

**CollectionUnitID (Foreign Key)**
  CollectionUnit collected. Field links to :ref:`CollectionUnits` table.

**ContactID (Foreign Key)**
  Person who collected the CollectionUnit. Multiple individuals are listed in separate records. Field links to the :ref:`Contacts` table.

**CollectorOrder**
  Order in which Collectors should be listed.

.. _Contacts:

Contacts
~~~~~~~~~~~~~~~~~~~

This table lists persons and organizations.  The table is referenced through Foreign Keys in the following tables: :ref:`Chronologies`, :ref:`Collectors`, :ref:`DatasetPIs`, :ref:`DatasetSubmissions`, :ref:`Projects`, :ref:`PublicationAuthors`, :ref:`SampleAnalysts`, and :ref:`SiteImages` tables.

+-----------------------+----------------+------+----------------------+
| **Contacts**                                                         |
+-----------------------+----------------+------+----------------------+
| ContactID             | Long Integer   | PK   |                      |
+-----------------------+----------------+------+----------------------+
| AliasID               | Long Integer   | FK   | Contacts:ContactID   |
+-----------------------+----------------+------+----------------------+
| ContactName           | Text           |      |                      |
+-----------------------+----------------+------+----------------------+
| ContactStatusID       | Long Integer   | FK   | ContactStatuses      |
+-----------------------+----------------+------+----------------------+
| FamilyName            | Text           |      |                      |
+-----------------------+----------------+------+----------------------+
| LeadingInitials       | Text           |      |                      |
+-----------------------+----------------+------+----------------------+
| GivenNames            | Text           |      |                      |
+-----------------------+----------------+------+----------------------+
| Suffix                | Text           |      |                      |
+-----------------------+----------------+------+----------------------+
| Title                 | Text           |      |                      |
+-----------------------+----------------+------+----------------------+
| Phone                 | Text           |      |                      |
+-----------------------+----------------+------+----------------------+
| Fax                   | Text           |      |                      |
+-----------------------+----------------+------+----------------------+
| Email                 | Text           |      |                      |
+-----------------------+----------------+------+----------------------+
| URL                   | Text           |      |                      |
+-----------------------+----------------+------+----------------------+
| Address               | Memo           |      |                      |
+-----------------------+----------------+------+----------------------+
| Notes                 | Memo           |      |                      |
+-----------------------+----------------+------+----------------------+

**ContactID (Primary Key)**
  An arbitrary Contact identification number.

**AliasID (Foreign Key)**
  The ContactID of a person’s current name. If the AliasID is different from the ContactID, the ContactID refers to the person’s former name. For example, if J. L. Bouvier became J. B. Kennedy, the ContactID for J. B. Kennedy is the AliasID for J. L. Bouvier.

**ContactName**
  Full name of the person, last name first (e.g. «Simpson, George Gaylord») or name of organization or project (e.g. «Great Plains Flora Association»).

**ContactStatusID (Foreign Key)**
  Current status of the person, organization, or project. Field links to the :ref:`ContactStatuses` lookup table.

**FamilyName**
  Family or surname name of a person.

**LeadingInitials**
  Leading initials for given or forenames without spaces (e.g. «G.G.»).

**GivenNames** 
  Given or forenames of a person (e.g. «George Gaylord»). Initials with spaces are used if full given names are not known (e.g. «G. G»).

**Suffix** 
  Suffix of a person’s name (e.g. «Jr.», «III»).

**Title** 
  A person’s title (e.g. «Dr.», «Prof.», «»).

**Phone** 
  Telephone number.

**Fax** 
  Fax number.

**Email** 
  Email address.

**URL** 
  Universal Resource Locator, an Internet World Wide Web address.

**Address** 
  Full mailing address.

**Notes** 
  Free form notes or comments about the person, organization, or project.

.. _ContactStatuses:

ContactStatuses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Contact Statuses. Table is referenced by the :ref:`Contacts` table.

+------------------------------+----------------+------+-----+
| **ContactStatuses**                                        |
+------------------------------+----------------+------+-----+
| ContactStatusID              | Long Integer   | PK   |     |
+------------------------------+----------------+------+-----+
| ContactStatus                | Text           |      |     |
+------------------------------+----------------+------+-----+
| StatusDescription            | Text           |      |     |
+------------------------------+----------------+------+-----+

**ContactStatusID (Primary Key)** 
  An arbitrary Contact Status identification number.

**ContactStatus**
  Status of person, organization, or project.

**StatusDescription**
  Description of the status.  The following statuses exist (with descriptions):
    -  active Person, project, or organization is active in the field
    -  deceased Person is deceased
    -  defunct Project or organization is defunct or non-operational
    -  extant Project or organization is extant
    -  inactive Person is inactive in the field
    -  retired Person is retired
    -  unknown Status is unknown

