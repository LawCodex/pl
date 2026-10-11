---
title: "Rozporządzenie Ministra Spraw Wewnętrznych i Administracji z dnia 21 lutego 2025 r. w sprawie warstwy elektronicznej dowodu osobistego"
identifier: "DU/2025/267"
official_citation: "Dz.U. 2025 poz. 267"
type: regulation
jurisdiction: pl
language: pl
date: 2025-02-21
promulgated: 2025-03-05
status: in_force
official_status: "obowiązujący"
text_version: "tekst ogłoszony (original)"
text_format: "pdf (text extracted)"
source: "https://api.sejm.gov.pl/eli/acts/DU/2025/267"
source_text: "https://api.sejm.gov.pl/eli/acts/DU/2025/267/text/I/D20250267.pdf"
isap: "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250000267"
retrieved: 2026-10-11
---

# Rozporządzenie Ministra Spraw Wewnętrznych i Administracji z dnia 21 lutego 2025 r. w sprawie warstwy elektronicznej dowodu osobistego

ROZPORZĄDZENIE MINISTRA SPRAW WEWNĘTRZNYCH I ADMINISTRACJI 1) z dnia 21 lutego 2025 r. w sprawie warstwy elektronicznej dowodu osobistego2), 3)

Na podstawie art. 12j ustawy z dnia 6 sierpnia 2010 r. o dowodach osobistych (Dz. U. z 2022 r. poz. 671 oraz z 2023 r. poz. 1234 i 1941) zarządza się, co następuje:

## Rozdział 1 – Przepisy ogólne

§ 1. Rozporządzenie określa:

1\) wymagania techniczne dla warstwy elektronicznej dowodu osobistego;

2\) sposób używania certyfikatów identyfikacji i uwierzytelnienia, podpisu osobistego i potwierdzenia obecności;

3\) sposób przekazywania i używania kodu umożliwiającego odblokowanie certyfikatu identyfikacji i uwierzytelnienia oraz certyfikatu podpisu osobistego;

4\) sposób i tryb zawieszania, cofania zawieszenia oraz unieważniania certyfikatów identyfikacji i uwierzytelnienia, podp isu osobistego i potwierdzenia obecności;

5\) wzór zaświadczenia potwierdzającego zgłoszenie zawieszenia lub cofnięcia zawieszenia certyfikatów identyfikacji i uwierzytelnienia, podpisu osobistego i potwierdzenia obecności.

## Rozdział 2 – Wymagania techniczne dla warstwy elektronicznej dowodu osobistego

§ 2. 1. Warstwa elektroniczna dowodu osobistego:

1\) obsługuje kody o długości minimalnej 4 cyfr, w tym kody z funkcją kodu początkowego dla każdego z kodów, w którego miejsce posiadacz dowodu osobistego ustala własne kody, o których mowa w art. 12b ust. 1 ustawy z dnia 6 sierpnia 2010 r. o dowodach osobistych, zwanej dalej „ustawą”:

a) dla certyfikatu identyfikacji i uwierzytelnienia, zwany dalej „kodem PIN1”, oraz b) dla certyfikatu podpisu osobistego, zwany dalej „kodem PIN2”;

1\) Minister Spraw Wewnętrznych i Administracji kieruje działem administracji rządowej – sprawy wewnętrzne, na podstawie § 1 ust. 2 pkt 2 rozporządzenia Prezesa Rady Ministrów z dnia 16 maja 2024 r. w sprawie szczegółowego zakresu działania Ministra Spraw Wewnętrznych i Administracji (Dz. U. poz. 738).

2\) Niniejsze rozporządzenie służy stosowaniu rozporządzenia Parlamentu Europejskiego i Rady (UE) 2019/1157 z dnia 20 czerwca 2019 r. w sprawie poprawy zabezpieczeń dowodów osobistych obywateli Unii i dokumentów pobytowych wydawanych obywatelom Unii i członkom ich rodzin korzystającym z prawa do swobodnego przemieszczania się (Dz. Urz. UE L 188 z 12.07.2019, str. 67 oraz Dz. Urz. UE L 2023/90018 z 13.10.2023).

3\) Niniejsze rozporządzenie zostało notyfikowane Komisji Europejskiej w dniu 9 września 2024 r. pod numerem 2024/0508/PL, zgodnie z § 4 rozporządzenia Rady Ministrów z dnia 23 grudnia 2002 r. w sprawie sposobu funkcjonowania krajowego systemu notyfikacji norm i aktów prawnych (Dz. U. poz. 2039 oraz z 2004 r. poz. 597), które wdraża dyrektywę (UE) 2015/1535 Parlamentu Europejskiego i Rady z dnia 9 września 2015 r. ustanawiającą procedurę udzielania informacji w dziedzinie przepisów technicznych oraz zasad dotyczących usług społeczeństwa informacyjnego (Dz. Urz. UE L 241 z 17.09.2015, str. 1).

2\) umożliwia zmianę kodu PIN1 i kodu PIN2, za pomocą dotychczasowego kodu PIN1 albo odpowiednio kodu PIN2, albo kodu odblokowującego, o którym mowa w art. 12b ust. 4 ustawy, zwanego dalej „kodem PUK”;

3\) umożliwia odblokowanie kodu PIN1 i kodu PIN2 za pomocą kodu PUK;

4\) zawiera licznik błędnych prób wprowadzenia kodu PIN1 i kodu PIN2 z możliwością ustawienia parametru liczby błędnych prób, która powoduje zablokowanie tych kodów;

5\) w przypadku podania poprawnego kodu PIN1 albo kodu PIN2 zeruje mechanizm licznika, o którym mowa w pkt 4;

6\) zapewnia komunikację z użyciem interfejsu bezstykowego pozwalającego na bezpieczne połączenie, które gwarantuje, na skutek użycia technik kryptograficznych, poufność i integralność danych oraz uwierzytelnienie stron komunikacji;

7\) uniemożliwia odblokowanie kodu PIN1 albo kodu PIN2 po zablokowaniu kodu PUK;

8\) uniemożliwia odblokowanie kodu PUK;

9\) spełnia zalecenia Organizacji Międzynarodowego Lotnictwa Cywilnego, zwanej dalej „ICAO”, określone w dokumencie – Doc 9303 Machine Readable Travel Documents część 10, 11 i 12 (wersja ósma z 2021 r.);

10\) zawiera aplikację zgodną z wymaganiami ICAO umożliwiającą automatyczną odprawę przy przekraczaniu granic państw.

2\. W warstwie elektronicznej dowodu osobistego są wydzielone logiczne części, które są niezależnie zarządzane oraz zawierają dane, o których mowa w art. 12a ust. 1 ustawy.

3\. Wymagania techniczne dla warstwy elektronicznej dowodu osobistego określa załącznik nr 1 do rozporządzenia.

