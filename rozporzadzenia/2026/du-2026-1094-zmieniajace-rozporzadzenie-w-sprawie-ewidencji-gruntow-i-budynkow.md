---
title: "Rozporządzenie Ministra Finansów i Gospodarki z dnia 6 sierpnia 2026 r. zmieniające rozporządzenie w sprawie ewidencji gruntów i budynków"
identifier: "DU/2026/1094"
official_citation: "Dz.U. 2026 poz. 1094"
type: regulation
jurisdiction: pl
language: pl
date: 2026-08-06
promulgated: 2026-08-13
entry_into_force: 2026-08-28
status: in_force
official_status: "obowiązujący"
text_version: "tekst ogłoszony (original)"
text_format: "pdf (text extracted)"
source: "https://api.sejm.gov.pl/eli/acts/DU/2026/1094"
source_text: "https://api.sejm.gov.pl/eli/acts/DU/2026/1094/text/I/D20261094.pdf"
isap: "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260001094"
retrieved: 2026-10-12
---

# Rozporządzenie Ministra Finansów i Gospodarki z dnia 6 sierpnia 2026 r. zmieniające rozporządzenie w sprawie ewidencji gruntów i budynków

ROZPORZĄDZENIE MINISTRA FINANSÓW I GOSPODARKI 1) z dnia 6 sierpnia 2026 r. zmieniające rozporządzenie w sprawie ewidencji gruntów i budynków Na podstawie art. 26 ust. 2 ustawy z dnia 17 maja 1989 r. – Prawo geodezyjne i kartograficzne (Dz. U. z 2024 r. poz. 1151 i 1824 oraz z 2025 r. poz. 1019, 1542 i 1792) zarządza się, co następuje:

§ 1. W rozporządzeniu Ministra Rozwoju, Pracy i Technologii z dnia 27 lipca 2021 r. w sprawie ewidencji gruntów i budynków (Dz. U. z 2024 r. poz. 219 i 1954) wprowadza się następujące zmiany:

1\) w § 40 w ust. 11 wyrazy „lub wyciągów w postaci papierowej” zastępuje się wyrazami „oraz zarchiwizowanych plików GML w formacie kompresji ZIP udostępnianych w portalach internetowych, w szczególności w portalu danych w rozumieniu art. 2 pkt 13 ustawy z dnia 11 sierpnia 2021 r. o otwartych danych i ponownym wykorzystywaniu informacji sektora publicznego (Dz. U. z 2023 r. poz. 1524)”;

2\) załącznik nr 9 do rozporządzenia otrzymuje brzmienie określone w załączniku nr 1 do niniejszego rozporządzenia;

3\) załącznik nr 10 do rozporządzenia otrzymuje brzmienie określone w załączniku nr 2 do niniejszego rozporządzenia.

§ 2. Organ prowadzący rejestr cen nieruchomości dostosuje sposób udostępniania danych z rejestru cen nieruchomości do przepisów rozporządzenia zmienianego w § 1 w brzmieniu nadanym niniejszym rozporządzeniem do dnia 30 września 2026 r. § 3. Rozporządzenie wchodzi w życie po upływie 14 dni od dnia ogłoszenia. Minister Finansów i Gospodarki: wz. M. Jaros Załączniki do rozporządzenia Ministra Finansów i Gospodarki z dnia 6 sierpnia 2026 r. (Dz. U. poz. 1094)

## Załącznik nr 1

SPECYFIKACJA POJĘCIOWEGO MODELU DANYCH REJESTRU CEN NIERUCHOMOŚCI (RCN)

## Załączniki do rozporządzenia

Ministra Finansów i Gospodarki

z dnia 6 sierpnia 2026 r. (poz. …)

## Załącznik nr 1

SPECYFIKACJA POJĘCIOWEGO MODELU DANYCH REJESTRU CEN NIERUCHOMOŚCI (RCN)

1\. Model pojęciowy danych rejestru cen nieruchomości

2\. Ograniczenia nałożone na atrybuty Klasa RCN\_Nieruchomosc

