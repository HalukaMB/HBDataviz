Dies ist eine Beschreibung des Datensatzes "202310_GebieteMitAusbaudefizit.gpkg"

Beschreibung: Gebiete mit Ausbaudefizit nach § 84 Abs. 1 TKG | Als Gebiete mit Ausbaudefizit im Mobilfunkbereich sind Flächen definiert, in denen aktuell sowie in den nächsten 12 Monaten voraussichtlich keine Versorgung und keine Ausbauplanung mit einem Mobilfunknetz mit sehr hoher Kapazität oder einer Mobilfunktechnologie der vierten (4G) oder fünften (5G) Generation vorliegt.

Zeitlicher Bezug:
	Datenstand: Oktober 2023
	Aktualisierung: halbjährlich 

Format: OGC GeoPackage

Datenstruktur: 1 Polygon-Feature-Class je Bundesland der Bundesrepublik Deutschland sowie 1 Polygon-Feature-Class der gesamten Bundesrepublik Deutschland

Attribute:
	id [Integer] - Feature-Identifikator
	geom [Geometrie] - Geometrie-Attribut
	Nr [Integer] - Bundeslandübergreifende Kennziffer der Gebiete mit Ausbaudefizit
	betroffene_Laender [String] - Liste der Bundeslandschlüssel der betroffenen Bundesländer (durch Leerzeichen getrennt)
	betroffene_Kreise [String] - Liste der Kreisschlüssel der betroffenen Kreise (durch Leerzeichen getrennt)
	betroffene_Gemeinden [String] - Liste der Gemeindeschlüssel (AGS) der betroffenen Gemeinden (durch Leerzeichen getrennt)
	gebietsflaeche_qkm [Double] - Gebietsfläche des Gebietes mit Ausbaudefizit in Quadratkilometer

Räumlicher Bezug:
	Projiziertes Koordinatensystem: ETRS_1989_UTM_Zone_32N
	Geographisches Koordinatensystem: GCS_ETRS_1989
	EPSG: 25832
	
Datengrundlage: 
	Daten der Mobilfunknetzbetreiber, die nach §§ 80, 81 TKG  erhoben werden.
	Grunddaten: Geographische Gitter für Deutschland in UTM-Projektion - © GeoBasis-DE / BKG (2021) | Verwaltungsgebiete 1:250 000 (Stand 01.01.2021) - © GeoBasis-DE / BKG (2022)

Anmerkungen: Die Gebiete werden als zusammenhängende Flächen erfasst. Gebiete, die innerhalb mehrerer Bundesländer liegen, sind in der Feature-Class jedes betroffenen Bundeslandes enthalten. Bundesländer, die keine Gebiete mit Ausbaudefizit aufweisen, sind nicht enthalten.

Quellenvermerk: © Bundesnetzagentur
		
Kontakt: Bundesnetzagentur | Referat 214 Monitoring Mobilfunk | mobilfunkmonitoring@bnetza.de