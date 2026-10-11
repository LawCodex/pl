---
title: "Rozporządzenie Ministra Cyfryzacji z dnia 16 września 2026 r. w sprawie szczegółowych wymagań dotyczących adresowania dla właściwego kierowania połączeń, numeracji punktów sygnalizacyjnych oraz tworzenia i udostępniania znaków identyfikujących abonenta"
identifier: "DU/2026/1265"
official_citation: "Dz.U. 2026 poz. 1265"
type: regulation
jurisdiction: pl
language: pl
date: 2026-09-16
promulgated: 2026-09-28
entry_into_force: 2026-10-01
status: in_force
official_status: "obowiązujący"
text_version: "tekst ogłoszony (original)"
text_format: "pdf (text extracted)"
source: "https://api.sejm.gov.pl/eli/acts/DU/2026/1265"
source_text: "https://api.sejm.gov.pl/eli/acts/DU/2026/1265/text/I/D20261265.pdf"
isap: "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260001265"
retrieved: 2026-10-12
---

# Rozporządzenie Ministra Cyfryzacji z dnia 16 września 2026 r. w sprawie szczegółowych wymagań dotyczących adresowania dla właściwego kierowania połączeń, numeracji punktów sygnalizacyjnych oraz tworzenia i udostępniania znaków identyfikujących abonenta

ROZPORZĄDZENIE MINISTRA CYFRYZACJI 1) z dnia 16 września 2026 r. w sprawie szczegółowych wymagań dotyczących adresowania dla właściwego kierowania połączeń, numeracji punktów sygnalizacyjnych oraz tworzenia i udostępniania znaków identyfikujących abonenta Na podstawie art. 162 ust. 4 ustawy z dnia 12 lipca 2024 r. – Prawo komunikacji elektronicznej (Dz. U. poz. 1221, z 2025 r. poz. 637 i 820 oraz z 2026 r. poz. 252 i 815) zarządza się, co następuje:

§ 1. Szczegółowe wymagania dotyczące adresowania dla właściwego kierowania połączeń, numeracji punktów sygnalizacyjnych oraz tworzenia i udostępniania znaków identyfikujących abonenta określa załącznik do rozporządzenia.

§ 2. Rozporządzenie wchodzi w życie z dniem 1 października 2026 r., z wyjątkiem pkt 4 ppkt 2, pkt 5 ppkt 1 w zakresie, w jakim dotyczy sieci wykorzystujących protokół sygnalizacyjny SIP, oraz pkt 5 ppkt 2 załącznika do rozporządzenia, które wchodzą w życie z dniem 1 września 2027 r.2)

Minister Cyfryzacji: K. Gawkowski

## Załącznik do rozporządzenia Ministra Cyfryzacji

z dnia 16 września 2026 r. (Dz. U. poz. 1265)

SZCZEGÓŁOWE WYMAGANIA DOTYCZĄCE ADRESOWANIA DLA WŁAŚCIWEGO KIEROWANIA POŁĄCZEŃ, NUMERACJI PUNKTÓW SYGNALIZACYJNYCH ORAZ TWORZENIA I UDOSTĘPNIANIA ZNAKÓW IDENTYFIKUJĄCYCH ABONENTA

1\. Użyte w załączniku pojęcia i skróty oznaczają:

1\) abonent A – użytkownik inicjujący połączenie;

2\) AB – wskaźnik strefy numeracyjnej;

3\) abonent B – adresat, do którego jest kierowane połączenie;

4\) adresowanie metodą „en –bloc” – sposób adresowania polegający na równoczesnym przekazywaniu wszystkich cyfr numeru abonenta przez umieszczenie ich w jednym bloku wiadomości przesyłanych w procesie zestawiania połączenia;

5\) numer AUS – numery abonenckich usług specjalnych, przeznaczone dla usług świadczonych w sieci stacjonarnej, polegających na udzielaniu różnych informacji, przyjmowaniu zleceń oraz całodobowym przyjmowaniu wywołań kierowanych na numery alarmowe;

6\) „C hex” – parametr adresacyjny wykorzystywany w procesie kierowania połączeń, którego wartość jest przedstawiana w systemie szesnastkowym;

7\) CLIR (Calling Line Identification Restriction) – mechanizm stosowany w publicznych sieciach telekomunikacyjnych umożliwiający ograniczenie prezentacji informacji adresowej identyfikującej abonenta A; mechanizm ten nie wpływa na przekazywanie informacji adresowej między elementami sieci niezbędnej dla właściwego kierowania połączeń;