§ 3. Nawiązanie połączenia między warstwą elektroniczną dowodu osobistego a urządzeniem lub systemem teleinformatycznym za pośrednictwem czytnika kart wymaga podania numeru dostępowego zamieszczonego na blankiecie dowodu osobistego, zwanego dalej „numerem CAN”.

§ 4. Pierwszy dostęp do przestrzeni umożliwiającej zamieszczenie kwalifikowanego certyfikatu podpisu elektroniczne go zgodnego z art. 28 rozporządzenia Parlamentu Europejskiego i Rady (UE) nr 910/2014 z dnia 23 lipca 2014 r. w sprawie identyfikacji elektronicznej i usług zaufania w odniesieniu do transakcji elektronicznych na rynku wewnętrznym oraz uchylającego dyrektywę 1999/93/WE (Dz. Urz. UE L 257 z 28.08.2014, str. 73, z późn. zm.4)) wymaga podania numeru CAN, a następnie użycia kodu PUK.

## Rozdział 3 – Sposób używania certyfikatów identyfikacji i uwierzytelnienia, podpisu osobistego i potwierdzenia obecności

§ 5. Użycie certyfikatu identyfikacji i uwierzytelnienia wymaga podania numeru CAN oraz czterocyfrowego kodu PIN1, który ustala osobiście posiadacz dowodu osobistego.

§ 6. Użycie podpisu osobistego, weryfikowanego za pomocą certyfikatu podpisu osobistego, wymaga podania numeru CAN ora z sze ściocyfrowego kodu PIN2, który ustala osobiście posiadacz dowodu osobistego.

§ 7. 1. Zmiana kodu PIN1 albo kodu PIN2 wymaga podania numeru CAN oraz podania odpowiednio dotychczasowego kodu PIN1 albo kodu PIN2, albo kodu PUK.

2\. Trzykrotne wprowadzenie nieprawidłowego kodu PIN1 albo kodu PIN2 powoduje zablokowanie możliwości korzystania odpowiednio z certyfikatu identyfikacji i uwierzytelnienia lub certyfikatu podpisu osobistego.

3\. W przypadku, o którym mowa w ust. 2, przywrócenie możliwości korzystania z certyfikatu identyfikacji i uwierzytelnienia lub certyfikatu podpisu osobistego jest możliwe po podaniu numeru CAN, a następnie użyciu kodu PUK i ustaleniu odpowiednio nowego kodu PIN1 albo nowego kodu PIN2.

§ 8. Użycie certyfikatu potwierdzenia obecności wymaga podania numeru CAN.

§ 9. Ponowne podanie numeru CAN w przypadkach, o których mowa w § 5–8, nie jest wymagane, jeśli połączenie nie zostało zakończone.

4\) Zmiany wymienionego rozporządzenia zostały ogłoszone w Dz. Urz. UE L 333 z 27.12.2022, str. 80 oraz Dz. Urz. UE L 2024/1183 z 30.04.2024.

## Rozdział 4 – Sposób przekazywania i używania kodu PUK

§ 10. Kod PUK, składający się z ośmiu cyfr, jest przekazywany posiadaczowi dowodu osobistego, w którego warstwie elektronicznej zamieszczono certyfikat identyfikacji i uwierzytelnienia lub certyfikat podpisu osobistego. Posiadacz dowodu osobistego, w którego warstwie elektronicznej zamieszczono wyłącznie certyfikat potwierdzenia obecności, nie otrzymuje kodu PUK.

§ 11. Organ gminy przekazuje posiadaczowi dowodu osobistego zabezpieczony dokument z kodem PUK przy odbiorze dowodu osobistego w siedzibie organu gminy albo w miejscu pobytu osoby w przypadkach określonych w art. 30c ust. 1 ustawy lub w każdym czasie po odbiorze dowodu osobistego.

§ 12. 1. W przypadku utraty kodu PUK posiadacz dowodu osobistego, działając osobiście, może przywrócić możliwość korzystania z certyfikatu identyfikacji i uwierzytelnienia lub podpisu osobistego w siedzibie organu dowolnej gminy. Prz epis § 7 ust. 3 stosuje się odpowiednio.

2\. Przywrócenie możliwości korzystania z certyfikatu identyfikacji i uwierzytelnienia lub podpisu osobistego następuje z wykorzystaniem systemu teleinformatycznego, o którym mowa w § 21, z zachowaniem zasad poufności za pomocą certyfikatu potwierdzenia obecności.

§ 13. Trzykrotne nieprawidłowe wprowadzenie kodu PUK powoduje brak możliwości odblokowania kodu PIN1 i kodu PIN2.

## Rozdział 5 – Sposób i tryb zawieszania, cofania zawieszenia oraz unieważniania certyfikatów identyfikacji i uwierzytelnienia, podpisu osobistego i potwierdzenia obecności

§ 14. Zgłoszenie zawieszenia lub cofnięcia zawieszenia certyfikatów zamieszczonych w warstwie elektronicznej dow odu osobistego w trybie określonym w art. 32b ust. 1 pkt 3 ustawy odbywa się na podstawie danych, które podała osoba dokonująca zgłoszenia, oraz danych zawartych w Rejestrze Dowodów Osobistych.

§ 15. Do zgłoszenia zawieszenia lub cofnięcia zawieszenia certyfikatów zamieszczonych w warstwie elektronicznej dowodu osobistego, dokonanego w trybie określonym w art. 32b ust. 1 pkt 1 ustawy przez pełnomocnika, opiekuna lub kuratora, dołącza się:

1\) pełnomocnictwo szczególne do dokonania zgłoszenia sporządzone na piśmie utrwalonym w postaci elektronicznej, opatrzonym przez posiadacza dowodu osobistego kwalifikowanym podpisem elektronicznym, podpisem zaufanym albo podpisem osobistym, albo dokument pozwalający na ustalenie stosunku prawnego istniejącego między wnoszącym zgłoszenie a osobą, w której imieniu zgłoszenie jest wnoszone, sporządzony na piśmie utrwalonym w postaci elektronicznej, albo

2\) odwzorowanie cyfrowe dokumentu, o którym mowa w pkt 1, opatrzone przez osobę dokonującą zgłoszenia kwalifikowanym podpisem elektronicznym, podpisem zaufanym albo podpisem osobistym.

§ 16. 1. Organ gminy, do którego zgłoszono zawieszenie lub cofnięcie zawieszenia certyfikatów zamieszczonych w warstwie elektronicznej dowodu osobistego w trybie określonym w art. 32b ust. 1 pkt 1 i 3 ustawy, ustala zgodność danych posiadacza dowodu osobistego z danymi zawartymi w dostępnych rejestrach publicznych oraz z danymi zawartymi w innych dokumentach tożsamości, jeśli są dostępne.