Ograniczenie: Nazwa: polePowierzchniNieruchomosciGruntowej Język naturalny: Atrybut pole powierzchni nieruchomości gruntowej jest sumą powierzchni działek będących przedmiotem transakcji. Nazwa: cenaNieruchomosciBrutto

Język naturalny: Cena nieruchomości brutto nie może być wyższa niż cena transakcji brutto, a także mniejsza niż suma cen brutto działek, budynków i lokali wchodzących w skład nieruchomości. Klasa RCN\_Dzialka

Ograniczenie: Nazwa: wymagalnoscGeometria Język naturalny: Atrybut wymagany dla wszystkich działek:

1\) które posiadają geometrię w bazie danych ewidencji gruntów i budynków,

2\) dla których transakcja obejmująca działkę jest wykazywana w RCN po wejściu w życie niniejszego modelu danych RCN. Klasa RCN\_Budynek

Ograniczenie: Nazwa: wymagalnoscGeometria Język naturalny: Atrybut wymagany dla wszystkich budynków:

1\) które posiadają geometrię w bazie danych ewidencji gruntów i budynków,

2\) dla których transakcja obejmująca budynek jest wykazywana w RCN po wejściu w życie niniejszego modelu danych RCN. Klasa RCN\_Lokal

Ograniczenie: Nazwa: wymagalnoscGeoreferencja Język naturalny: Atrybut wymagany dla wszystkich lokali:

1\) które są zlokalizowane w budynku, który posiada geometrię w bazie danych ewidencji gruntów i budynków,

2\) dla których transakcja obejmująca lokal jest wykazywana w RCN po wejściu w życie niniejszego modelu danych RCN.

## Załącznik nr 2

SPECYFIKACJA USŁUG SIECIOWYCH DOTYCZĄCYCH UDOSTĘPNIANIA DANYCH Z REJESTRU CEN NIERUCHOMOŚCI

1\. Usługi publikujące dane dotyczące rejestru cen nieruchomości są zgodne ze standardem Web Map Service (WMS) i Web Feature Service (WFS).

2\. Usługi publikują dane w podziale na warstwy i obiekty:

1\) Działki,

2\) Budynki,

3\) Lokale.

3\. Warstwy, o których mowa w pkt 2, prezentują lokalizację przestrzenną przedmiotów transakcji z rejestru cen nieruchomości zgodnie z geometrią określoną w schemacie aplikacyjnym w załączniku nr 9 do rozporządzenia Ministra Rozwoju, Pracy i Technologii z dnia 27 lipca 2021 r. w sprawie ewidencji gruntów i budynków (Dz. U. z 2024 r. poz. 219, z późn. zm.) oraz dane opisowe tych obiektów zwracane przez funkcję GetFeatureInfo (GFI).

4\. Skala mapy jest rozumiana jako wartość ScaleDenominator stosowana w standardach Open Geospatial Consortium (OGC) i jest wyznaczana przy założeniu znormalizowanego rozmiaru piksela renderowania wynoszącego 0,28 mm, co odpowiada zależności: skala mapy = rozdzielczość mapy (metry na piksel) / 0,00028 .

5\. Szczegółową charakterystykę publikowanych warstw i stosowanych symboli graficznych określa tabela nr 1. Tabela nr 1

Tytuł

warstwy

Nazwa

warstwy Symbol Kolor bazowy (RGB) Parametry prezentacji Działki dzialki

obrys i czcionka 255 0 127

wypełnienie transparentne minimalna grubość obrysu 2 px Budynki budynki

obrys 127 255 0

wypełnienie 244 255 234 minimalna grubość obrysu 3 px Lokale lokale

obrys 0 204 0

czcionka 0 0 0

wypełnienie 127 255 0

minimalna grubość obrysu 2 px

6\. Zasady prezentacji warstw w zależności od skali generowanej mapy określa tabela nr 2. Tabela nr 2

Zakres widoczności Przybliżony poziom skalowy Warstwy widoczne Uwagi w skalach ≥ 1:5000

oraz &lt; 1:2000 1:5000 – 1:2000 dzialki tylko kontury działek w skalach ≥ 1:2000 1:2000 i większe dzialki, budynki, lokale wszystkie warstwy są włączone

