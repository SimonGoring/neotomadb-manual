Taxonomy Related Tables
--------------------------------

.. _EcolGroups:

EcolGroups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Taxa are assigned to Sets of Ecological Groups. A taxon may be assigned
to more than one Set of Ecological Groups, representing different
schemes for organizing taxa.

+-------------------------+----------------+----------+------------------+
| **EcolGroups**                                                         |
+-------------------------+----------------+----------+------------------+
| TaxonID                 | Long Integer   | PK, FK   | Taxa             |
+-------------------------+----------------+----------+------------------+
| EcolSetID               | Long Integer   | PK, FK   | EcolSetTypes     |
+-------------------------+----------------+----------+------------------+
| EcolGroupID             | Text           | FK       | EcolGroupTypes   |
+-------------------------+----------------+----------+------------------+

**TaxonID (Primary Key, Foreign Key)** 
   Taxon identification number.  The field links to the :ref:`Taxa` table.

**EcolSetID (Primary Key, Foreign Key)** 
   Ecological Set identification number. Field links to the :ref:`EcolSetTypes` table.

**EcolGroupID (Foreign Key)**
   A four-letter Ecological Group identification code. Field links to the :ref:`EcolGroupTypes` table.

SQL Example
`````````````````````````````

The following query produces a list of Ecological Groups for vascular plants (VPL).

.. code-block:: sql
   :linenos:

   SELECT
      Taxa.TaxaGroupID,
      EcolGroups.EcolGroupID,
      EcolSetTypes.EcolSetName,
      EcolGroupTypes.EcolGroup
   FROM
      EcolSetTypes
   INNER JOIN (
      EcolGroupTypes
      INNER JOIN (
         Taxa
         INNER JOIN EcolGroups ON Taxa.TaxonID = EcolGroups.TaxonID
      ) ON EcolGroupTypes.EcolGroupID = EcolGroups.EcolGroupID
   ) ON EcolSetTypes.EcolSetID = EcolGroups.EcolSetID
   GROUP BY
      Taxa.TaxaGroupID,
      EcolGroups.EcolGroupID,
      EcolSetTypes.EcolSetName,
      EcolGroupTypes.EcolGroup
   HAVING
      (((Taxa.TaxaGroupID) = "VPL"));

Result:

+-------------------+-------------------+-------------------+-----------------------------------+
| **TaxaGroupID**   | **EcolGroupID**   | **EcolSetName**   | **EcolGroup**                     |
+-------------------+-------------------+-------------------+-----------------------------------+
| VPL               | ANAC              | Default plant     | Anachronic                        |
+-------------------+-------------------+-------------------+-----------------------------------+
| VPL               | AQVP              | Default plant     | Aquatic Vascular Plants           |
+-------------------+-------------------+-------------------+-----------------------------------+
| VPL               | TRSH              | Default plant     | Trees and Shrubs                  |
+-------------------+-------------------+-------------------+-----------------------------------+
| VPL               | UNID              | Default plant     | Unknown and Indeterminable        |
+-------------------+-------------------+-------------------+-----------------------------------+
| VPL               | UPHE              | Default plant     | Upland Herbs                      |
+-------------------+-------------------+-------------------+-----------------------------------+
| VPL               | VACR              | Default plant     | Terrestrial Vascular Cryptogams   |
+-------------------+-------------------+-------------------+-----------------------------------+

SQL Example
`````````````````````````````

This query lists all the taxa in the Ecological Group «Sirenia».

.. code-block:: sql
   :linenos:

   SELECT
      EcolGroupTypes.EcolGroup,
      Taxa.TaxonName
   FROM
      EcolGroupTypes
   INNER JOIN (
      Taxa
      INNER JOIN EcolGroups ON Taxa.TaxonID = EcolGroups.TaxonID
   ) ON EcolGroupTypes.EcolGroupID = EcolGroups.EcolGroupID
   WHERE
      (
         (
            (EcolGroupTypes.EcolGroup) = "Sirenia"
         )
      );

Result:

+-----------------+----------------------+
| **EcolGroup**   | **TaxonName**        |
+-----------------+----------------------+
| Sirenia         | Dugongidae           |
+-----------------+----------------------+
| Sirenia         | Hydrodamalis gigas   |
+-----------------+----------------------+
| Sirenia         | Sirenia              |
+-----------------+----------------------+
| Sirenia         | Trichechidae         |
+-----------------+----------------------+
| Sirenia         | Trichechus manatus   |
+-----------------+----------------------+
| Sirenia         | Hydrodamalis         |
+-----------------+----------------------+
| Sirenia         | Trichechus           |
+-----------------+----------------------+

.. _EcolGroupTypes:

EcolGroupTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Ecological Group Types. The table is referenced by the :ref:`EcolGroups` table.

+-----------------------------+--------+------+-----+
| **EcolGroupTypes**                                |
+-----------------------------+--------+------+-----+
| EcolGroupID                 | Text   | PK   |     |
+-----------------------------+--------+------+-----+
| EcolGroup                   | Text   |      |     |
+-----------------------------+--------+------+-----+