8\) DNS – rozproszony system adresacji wykorzystywany w procesie kierowania połączeń w sieciach IP, służący do odwzorowywania numerów i identyfikatorów logicznych na adresy i parametry sieciowe węzłów publicznych sieci telekomunikacyjnych realizujących zestawianie połączeń;

9\) FQDN – pełna, jednoznaczna nazwa domenowa, określająca położenie danego węzła publicznej sieci telekomunikacyjnej w systemie DNS;

10\) HOST – ID – numer centrali albo innego węzła publicznej sieci telekomunikacyjnej, który obsługuje lokalizację abonenta z przeniesionym numerem;

11\) ISPC – numer międzynarodowego punktu sygnalizacyjnego;

12\) karta SIM (Subscriber Identity Module) – wielofunkcyjna, inteligentna karta identyfikacyjna;

13\) KNA – krajowy numer abonenta;

14\) nagłówki P-Asserted-Identity oraz Privacy – informacje adresowe abonenta przenoszone przez sieć SIP z wykorzystaniem mechanizmów zawartych w zaleceniach dotyczących SIP opublikowanych przez IETF (Internet Engineering Task Force) RFC 33251) oraz RFC 33232), wydanych w 2002 r.;

15\) nagłówek From – informacja adresowa abonenta przenoszona przez sieć SIP z wykorzystaniem mechanizmów zawartych w zaleceniu dotyczącym SIP opublikowanym przez IETF w dokumencie RFC 32613), wydanym w 2002 r.;

16\) NKA – numer kierowania alarmowego związany z położeniem abonenta w obszarze gminy wykorzystywany do realizowania połączeń do numerów alarmowych;

17\) NSPC – numer krajowego punktu sygnalizacyjnego;

18\) numer alarmowy – trzycyfrowy numer AUS lub wspólny numer alarmowy 112;

19\) NR – numer rutingowy;

20\) parametr Called Party Number – parametr stosowany w Systemie Sygnalizacji ITU-T nr 7 (SS7), zawarty w wiadomości IAM, zawierający w szczególności zakodowany numer abonenta wywoływanego;

21\) parametr NoA (Nature of Address) – wskaźnik określający typ adresu (numeru telefonu) przesyłanego w sygnalizacji;

22\) pole To – składowa część wiadomości INVITE zawierająca numer abonenta B;

23\) protokół ISUP (ISDN User Part) – część Systemu Sygnalizacji ITU-T nr 7 (Signaling System 7 – SS7), odpowiadająca za ustalanie, zarządzanie i zwalnianie połączeń w sieci publicznej PSTN oraz w sieciach ISDN;

24\) Request URI – pole w wiadomości INVITE zawierające numer abonenta B;

25\) SIP – protokół sygnalizacyjny służący do inicjowania, modyfikowania i kończenia sesji komunikacyjnych w sieciach opartych na protokole internetowym (Internet Protocol);

26\) SN – strefa numeracyjna dla części obszaru kraju będąca częścią stacjonarnej publicznej sieci telekomunikacyjnej;

27\) wiadomość IAM (Initial Address Message) – wiadomość zawarta w ISUP, przesyłana w procesie zestawiania połączenia;

28\) wiadomość INVITE – wiadomość zawarta w SIP przesyłana między urządzeniami w celu zestawienia połączenia między nimi;

29\) znak identyfikujący abonenta A – informacja adresowa identyfikująca abonenta inicjującego połączenie, obejmująca KNA;

30\) znak identyfikujący abonenta B – informacja adresowa identyfikująca abonenta wywoływanego w procesie zestawiania i kierowania połączeń, obejmująca KNA;

31\) ZT – HOST – ID danej SN (dla danego wskaźnika strefy numeracyjnej AB).

2\. Informacja adresowa o numerze abonenta A jest niezmienna na całej drodze połączeniowej od pierwszej centrali operatorskiej obsługującej abonenta, z wyjątkiem przypadków określonych w pkt 3.

3\. Numer zastępujący numer abonenta A (numer techniczny) jest wykorzystywany przy realizowaniu połączenia na numery alarmowe:

1\) z telekomunikacyjnego urządzenia końcowego bez użycia przez użytkownika karty SIM;

2\) z użyciem przez abonenta A karty SIM zalogowanej w sieci innej niż sieć wykorzystywana przez dostawcę usług, z którym abonent A zawarł umowę o świadczenie usług komunikacji elektronicznej, w przypadku braku zasięgu tej sieci.

