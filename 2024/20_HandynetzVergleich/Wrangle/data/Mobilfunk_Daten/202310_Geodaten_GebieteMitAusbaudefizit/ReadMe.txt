Dies ist eine Beschreibung des Datensatzes "202310_GebieteMitAusbaudefizit.gpkg"

Beschreibung: Gebiete mit Ausbaudefizit nach � 84 Abs. 1 TKG | Als Gebiete mit Ausbaudefizit im Mobilfunkbereich sind Fl�chen definiert, in denen aktuell sowie in den n�chsten 12 Monaten voraussichtlich keine Versorgung und keine Ausbauplanung mit einem Mobilfunknetz mit sehr hoher Kapazit�t oder einer Mobilfunktechnologie der vierten (4G) oder f�nften (5G) Generation vorliegt.

Zeitlicher Bezug:
	Datenstand: Oktober 2023
	Aktualisierung: halbj�hrlich 

Format: OGC GeoPackage

Datenstruktur: 1 Polygon-Feature-Class je Bundesland der Bundesrepublik Deutschland sowie 1 Polygon-Feature-Class der gesamten Bundesrepublik Deutschland

Attribute:
	id [Integer] - Feature-Identifikator
	geom [Geometrie] - Geometrie-Attribut
	Nr [Integer] - Bundesland�bergreifende Kennziffer der Gebiete mit Ausbaudefizit
	betroffene_Laender [String] - Liste der Bundeslandschl�ssel der betroffenen Bundesl�nder (durch Leerzeichen getrennt)
	betroffene_Kreise [String] - Liste der Kreisschl�ssel der betroffenen Kreise (durch Leerzeichen getrennt)
	betroffene_Gemeinden [String] - Liste der Gemeindeschl�ssel (AGS) der betroffenen Gemeinden (durch Leerzeichen getrennt)
	gebietsflaeche_qkm [Double] - Gebietsfl�che des Gebietes mit Ausbaudefizit in Quadratkilometer

R�umlicher Bezug:
	Projiziertes Koordinatensystem: ETRS_1989_UTM_Zone_32N
	Geographisches Koordinatensystem: GCS_ETRS_1989
	EPSG: 25832
	
Datengrundlage: 
	Daten der Mobilfunknetzbetreiber, die nach �� 80, 81 TKG  erhoben werden.
	Grunddaten: Geographische Gitter f�r Deutschland in UTM-Projektion - � GeoBasis-DE / BKG (2021) | Verwaltungsgebiete 1:250 000 (Stand 01.01.2021) - � GeoBasis-DE / BKG (2022)

Anmerkungen: Die Gebiete werden als zusammenh�ngende Fl�chen erfasst. Gebiete, die innerhalb mehrerer Bundesl�nder liegen, sind in der Feature-Class jedes betroffenen Bundeslandes enthalten. Bundesl�nder, die keine Gebiete mit Ausbaudefizit aufweisen, sind nicht enthalten.

Quellenvermerk: � Bundesnetzagentur
		
Kontakt: Bundesnetzagentur | Referat 214 Monitoring Mobilfunk | mobilfunkmonitoring@bnetza.de