7\. Szczegółową charakterystykę parametrów funkcji GetMap usługi WMS określa tabela nr 3. Tabela nr 3

Parametr Opis lub wartość Uwagi VERSION 1.3.0 Usługa może wspierać starsze wersje standardu WMS.

LAYERS dzialki, budynki, lokale Usługa może publikować dodatkowe warstwy.

## Załącznik nr 2

SPECYFIKACJA USŁUG SIECIOWYCH DOTYCZĄCYCH UDOSTĘPNIANIA DANYCH Z REJESTRU CEN NIERUCHOMOŚCI

STYLES – Usługa jako domyślne wspiera style w tabeli nr 1. Dopuszczalna jest obsługa dodatkowych stylów. CRS Oznaczenie układu współrzędnych Usługa wspiera co najmniej układy współrzędnych PL-1992 (EPSG:2180), układ geograficzny WGS84 (EPSG:4326) oraz PL-2000, przy czym w przypadku układu PL-2000 usługa musi wspierać właściwą strefę układu, w której określono współrzędne publikowanych obiektów (EPSG:2176, 2177, 2178 lub 2179). BBOX minX, minY, maxX, maxY Współrzędne ograniczające zakres przestrzenny zapytania.

WIDTH Szerokość obrazu w pikselach Serwer może odrzucić żądanie utworzenia obrazu o rozmiarze przekraczającym 4096 pikseli. HEIGHT Wysokość obrazu w pikselach Serwer może odrzucić żądanie utworzenia obrazu o rozmiarze przekraczającym 4096 pikseli. FORMAT image/png Dopuszcza się dodatkowo inne formaty. TRANSPARENT TRUE Tło obrazu przezroczyste. Parametr TRANSPARENT dotyczy wyłącznie formatów rastrowych obsługujących przezroczystość (np. PNG).

8\. Podstawowe parametry funkcji GetFeatureInfo usługi WMS określa tabela nr 4, przy czym pozostałe parametry są tożsame z parametrami funkcji GetMap. Tabela nr 4

Parametr Wymagane wartości parametru Uwagi QUERY\_LAYERS dzialki, budynki, lokale – INFO\_FORMAT text/xml

Dopuszcza się również wsparcie

dodatkowych formatów (np. HTML) przy zachowaniu co najmniej tego samego zakresu treści.

FEATURE\_COUNT liczba obiektów – I numer kolumny piksela –

J numer wiersza piksela –

9\. Zasady ogólne odpowiedzi GetFeatureInfo.

1\) Funkcja GetFeatureInfo dla warstw: dzialki, budynki, lokale zwraca odpowiedź w formacie text/xml zgodnie ze schematem aplikacyjnym, z uwzględnieniem modelu określonego w tabelach nr 5 –8.

2\) Jeżeli identyfikacja wskazuje na więcej niż jeden obiekt, funkcja GetFeatureInfo zwraca wszystkie obiekty w ramach jednej odpowiedzi.

3\) Elementy o krotności 0..\* w modelu (np. DZI\_PRZEZN\_WMPZP, DZI\_ADRES) w odpowiedzi GetFeatureInfo są przekazywane do postaci pojedynczego elementu (0..1), którego wartość jest listą wartości zakodowaną w postaci tekstowej.

10\. Zasady zapisu adresu w odpowiedzi GetFeatureInfo.

1\) W odpowiedzi GetFeatureInfo element adres występuje co najwyżej raz (0..1).

2\) Jeżeli obiekt posiada więcej niż jeden adres, wszystkie adresy są przekazywane w jednej wartości elementu adres jako lista rozdzielona separatorem pionowym |.

3\) Format pojedynczego adresu:

– składowe adresu oddziela się średnikami,

– składowe zapisuje się w postaci SKRÓT: Wartość,

– dopuszcza się pomijanie składowych opcjonalnych, dla których brak wartości.

4\) Skróty i znaczenie składowych:

– MSC: miejscowość,

– UL: ulica,

– NR\_PORZ: numer porządkowy.