2\. W przypadku zawieszenia lub cofnięcia zawieszenia certyfikatów zamieszczonych w warstwie elektronicznej dowodu oso bistego w trybie określonym w art. 32b ust. 1 pkt 2 ustawy ustalenie zgodności danych, o których mowa w ust. 1, następuje automatycznie przez porównanie danych przekazywanych przez usługę elektroniczną, za której pomocą zgłoszono zawieszenie lub cofnięcie zawieszenia, z danymi zawartymi w Rejestrze Dowodów Osobistych.

§ 17. Zgłoszenie zawieszenia lub cofnięcia zawieszenia certyfikatów w warstwie elektronicznej dowodu osobistego dokonane w trybie określonym w art. 32b ust. 1 pkt 2 ustawy powoduje automatyczne zawieszenie lub cofnięcie zawieszenia certyfikatów zamieszczonych w warstwie elektronicznej dowodu osobistego.

§ 18. Organ gminy, do którego zgłoszono zawieszenie lub cofnięcie zawieszenia certyfikatów zamieszczonych w warstwie elektronicznej dowodu osobistego w trybie określonym w art. 32b ust. 1 pkt 1 i 3 ustawy, dokonuje rejestracji tej czynności w Rejestrze Dowodów Osobistych przez zawieszenie lub cofnięcie zawieszenia dowodu osobistego i wprowadzenie daty i czasu zawieszenia lub daty i czasu cofnięcia zawieszenia.

§ 19. W przypadku zawieszenia lub cofnięcia zawieszenia certyfikatów zamieszczonych w warstwie elektronicznej dowodu osobistego w trybie określonym w art. 32b ust. 1 pkt 2 ustawy zaświadczenie, o którym mowa w art. 32b ust. 2 ustawy, jest generowane automatycznie przez usługę elektroniczną, za której pomocą zgłoszono zawieszenie lub cofnięcie zawieszenia.

§ 20. 1. Wzór zaświadczenia potwierdzającego zgłoszenie zawieszenia certyfikatów zamieszczonych w warstwie elektronicznej dowodu osobistego stanowi załącznik nr 2 do rozporządzenia.

2\. Wzór zaświadczenia potwierdzającego zgłoszenie cofnięcia zawieszenia certyfikatów zamieszczonych w warstwie elektronicznej dowodu osobistego stanowi załącznik nr 3 do rozporządzenia.

§ 21. Dane o zawieszeniu lub cofnięciu zawieszenia certyfikatów zamieszczonych w warstwie elektronicznej dowodu osobistego są przekazywane z Rejestru Dowodów Osobistych do systemu teleinformatycznego, który obsługuje funkcjonalności warstwy elektronicznej dowodu osobistego, prowadzonego przez ministra właściwego do spraw wewnętrznych, zwanego dalej „ministrem”.

§ 22. Unieważnienie certyfikatów zamieszczonych w warstwie elektronicznej dowodu osobistego oraz unieważnienie dowodu osobistego z powodu upływu terminu przewidzianego na cofnięcie zawieszenia następuje w sposób automatyczny.

§ 23. 1. Unieważnienia certyfikatów zamieszczonych w warstwie elektronicznej dowodu osobistego na podstawie art. 12g ust. 1 ustawy dokonuje minister w systemie teleinformatycznym, o którym mowa w § 21.

2\. Minister przekazuje ministrowi właściwemu do spraw informatyzacji informację o unieważnionych certyfikatach zamieszczonych w warstwie elektronicznej dowodu osobistego w celu aktualizacji statusów warstwy elektronicznej dowodów osobistych w Rejestrze Dowodów Osobistych, a w przypadku przedłużenia ważności dowodu osobistego w zakresie warstwy graficznej – informację o dacie ważności dowodu osobistego.

§ 24. Unieważnienie dowodu osobistego w Rejestrze Dowodów Osobistych powoduje unieważnienie certyfikatów zamieszczonych w warstwie elektronicznej dowodu osobistego. Dane o unieważnieniu dowodu osobistego są przekazywane z Rejestru Dowodów Osobistych do systemu teleinformatycznego, o którym mowa w § 21.

## Rozdział 6 – Przepis końcowy

§ 25. Rozporządzenie wchodzi w życie z dniem określonym w komunikacie wydanym na podstawie art. 75 ust. 1 pkt 3 ustawy z dnia 26 maja 2023 r. o aplikacji mObywatel (Dz. U. z 2024 r. poz. 1275 i 1717).5) Minister Spraw Wewnętrznych i Administracji: wz. T. Szymański

