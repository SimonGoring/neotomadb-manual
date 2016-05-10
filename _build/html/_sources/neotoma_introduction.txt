Introduction
============

Neotoma is a public database containing fossil data from the Holocene, Pleistocene, and Pliocene, or approximately the last 5.3 million years.  The database stores associated physical data from fossil bearing deposits, for example sediment loss-on-ignition and geochemical data.  The database also stores data from modern samples that are used to interpret fossil data.

The initial development of Neotoma was funded by a grant from the U.S. National Science Foundation Geoinformatics program. This grant is collaborative between Penn State University [1]_ and the Illinois State Museum [2]_. It has five Principle Investigators, Russell W. Graham, Eric C. Grimm, Stephen T. Jackson, Allan C. Ashworth, and John W. (Jack) Williams. The database is served from the Center for Environmental Informatics at Penn State University.

Initially, data are being merged from four existing databases: the Global Pollen Database, FAUNMAP (a database of mammalian fauna), the North American Plant Macrofossil Database, and a fossil beetle database assembled by Allan Ashworth. The design of this database is such that many other kinds of fossil data can easily be incorporated in the future, for example, the addition of ostracode, diatom, chironmid, and freshwater mussel datasets.

The existing databases were developed in the 1990’s and have not been updated structurally since. New data have been added, but the structures of these databases have not changed, despite significant advances in database and internet technology. Although structurally different, these databases contain similar kinds of data, and merging them was quite practical. The rationale for this merging was twofold: (1) to facilitate analyses of past biotic communities at the ecosystem level and (2) to reduce the overhead in maintaining and distributing several independent databases..

The new Neotoma database was initially designed by E. C. Grimm and implemented in Microsoft® Access®. This database will be ported to a higher end RDBMS for Internet distribution, but it will continue to be distributed as a standalone Access database for researchers who need access to the entire database.

Whence Neotoma
--------------

In the original NSF proposal, this database was called a “Late Neogene Terrestrial Ecosystem Database.” At the time this proposal was written, the Neogene Period included the Miocene, Pliocene, Pleistocene, and Holocene epochs. However, a proposal before the International Commission on Stratigraphy would elevate the Quaternary to a System or Period following the Neogene and terminate the Neogene at the end of Pliocene.

Because this proposal renders the Neogene description of this database obsolete, a new name was sought. Numerous names and companion acronyms were considered, but none engendered enthusiastic support. B. Brandon Curry proposed the name Neotoma, and this name struck a fancy. *Neotoma* is the genus for the packrat. Packrats are prodigious collectors of anything in their territory, and moreover they are collectors of fossil data. They collect plant macrofossils and bones, and pollen is preserved in their amberat—hardened, dried urine, which impregnates their middens and preserves them for millennia.

Rationale
---------

Paleobiological data from the recent geological past have been
invaluable for understanding ecological dynamics at timescales
inaccessible to direct observation, including ecosystem evolution,
contemporary patterns of biodiversity, principles of ecosystem
organization, particularly the individualistic response of species to
environmental gradients, and the biotic response to climatic change,
both gradual and abrupt. Understanding the dynamics of ecological
systems requires ecological time series, but many ecological processes
operate too slowly to be amenable to experimentation or direct
observation. In addition to having ecological significance, fossil data
have tremendous importance for climatology and global change research.
Fossil floral and faunal data are crucial for climate-model verification
and are essential for elucidating climate-vegetation interactions that
may partly control climate.

Basic paleobiological research is site based, and paleobiologists have
devoted innumerable hours to identifying, counting, and cataloging
fossils from cores, sections, and excavations. These data are typically
published in papers describing single sites or small numbers of sites.
Often, the data are published graphically, as in a pollen diagram, and
the actual data reside on the investigator’s computer or in a file
cabinet. These basic data are similar to museum collections, costly to
replace, sometimes irreplaceable, and their value does not diminish with
time. Also similar to museum collections, the data require cataloging
and curation. Whereas physical specimens of large fossils, such as
animal bones, are typically accessioned into museums, microfossils, such
as pollen, are not accessioned, and the digital data are the primary
objects, and their loss is equivalent to losing valuable museum
specimens. The integrated database that we propose ensures safe,
long-term archiving of these data.