**EcolGroupID (Primary Key)** 
   An arbitrary Ecological Group identification number.

**EcolGroup**
   Ecological Group.

.. _EcolSetTypes:

EcolSetTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Ecological Set Types. The table is referenced by the :ref:`EcolGroups` table.

+---------------------------+----------------+------+-----+
| **EcolSetTypes**                                        |
+---------------------------+----------------+------+-----+
| EcolSetID                 | Long Integer   | PK   |     |
+---------------------------+----------------+------+-----+
| EcolSetName               | Text           |      |     |
+---------------------------+----------------+------+-----+

**EcolSetID (Primary Key)** 
   An arbitrary Ecological Set identification number.

**EcolSetName** The Ecological Set name.

.. _Synonyms:

Synonyms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table lists common synonyms for taxa in the :ref:`Taxa` table. No effort has been made to provide a complete taxonomic synonymy, but rather to list synonyms commonly used in recent literature.

+-----------------------+----------------+------+----------------+
| **Table: Synonyms**                                            |
+-----------------------+----------------+------+----------------+
| SynonymID             | Long Integer   | PK   |                |
+-----------------------+----------------+------+----------------+
| SynonymName           | Text           |      |                |
+-----------------------+----------------+------+----------------+
| TaxonID               | Long Integer   | FK   | Taxa           |
+-----------------------+----------------+------+----------------+
| PublicationID         | Long Integer   | FK   | Publications   |
+-----------------------+----------------+------+----------------+
| SynonymTypeID         | Long Integer   | FK   | SynonymTypes   |
+-----------------------+----------------+------+----------------+
| Notes                 | Memo           |      |                |
+-----------------------+----------------+------+----------------+

**SynonymID (Primary Key)** 
   An arbitrary synonym identification number.

**SynonymName** 
   Name of the synonym.

**TaxonID (Foreign Key)** 
   The accepted taxon name in Neotoma. This field links to :ref:`Taxa` table.

**PublicationID (Foreign Key)**
   Published authority for synonymy. Field links to :ref:`Publications` table.

**SynonymTypeID (Foreign Key)**
   Type of synonym. Field links to the `SynonymTypes` lookup table.

**Notes** 
   Free form notes or comments about the synonymy.

.. _SynonymTypes:

SynonymTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Synonym Types. Table is referenced by the :ref:`Synonyms` table.

+---------------------------+----------------+------+-----+
| **Table: SynonymTypes**                                 |
+---------------------------+----------------+------+-----+
| SynonymTypeID             | Long Integer   | PK   |     |
+---------------------------+----------------+------+-----+
| SynonymType               | Text           |      |     |
+---------------------------+----------------+------+-----+

**SynonymTypeID (Primary Key)** 
   An arbitrary Synonym Type identification number.