5\) Niniejsze rozporządzenie było poprzedzone rozporządzeniem Ministra Spraw Wewnętrznych i Administracji z dnia 26 lutego 2019 r. w sprawie warstwy elektronicznej dowodu osobistego (Dz. U. z 2022 r. poz. 1431), które traci moc z dniem określonym w komunikacie wydanym na podstawie art. 75 ust. 1 pkt 3 ustawy z dnia 26 maja 2023 r. o aplikacji mObywatel (Dz. U. z 2024 r. poz. 1275 i 1717) w związku z wejściem w życie art. 37 pkt 1 ustawy z dnia 26 maja 2023 r. o aplikacji mObywatel. /͘ ϭ͘ Warstwę elektroniczną ĚŽǁŽĚƵ ŽƐŽďŝƐƚĞŐŽ stanowią: ϭͿ ŵŝŬƌŽƉƌŽĐĞƐŽƌ͖ ϮͿ ďŝďůŝŽƚĞŬĂ ŬƌǇƉƚŽŐƌĂĨŝĐǌŶĂ͖ // ͘ ///͘ /s͘ ϯͿ Ɖů ĂƚĨŽƌŵĂ ŽƉĞƌĂĐǇũŶĂ͕ ǁ ƚǇŵ środowisko ŽƉƌŽŐƌĂŵŽǁĂŶŝĂ :ĂǀĂ ŽƌĂǌ ĚĞĚǇŬŽǁĂŶĞ ŽƉƌŽŐƌĂŵŽǁĂŶŝĞ͖ ϰͿ ŝŶƚĞƌĨĞũƐ ďĞǌƐƚǇŬŽǁǇ ǌŐŽĚŶǇ ǌ normą /^Kͬ/ ϭϰϰϰϯ ƚǇƉ ůƵď ͖ ϱͿ ĂƉůĞƚ ůƵď ĂƉůĞƚǇ :ĂǀĂ odpowiadające ǌĂ funkcjonalności określone ǁ Ăƌƚ͘ ϭϮĂ ƵƐƚĂǁǇ ǌ ĚŶŝĂ ϲ ƐŝĞƌƉŶŝĂ ϮϬϭϬ ƌ͘ Ž ĚŽǁŽĚĂĐŚ ŽƐŽďŝƐƚǇĐŚ ;ǌ͘ h͘ ǌ ϮϬϮϮ ƌ͘ ƉŽǌ͘ ϲϳϭ, z późn. zm.Ϳ͕ ǌǁĂŶĞũ ĚĂůĞũ „ustawą”. Ϯ͘ tĂƌƐƚǁĂ ĞůĞŬƚƌŽŶŝĐǌŶĂ ĚŽǁŽĚƵ ŽƐŽďŝƐƚĞŐŽ może być ǌďƵĚŽǁĂŶĂ ǌ komponentów ǁ ŝŶŶĞũ ŬŽŶĨŝŐƵƌĂĐũŝ niż określona ǁ ƉŬƚ ϭ͕ które łącznie spełniają ƚĞ ƐĂŵĞ ǁǇŵĂŐĂŶŝĂ bezpieczeństwa ŝ ƉŽǌŝŽŵƵ ƵǌĂƐĂĚŶŝĞŶŝĂ ǌĂƵĨĂŶŝĂ͘ ϯ͘ tĂƌƐƚǁĂ ĞůĞŬƚƌŽŶŝĐǌŶĂ ĚŽǁŽĚƵ ŽƐŽďŝƐƚĞŐŽ ǁƌĂǌ ǌ dokumentacją ją opisującą ƐƚĂŶŽǁŝą łącznie ƉƌǌĞĚŵŝŽƚ ŽĐĞŶǇ ǁ ƌŽǌƵŵŝĞŶŝƵ ŶŽƌŵǇ WEͲE /^Kͬ/ ϭϱϰϬϴ ůƵď ŶŽƌŵǇ równoważnej. ϭ͘ tĂƌƐƚǁĂ ĞůĞŬƚƌŽŶŝĐǌŶĂ ĚŽǁŽĚƵ ŽƐŽďŝƐƚĞŐŽ podlega ocenie bezpieczeństwa zgodnie ǌ ǁǇŵĂŐĂŶŝĂŵŝ ǌĂǁĂƌƚǇŵŝ ǁ ŶŽƌŵŝĞ WEͲE /^Kͬ/ ϭϱϰϬϴ ůƵď ŶŽƌŵŝĞ równoważnĞũ͘ Ϯ͘ KĐĞŶǇ bezpieczeństwa ŝ ĐĞƌƚǇĨŝŬĂĐũŝ ĚŽŬŽŶƵũĞ się ŶĂ zgodność ǌ ƉƌŽĨŝůĞŵ zabezpieczeń ;ĂŶŐ͘ WƌŽƚĞĐƚŝŽŶ WƌŽĨŝůĞͿ ůƵď ŶĂ zgodność ǌĞ specyfikacją techniczną ;ĂŶŐ͘ ^ĞĐƵƌŝƚǇ dĂƌŐĞƚͿ ǁĂƌƐƚǁǇ ĞůĞŬƚƌŽŶŝĐǌŶĞũ ĚŽǁŽĚƵ ŽƐŽďŝƐƚĞŐŽ͘ ϯ͘ ĞƌƚǇĨŝŬĂĐũŝ ĚŽŬŽŶƵũĞ ũĞĚŶŽƐƚŬĂ certyfikująca, która ǌĂƉĞǁŶŝĂ ƵǌŶĂŶŝĞ ĐĞƌƚǇĨŝŬĂƚƵ ǌŐŽĚŶŝĞ ǌ ƉŽƌŽǌƵŵŝĞŶŝĂŵŝ międzynarodowymi: WŽƌŽǌƵŵŝĞŶŝĞŵ Ž ǁǌĂũĞŵŶǇŵ ƌĞƐƉĞŬƚŽǁĂŶŝƵ rezultatów ŽĐĞŶǇ ŝ ĐĞƌƚǇĨŝŬĂĐũŝ ďĞǌƉŝĞĐǌŶǇĐŚ produktów ŝŶĨŽƌŵĂƚǇĐǌŶǇĐŚ Ͳ Z ůƵď hmową w sprawie uznawania certyfikatów Common Criteria Ͳ ^K'/^ͲDZ͕ ůƵď ƵƌŽƉĞũƐŬŝŵ ƐĐŚĞŵĂƚĞŵ certyfikacji cyberbezpieczeństwa zgodnym z Common Criteria;hͿ͘ ϭ͘ WƌŽ Ĩŝů zabezpieczeń, Ž kt órym ŵŽǁĂ ǁ ƉŬƚ //͘ Ϯ͕ ũĞƐƚ ĚŽŬƵŵĞŶƚĞŵ ƉƵďůŝĐǌŶŝĞ dostępnym, ƉƵďůŝŬŽǁĂŶǇŵ ƉƌǌĞǌ niezależne ŽĚ ƉƌŽĚƵĐĞŶƚĂ ǁĂƌƐƚǁǇ ĞůĞŬƚƌŽŶŝĐǌŶĞũ ũĞĚŶŽƐƚŬŝ zajmujące się certyfikacją. Ϯ͘ ^ƉĞĐǇĨŝŬĂĐũĂ ƚĞĐŚŶŝĐǌŶĂ ǁĂƌƐƚǁǇ ĞůĞŬƚƌŽŶŝĐǌŶĞũ ĚŽǁŽĚƵ ŽƐŽďŝƐƚĞŐŽ ũĞƐƚ ǌŐŽĚŶĂ ǌ ƉƌŽĨŝůĞŵ zabezpieczeń, Ž którym mowa ǁ ƉŬƚ ϭ͕ jeśli ƚĞŶ ƉƌŽĨŝů zabezpieczeń został opracowany. ϯ͘ ^ƉĞĐǇĨŝŬĂĐũĂ ƚĞĐŚŶŝĐǌŶĂ ǁĂƌƐƚǁǇ ĞůĞŬƚƌŽŶŝĐǌŶĞũ ĚŽǁŽĚƵ ŽƐŽďŝƐƚĞŐŽ ǁ części, ǁ której ŽƉŝƐĂŶŽ szczegółowy sposób ƌĞĂůŝǌĂĐũŝ wymagań bezpieczeństwa, może stanowić tajemnicę przedsiębiorstwa ǁ ƌŽǌƵŵŝĞŶŝƵ ƉƌǌĞƉŝƐƵ Ăƌƚ͘ ϭϭ ƵƐƚ͘ Ϯ ƵƐƚĂǁǇ ǌ ĚŶŝĂ ϭϲ ŬǁŝĞƚŶŝĂ ϭϵϵϯ ƌ͘ Ž ǌǁĂůĐǌĂŶŝƵ ŶŝĞƵĐǌĐŝǁĞũ ŬŽŶŬƵƌĞŶĐũŝ ;ǌ͘ h͘ ǌ ϮϬϮϮ ƌ͘ ƉŽǌ͘ ϭϮϯϯͿ͘ ϭ͘ t ƉƌǌǇƉĂĚŬƵ ŐĚǇ ŽĐĞŶĂ bezpieczeństwa ǁĂƌƐƚǁǇ ĞůĞŬƚƌŽŶŝĐǌŶĞũ ƉƌŽǁĂĚǌŽŶĂ ũĞƐƚ ũĂŬŽ ŽĐĞŶĂ złożona ;ĂŶŐ͘ ŽŵƉŽƐŝƚĞ ǀĂůƵĂƚŝŽŶͿ͕ ǁǇŵĂŐĂŶĞ ũĞƐƚ͕ ĂďǇ ƐƉĞĐǇĨŝŬĂĐũĂ ƚĞĐŚŶŝĐǌŶĂ zawierała ŽƉŝƐǇ͗ ϭͿ spójności ƉŽůŝƚǇŬŝ bezpieczeństwa produktu złożonego; ϮͿ ƐƉŽƐŽďƵ ŝŶƚĞŐƌĂĐũŝ poszczególnych komponentów ƚĞŐŽ ƉƌŽĚƵŬƚƵ͖ ϯͿ ƉƌŽĐĞĚƵƌ ĚŽƐƚĂǁ poszczególnych komponentów; ϰͿ spójności wewnętrznej ƉƌŽũĞŬƚƵ ƉƌŽĚƵŬƚƵ złożonego; ϱͿ testów funkcjonalnych produktu złożonego; ϲͿ ŽĐĞŶǇ podatności ŶĂ zagrożenia.