5\) Wzorzec zapisu wartości elementu adres (wyrażenie regularne): ^MSC:[^;&lt;&gt;|&"]+(?:;UL:[^;&lt;&gt;|&"]+)?(?:;NR\_PORZ:[^;&lt;&gt;|&"]+)?(?:\\|MSC:[^;&lt;&gt;|&"]+(?:;UL:[^;&lt;&gt;| &"]+)?(?:;NR\_PORZ:[^;&lt;&gt;|&"]+)?)\*$

11\. Zasady zapisu przeznaczenia w MPZP w odpowiedzi GetFeatureInfo.

1\) W odpowiedzi GetFeatureInfo element DZI\_PRZEZN\_WMPZP występuje co najwyżej raz (0..1).

2\) Jeżeli dla działki występuje więcej niż jedno przeznaczenie w MPZP, wartości są przekazywane w jednej wartości elementu DZI\_PRZEZN\_WMPZP rozdzielone średnikiem.

3\) Wzorzec zapisu wartości elementu DZI\_PRZEZN\_WMPZP: ^[A-Za-z]+(?:;[A-Za-z]+)\*$

12\. Wspólne dane zwracane dla obiektów DZIALKA, BUDYNEK i LOKAL określa tabela nr 5. Tabela nr 5 – ATRYBUTY\_WSPOLNE

Atrybut / element Opis

SERWIS\_RCN adres URL serwisu, z którego pochodzi obiekt

TERYT kod TERYT powiatu

TRAN\_PRZESTRZEN\_NAZW przestrzeń nazw identyfikatora IIP TRAN\_LOKALNY\_ID\_IIP lokalnyId identyfikatora IIP TRAN\_WERSJA\_ID wersjaId identyfikatora IIP TRAN\_OZNACZENIE\_TRANS oznaczenie transakcji TRAN\_RODZAJ\_TRANS rodzaj transakcji TRAN\_RODZAJ\_RYNKU rodzaj rynku

TRAN\_SPRZEDAJACY strona sprzedająca TRAN\_KUPUJACY strona kupująca

TRAN\_CENA\_BRUTTO cena transakcji brutto TRAN\_VAT kwota podatku VAT

DOK\_OZNACZENIE oznaczenie dokumentu DOK\_DATA data sporządzenia dokumentu DOK\_TWORCA twórca dokumentu

NIER\_RODZAJ rodzaj nieruchomości NIER\_PRAWO rodzaj prawa do nieruchomości NIER\_UDZIAL udział w prawie do nieruchomości NIER\_POW\_GRUNTU pole powierzchni nieruchomości gruntowej

NIER\_OPIS opis nieruchomości

NIER\_CENA\_BRUTTO cena nieruchomości brutto NIER\_VAT kwota podatku VAT dla

nieruchomości

13\. Funkcja GetFeatureInfo dla warstwy „dzialki” zwraca obiekt typu DZIALKA z atrybutami określonymi w tabeli nr 6.

Tabela nr 6 – DZIALKA

Atrybut / element Opis

ATRYBUTY\_WSPOLNE na początku obiektu występują atrybuty wspólne określone w tabeli nr 5

DZI\_ID\_DZIALKI identyfikator działki DZI\_NR\_DZIALKI numer działki

DZI\_PRZEZN\_WMPZP przeznaczenie w miejscowym planie zagospodarowania przestrzennego; wartość elementu zapisana zgodnie z zasadami określonymi w pkt 11 DZI\_POW\_EWID pole powierzchni ewidencyjnej DZI\_SPOSOB\_UZYT sposób użytkowania DZI\_CENA\_BRUTTO cena działki brutto DZI\_VAT kwota podatku VAT dla działki DZI\_INFO dodatkowe informacje

DZI\_ADRES adres powiązany z obiektem; wartość elementu zapisana zgodnie z zasadami określonymi w pkt 10

14\. Funkcja GetFeatureInfo dla warstwy „budynki” zwraca obiekt typu BUDYNEK z atrybutami określonymi w tabeli nr 7.

Tabela nr 7 – BUDYNEK

Atrybut / element Opis