Large independent databases exist for fossil pollen, plant macrofossils,
and mammals: the Global Pollen Database (GPD), the North American Plant
Macrofossil Database (NAPMD), and FAUNMAP. In addition, a database of
fossil beetles (BEETLE) has been assembled, but it is not yet publicly
available. These databases have become essential cyberinfrastructure.
Nevertheless, they were developed as standalone databases in the early
1990’s with PC database software. GPD and NAPMD are in Paradox®; FAUNMAP
is in Access. Since initial database development, emphasis has been
placed on ingest of new and legacy data. However, database and Internet
technology have advanced greatly in the past 15 years, and the current
relational database software, ingest programs, data retrieval
algorithms, output formats, and analysis tools are outdated and minimal.
Moreover, the databases are not linked, so that integrated analyses are
difficult.

Although GPD, NAPMD, and FAUNMAP were developed independently, they have
much in common. The basic data of all three databases as well as BEETLE
are essentially lists of taxa from cores, excavations, or sections,
often with quantitative measures of abundance. The three databases
include similar metadata. The objective of Neotoma is to build a unified
data structure that will incorporate all of these databases. The
database will initially incorporate pollen, plant macrofossil, mammal,
and beetle data. However, the database designed facilitates the
incorporation of all kinds of fossil data.

Various teams of investigators have developed databases for
paleobiological data that have been project or discipline based,
including the four databases to be integrated in this project. However,
long-term maintenance and sustainability have been problematic because
of the need to secure continuous funding. Nevertheless, these databases
have become the established archives for their disciplines and, new data
are continuously contributed. However, because of funding hiatuses, long
spells may intervene between times of data contribution and their public
availability. For example, the plant macrofossil database has not
incorporated any new data since 1999. The number of different databases
and disciplines exacerbates the problem, because each database requires
a database manager. Consolidation of informatics technology helps
address this overhead issue. However, specialists are still essential
for management and supervision of data collection and quality control
for their disciplines or organismal groups.

The purposes of Neotoma are (1) to facilitate studies of ecosystem
development and response to climate change, (2) to provide the
historical context for understanding biodiversity dynamics, including
genetic diversity, (3) to provide the data for climate-model validation,
(4) to provide a safe, long-term, low-cost archive for a wide variety of
paleobiological data. Site-based studies are invaluable in their own
right, and they are the generators of new data. However, much is gained
by marshalling data from geographic arrays of sites for synoptic,
broad-scale ecosystem studies. In order to carry out such studies
efficiently, a queryable database is required. Thus, it is much more
than an archive; it is essential cyberinfrastructure for
paleoenvironmental research. The database facilitates integration,
synthesis, and understanding, and it promotes information sharing and
collaboration. The individual databases have been extensively used for
scientific research, with several hundred scientific publications
directly based upon data drawn from these databases. This project will
enhance those databases and will continue their public access. By
integrating these databases and by simplifying the contributor
interface, we can reduce the number of people necessary for
community-wide database maintenance, and thereby help ensure their
long-term sustainability and existence.

History of the Constituent Databases
``````````````````````````````````````````````````

Global Pollen Database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In an early effort, the Cooperative Holocene Mapping Project (COHMAP Members 1988, Wright et al. 1993) assembled pollen data in the 1970s and 1980s to test climate models. Although data-model comparison was the principal objective of the COHMAP project, the synoptic analyses of the pollen data, particularly maps showing the constantly shifting ranges of species in response to climate change, were revelatory and led to much ecological insight (e.g. Webb 1981, 1987, 1988).

The COHMAP pollen “database” consisted of a multiplicity of flat files with prescribed formats for data and chronologies. FORTRAN programs were written to read these files and to assemble data for particular analyses. Thompson Webb III managed the COHMAP pollen database at , but as the quantity of data increased, data management became increasingly cumbersome. Clearly, the data needed to be migrated to a relational database management system. Discussions with E. C. Grimm led to the initiation of the North American Pollen Database (NAPD) at the in 1990.

At the same time in , the International Geological Correlation Project IGCP 158 was conducting a major collaborative synthesis of paleoecological data, primarily of pollen, and the need for a pollen database became painfully obvious. In the forward to the book resulting from this project (Berglund et al. 1996), J.L. de Beaulieu describes the role that this project had in launching the European Pollen Database. A workshop to develop a European Pollen Database (EPD) was held in in 1989. North American representatives also attended, and the organizers of NAPD and EPD commenced a long-standing collaboration to develop
compatible databases. NAPD and EPD held several joint workshops and developed the same data structure. Nevertheless, the two databases were independently established, partly because Internet capabilities were not yet sufficient to easily manage a merged database. The pollen databases were developed in Paradox, which at the time was the most powerful RDBMS readily available for the PC platform. NAPD and EPD established two important protocols: 

	(1) the databases were relational and queryable
	(2) they were publicly available. 