## Załączniki do rozporządzenia Ministra Spraw Wewnętrznych

i Admi

nistracji z dni

a 21 lutego 2025 r. (Dz. U. poz. 267)

## Załącznik nr 1

WYMAGANIA TECHNICZNE DLA WARSTWY ELEKTRONICZNEJ DOWODU OSOBISTEGO Ϯ͘ ŽƉƵƐǌĐǌĂ się, że poszczególne ŬŽŵƉŽŶĞŶƚǇ ǁĂƌƐƚǁǇ ĞůĞŬƚƌŽŶŝĐǌŶĞũ ĚŽǁŽĚƵ ŽƐŽďŝƐƚĞŐŽ będącego ƉƌǌĞĚŵŝŽƚĞŵ ŽĐĞŶǇ bezpieczeństwa mogąmieć ĐĞƌƚǇĨŝŬĂƚǇ ƵƉƌǌĞĚŶŝŽ ǁǇĚĂŶĞ ƉƌǌĞǌ jednostkę certyfikującą,Ž której ŵŽǁĂ ǁ ƉŬƚ //͘ ϯ͘

s͘

ϭ͘ KĐĞ

ŶĂ bezpieczeństwa ŵŝŬƌŽƉƌŽĐĞƐŽƌĂ ũĞƐƚ ĚŽŬŽŶǇǁĂŶĂ ŶĂ ƉŽǌŝŽŵŝĞ ƵǌĂƐĂĚŶŝŽŶĞŐŽ ǌĂƵĨĂŶŝĂ ĚŽ zgodności ǌ ǁǇŵĂŐĂŶŝĂŵŝ ŶĂ ƉŽǌŝŽŵŝĞ ŶŝĞ niższym niż EAL5, zgodnie z normą PNͲE /^Kͬ/ ϭϱϰϬϴ ůƵď normą równoważną, rozszerzonym o komponenty uzasadnienia zaufania zgodnie z normą PN ͲE /^Kͬ/ ϭϱϰϬϴ ůƵď normą równoważną, obejmujące co najmniej AVA\_VAN.5, &gt;ͺs^͘Ϯ͘

Ϯ͘ KĐĞŶĂ bezpieczeństwa ƉůĂƚĨŽƌŵǇ ŽƉĞƌĂĐǇũŶĞũ ũĞƐƚ ĚŽŬŽŶǇǁĂŶĂ ŶĂ ƉŽǌŝŽŵŝĞ ƵǌĂƐĂĚŶŝŽŶĞŐŽ ǌĂƵĨĂŶŝĂ ĚŽ zabezpieczeń ŶŝĞ niższym niżƉŽǌŝŽŵ EAL5, zgodnie z normą PNͲE /^Kͬ/ ϭϱϰϬϴ ůƵď normą równoważną, rozszerzonym o komponenty uzasadnienia zaufania zgodnie z normą WEͲE /^Kͬ/ ϭϱϰϬϴůƵď normą równoważną, obejmujące cŽ ŶĂũŵŶŝĞũ sͺsE͘ϱ͕ &gt;ͺs^͘Ϯ͘ ϯ͘ KĐĞŶĂ bezpieczeństwa ĂƉůĞƚƵ ũĞƐƚ ĚŽŬŽŶǇǁĂŶĂ ŶĂ ƉŽǌŝŽŵŝĞ ƵǌĂƐĂĚŶŝŽŶĞŐŽ ǌĂƵĨĂŶŝĂ ĚŽ zabezpieczeń ŶŝĞ niższym niż ƉŽǌŝŽŵ EAL4, zgodnie z normą PNͲE /^Kͬ/ ϭϱϰϬϴ ůƵď normą równoważną, rozszerzonym o komponenty ƵǌĂƐĂĚŶŝĞŶŝĂ ǌĂƵĨĂŶŝĂ ǌ godnie z normą PNͲE /^Kͬ/ ϭϱϰϬϴ ůƵď normą równoważną, obejmujące co najmniej AVA\_VAN.5, ALC\_DVS.2. s/͘

DŝŬ

ƌŽƉƌŽĐĞƐŽƌ spełnia następująceŵŝŶŝŵĂůŶĞ ǁǇŵĂŐĂŶŝĂ͗

ϭͿ ƵƚƌǌǇŵƵũĞ integralność ĚĂŶǇĐŚ użytkownika, które są ƉƌǌĞƚǁĂƌǌĂŶĞ ŝ ƉƌǌĞĐŚŽǁǇǁĂŶĞ ǁ pamięci ŵŝŬƌŽƉƌŽĐĞƐŽƌĂ͖

ϮͿ ƵƚƌǌǇŵƵũĞ poufność ĚĂŶǇĐŚ użytkownika, które są ƉƌǌĞƚǁĂƌǌĂŶĞ ŝ ƉƌǌĞĐŚŽǁǇǁĂŶĞ ǁ pamięci ŵŝŬƌŽƉƌŽĐĞƐŽƌĂ͖

ϯͿ ǌĂƉĞǁŶŝĂ poprawność wszystkich funkcji bezpieczeństwa realizowanych przez mikroprocesor; ϰͿ ǌĂƉĞǁŶŝĂ ůŽƐŽǁĞ ŐĞŶĞƌŽǁĂŶŝĞ ůŝĐǌď ǁ ĐĞůƵ ƌĞĂůŝǌĂĐũŝ ĨƵŶŬĐũŝ ŬƌǇƉƚŽŐƌĂĨŝĐǌŶǇĐŚ͖ ϱͿ ǌĂƉĞǁŶŝĂ ŽĐŚƌŽŶę ƉƌǌĞĚ ǁǇĐŝĞŬŝĞŵ ŝŶĨŽƌŵĂĐũŝ wynikającym zarówno ǌ ƌĞĂůŝǌĂĐũŝ wewnętrznych ŽƉĞƌĂĐũŝ ŵŝŬƌŽƉƌŽĐĞƐŽƌĂ͕ ũĂŬ ŝ umyślnych działań atakującego; ϲͿ ǌĂƉĞǁŶŝĂ ŽĐŚƌŽŶ ę ƉƌǌĞĚ fizyczną ingerencją umożliwiającą ŽĚĐǌǇƚĂŶŝĞ ĚĂŶǇĐŚ użytkownika ƉƌǌĞĐŚŽǁǇǁĂŶǇĐŚ ǁ pamięci ŵŝŬƌŽƉƌŽĐĞƐŽƌĂ͖