ATRYBUTY\_WSPOLNE na początku obiektu występują atrybuty wspólne określone w tabeli nr 5

BUD\_ID\_BUDYNKU identyfikator budynku BUD\_RODZAJ rodzaj budynku

BUD\_POW\_UZYT powierzchnia użytkowa budynku BUD\_CENA\_BRUTTO cena budynku brutto BUD\_VAT kwota podatku VAT dla budynku BUD\_INFO dodatkowe informacje

BUD\_ADRES adres powiązany z obiektem; wartość elementu zapisana zgodnie z zasadami określonymi w pkt 10

15\. Funkcja GetFeatureInfo dla warstwy „lokale” zwraca obiekt typu LOKAL z atrybutami określonymi w tabeli nr 8.

Tabela nr 8 – LOKAL

Atrybut / element Opis

ATRYBUTY\_WSPOLNE na początku obiektu występują atrybuty wspólne określone w tabeli nr 5

LOK\_ID\_LOKALU identyfikator lokalu LOK\_FUNKCJA funkcja lokalu

LOK\_LICZBA\_IZB liczba izb

LOK\_NR\_KOND numer kondygnacji

LOK\_POW\_UZYT powierzchnia użytkowa lokalu LOK\_POW\_PRZYN powierzchnia pomieszczeń przynależnych

LOK\_CENA\_BRUTTO cena lokalu brutto LOK\_VAT kwota podatku VAT dla lokalu LOK\_INFO dodatkowe informacje

LOK\_ADRES adres budynku z lokalem; wartość elementu zapisana zgodnie

z zasadami określonymi w pkt 10

16\. Strukturę odpowiedzi GetFeatureInfo w formacie XML określa poniższy schemat aplikacyjny. &lt;?xml version="1.0" encoding="UTF-8"?&gt; &lt;xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"&gt; &lt;xs:element name="GETFEATUREINFO"&gt; &lt;xs:complexType&gt;

&lt;xs:sequence maxOccurs="unbounded"&gt; &lt;xs:choice minOccurs="0"&gt;

&lt;xs:element ref="DZIALKA"/&gt;

&lt;xs:element ref="BUDYNEK"/&gt;

&lt;xs:element ref="LOKAL"/&gt;

&lt;/xs:choice&gt;

&lt;/xs:sequence&gt;

&lt;/xs:complexType&gt;

&lt;/xs:element&gt;

&lt;xs:group name="TRANSAKCJA"&gt;

&lt;xs:sequence&gt;

&lt;xs:element name="TRAN\_PRZESTRZEN\_NAZW" type="xs:string"/&gt; &lt;xs:element name="TRAN\_LOKALNY\_ID\_IIP" type="xs:string"/&gt; &lt;xs:element name="TRAN\_WERSJA\_ID" type="xs:dateTime"/&gt; &lt;xs:element name="TRAN\_OZNACZENIE\_TRANS" type="xs:string"/&gt; &lt;xs:element name="TRAN\_RODZAJ\_TRANS" type="RCN\_RodzajTransakcji"/&gt; &lt;xs:element name="TRAN\_RODZAJ\_RYNKU" type="RCN\_RodzajRynku" minOccurs="0"/&gt; &lt;xs:element name="TRAN\_SPRZEDAJACY" type="RCN\_StronaSprzedajacaKupujaca"/&gt; &lt;xs:element name="TRAN\_KUPUJACY" type="RCN\_StronaSprzedajacaKupujaca"/&gt; &lt;xs:element name="TRAN\_CENA\_BRUTTO" type="xs:decimal"/&gt; &lt;xs:element name="TRAN\_VAT" type="xs:decimal" minOccurs="0"/&gt; &lt;xs:element name="DOK\_OZNACZENIE" type="xs:string"/&gt; &lt;xs:element name="DOK\_DATA" type="xs:date"/&gt; &lt;xs:element name="DOK\_TWORCA" type="xs:string"/&gt; &lt;/xs:sequence&gt;

&lt;/xs:group&gt;

&lt;xs:group name="NIERUCHOMOSC"&gt;

&lt;xs:sequence&gt;