As the success the NAPD-EPD partnership escalated, working groups initiated pollen databases for other regions, including the Latin American Pollen Database (LAPD) in 1994, the Pollen Database for and the Russian Far East (PDSRFE) in 1995, and the African Pollen Database (APD) in 1996. At its initial organizational workshop, LAPD opted to merge with NAPD, rather than develop a standalone database, and the Global Pollen Database was born. PDSRFE also followed this model. APD developed independently, but uses the exact table structure of GPD and EPD. Pollen database projects have also been initiated in other regions, and the GPD contains some of these data, including the Indo-Pacific Pollen Database and the Japanese Pollen Database.

The pollen databases contain data from the Holocene, Pleistocene, and Pliocene, although most data are from the last 20,000 years. Included are fossil data, mainly from cores and sections, and modern surface samples, which are essential for calibrating fossil data. NAPD data are not separate from the GPD, but rather NAPD is the North American subset of GPD. EPD has both public and restricted data—a concession that had to be made early on to assuage some contributors.

North American Plant Macrofossil Database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plant macrofossils include plant organs generally visible to the naked
eye, including seeds, fruits, leaves, needles, wood, bud scales, and
megaspores. Synoptic-scale mapping of plant macrofossils from modern
assemblages (Jackson et al. 1997) and fossil assemblages (Jackson et al.
1997, Jackson et al. 2000, Jackson and Booth 2002) have shown the
utility of plant macrofossils in providing spatially and taxonomically
precise reconstructions of past species ranges. Although plant
macrofossil records are spatially precise, synoptic networks of
high-quality sites can scale up to yield aggregate views of past
distributions (Jackson et al. 1997). In addition, macrofossils, with
their greater taxonomic resolution, augment the pollen data by providing
information on which species might have been present, and can resolve
issues of long-distance transport (Birks 2003).

The North American Plant Macrofossil Database (NAPMD) has been directed
by S.T. Jackson at the . Highest priority has been placed on data from
the last 30,000 years, although some earlier Pleistocene and late
Pliocene data are included. The database originated as a research
database for selected taxa from Late Quaternary sediments of eastern
North America (Jackson et al. 1997). In 1994, an effort was initiated
with NOAA funding to build on this foundation to develop a cooperative,
relational database comprising all of , a longer time span, and all
plant taxa.

The structure of NAPMD was adapted from the pollen database and is also
in Paradox. The principal modifications made to the pollen database
structure to accommodate plant macrofossils were those to cope with
different organs from the same species and to deal with the various
quantitative measures of abundance. The database also includes surface
samples, which are useful for interpretation of fossil data.

FAUNMAP
~~~~~~~

R.W. Graham, E.L. Lundelius, Jr., and a group of Regional Collaborators
organized a project to develop a database for late Quaternary faunal
data from the , which the U.S. NSF funded in 1990. This project had a
research agenda, and its seminal paper focused on the individualistic
behavior displayed by animal species (FAUNMAP Working Group 1996).

Two FAUNMAP databases exist, FAUNMAP I and FAUNMAP II. Both databases
were coordinated by R. W. Graham and E. L. Lundelius, Jr. and funded by
NSF. Both are relational databases for fossil mammal sites. The data
were extracted from peer-reviewed literature, selected theses and
dissertations, and selected contract reports for both paleontology and
archaeology. Unpublished collections were not included. Data were
originally captured in Paradox but were later migrated to Access.

FAUNMAP I contains data from sites in the lower 48 states that date
between 500 BP and ~40,000 BP. Funding for this project ended in 1994,
with the production of two major publications by the FAUNMAP Working
Group (1994, 1996), as well as numerous other publications by individual
members and by many others who accessed the database on-line. Graham and
Lundelius continued the FAUNMAP project, developing FAUNMAP II with
funding from NSF beginning in 1998. FAUNMAP II shares the same structure
as FAUNMAP I but expands the spatial coverage to include and and extends
the temporal coverage to the Pliocene (5 Ma). In addition, sites
published since 1994, when FAUNMAP I was completed, have been added for
the contiguous 48 states. In all, FAUNMAP I and II contain more than
5000 fossil-mammal sites with more than 600 mammal species for all of
North America north of Mexico that range in age from 0.5 ka to 5 Ma­.

The detailed structure of the FAUNMAP database is described in FAUNMAP
Working Group (1994). Sites identified by name and location were
subdivided into Analysis Units (AU’s), which varied from site to site
depending upon the definitions used in the original publications (e.g.,
stratigraphic horizons, cultural horizons, excavation levels,
biostratigraphic zones). All data (i.e. taxa identified and counts of
individual specimens) and metadata (sediment types, depositional
environments, facies, radiometric and other geochronological dates,
modifications of bone) were captured by AU. This structure allows for
the extraction of information at either the level of the site or the
smallest subdivision (AU). The AU permits fine-scale temporal resolution
and analysis. Similar to GPD and NAPMD, FAUNMAP contains archival and
research tables. Similar to the plant macrofossil database, FAUNMAP
contains a variety of quantitative measures of abundance, and presence
data are more commonly used for analysis.