ϳͿ ǌĂƉĞǁŶŝĂ ǁǇŬƌǇǁĂŶŝĞ prób ǁǇŵƵƐǌĞŶŝĂ ƌĞĂůŝǌĂĐũŝ ŽƉĞƌĂĐũŝ ŵŝŬƌŽƉƌŽĐĞƐŽƌĂ ŽƌĂǌ przeciwdziałaniĞ takim próbom ǁ ƐǇƚƵĂĐũĂĐŚ͕ ǁ których niezawodnośćŝ bez pieczeństwo tych ŽƉĞƌĂĐũŝ ŶŝĞ były ƚĞƐƚŽǁĂŶĞ ůƵď ƵĚŽǁŽĚŶŝŽŶĞ͖

ϴͿ ǌĂƉĞǁŶŝĂ ŽĐŚƌŽŶę ƉƌǌĞĚ ĨŝǌǇĐǌŶǇŵŝ ŵĂŶŝƉƵůĂĐũĂŵŝ wpływającymi ŶĂ ŽƉĞƌĂĐũĞ ŵŝŬƌŽƉƌŽĐĞƐŽƌĂ͕ ǁ ƚǇŵ ŶĂ ŽƉƌŽŐƌĂŵŽǁĂŶŝĞ ŵŝŬƌŽƉƌŽĐĞƐŽƌĂ͕ ĚĂŶĞ ǁǇŬŽƌǌǇƐƚǇǁĂŶĞ ĚŽ ƌĞĂůŝǌĂĐũŝ ĨƵŶŬĐũŝ bezpieczeństwa ŽƌĂǌ ĚĂŶĞ użytkownika;

ϵͿ ǌĂƉĞǁŶŝĂ ŽĐŚƌŽŶę ƉƌǌĞĚ ŶŝĞƵƉƌĂǁŶŝŽŶǇŵ użyciem ĨƵŶŬĐũŝ ĚĞĚǇŬŽǁĂŶǇĐŚ ĚŽ ƚĞƐƚŽǁĂŶŝĂ ŵŝŬƌŽƉƌŽĐĞƐŽƌĂ ŽƌĂǌ ŝŶŶǇĐŚ komponentów, ďůŽŬŽǁĂŶǇĐŚ ƉŽ zakończeniu ĨĂǌǇ ƚĞƐƚŽǁĂŶŝĂ urządzenia;

ϭϬͿ ǌĂƉĞǁŶŝĂ ŝĚĞŶƚǇĨŝŬĂĐũę ƉŽƉƌǌĞǌ ƵŵŝĞƐǌĐǌĞŶŝĞ ĚĂŶǇĐŚ inicjujących ŽƌĂǌ ĚĂŶǇĐŚ ƉƌǌĞĚ personalizacją ǁ ŶŝĞƵůŽƚŶĞũ pamięci ŵŝŬƌŽƉƌŽĐĞƐŽƌĂ͘

s//͘

DŝŬ

ƌŽƉƌŽĐĞƐŽƌ ůƵď ŵŝŬƌŽƉƌŽĐĞƐŽƌ ǁƌĂǌ ǌ implementacją ďŝďůŝŽƚĞŬ ŬƌǇƉƚŽŐƌĂĨŝĐǌŶǇĐŚ spełnia następujące ǁǇŵĂŐĂŶŝĂ͗

ϭͿ ƌĞĂůŝǌƵũĞ sprzętowe ĨƵŶŬĐũĞ ƐǌǇĨƌŽǁĂŶŝĂ ^͖

ϮͿ obsługuje następujące ĂůŐŽƌǇƚŵǇ ŬƌǇƉƚŽŐƌĂĨŝĐǌŶĞ͗

ĂͿ ƐǇŵĞƚƌǇĐǌŶĞ͗ ^͕

ďͿ ĂƐǇŵĞƚƌǇĐǌŶĞ͗ Z^͕ ^͕ ǁ ƚǇŵ ŐĞŶĞƌŽǁĂŶŝĂ ůƵď ŽďůŝĐǌĂŶŝĂ ƉĂƌ ŬůƵĐǌǇ͕ ĐͿ wymianę ŬůƵĐǌǇ͗ ,&lt;͕

ĚͿ funkcję skrótu: ^,ͲϮϮϰ͕ ^,ͲϮϱϲ͕ ^,Ͳϯϴϰ͕ ŝ ^,ͲϱϭϮ͖

ϯͿ ǁ ŽĚŶŝĞƐŝĞŶŝƵ ĚŽ algorytmów ŬƌǇƉƚŽŐƌĂĨŝĐǌŶǇĐŚ ^ ŝ Z^ – ǌĂƉĞǁŶŝĂ składanie ŝ weryfikację ƉŽĚƉŝƐƵ͖

ϰͿ ƌĞĂůŝǌƵũĞ ĨƵŶŬĐũĞ ŬƌǇƉƚŽŐƌĂĨŝĐǌŶĞ wymagające ŬŽƉŝŽǁĂŶŝĂ͕ porównywania, powtórnego użycia określonych obszarów pamięci ŽƉĞƌĂĐǇũŶĞũ͕ ǌĂƉĞǁŶŝĂ ochronę ƉƌǌĞĚ podatnościami ǌŶĂŶǇŵŝ ǁ ŵŽŵĞŶĐŝĞ ǁǇŬŽŶĂŶŝĂ oceny bezpieczeństwa;

ϱͿ ǌĂƉĞǁŶŝĂ środki bezpieczeństwaƉƌǌĞĚ ƉŽǌŽƐƚĂǁŝĞŶŝĞŵ ŝŶĨŽƌŵĂĐũŝ szczątkowych ǁ pamięci ŽƉĞƌĂĐǇũŶĞũ ƉŽ ǌƌĞĂůŝǌŽǁĂŶŝƵ ĨƵŶŬĐũŝ ŬƌǇƉƚŽŐƌĂĨŝĐǌŶĞũ͘

s///͘

Pl