&lt;xs:element name="NIER\_RODZAJ" type="RCN\_RodzajNieruchomosci"/&gt; &lt;xs:element name="NIER\_PRAWO" type="RCN\_RodzajPrawa"/&gt; &lt;xs:element name="NIER\_UDZIAL" type="xs:string"/&gt; &lt;xs:element name="NIER\_POW\_GRUNTU" type="xs:decimal" minOccurs="0"/&gt; &lt;xs:element name="NIER\_OPIS" type="xs:string" minOccurs="0"/&gt; &lt;xs:element name="NIER\_CENA\_BRUTTO" type="xs:decimal" minOccurs="0"/&gt; &lt;xs:element name="NIER\_VAT" type="xs:decimal" minOccurs="0"/&gt; &lt;/xs:sequence&gt;

&lt;/xs:group&gt;

&lt;xs:element name="DZIALKA"&gt;

&lt;xs:complexType&gt;

&lt;xs:sequence&gt;

&lt;xs:element name="SERWIS\_RCN" type="xs:string"/&gt; &lt;xs:element name="TERYT" type="xs:string"/&gt; &lt;xs:group ref="TRANSAKCJA"/&gt;

&lt;xs:group ref="NIERUCHOMOSC"/&gt;

&lt;xs:element name="DZI\_ID\_DZIALKI" type="xs:string"/&gt; &lt;xs:element name="DZI\_NR\_DZIALKI" type="xs:string"/&gt; &lt;xs:element name="DZI\_PRZEZN\_WMPZP" type="xs:string" minOccurs="0"/&gt; &lt;xs:element name="DZI\_POW\_EWID" type="xs:decimal"/&gt; &lt;xs:element name="DZI\_SPOSOB\_UZYT" type="RCN\_SposobUzytkowania"/&gt; &lt;xs:element name="DZI\_CENA\_BRUTTO" type="xs:decimal"/&gt; &lt;xs:element name="DZI\_VAT" type="xs:decimal" minOccurs="0"/&gt; &lt;xs:element name="DZI\_INFO" type="xs:string" minOccurs="0"/&gt; &lt;xs:element name="DZI\_ADRES" type="xs:string" minOccurs="0"/&gt; &lt;/xs:sequence&gt;

&lt;/xs:complexType&gt;

&lt;/xs:element&gt;

&lt;xs:element name="BUDYNEK"&gt;

&lt;xs:complexType&gt;

&lt;xs:sequence&gt;

&lt;xs:element name="SERWIS\_RCN" type="xs:string"/&gt; &lt;xs:element name="TERYT" type="xs:string"/&gt; &lt;xs:group ref="TRANSAKCJA"/&gt;

&lt;xs:group ref="NIERUCHOMOSC"/&gt;

&lt;xs:element name="BUD\_ID\_BUDYNKU" type="xs:string"/&gt; &lt;xs:element name="BUD\_RODZAJ" type="RCN\_RodzajBudynku"/&gt; &lt;xs:element name="BUD\_POW\_UZYT" type="xs:decimal" minOccurs="0"/&gt; &lt;xs:element name="BUD\_CENA\_BRUTTO" type="xs:decimal" minOccurs="0"/&gt; &lt;xs:element name="BUD\_VAT" type="xs:decimal" minOccurs="0"/&gt; &lt;xs:element name="BUD\_INFO" type="xs:string" minOccurs="0"/&gt; &lt;xs:element name="BUD\_ADRES" type="xs:string" minOccurs="0"/&gt; &lt;/xs:sequence&gt;

&lt;/xs:complexType&gt;

&lt;/xs:element&gt;

&lt;xs:element name="LOKAL"&gt;

&lt;xs:complexType&gt;

&lt;xs:sequence&gt;

&lt;xs:element name="SERWIS\_RCN" type="xs:string"/&gt; &lt;xs:element name="TERYT" type="xs:string"/&gt; &lt;xs:group ref="TRANSAKCJA"/&gt;

&lt;xs:group ref="NIERUCHOMOSC"/&gt;