BEETLE
~~~~~~

Many beetles have highly specific ecological and climatic requirements and are valuable indicators of past environments (Morgan et al. 1983, Ashworth 2001, 2004). They are one of the most diverse groups of organisms on earth, and of the insects, perhaps the most commonly preserved as fossils. Allan Ashworth has assembled a database of fossil beetles from . The data, which were recorded in Excel, contain 5523 individual records of 2567 taxa from 199 sites and 165 publications. Metadata include site name, latitude and longitude, lithology of sediment, absolute age, and geological age. The basic data are similar to plant and mammal databases—lists of taxa from sites. The metadata have not been recorded to the extent of the other databases, especially chronological data, but Ashworth has resolved the taxonomic issues and has assembled the publications, so that the additional metadata can be easily pulled together.

Who Will Use Neotoma?
---------------------

The existing databases have been used widely for a variety of studies. Because the databases have been available on-line, precise determination of how many publications have made use of them is difficult. In addition, the databases are widely used for instructional purposes. Below are examples of the kinds of people who have used these databases and who we expect will find the new, integrated database even more useful.

	-  **Paleoecologists** seeking to place a new record into a regional/continental/global context (e.g., Bell and Mead 1998, Czaplewski et al. 1999, Bell and Barnosky 2000, Newby et al. 2000, Futyma and Miller 2001, Gavin et al. 2001, Czaplewski et al. 2002, Schauffler and Jacobson 2002, Camill et al. 2003, Rosenberg et al. 2003, Willard et al. 2003, Pasenko and Schubert 2004, and many others).

	- **Synoptic paleoecologists** interested in mapping regional to sub-continental to global patterns of vegetation change (e.g., Jackson et al. 1997, Williams et al. 1998, Jackson et al. 2000, Prentice et al. 2000, Thompson and Anderson 2000, Williams et al. 2000, Williams et al. 2001, Williams 2003, Webb et al. 2004, Williams et al. 2004, Asselin and Payette 2005).

	- **Synoptic paleoclimatologists** building benchmark paleoclimatic reconstructions for GCM evaluation (e.g., Bartlein et al. 1998, Farrera et al. 1999, Guiot et al. 1999, Kohfeld and Harrison 2000, CAPE Project Members 2001, Kageyama et al. 2001, Kaplan et al. 2003).

	- **Paleontologists** trying to understand the timing, patterns, and causes of extinction events (e.g., Jackson and Weng 1999, Graham 2001, Barnosky et al. 2004, Martínez-Meyer et al. 2004, Wroe et al. 2004).

	- **Evolutionary biologists** mapping the genetic legacies of Quaternary climatic variations (e.g., Petit et al. 1997, Fedorov 1999, Tremblay and Schoen 1999, Hewitt 2000, Comps et al. 2001, Good and Sullivan 2001, Petit et al. 2002, Kropf et al. 2003, Lessa et al. 2003, Petit et al. 2003, Hewitt 2004, Lascoux et al. 2004, Petit et al. 2004, Whorley et al. 2004, Runck and Cook 2005).

	- **Macroecologists** interested in temporal records of species turnover and biodiversity and historical controls on modern patterns of floristic diversity (e.g., Silvertown 1985, Qian and Ricklefs 2000, Brown et al. 2001, Haskell 2001).

	- **Archeologists** who are studying human subsistence patterns and interactions with their environment (e.g., Grayson 2001, Grayson and Meltzer 2002, Cannon and Meltzer 2004, Grayson in press).

	- **Natural resource managers** who need to know historical ranges and abundances of plants and animals for designing conservation and management plans (e.g., Graham and Graham 1994, Cole et al. 1998, Noss et al. 2000, Owen et al. 2000, Committee on Ungulate Management in Yellowstone National Park 2002, Burns et al. 2003)

	- **Scientists** trying to understand the potential response of plants, animals, biomes, ecosystems, and biodiversity to global warming (e.g., Bartlein et al. 1997, Davis et al. 2000, Barnosky et al. 2003, Burns et al. 2003, Kaplan et al. 2003, Schmitz et al. 2003, Jackson and Williams 2004, Martínez-Meyer et al. 2004)

	- **Teachers** who use the databases for teaching purposes and class exercises.

.. [1]
   Grant number 0622349

.. [2]
   Grant number 0622289