**SynonymType**
   Synonym type. Below are some examples:

   **nomenclatural, homotypic, or objective synonym**
      a synonym that unambiguously refers to the same taxon, particularly one with the same description or type specimen.  These synonyms are particularly common above the species level. For example, Gramineae = Poaceae, *Clethrionomys gapperi* = *Myodes gapperi*. The term «objective» is used in zoology, whereas «nomenclatural» or «homotypic» is used in botany.

   **taxonomic, heterotypic, or subjective synonym**
      a synonym typically based on a different type specimen, but which is now regarded as the same taxon as the senior synonym. For example, *Iva ciliata* = *Iva annua*. The term «subjective» is used in zoology, whereas «taxonomic» or «heterotypic» is used in botany.

   **genus merged into another genus**
      heterotypic or subjective synonym; a genus has been merged into another genus and has not been retained at a subgeneric rank. This synonymy may apply to either the generic or specific level, for example: *Petalostemon* = *Dalea*, *Petalostemon purpureus* = *Dalea purpurea*.

   **family merged into another family** 
      Heterotypic or subjective synonym; a family has been merged into another family and has not been retained at a subfamilial rank. For example, the Taxodiaceae has been merged with the Cupressaceae. This synonymy creates issues for data entry, because palynologically the Taxodiaceae *sensu stricto* is sometimes distinguishable from the Cupressaceae sensu stricto. If a pollen type was identified as «Cupressaceae/Taxodiaceae», then synonymizing to «Cupressaceae» results in no loss of information.  However, synonymizing «Taxodiaceae» to «Cupressaceae» potentially does. In this case, consultation with the original literature or knowledge of the local biogeography may point to a logical name change that will retain the precision of the original identification. For example, in the southeastern , «Taxodiaceae» can be changed to «\ *Taxodium*\ » or «\ *Taxodium*-type» in most situations. If «Cupressaceae» was also identified, then it should be changed to «Cupressaceae undiff.» or possibly «Juniperus-type» if other Cupressaceae such as Chamaecyperus are unlikely.

   **rank change: species reduced to subspecific rank**
      heterotypic or subjective synonym; a species has been reduced to a subspecies or variety of another species. These synonyms may be treated in two different ways, depending on the situation or protocols of the contributing data cooperative: (1) The taxon is reduced to the subspecific rank (e.g. *Alnus* *fruticosa* = *Alnus viridis* subsp. *fruticosa*, *Canis familiaris* = *Canis lupus familiaris*), either because the fossils can be assigned to the subspecies based on morphology, as is likely the case with the domestic dog, *Canis lupus familiaris*, or because the subspecies can be assigned confidently based on biogeography. (2) The taxon is changed to the new taxon and the subspecific rank is dropped because the fossil is not distinguishable at the subspecific level. For example, *Alnus rugosa* = *Alnus incana* subsp. *rugosa*, but may simply be changed to *Alnus incana* because the pollen of *A. incana* subsp. *rugosa* and *A. incana* subsp. *incana* are indistinguishable morphologically.

   **rank change: genus reduced to subgenus**
      heterotypic or subjective synonym; a genus has been reduced to subgeneric rank in another family. At the generic level, this synonymy is clear from the naming conventions, e.g. *Mictomys* = *Synaptomys (Mictomys)*; however, at the species level it is not, e.g. *Mictomys borealis* = *Synaptomys borealis*.

   **rank change: family reduced to subfamily**
      heterotypic or subjective synonym; a family has been reduced to subfamily rank in another family. By botanical convention the family name is retained, e.g. Pyrolaceae = Ericaceae subf. Monotropoideae; whereas by zoological convention it is not, e.g. Desmodontidae = Desmodontinae.

   **rank change: subspecific rank elevated to species**
      heterotypic or subjective synonym; a subspecies or variety has been raised to the species rank, e.g. *Ephedra fragilis* subsp. *campylopoda* = *Ephedra foeminea*.

   **rank change: subgeneric rank elevated to genus**
      heterotypic or subjective synonym; a subgenus or other subgeneric rank has been raised to the generic rank. At the subgeneric level, this synonymy is clear from the naming conventions, e.g. *Potamogeton* subg. *Coleogeton* = *Stuckenia*; however, at the species level it is not, e.g. *Potamogeton pectinatus* = *Stuckenia pectinata*.

   **rank change: subfamily elevated to family**
      heterotypic or subjective synonym; a subfamily has been raised to the family rank, e.g. Liliaceae subf. Amaryllidoideae = Amaryllidaceae, Pampatheriinae = Pampatheriidae.

   **rank elevated because of taxonomic uncertainty**
      because the precise taxonomic identification is uncertain, the rank has been raised to a level that includes the universe of possible taxa. A common cause of such uncertainty is taxonomic splitting subsequent to the original identification, in which case the originally identified taxon is now a much smaller group. For example, the genus *Psoralea* has been divided into several genera; the genus *Psoralea* still exists, but now includes a much smaller number of species. Consequently, in the database *Psoralea* has been synonymized with Fabaceae tribe Psoraleeae, which includes the former *Psoralea* sensu lato. A zoological example is *Mustela* sp. The genus *Mustela* formerly included the minks, which have now been separated into the genus *Neovison*. Consequently, *Mustela* sp. = *Mustela/Neovison* sp.

   **globally monospecific genus**
      Although identified at the genus level, specimens assigned to this genus can be further assigned to the species level because the genus is monospecific.

   **globally monogeneric family**
      although identified at the family level, specimens assigned to this family can be further assigned to the genus level because the family is monogeneric.