4\. Szczegółowe wymagania dotyczące adresowania dla właściwego kierowania połączeń w zakresie użycia NR:

1\) w sieciach wykorzystujących ISUP:

a) NR zamieszcza się w parametrze Called Party Number wiadomości IAM przed numerem abonenta B (tryb połączony „concatenated”),

b) parametr NoA przyjmuje wartość 3,

c) stosuje się adresowanie metodą „en–bloc”,

d) NR dołącza się po odpytaniu bazy dla numerów przeniesionych ; dopuszcza się dołączenie NR po odpytaniu bazy dla numerów nieprzeniesionych;

2\) w sieciach wykorzystujących SIP:

a) NR zamieszcza się w wiadomości INVITE w polach To oraz Request URI,

b) abonent B jest identyfikowany w następujący sposób: sip:&lt;NR&gt;&lt;KNA&gt;;phone-context=+48@hostname;user=phone

lub

sip:&lt;NR&gt;&lt;KNA&gt;@domena;user=phone

gdzie:

– parametr user=phone jest obowiązkowy,

– hostname może mieć formę nazwy domenowej lub adresu IP, ustalonych na styku systemów przez operatorów tych systemów,

– domena: FQDN; w przypadku gdy węzeł końcowy nie ma zarejestrowanej nazwy domenowej, dopuszcza się stosowanie adresu IP;

3\) ustala się następujący format NR:

NR (5 cyfr) = „C hex” + XYZT,

gdzie:

a) dla numerów geograficznych:

XY = AB = wskaźnik SN (X = 1–9),

ZT = HOST – ID w danej SN (dla danego AB); po dojściu ZT do wartości 99 ustala się inny wolny AB dla danej strefy numeracyjnej (SN),

b) dla numerów niegeograficznych:

XYZT = numer sieci (X = 0).

5\. Szczegółowe wymagania dotyczące adresowania dla właściwego kierowania połączeń do numerów alarmowych oraz format NKA:

1\) w sieciach wykorzystujących ISUP albo SIP:

a) połączenia do numerów alarmowych mogą być realizowane po odebraniu numeru w formatach:

– XYZ (3 cyfry) – z łącza abonenckiego,

– WSNd (2 cyfry) + „C hex” + IDL (3 cyfry) + XYZ (3 cyfry) – z łącza między elementami sieci telekomunikacyjnej, w tym z łącza międzyoperatorskiego,

b) NKA jest wprowadzany w elemencie sieci telekomunikacyjnej obsługującej zakończenie sieci, z którego nastąpiło wywołanie alarmowe,

c) w elemencie sieci telekomunikacyjnej obsługującym zakończenie sieci, z którego nastąpiło wywołanie alarmowe, następuje konwersja z numeru alarmowego odebranego od abonenta na numer w formacie WSNd + „C hex” + IDL + XYZ,

d) NKA jest niezmienny na całej drodze połączeniowej,

e) zamiana NKA na KNA (numer podkładowy) może nastąpić w elemencie sieci telekomunikacyjnej bezpośrednio obsługującej jednostkę, do której jest kierowane wywołanie alarmowe na numer alarmowy;

2\) w sieciach wykorzystujących SIP:

a) NKA umieszcza się w wiadomości INVITE w polach To oraz Request URI,

b) abonent B jest identyfikowany w następujący sposób: sip:&lt;NKA&gt;;phone-context=+48@hostname;user=phone

lub

sip:&lt;NKA&gt;@domena;user=phone

gdzie:

– parametr user=phone jest obowiązkowy,

– hostname może mieć formę nazwy domenowej lub adresu IP, ustalonych na styku systemów przez operatorów tych systemów,

– domena: FQDN; w przypadku, gdy węzeł końcowy nie ma zarejestrowanej nazwy domenowej, dopuszcza się stosowanie adresu IP;

3\) ustala się następujący format NKA:

NKA = WSNd (2 cyfry) + „C hex” + IDL (3 cyfry) + XYZ (3 cyfry), gdzie:

a) WSNd (Wskaźnik Strefy Numeracyjnej docelowej) – oznacza strefę numeracyjną, w jakiej znajduje się jednostka, do której jest kierowane wywołanie alarmowe,

b) IDL (Identyfikator Docelowej Lokalizacji) – wskazuje jednostkę, do której jest kierowane wywołanie alarmowe, występującą w danej lokalizacji w danej strefie numeracyjnej,

