SQL Quickly
------------------------------

SQL (Sturctured Query Language) is a standard language for querying and modifying relational databases. It is an ANSI and ISO standard, although various vendors have added proprietary extensions. It is beyond the scope of this document to describe SQL or the differences between Microsoft Access SQL and ANSI SQL. However, examples of SQL queries are provided in this document as a tutorial. Most users of Access probably use the graphical design view for queries, but SQL queries are better suited for examples. These queries can by typed or copied and pasted into the Access query SQL view. The query can then be executed or opened in design view to show the graphical representation. One difference between Access SQL and other flavors is the wildcard; Access uses \* rather than %.

SQL Example
~~~~~~~~~~~

The following SQL example lists the number of sites by GeoPoliticalID (the name of the country) for and GeoPoliticalID that is defined as a country.

.. code-block:: sql
	:linenos:

	SELECT
		COUNT(sites.SiteName),
		gpu.GeoPoliticalName,
		gpu.GeoPoliticalUnit
	FROM
		(
			SELECT
				*
			FROM
				GeoPoliticalUnits
			WHERE
				geopoliticalunits.GeoPoliticalUnit = "country"
		) AS gpu
	INNER JOIN (
		Sites
		INNER JOIN SiteGeoPolitical ON Sites.SiteID = SiteGeoPolitical.SiteID
	) ON gpu.GeoPoliticalID = SiteGeoPolitical.GeoPoliticalID
	GROUP BY
		gpu.GeoPoliticalID,
		gpu.GeoPoliticalUnit;


Table Keys
~~~~~~~~~~~

Within tables there are often Keys.  A Key may be a **Primary Key** (PK), which acts as a unique identifier for individual records within a table, or they may be a **Foreign Key** (FK) which refers to a unique identifier in another table.  Primary Keys and Foreign Keys are critical to join tables in a SQL query.  In the above example we can see that the 

Data Types
~~~~~~~~~~~

In the table descriptions in the following section, the SQL Server data types are given for field descriptions. The equivalent Access data types are given in the following table.

+------------------------------------+------------------------+
| **SQL Server data type**           | **Access data type**   |
+====================================+========================+
| bit                                | Yes/No                 |
+------------------------------------+------------------------+
| datetime                           | Date/Time              |
+------------------------------------+------------------------+
| float                              | Double                 |
+------------------------------------+------------------------+
| int                                | Long Integer           |
+------------------------------------+------------------------+
| nvarchar(n), where n = 1 to 4000   | Text                   |
+------------------------------------+------------------------+
| nvarchar(MAX)                      | Memo                   |
+------------------------------------+------------------------+