SQL Example
`````````````````````````````

This query provides the preferred synonym in the database for «Bison
alleni» along with the published authority for the synonymy and the
notes in the database on the rationale for the synonymy. The notes
indicate some potential problems with this synonymy.

.. code-block:: sql
   :linenos:

   SELECT Synonyms.SynonymName, Taxa.TaxonName, Publications.Citation,
   Synonyms.Notes

   FROM Publications INNER JOIN (Taxa INNER JOIN Synonyms ON Taxa.TaxonID =
   Synonyms.TaxonID) ON Publications.PublicationID = Synonyms.PublicationID

   WHERE (((Synonyms.SynonymName)="Bison alleni"));

Result:

+-------------------+-------------------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **SynonymName**   | **TaxonName**     | **Citation**                                                                                  | **Notes**                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Bison alleni      | Bison latifrons   | McDonald, J. N. 1981. North American bison: their classification and evolution. of Press, .   | According to MacDonald (1981, p. 73), the holotype of B. alleni is clearly consistent with B. latifrons; however, he notes that many specimens identified as B. alleni have been confused with B. alaskensis (=priscus), a situation which may relegate B. alleni to a nomen dubium. (1974) synonymized B. alleni with B. priscus. He also considered B. latifrons and B. alaskensis to be subspecies of B. priscus. [ECG, 3 Aug 2007].   |
+-------------------+-------------------+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _Taxa:

Taxa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table lists all taxa in the database. Most taxa are biological taxa; however, some are biometric measures and some are physical parameters.

+-------------------+----------------+------+------------------+
| **Table: Taxa**                                              |
+-------------------+----------------+------+------------------+
| TaxonID           | Long Integer   | PK   |                  |
+-------------------+----------------+------+------------------+
| TaxonCode         | Text           |      |                  |
+-------------------+----------------+------+------------------+
| TaxonName         | Text           |      |                  |
+-------------------+----------------+------+------------------+
| Author            | Text           |      |                  |
+-------------------+----------------+------+------------------+
| HigherTaxonID     | Long Integer   |      | Taxa:TaxonID     |
+-------------------+----------------+------+------------------+
| Extinct           | Yes/No         |      |                  |
+-------------------+----------------+------+------------------+
| TaxaGroupID       | Text           | FK   | TaxaGroupTypes   |
+-------------------+----------------+------+------------------+
| PublicationID     | Long Integer   | FK   | Publications     |
+-------------------+----------------+------+------------------+
| Notes             | Memo           |      |                  |
+-------------------+----------------+------+------------------+

**TaxonID (Primary Key)** 
   An arbitrary Taxon identification number.

**TaxonCode** 
   A code for the Taxon. These codes are useful for other software or output for which the complete name is too long. Because of the very large number of taxa, codes can be duplicated for different Taxa Groups. In general, these various Taxa Groups are analyzed separately, and no duplication will occur within a dataset. However, if Taxa Groups are combined, unique codes can be generated by prefixing with the TaxaGroupID, For example, VPL:Cle (*Clethra*) and MAM:Cle (*Clethrionomys*)

   A set of conventions has been established for codes. In some cases conventions differ depending on whether the organism is covered by rules of botanical nomenclature (BN) or zoological nomenclature (ZN).

   **Genus**
      Three-letter code, first letter capitalized, generally the first three unless already used: **Ace** (*Acer*) or **Cle** (*Clethrionomys*).

   **Subgenus**
      The genus code plus a two-letter subgenus code, first letter capitalized, separated by a period: **Pin.Pi** (*Pinus* subg. *Pinus*) or **Syn.Mi** (*Synaptomys (Mictomys)*).

   **Species**
      The genus code plus a two-letter, lower-case species code, separated by a period: **Ace.sa** (*Acer saccharum*), **Ace.sc** (*Acer saccharinum*), or **Cle.ga** (*Clethrionomys gapperi*)

   **Subspecies or variety**
      The species code a two-letter, lower-case subspecies code, separated by a period: **Aln.vi.si** (*Alnus viridis* subsp. *sinuata*), or **Bis.bi.an** (*Bison bison antiquus*)

   **Family**
      Six-letter code, first letter capitalized, consisting of three letters followed by «eae» (BN) or «dae» (ZN): **Roseae** (Rosaceae), or **Bovdae** (Bovidae)

   **Subfamily or tribe**
      (BN) Family code plus two-letter subfamily code, first letter capitalized, separated by a period. (ZN) Six-letter code, first letter capitalized, consisting of three letters followed by «nae»: **Asteae.As** (Asteraceae subf. Asteroideae),  **Asteae.Cy** (Asteraceae tribe Cynarea), or **Arvnae** Arvicolinae.

   **Order**
      (BN) Six-letter code, first letter capitalized, consisting of three letters followed by «les». (ZN) Six-letter code, first letter capitalized, consisting of three letters, followed by the last three letters of the order name, unless the order name is ≤6 letters long, in which case the code = the order name. Zoological orders do not have a common ending:  **Ercles** (Ericales), **Artyla** (Artiodactyla), or **Rodtia** (Rodentia).

   **Taxonomic levels higher than order**
      Six-letter code, first letter capitalized, consisting of three letters, followed by the last three letters of the order name, unless the order name is ≤6 letters long, in which case the code = the order name: **Magida** (Magnoliopsida), **Magyta** (Magnoliophyta), or **Mamlia** (Mammalia).

   **Types**
      The conventional taxon code followed by «-type»: **Aln.in-t** (*Alnus incana*-type), **Amb-t** (*Ambrosia*-type)

   **cf.**
      «cf. » is placed in the proper position: **Odc.cf.he** (*Odocoileus* cf. *O. hemionus*), **cf.Odc.he** (cf. *Odocoileus hemionus*), or **cf.Odc** (cf. *Odocoileus*).

   **aff.**
      «aff. » is abbreviated to «af. »: **af.Can.di** (aff. *Canis dirus*)

   **?**
      «?» is placed in the proper position. **?Pro.lo** (?*Procyon lotor*)

   **Alternative names**
      A slash is placed between the conventional abbreviations for the alternative taxa: **Ost/Cpn** (*Ostrya/Carpinus*), or **Mstdae/Mepdae** (Mustelidae/Mephitidae)

   **Undifferentiated taxa**
      (BN) «.ud» is added to the code. (ZN) «.sp » is added to the code: **Aln.ud** (*Alnus* undiff.), **Roseae.ud** (Rosaceae undiff.), **Mms.sp** (*Mammuthus* sp.), or **Taydae.sp** (*Tayassuidae* sp.).

   **Parenthetic modifiers**
      The conventional taxon code with an appropriate abbreviation for the modifier separated by periods. Multiple modifiers also separated by periods. Abbreviations for pollen morphological modifiers follow Iversen and Troels-Smith (1950): **Raneae.C3** (Ranunculaceae (tricolpate)), **Raneae.Cperi** (Ranunculaceae (pericolpate)), **Pineae.ves.ud** (Pinaceae (vesiculate) undiff.), **Myteae.Csyn.psi** (Myrtaceae (syncolpate, psilate)), **Bet.>20µ** (*Betula* (>20 µm))

   **Non-biological taxa**
      Use appropriate abbreviations: **bulk.dens** (Bulk density), **LOI** Loss-on-ignition, **Bet.pol.diam** (*Betula* mean pollen-grain diameter).

**TaxonName** 
   Name of the taxon. Most TaxonNames are biological taxa; however, some are biometric measures and some are physical parameters. In addition, some biological taxa may have parenthetic non-Latin modifers, e.g. «\ *Betula* (>20 µm)» for *Betula* pollen grains >20 µm in diameter. In general, the names used in Neotoma are those used by the original investigator. In particular, identifications are not changed, although Dataset notes can be added to the database regarding particular identifications. However, some corrections and synonymizations are made.

   These include:

   *  Misspellings are corrected.

   *  Nomenclatural, homotypic, or objective synonyms may be applied.  Because these synonyms unambiguously refer to the same taxon, no change in identification is implied. For example, the old family name for the grasses «Gramineae» is changed to «Poaceae».

   *  Taxonomic, heterotypic, or subjective synonyms may be applied if the change does not effectively assign the specimen to a different taxon. Although two names may have been based on different type specimens, if further research has shown that these are in fact the same taxon, the name is changed to the accepted name. These synonymizations should not cause confusion. However, uncritical synonymization, although taxonomically correct, can result in loss of information, and should be avoided. For example, although a number of recent studies have shown that the Taxodiaceae should be merged with the Cupressaceae, simply synonymizing Taxodiaceae with Cupressaceae may expand the universe of taxa beyond that implied by the original investigator. For example, a palynologist in the southeastern United States may have used «Taxodiaceae» to imply «\ *Taxodium*\ », which is the only genus of the family that has occurred in the region since the Pliocene, but used the the family name because, palynologically, *Taxodiuim* cannot be differentiated from other Taxodiaceae. However, well preserved *Taxodium* pollen grains can be differentiated from the other Cupressaceous genera in the regin, *Juniperus* and *Chamaecyperus*. Thus, the appropriate synonymization for «Taxodiaceae» in this region would be «\ *Taxodium*\ » or «\ *Taxodium*-type», which would retain the original taxonomic precision. On the other hand, the old «TCT» shorthand for «Taxodiaceae/Cupressaceae/Taxaceae» now becomes «Cupressaceae/Taxaceae» with no loss of information.

   *  For alternative taxonomic desginations, the order may be changed. For example, «\ *Ostrya/Carpinus*\ » would be substituted for «\ *Carpinus/Ostrya*\ ».

   The database has a number of conventions for uncertainty in identification. The uncertainty is included in the taxon name. Thus, «\ *Acer* *pensylvanicum*\ » and «\ *Acer* cf. *A. pensylvanicum*\ » are two different taxa.

   **cf.**
      Latin *confer*, which means compare. In taxonomy «cf. » generally means that the specimen compares well to or is similar to the type referred, but the identification is uncertain. Uncertainty may arise for a number of reasons. The specimen may not be well preserved. It may be nondescript. There may be other similar taxa that can not be ruled out. The analyst may not have access to a complete reference or comparative collection for the group, so other related taxa cannot be excluded with certainty.

    For uncertainty at the species level, the convention in Neotoma is, for example, «\ *Odocoileus* cf. *O. hemionus*\ », not
    «\ *Odocoileus* cf. *hemionus*\ ». Placement of «cf. » is important, because it indicates the taxonomic level of uncertaintly. For example, «\ *Odocoileus* cf. *O. hemionus*\ » implies that the identification of *Odocoileus* is secure, but that the species identification is not; whereas «cf. *Odocoileus hemionus*\ » implies that not even the genus identification is certain. A further implication in the latter example is that if the genus identification is correct, then the the specimen must also be that species, perhaps because of biogeographic considerations. Although commonly overlooked, it is also important to indicate the proper level of uncertainly in family-genus identifications. For example, «Brassicaceae cf. *Brassica*\ » implies that assignment to the Brassicaceae is secure; whereas simply «cf. *Brassica*\ » does not indicate that even the family identification is certain.

    In FAUNMAP, the uncertainty is recorded in a separate field from the taxon name, and for species it is not discernable whether the uncertainty is at the genus or species level. When data were imported from FAUNMAP, the «cf. » uncertainty was conservatively assigned to the genus level. Thus, if «\ *Bison bison*\ » was indicated to have «cf. » uncertainty, this record was imported as «cf. *Bison bison*\ » rather than «\ *Bison* cf. *B. bison*\ ». However, in many cases, the uncertainty in the original data was probably at the species level.

   **aff.**
      «aff. » Latin *affinis*, which means having affinity with, but distinct from, the referred taxon. This desgination is often applied to a taxon thought to be undescribed. Thus, «aff. *Canis dirus*\ » implies an affinity to *Canus dirus*, but the specimen is likely from another species.

   **?**
      «?» is used to designate a questionable identification. It may indicate even less certainty than «cf. ». An example is «?Procyon lotor».

   **Types**
      Many pollen taxa are designated as types, e.g. «\ *Ambrosia*-type». A type denotes a morphological type that is consistent with the referred taxon, but also includes other taxa that are palynologically indistinguishable. For example, «\ *Ambrosia*-type» includes *Ambrosia* and *Iva* *axillaris*. The referred name commonly indicates the sporophyte taxon thought to be the most probable source of the pollen. An analyst may choose a «-type» designation referring to a lower taxonomic rank rather than an inclusive higher taxonomic rank because the referred taxon is thought to be the source taxon with very high probability. For example, in eastern , *Pinus strobus* is the only species of *Pinus* subg. *Strobus*, although several other species of this subgenus occur in western . Consequently, some analysts refer to «\ *Pinus strobus*-type» rather than «\ *Pinus* subg. *Strobus*\ ». Ideally, a type would comprise a well defined universe of taxa, but in practice types are often vaguely defined. For example, in eastern «\ *Populus balsamifera*-type» includes a large proportion of *P. balsamifera* and probably smaller proportions of *P. tremuloides, P. grandidentata,* and *P. deltoides*; whereas «\ *Populus tremuloides*-type» includes larger proportions of these latter three species and a smaller proportion of *P. balsamifera*. However, these proportions are ill-defined.

   **Alternative taxonomic designations**
      In some cases, fossil specimens of two taxa are indistinguishable and are more-or-less equally likely. The names can then be separated by a slash, e.g. «\ *Ostrya/Carpinus*\ », «Mustelidae/Mephitidae». If one taxon is more likely, the analyst may choose to use a «-type» designation instead, e.g. «\ *Ostrya*-type». Although the order of alternative names may be changed by the database, a «-type» designation is not substituted for alternatives. However, the use of more two alternatives is discouraged. In cases in which taxonomic revisions have reduced the number of speices within a taxon, the original universe of species may be retained with the slash designation. An example is «Mustelidae», which in older literature included the skunks, which have now been placed in their own family the Mephitidae; thus «Mustelidae/Mephitidae» retains the original set of possible taxa.

   **Undifferentiated taxa**
      Lower taxonomic ranks may not be differentiated. The convention among palynologists is to specify these by the suffix «undiff. ». Thus, «Rosaceae undiff.» designates undifferentiated Rosaceae. However, palynologists have inconsistently applied the «undiff.» appellation, and the pollen databases established a convention that taxa must be mutually exclusive within a dataset. Thus, if a higher-rank taxon is present in a dataset, the «undiff.» suffix is applied only if lower-rank taxa are also present. For example, if «\ *Spiraea*\ » occurs in a dataset, «Rosaceae» would be changed to «Rosaceae undiff.», because *Spiraea* is a genus in the family Rosaceae. On the other hand, if «Rosaceae undiff.» occurs with no other Rosaceae, then «Rosaceae undiff.» is changed to simply «Rosaceae»; it is implicit that the family is not differentiated.

   Faunal analysts customarily use the appellation «sp.» to designate undifferentiated taxa. Thus, «\ *Microtus* sp.» indicates undifferentiated *Microtus*. In addition, faunal analysts regularly use the «sp.» designation even when no lower-rank taxa are identified. The «sp.» appellation is most frequently used with genera. The principle of taxonomic mutual exclusivity has not been applied to fauanl datasets, although it should probably be considered.

**Author**
   Author(s) of the name. Neither the pollen database nor FAUNMAP stored author names, so these do not currently exist in Neotoma for plant and mammal names. These databases follow standard taxonomic references (e.g. *Flora of North America*, *Flora Europaea*, Wilson and Reeder's *Mammal Species of the World*), which, of course, do cite the original authors. However, for beetles, the standard practice is to cite original author names; therefore, this field was added to Neotoma.

**HigherTaxonID**
   The TaxonID of the next higher taxonomic rank, for example, the HigherTaxonID for «\ *Bison*\ » is the TaxonID for «Bovidae». For «cf.'s» and «-types», the next higher rank may be much higher owing to the uncertainty of the identification; the HigherTaxonID for «cf. *Bison bison*\ » is the TaxonId for «Mammalia». The HigherTaxonID implements the taxonomic hierarchy in Neotoma.

**Extinct**
   Boolean (True/False) variable. The value is True if the taxon is extinct, False if extant.

**TaxaGroupID (Foreign Key)** 
   The TaxaGroupID facilitates rapid extraction of taxa groups that are typically grouped together for analysis. Some of these groups contain taxa in different classes or phyla. For example, vascular plants include the Spermatophyta and Pteridophyta; the herps include Reptilia and Amphibia; the testate amoebae include taxa from different phyla. Field links to the :ref:`TaxaGroupTypes` table.

**PublicationID (Foreign Key)** 
   Publication identification number. Field links to the :ref:`Publications` table.

**Notes** 
   Free form notes or comments about the Taxon.

.. _TaxaGroupTypes:

TaxaGroupTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table for Taxa Group Types. This table is referenced by the
:ref:`Taxa` table.

+-----------------------------+--------+------+-----+
| **TaxaGroupTypes**                                |
+-----------------------------+--------+------+-----+
| TaxaGroupID                 | Text   | PK   |     |
+-----------------------------+--------+------+-----+
| TaxaGroup                   | Text   |      |     |
+-----------------------------+--------+------+-----+

**TaxaGroupID (Primary Key)**
   A three-letter Taxa Group code.

**TaxaGroup** 
   The taxa group. Below are some examples:

   +---------------+---------------------------+
   | TaxaGroupID   | TaxaGroup                 |
   +---------------+---------------------------+
   | AVE           | Birds                     |
   +---------------+---------------------------+
   | BIM           | Biometric variables       |
   +---------------+---------------------------+
   | BRY           | Bryophytes                |
   +---------------+---------------------------+
   | BTL           | Beetles                   |
   +---------------+---------------------------+
   | ...           | ...                       |
   +---------------+---------------------------+
   | FSH           | Fish                      |
   +---------------+---------------------------+

.. _Variables:

Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table lists Variables, which always consist of a Taxon and Units of measurement. Variables can also have Elements, Contexts, and Modifications. Thus, the same taxon with different measurement units (e.g. present/absent, NISP, MNI) are different Variables.

+--------------------------+----------------+------+-------------------------+
| **Table: Variables**                                                       |
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

**VariableID (Primary Key)** 
   An arbitrary Variable identification number.

**TaxonID (Foreign Key)** 
   Taxon identification number. Field links to the :ref:`Taxa` table.

**VariableElementID (Foreign Key)** 
   Variable Element identification number. Field links to the :ref:`VariableElements` lookup table.

**VariableUnitsID (Foreign Key)** 
   Variable Units identification number. Field links to the :ref:`VariableUnits` lookup table.

**VariableContextID (Foreign Key)**
   Variable Context identification number. Field links to the :ref:`VariableContexts` lookup table.

**VarialbeModificationID (Foreign Key)** 
   Variable Modification identification number. Field links to the :ref:`VariableModifications` lookup table.

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

.. _VariableContexts:

VariableContexts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Variable Contexts lookup table. Table is referenced by the
:ref:`Variables` table.

+-------------------------------+----------------+------+-----+
| **Table: VariableContexts**                                 |
+-------------------------------+----------------+------+-----+
| VariableContextID             | Long Integer   | PK   |     |
+-------------------------------+----------------+------+-----+
| VariableContext               | Text           |      |     |
+-------------------------------+----------------+------+-----+

**VariableContextID (Primary Key)** 
   An arbitrary Variable Context identification number.

**VariableContext** 
   Depositional context. Examples are:

   **anachronic**
      A specimen older than the primary deposit, e.g. a Paleozoic spore in a Holocene deposit. The specimen may be redeposited from the catchment, or may be derived from long distance, e.g. Tertiary pollen grains in Quaternary sediments with no local Tertiary source. A Pleistocene specimen in a Holocene archaeological deposit, possibly resulting from aboriginal fossil collecting, would also be anachronic.

   **intrusive**
      A specimen, generally younger than the primary deposit, *e.g*. a domestic pig in an otherwise Pleistocene deposit.

   **redeposited**
      A specimen older than the primary deposit and assumed to have been redeposited from a local source by natural causes.

   **articulated**
      An articulated skeleton

   **clump**
      A clump, esp. of pollen grains

.. _VariableElements:

VariableElements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Variable Elements. Table is referenced by the :ref:`Variables` table.

+-------------------------------+----------------+------+-----+
| **Table: VariableElements**                                 |
+-------------------------------+----------------+------+-----+
| VariableElementID             | Long Integer   | PK   |     |
+-------------------------------+----------------+------+-----+
| VariableElement               | Text           |      |     |
+-------------------------------+----------------+------+-----+

**VariableElementID (Primary Key)** An arbitrary Variable Element identification number.

**VariableElement** 
   The element, part, or organ of the taxon identified. For plants, these include pollen, spores, and various macrofossil organs, such as «seed», «twig», «cone», and «cone bract». Thus, *Betula* pollen and *Betula* seeds are two different Variables. For mammals, Elements include the bone or tooth identified, e.g. «tibia». «tibia, distal, left», «M2, lower, left». Some more unusual elements are *Neotoma* fecal pellets and *Erethizon dorsata* quills. If no element is indicated for mammalian fauna, then the genric element «bone/tooth» is assigned. Elements were not assigned in FAUNMAP, so all Variables ingested from FAUNMAP were assigned the «bone/tooth» element. Physical Variables may also have elements. For example, the Loss-on-ignition Variables have «Loss-on-ignition» as a Taxon, and temperature of analysis as an element, e.g. «500°C», «900°C». Charcoal Variables have the size fragments as elements, e.g. «75-100 µm», «100-125 µm».

.. _VariableModifications:

VariableModifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Variable Modifications. Table is referenced by the
:ref:`Variables` table.

+------------------------------------+----------------+------+-----+
| **Table: VariableModifications**                                 |
+------------------------------------+----------------+------+-----+
| VariableModificationID             | Long Integer   | PK   |     |
+------------------------------------+----------------+------+-----+
| VariableModification               | Text           |      |     |
+------------------------------------+----------------+------+-----+

**VariableModificationID (Primary Key)** 
   An arbitrary Variable Modification identification number.

**VariableModification** 
   Modification to a specimen. Examples of modifications to bones include «carnivore gnawed», «rodent gnawed», «burned», «human butchering». Modifications to pollen grains include various preservation states, e.g. «1/2 grains», «degraded», «corroded», «broken». Most Variables do not have a modification assigned.

.. _VariableUnits:

VariableUnits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table of Variable Units. Table is referenced by the
:ref:`Variables` table.

+----------------------------+----------------+------+-----+
| **Table: VariableUnits**   |                             |
+----------------------------+----------------+------+-----+
| VariableUnitsID            | Long Integer   | PK   |     |
+----------------------------+----------------+------+-----+
| VariableUnit               | Text           |      |     |
+----------------------------+----------------+------+-----+

**VariableUnitsID (Primary Key)** 
   An arbitrary Variable Units identification number.

**VariableUnit** 
   The units of measurement. For fauna, these are «present/absent», «NISP» (Number of Individual Specimens), and «MNI» (Minimum Number of Individals). For pollen, these are «NISP» (pollen counts) and «percent». Units for plant macrofossils include «present/abesnt» and «NISP», as well as a number of quantitative concentration measurements and semi-quantitative abundance measurements such as «1-5 scale». Examples of charcoal measurement units are «fragments/ml» and «µm^2/ml».

.. _RepositoryInstitutions:

RepositoryInstitutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A lookup table of institutions that are repositories for fossil specimens. Table is referenced by the :ref:`RepositorySpecimens` table.

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

**RepositoryID (PrimaryKey)** 
   An arbitrary Repository identification number. Repositories include museums, university departments, and various governmental agencies.

**Acronym** 
   A unique acronym for the repository. Many repositories have well-established acronyms (e.g. AMNH = of Natural History); however, there is no official list. Various acronyms have been used for some institutions, and in some cases the same acronym has been used for different institutions. Consequently, the database acronym may differ from the acronym used in some publications. For example, «CMNH» has been used for the Carnegie Museum of Natural History, the Cleveland Museum of Natural History, and the Cincinnati Museum of Natural History. In Neotoma, two of these institutions were assigned different acronyms, ones that have been used for them in other publications: CM – Carnegie Museum of Natural History, CLM – Cleveland Museum of Natural History.

**Repository** 
   The full name of the repository.

**Notes**
   Free form notes or comments about the repository, especially notes about name changes, closures, and specimen transfers. In some cases, it is known that the specimens were transferred, but their current disposition may be uncertain.

.. _RepositorySpecimens:

RepositorySpecimens
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table lists the repositories in which fossil specimens have been accessioned or reposited. The inventory in Neotoma is by Dataset, which is the collection of specimens from a Collection Unit. Occasionally, specimens from a single Collection Unit have been reposited at different institutions, in which case multiple records for that Dataset occur in the table.

+----------------------------------+----------------+----------+---------------------------+
| **Table: RepositorySpecimens**                                                           |
+----------------------------------+----------------+----------+---------------------------+
| DatasetID                        | Long Integer   | PK, FK   |  Datasets                 |
+----------------------------------+----------------+----------+---------------------------+
| RepositoryID                     | Long Integer   | PK, FK   |  RepositoryInstitutions   |
+----------------------------------+----------------+----------+---------------------------+
| Notes                            | Memo           |          |                           |
+----------------------------------+----------------+----------+---------------------------+

**DatasetID (Primary Key, Foreign Key)** 
   Dataset identification number. Field links to the :ref:`Datasets` table.

**RepositoryID (Primary Key, Foreign Key)** 
   Repository identification number. Field links to the :ref:`RepositoryInstitutions` lookup table.

**Notes** 
   Free form notes or comments about the disposition of the specimens.

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

.. _SpecimenDates:

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

**SpecimenDateID (Primary Key)** 
   An arbitrary specicimen date ID.

**GeochronID (Foreign Key)** 
   Geochronologic identification number. Field links to the :ref:`Geochronology` table.

**TaxonID (Foreign Key)** 
   Accepted name in Neotoma. Field links to :ref:`Taxa` table.

**VariableElementID (Foreign Key)**
   Variable Element identification number. Field links to the :ref:`VariableElements` lookup table.

**SampleID (Primary Key, Foreign Key)**
   Sample ID number. Field links to the :ref:`Samples` table.

**Notes**
   Free form notes or comments about dated specimen.