c) XYZ – oznacza wybrany trzycyfrowy numer AUS albo numer alarmowy 112;

4\) w przypadku wystąpienia awarii:

a) operator bezpośrednio obsługujący jednostkę służby alarmowej przyjmującą połączenia do numeru alarmowego na czas trwania awarii adresuje połączenia na podstawie aktualnych danych otrzymanych od obsługiwanej jednostki służby alarmowej,

b) adresowanie następuje do lokalizacji zastępczej, innej jednostki służby alarmowej lub numeru alternatywnego,

c) adresowanie do lokalizacji zastępczej, innej jednostki służby alarmowej lub numeru alternatywnego nie może trwać dłużej niż 7 dni kalendarzowych.

6\. Szczegółowe wymagania dotyczące prezentacji informacji adresowej:

1\) dla sieci wykorzystujących SIP:

a) informacja adresowa o numerze abonenta A jest przesyłana w nagłówku P -Asserted-Identity z informacją o zastrzeżeniu prezentacji numeru przesłanym w nagłówku Privacy,

b) w przypadku wywołań na numery alarmowe przesyłanie informacji o numerze wywołującym w nagłówku P-Asserted-Identity jest obowiązkowe;

2\) dla wywołań z numerów zastrzeżonych w sieciach wykorzystujących SIP (nagłówek Privacy) oraz SS7 (CLIR): przy wysyłaniu na łącze abonenckie (nie dotyczy łączy do służb alarmowych) wywołania muszą mieć usunięte pola służące do identyfikacji abonenta A; w przypadku wywołań przychodzących z sieci niezaufanej w sieciach wykorzystujących SIP usuwa się także nagłówek P-Asserted-Identity oraz w nagłówku From wstawia się &lt;sip:Anonymous@anonymous.invalid&gt;.

7\. Szczegółowe wymagania dotyczące numeracji punktów sygnalizacyjnych:

1\) międzynarodowy punkt sygnalizacyjny identyfikowany jest jednym ISPC;

2\) format ISPC stanowi 14-bitowy kod binarny;

3\) NSPC służy do identyfikacji elementów krajowej sieci sygnalizacyjnej;

4\) format NSPC stanowi 14-bitowy kod binarny.

8\. Szczegółowe wymagania dotyczące tworzenia i udostępniania znaków identyfikujących abonenta:

1\) znak identyfikujący abonenta B stanowi element informacji adresowej wykorzystywanej w procesie zestawiania i kierowania połączeń;

2\) przedsiębiorcy telekomunikacyjni zapewniają przekazywanie znaków identyfikujących abonenta A i abonenta B między sieciami telekomunikacyjnymi w sposób umożliwiający ich wykorzystanie w procesach:

a) kierowania połączeń,

b) identyfikacji punktu zakończenia sieci,

c) realizacji uprawnień abonenta, w tym związanych z przenoszeniem numeru;

3\) znak identyfikujący abonenta A jest niezmienny na całej drodze połączeniowej.

---

Przypisy:

1\) Minister Cyfryzacji kieruje działem administracji rządowej – informatyzacja, na podstawie § 1 ust. 2 rozporządzenia Prezesa Rady Ministrów z dnia 18 grudnia 2023 r. w sprawie szczegółowego zakresu działania Ministra Cyfryzacji (Dz. U. poz. 2720).

2\) Niniejsze rozporządzenie było poprzedzone rozporządzeniem Ministra Administracji i Cyfryzacji z dnia 12 grudnia 2014 r. w sprawie szczegółowych wymagań dotyczących zasad adresowania dla właściwego kierowania połączeń (Dz. U. z 2015 r. poz. 12), które traci moc z dniem wejścia w życie niniejszego rozporządzenia zgodnie z art. 104 pkt 13 lit. b ustawy z dnia 12 lipca 2024 r. – Przepisy wprowadzające ustawę – Prawo komunikacji elektronicznej (Dz. U. poz. 1222 oraz z 2026 r. poz. 252).

1\) Zalecenie RFC 3325 jest dostępne na stronie internetowej IETF (Internet Engineering Task Force) – https://datatracker.ietf.org/doc/rfc3325/.

2\) Zalecenie RFC 3323 jest dostępne na stronie internetowej IETF (Internet Engineering Task Force) – https://datatracker.ietf.org/doc/rfc3323/.

3\) Zalecenie RFC 3261 jest dostępne na stronie internetowej IETF (Internet Engineering Task Force) – https://datatracker.ietf.org/doc/html/rfc3261.