&lt;xs:element name="LOK\_ID\_LOKALU" type="xs:string"/&gt; &lt;xs:element name="LOK\_FUNKCJA" type="RCN\_FunkcjaLokalu"/&gt; &lt;xs:element name="LOK\_LICZBA\_IZB" type="xs:int" minOccurs="0"/&gt; &lt;xs:element name="LOK\_NR\_KOND" type="xs:int" minOccurs="0"/&gt; &lt;xs:element name="LOK\_POW\_UZYT" type="xs:decimal"/&gt; &lt;xs:element name="LOK\_POW\_PRZYN" type="xs:decimal" minOccurs="0"/&gt; &lt;xs:element name="LOK\_CENA\_BRUTTO" type="xs:decimal" minOccurs="0"/&gt; &lt;xs:element name="LOK\_VAT" type="xs:decimal" minOccurs="0"/&gt; &lt;xs:element name="LOK\_INFO" type="xs:string" minOccurs="0"/&gt; &lt;xs:element name="LOK\_ADRES" type="xs:string" minOccurs="0"/&gt; &lt;/xs:sequence&gt;

&lt;/xs:complexType&gt;

&lt;/xs:element&gt;

&lt;xs:simpleType name="RCN\_RodzajRynku"&gt; &lt;xs:restriction base="xs:string"&gt; &lt;xs:enumeration value="rynekPierwotny"/&gt; &lt;xs:enumeration value="rynekWtorny"/&gt; &lt;/xs:restriction&gt;

&lt;/xs:simpleType&gt;

&lt;xs:simpleType name="RCN\_RodzajTransakcji"&gt; &lt;xs:restriction base="xs:string"&gt; &lt;xs:enumeration value="wolnyRynek"/&gt; &lt;xs:enumeration value="sprzedazBezprzetargowa"/&gt; &lt;xs:enumeration value="sprzedazPrzetargowa"/&gt; &lt;xs:enumeration value="sprzedazWPostepowaniuEgzekucyjnym"/&gt; &lt;xs:enumeration value="sprzedazNaCelPubliczny"/&gt; &lt;xs:enumeration value="sprzedazZBonifikata"/&gt; &lt;/xs:restriction&gt;

&lt;/xs:simpleType&gt;

&lt;xs:simpleType name="RCN\_StronaSprzedajacaKupujaca"&gt; &lt;xs:restriction base="xs:string"&gt; &lt;xs:enumeration value="skarbPanstwa"/&gt; &lt;xs:enumeration value="jednostkaSamorzaduTerytorialnego"/&gt; &lt;xs:enumeration value="osobaFizyczna"/&gt; &lt;xs:enumeration value="osobaPrawna"/&gt; &lt;/xs:restriction&gt;

&lt;/xs:simpleType&gt;

&lt;xs:simpleType name="RCN\_RodzajPrawa"&gt; &lt;xs:restriction base="xs:string"&gt; &lt;xs:enumeration value="wlasnoscNieruchomosciGruntowej"/&gt; &lt;xs:enumeration value="uzytkowanieWieczyste"/&gt; &lt;xs:enumeration value="wlasnoscLokaluWrazZPrawemZwiazanym"/&gt; &lt;xs:enumeration value="wlasnoscBudynkuWrazZPrawemZwiazanym"/&gt; &lt;/xs:restriction&gt;

&lt;/xs:simpleType&gt;

&lt;xs:simpleType name="RCN\_RodzajNieruchomosci"&gt; &lt;xs:restriction base="xs:string"&gt; &lt;xs:enumeration value="nieruchomoscGruntowaNiezabudowana"/&gt; &lt;xs:enumeration value="nieruchomoscGruntowaZabudowana"/&gt; &lt;xs:enumeration value="nieruchomoscBudynkowa"/&gt; &lt;xs:enumeration value="nieruchomoscLokalowa"/&gt; &lt;/xs:restriction&gt;

&lt;/xs:simpleType&gt;