atforma operacyjna warstwy elektronicznej dowodu osobistego spełnia wymagania funkcjonalne i wymagania bezpieczeństwa określone w profilu zabezpieczeń, zawarte w dokumencie „Java Card WƌŽƚĞĐƚŝŽŶ WƌŽĨŝůĞ Ͳ Open Configuration, Version 3.0, May 2012” (ANSSIͲWWͲϮϬϭϬͬϬϯͲDϬϭͿ ůƵď ŶŽǁƐǌǇŵ͕ z zastrzeżeniem pkt I. 2.

/y͘

ϭ͘ ƉůĞƚ ǁ cz ęści realizującej funkcjęďĞǌƉŝĞĐǌŶĞŐŽ urządzenia ĚŽ składania ŬǁĂůŝĨŝŬŽǁĂŶĞŐŽ ƉŽĚƉŝƐƵ ĞůĞŬƚƌŽŶŝĐǌŶĞŐŽ ĂůďŽ urządzenia ĚŽ składania ƉŽĚƉŝƐƵ ŽƐŽďŝƐƚĞŐŽ spełnia ǁǇŵĂŐĂŶŝĂ bezpieczeństwa określoneǁ ŶŽƌŵŝĞ WEͲE ϰϭϵϮϭϭͲϮ ĂůďŽ ǁ ŶŽƌŵŝĞ WEͲE ϰϭϵϮϭϭͲϯ ůƵď ǁ ŶŽƌŵĂĐŚ ũĞ zastępujących.

Ϯ͘ Aplet w części realizującej funkcję dokumentu uznawanego zgodnie z odrębnymi przepisami za dokument podróży spełnia wymagania bezpieczeństwa określone w profilu zabezpieczeń BSI Ͳ ͲͲWWͲϬϬϲϴͲsϮͲϮϬϭϭ͕ ŽŵŵŽŶ ƌŝƚĞƌŝĂ WƌŽƚĞĐƚŝŽŶ WƌŽĨŝůĞ͕ DĂĐŚŝŶĞ ZĞĂĚĂďůĞ dƌĂǀĞů ŽĐƵŵĞŶƚ with „ICAO Application”, Extended Access Control with PACE (EAC PP); BSI ͲͲWWͲϬϬϱϲͲsϮͲ ͲϮϬϭϮ͘

ϯ͘ ƉůĞƚ ǁ części realizującejĨƵŶŬĐũĞ ǁƐŬĂǌĂŶĞ ǁ Ăƌƚ͘ ϭϮĂ ƵƐƚ͘ ϭ ƉŬƚ Ϯ–ϱ ƵƐƚĂǁǇ spełnia następujące ǁǇŵĂŐĂŶŝĂ bezpieczeństwa ůƵď ŬŽƌǌǇƐƚĂ ǌĞ środków ŽĐŚƌŽŶǇ ǌĂƉĞǁŶŝĂŶǇĐŚ ƉƌǌĞǌ inne komponenty warstwy elektronicznej dowodu osobistego w celu spełnienia tych wymagań: ϭͿ ǌĂƉĞǁŶŝĂ integralność ĚĂŶǇĐŚ użytkownika ŽƌĂǌ ĚĂŶǇĐŚ służących ĚŽ ƌĞĂůŝǌĂĐũŝ ĨƵŶŬĐũŝ bezpieczeństwa ƉŽĚĐǌĂƐ͗

ĂͿ ƉƌǌĞĐŚŽǁǇǁĂŶŝĂ͕ ƚǌŶ͘ ǌĂƉĞǁŶŝĞŶŝĂ ŽĐŚƌŽŶǇ ƚǇĐŚ ĚĂŶǇĐŚ ƉƌǌĞĚ nieuprawnioną modyfikacją ůƵď manipulacją,

ďͿ ǁǇŵŝĂŶǇ danych między ĂƉůĞƚĞŵ Ă dostawcą usługi zewnętrznej, ƉŽ ƵǁŝĞƌǌǇƚĞůŶŝĞŶŝƵ ƚĞƌŵŝŶĂůĂ ŽƌĂǌ ǁĂƌƐƚǁǇ ĞůĞŬƚƌŽŶŝĐǌŶĞũ ĚŽǁŽĚƵ ŽƐŽďŝƐƚĞŐŽ͖

ϮͿ ǌĂƉĞǁŶŝĂ autentyczność:

ĂͿ ĚĂŶǇĐŚ użytkownika ŽƌĂǌ ĚĂŶǇĐŚ służących ĚŽ ƌĞĂůŝǌĂĐũŝ ĨƵŶŬĐũŝ bezpieczeństwa ƉŽĚĐǌĂƐ ƉƌǌĞĐŚŽǁǇǁĂŶŝĂ ƉƌǌĞǌ umożliwienie ǁĞƌǇĨŝŬĂĐũŝ ŝĐŚ autentyczności ƉŽ ƐƚƌŽŶŝĞ ƚĞƌŵŝŶĂůĂ͕

ďͿ ĚĂŶǇĐŚ użytkownika ƉŽĚĐǌĂƐ ŝĐŚ ǁǇŵŝĂŶǇ między ĂƉůĞƚĞŵ Ă dostawcą usługi zewnętrznej ƉŽ ƵǁŝĞƌǌǇƚĞůŶŝĞŶŝƵ ƚĞƌŵŝ ŶĂ ůĂ ŽƌĂǌ ǁĂƌƐƚǁǇ ĞůĞŬƚƌŽŶŝĐǌŶĞũ ĚŽǁŽĚƵ ŽƐŽďŝƐƚĞŐŽ͖

ϯͿ ǌĂƉĞǁŶŝĂ poufność ĚĂŶǇĐŚ użytkownika ŽƌĂǌ ĚĂŶǇĐŚ służących ĚŽ ƌĞĂůŝǌĂĐũŝ ĨƵŶŬĐũŝ bezpieczeństwa:

ĂͿ ƉƌǌĞǌ ŶĂĚĂŶŝĞ ƉƌĂǁ ĚŽ ŽĚĐǌǇƚƵ ũĞĚǇŶŝĞ ƉŽƉƌĂǁŶŝĞ ƵǁŝĞƌǌǇƚĞůŶŝŽŶǇŵ ƚĞƌŵŝŶĂůŽŵ͕ ǌ określonym poziomem ich ĂƵƚŽƌǇǌĂĐũŝ͕

ďͿ ƉŽĚĐǌĂƐ ǁǇŵŝĂŶǇ ĚĂŶǇĐŚ między ĂƉůĞƚĞŵ Ă dostawcą usługi zewnętrznej, ƉŽ ƵǁŝĞƌǌǇƚĞůŶŝĞŶŝƵ ƚĞƌŵŝŶĂůĂ ŽƌĂǌ ǁĂƌƐƚǁǇ ĞůĞŬƚƌŽŶŝĐǌŶĞũ ĚŽǁŽĚƵ ŽƐŽďŝƐƚĞŐŽ͖ ϰͿ ǌĂƉĞǁŶŝĂ ochronę ƉƌǌĞĚ śledzeniem ŝĚĞŶƚǇĨŝŬĂƚŽƌĂ ǁĂƌƐƚǁǇ ĞůĞŬƚƌŽŶŝĐǌŶĞũ ĚŽǁŽĚƵ ŽƐŽďŝƐƚĞŐŽ ǌĂ pośrednictwem monitorowania ŝŶƚĞƌĨĞũƐƵ ďĞǌƐƚǇŬŽǁĞŐŽ͕ ǁ ƐǇƚƵĂĐũŝ ŐĚǇ ŶŝĞ posiadał ƵƉƌǌĞĚŶŝŽ ŝŶĨŽƌŵĂĐũŝ Ž ƉŽƉƌĂǁŶǇĐŚ wartościach współdzielonych kodów ;ŵŝŶŝŵƵŵ E ůƵď DZͿ͖

ϱͿ ǌĂƉĞǁŶŝĂ ƚĞƌŵŝŶĂůŽǁŝ͕ ǌ którym nawiązywane ũĞƐƚ połączenie, możliwość ǁĞƌǇĨŝŬĂĐũŝ ƐǁŽũĞũ autentyczności ũĂŬŽ całego urządzenia ĚŽƐƚĂƌĐǌŽŶĞŐŽ ƉƌǌĞǌ wydawcę ǁĂƌƐƚǁǇ ĞůĞŬƚƌŽŶŝĐǌŶĞũ ĚŽǁŽĚƵ ŽƐŽďŝƐƚĞŐŽ ǌĂ pomocą ŬƌǇƉƚŽŐƌĂĨŝĐǌŶŝĞ ƉŽƚǁŝĞƌĚǌĂŶǇĐŚ ĚĂŶǇĐŚ͖ ϲͿ ǌĂƉĞǁŶŝĂ ochronę ĨƵŶŬĐũŝ͕ które ŶŝĞ są używane ǁ ĨĂǌŝĞ ŽƉĞƌĂĐǇũŶĞũ͕ ƉƌǌĞĚ ŝĐŚ nadużywaniem ǁ ĐĞůƵ͗

ĂͿ ǌŵĂŶŝƉƵůŽǁĂŶŝĂ ůƵď ƵũĂǁŶŝĞŶŝĂ ĚĂŶǇĐŚ użytkownika ůƵď ĚĂŶǇĐŚ służących ĚŽ ƌĞĂůŝǌĂĐũŝ ĨƵŶŬĐũŝ bezpieczeństwa ƉƌǌĞĐŚŽǁǇǁĂŶǇĐŚ ǁ ǁĂƌƐƚǁŝĞ ĞůĞŬƚƌŽŶŝĐǌŶĞũ ĚŽǁŽĚƵ ŽƐŽďŝƐƚĞŐŽ͕

ďͿ ǌŵĂŶŝƉƵůŽǁĂŶŝĂ (obejścia, ǌĂďůŽŬŽǁĂŶŝĂ ůƵď ǌŵŽĚǇĨŝŬŽǁĂŶŝĂͿ ĨƵŶŬĐũŝ bezpieczeństwa ƌĞĂůŝǌŽǁĂŶǇĐŚ ƉƌŽŐƌĂŵŽǁŽ͖

ϳͿ ǌĂƉĞǁŶŝĂ ochronę ƉƌǌĞĚ ƵũĂǁŶŝĞŶŝĞŵ ĚĂŶǇĐŚ użytkownika ŽƌĂǌ ĚĂŶǇĐŚ służących ĚŽ ƌĞĂůŝǌĂĐũŝ ĨƵŶŬĐũŝ bezpieczeństwa, ƉƌǌĞĐŚŽǁǇǁĂŶǇĐŚ ůƵď ƉƌǌĞƚǁĂƌǌĂŶǇĐŚ͕ ǌĂ pomocą: ĂͿ ŵŽŶŝƚŽƌŽǁĂŶŝĂ ŝ ĂŶĂůŝǌǇ poprawności ŽƉĞƌĂĐũŝ ŶĂ ƉŽǌŝŽŵŝĞ sygnałowym, zarówno ǁ ŽĚŶŝĞƐŝĞŶŝƵ ĚŽ ŽƉĞƌĂĐũŝ wewnętrznych, ũĂŬ ŝ ŶĂ interfejsach zewnętrznych, ďͿ ǁǇŵƵƐǌĂŶŝĂ ŶŝĞƉŽƉƌĂǁŶĞŐŽ działania ĨƵŶŬĐũŝ ǁ ǁĂƌƵŶŬĂĐŚ ǁǇŬƌǇĐŝĂ ĂƚĂŬƵ͕ ĐͿ ǁǇŬƌǇǁĂŶŝĂ ŝ ƌĞĂŬĐũŝ ŶĂ próby ĨŝǌǇĐǌŶĞũ ŵĂŶŝƉƵůĂĐũŝ͖

ϴͿ zapewnia poufność i integralność danych użytkownika, danych służących do realizacji funkcji bezpieczeństwa oraz zabezpiecza, dzięki ǁďƵĚŽǁĂŶĞŵƵ ŽƉƌŽŐƌĂŵŽǁĂŶŝƵ ǁĂƌƐƚǁǇ ĞůĞŬƚƌŽŶŝĐǌŶĞũ ĚŽǁŽĚƵ ŽƐŽďŝƐƚĞŐŽ͕ ƉƌǌĞĚ ŶĂƌƵƐǌĞŶŝĞŵ bezpieczeństwa fizycznego przez zastosowanie środków chroniących przed atakami polegającymi na: ĂͿ ƉŽŵŝĂƌǌĞ napięcia ůƵď natężenia prądu ŶĂ ƐƚǇŬĂĐŚ ŐĂůǁĂŶŝĐǌŶǇĐŚ ƉŽǁŝĞƌǌĐŚŶŝ układu ƐĐĂůŽŶĞŐŽ͕ ǌ wyłączeniem obwodów połączonych ;ǌ użyciem ƐƚĂŶĚĂƌĚŽǁǇĐŚ narzędzi pomiaru napięcia lub natężeniaprądu),

ďͿ wykorzystaniu innych rodzajów ĨŝǌǇĐǌŶĞŐŽ współdziałania ładunków ĞůĞŬƚƌǇĐǌŶǇĐŚ͕ ĐͿ ŬŽŶƚƌŽůŽǁĂŶĞũ ŵĂŶŝƉƵůĂĐũŝ zawartością pamięci ǁ ĐĞůƵ ƉŽǌǇƐŬĂŶŝĂ ĚĂŶǇĐŚ użytkownika lub danych służących do realizacjiĨƵŶŬĐũŝ bezpieczeństwa

– bazując ŶĂ ƵƉƌǌĞĚŶŝŵ ǁǇŬŽŶĂŶŝƵ inżynierii ǁƐƚĞĐǌŶĞũ ƵǌǇƐŬĂŶĞŐŽ ŬŽĚƵ ďŝŶĂƌŶĞŐŽ͘
