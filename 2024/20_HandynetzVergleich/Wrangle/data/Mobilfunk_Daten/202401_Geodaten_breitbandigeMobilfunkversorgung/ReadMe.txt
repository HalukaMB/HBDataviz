Dies ist eine Beschreibung des Datensatzes "202401_Geodaten_breitbandigeMobilfunkversorgung.gpkg"

Beschreibung: Breitbandige Mobilfunkversorgung nach Anzahl der Mobilfunknetzbetreiber | Es handelt sich um Flächen, die anhand der Anzahl der Mobilfunknetzbetreiber unterschieden werden, die in dieser eine Mobilfunktechnologie der vierten (4G) oder fünften (5G) Generation anbieten. Es werden nur die etablierten Mobilfunknetzbetreiber (Deutsche Telekom, Vodafone und Telefónica) berücksichtigt. Die 1&1 verfügt derzeit über kein Frequenzspektrum, das für eine Mobilfunknetzabdeckung in der Fläche geeignet ist.

Zeitlicher Bezug:
	Datenstand: Januar 2024
	Aktualisierung: quartalsweise 

Format: OGC GeoPackage

Datenstruktur: 1 Polygon-Feature-Class für die Bundesrepublik Deutschland

Attribute:
	id [Integer] - Feature-Identifikator
	geom [Geometrie] - Geometrie-Attribut
	BL [String] - Identifikator des Bundeslandes; entspricht den ersten zwei Stellen des Amtlichen Gemeindeschlüssels (AGS)
	mobilesBB_AnzahlMNB [Integer] - Anzahl der Mobilfunknetzbetreiber, die eine breitbandige Mobilfunkversorgung (4G oder 5G) liefern

Räumlicher Bezug:
	Projiziertes Koordinatensystem: ETRS_1989_UTM_Zone_32N
	Geographisches Koordinatensystem: GCS_ETRS_1989
	EPSG: 25832
	
Datengrundlage: 
	Daten der Mobilfunknetzbetreiber, die nach § 103 Abs. 3 TKG  erhoben werden.
	Grunddaten: Geographische Gitter für Deutschland in UTM-Projektion - © GeoBasis-DE / BKG (2021) | Verwaltungsgebiete 1:250 000 (Stand 01.01.2021) - © GeoBasis-DE / BKG (2022)

Anmerkungen: Die Flächen werden als zusammenhängende Gebiete gleicher sachlicher Informationen erfasst. Ein Polygon wird aus Gitterzellen gebildet, die eine einheitliche breitbandige Mobilfunkversorgung aufweisen sowie dem gleichen Bundesland zugeordnet sind.

Quellenvermerk: © Bundesnetzagentur
		
Kontakt: Bundesnetzagentur | Referat 214 Monitoring Mobilfunk | mobilfunkmonitoring@bnetza.de