&lt;xs:simpleType name="RCN\_RodzajBudynku"&gt; &lt;xs:restriction base="xs:string"&gt; &lt;xs:enumeration value="przemyslowy"/&gt; &lt;xs:enumeration value="transportuILacznosci"/&gt; &lt;xs:enumeration value="handlowoUslugowy"/&gt; &lt;xs:enumeration value="zbiornikiSilosyMagazyny"/&gt; &lt;xs:enumeration value="biurowy"/&gt; &lt;xs:enumeration value="szpitale"/&gt; &lt;xs:enumeration value="oswiatyISportu"/&gt; &lt;xs:enumeration value="gospodarczy"/&gt; &lt;xs:enumeration value="pozostaleNiemieszkalne"/&gt; &lt;xs:enumeration value="mieszkalny"/&gt; &lt;/xs:restriction&gt;

&lt;/xs:simpleType&gt;

&lt;xs:simpleType name="RCN\_SposobUzytkowania"&gt; &lt;xs:restriction base="xs:string"&gt; &lt;xs:enumeration value="gruntyRolne"/&gt; &lt;xs:enumeration value="gruntyLesne"/&gt; &lt;xs:enumeration value="gruntyZabudowaneIZurbanizowane"/&gt; &lt;xs:enumeration value="terenyKomunikacyjne"/&gt; &lt;xs:enumeration value="inne"/&gt;

&lt;/xs:restriction&gt;

&lt;/xs:simpleType&gt;

&lt;xs:simpleType name="RCN\_FunkcjaLokalu"&gt; &lt;xs:restriction base="xs:string"&gt; &lt;xs:enumeration value="mieszkalna"/&gt; &lt;xs:enumeration value="handlowoUslugowa"/&gt; &lt;xs:enumeration value="biurowa"/&gt; &lt;xs:enumeration value="produkcyjna"/&gt; &lt;xs:enumeration value="garaz"/&gt; &lt;xs:enumeration value="inna"/&gt;

&lt;/xs:restriction&gt;

&lt;/xs:simpleType&gt;

&lt;xs:simpleType name="RCN\_PrzeznaczenieWMPZP"&gt; &lt;xs:restriction base="xs:string"&gt; &lt;xs:enumeration value="BP"/&gt;

&lt;xs:enumeration value="MN"/&gt;

&lt;xs:enumeration value="MW"/&gt;

&lt;xs:enumeration value="U"/&gt;

&lt;xs:enumeration value="US"/&gt;

&lt;xs:enumeration value="UC"/&gt;

&lt;xs:enumeration value="R"/&gt;

&lt;xs:enumeration value="RU"/&gt;

&lt;xs:enumeration value="RM"/&gt;

&lt;xs:enumeration value="P"/&gt;

&lt;xs:enumeration value="PG"/&gt;

&lt;xs:enumeration value="ZN"/&gt;

&lt;xs:enumeration value="ZL"/&gt;

&lt;xs:enumeration value="ZP"/&gt;

&lt;xs:enumeration value="ZD"/&gt;

&lt;xs:enumeration value="ZC"/&gt;

&lt;xs:enumeration value="WM"/&gt;

&lt;xs:enumeration value="WS"/&gt;

&lt;xs:enumeration value="KD"/&gt;

&lt;xs:enumeration value="KDW"/&gt;

&lt;xs:enumeration value="KW"/&gt;

&lt;xs:enumeration value="TIT"/&gt;

&lt;xs:enumeration value="INN"/&gt;

&lt;xs:enumeration value="WZ"/&gt;

&lt;/xs:restriction&gt;

&lt;/xs:simpleType&gt;

&lt;/xs:schema&gt;

17\. Struktura odpowiedzi GetFeature dla usługi WFS zawiera wszystkie elementy odpowiedzi GetFeatureInfo usługi WMS oraz jest uzupełniona o atrybut GEOMETRIA zawierający geometrię zwracanego obiektu w formacie GML.

---

Przypisy:

1\) Minister Finansów i Gospodarki kieruje działem administracji rządowej – budownictwo, planowanie i zagospodarowanie przestrzenne oraz mieszkalnictwo, na podstawie § 1 ust. 2 pkt 1 rozporządzenia Prezesa Rady Ministrów z dnia 25 lipca 2025 r. w sprawie szczegółowego zakresu działania Ministra Finansów i Gospodarki (Dz. U. poz. 997).
