---
title: "Rozporządzenie Ministra Zdrowia z dnia 30 czerwca 2026 r. w sprawie sposobu obliczania prognozowanego czasu oczekiwania na udzielenie świadczeń opieki zdrowotnej objętych centralną elektroniczną rejestracją"
identifier: "DU/2026/874"
official_citation: "Dz.U. 2026 poz. 874"
type: regulation
jurisdiction: pl
language: pl
date: 2026-06-30
promulgated: 2026-06-30
entry_into_force: 2026-07-01
status: in_force
official_status: "obowiązujący"
text_version: "tekst ogłoszony (original)"
text_format: "pdf (text extracted)"
source: "https://api.sejm.gov.pl/eli/acts/DU/2026/874"
source_text: "https://api.sejm.gov.pl/eli/acts/DU/2026/874/text/I/D20260874.pdf"
isap: "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000874"
retrieved: 2026-10-11
---

# Rozporządzenie Ministra Zdrowia z dnia 30 czerwca 2026 r. w sprawie sposobu obliczania prognozowanego czasu oczekiwania na udzielenie świadczeń opieki zdrowotnej objętych centralną elektroniczną rejestracją

ROZPORZĄDZENIE MINISTRA ZDROWIA 1) z dnia 30 czerwca 2026 r. w sprawie sposobu obliczania prognozowanego czasu oczekiwania na udzielenie świadczeń opieki zdrowotnej objętych centralną elektroniczną rejestracją Na podstawie art. 23c ust. 10 ustawy z dnia 27 sierpnia 2004 r. o świadczeniach opieki zdrowotnej finansowanych ze środków publicznych (Dz. U. z 2025 r. poz. 1461, 1537 i 1739 oraz z 2026 r. poz. 26, 203 i 791) zarządza się, co następuje:

§ 1. Rozporządzenie określa sposób obliczania prognozowanego czasu oczekiwania na udzielenie świadczeń opieki zdrowotnej, o których mowa w przepisach wydanych na podstawie art. 23h ust. 2 pkt 1 ustawy z dnia 27 sierpnia 2004 r. o świadczeniach opieki zdrowotnej finansowanych ze środków publicznych, zwanego dalej „PCUŚ”.

§ 2. 1. PCUŚ jest obliczany i aktualizowany raz dziennie dla każdego świadczeniodawcy odrębnie, na podstawie danych przekazanych przez świadczeniodawcę do systemu teleinformatycznego, o którym mowa w art. 7 ust. 1 ustawy z dnia 28 kwietnia 2011 r. o systemie in formacji w ochronie zdrowia (Dz. U. z 2026 r. poz. 208, 252 i 791), z wykorzystaniem prognozowanej w wyniku symulacji daty udzielenia świadczenia opieki zdrowotnej dla nowych świadczeniobiorców, zwanej dalej „PDS”, dla liczby n nowych świadczeniobiorców, z zastosowaniem symulacji do wyznaczenia terminów udzielenia świadczeń opieki zdrowotnej dla wszystkich świadczeniobiorców umieszczonych w centralnym wykazie oczekujących, zgodnie ze wzorem:

PCUŚ = 𝑡0 + ∑ PDS𝑘𝑛𝑘=1 𝑛 przy czym PDS wyznacza się jako najmniejszą różnicę między dostępnym terminem świadczenia a datą bieżącą, zgodnie ze wzorem:

PDS = min(𝑎𝑖 − 𝑡0) gdzie: t0 – oznacza datę bieżącą, ai – oznacza dostępne terminy świadczeń opieki zdrowotnej spełniające kryteria zdefiniowane przez użytkownika, PDSk – oznacza jednostkowy prognozowany czas oczekiwania na udzielenie świadczenia opieki zdrowotnej dla pojedynczego potencjalnego nowego świadczeniobiorcy, wyrażony w dniach kalendarzowych i liczony od daty bieżącej, n – oznacza liczbę potencjalnych nowych świadczeniobiorców uwzględnianych przy obliczaniu PCUŚ.

2\. PCUŚ do 40 dni jest wyrażony w dniach i jest prezentowany wraz z liczbą dostępnych terminów świadczeń opieki zdrowotnej, obliczaną zgodnie ze wzorem:

PCUŚ do T40 = ∑ 𝑓(𝑎𝑖), gdzie 𝑓(𝑎𝑖) = {1 dla 𝑎𝑖 ≤ (𝑡0 + 40)0 dla 𝑎𝑖 &gt; (𝑡0 + 40)𝑁𝑖=1 gdzie:

N – oznacza liczbę dostępnych terminów świadczeń opieki zdrowotnej spełniających kryteria zdefiniowane przez użytkownika.

3\. PCUŚ od 40 dni do 12 miesięcy jest wyrażony w miesiącach i jest obliczany zgodnie ze wzorem: PCUŚ powyżej T40 = ⌊ PCUŚ−𝑡0 30 ⌋

4\. Dla PCUŚ powyżej 12 miesięcy prezentowana jest informacja: „Termin powyżej 12 miesięcy”.

5\. Informacja o wartości parametru n, uwzględnianego przy obliczeniu PCUŚ, jest publikowana w Biuletynie Informacji Publicznej na stronie podmiotowej urzędu obsługującego ministra właściwego do spraw zdrowia.

6\. Symulacja, o której mowa w ust. 1, jest dokonywana przez system teleinformatyczny, o którym mowa w art. 7 ust. 1 ustawy z dnia 28 kwietnia 2011 r. o systemie informacji w ochronie zdrowia, dla każdego świadczeniodawcy odrębnie, na podstawie przekazanych do tego systemu danych dotyczących:

1\) świadczeniobiorców umieszczonych w centralnym wykazie oczekujących;

2\) dostępnych terminów udzielenia świadczeń opieki zdrowotnej u świadczeniodawcy, dla którego jest obliczany PCUŚ;

3\) dostępnych terminów udzielenia świadczeń opieki zdrowotnej u innych świadczeniodawców niż świadczeniodawca, dla którego jest obliczany PCUŚ;

4\) kategorii medycznych, do których świadczeniobiorcy zostali zakwalifikowani zgodnie z kryteriami medycznymi, o których mowa w przepisach wydanych na podstawie art. 20 ust. 11 ustawy z dnia 27 sierpnia 2004 r. o świadczeniach opieki zdrowotnej finansowanych ze środków publicznych, zwanej dalej „ustawą”;

5\) kryteriów wybranych przez świadczeniobiorców, o których mowa w art. 23e ust. 6 ustawy;

6\) informacji o uprawnieniach do korzystania ze świadczeń opieki zdrowotnej poza kolejnością, o których mowa w art. 47c ustawy;

7\) skierowań, zgodnie z wykazem świadczeń opieki zdrowotnej, o którym mowa w art. 59aa ust. 2 ustawy, jeżeli są wymagane;

8\) daty dokonania zgłoszenia centralnego;

9\) daty dokonania przez świadczeniobiorcę zgłoszenia na udzielenie świadczeń opieki zdrowotnej, o którym mowa w art. 23g ust. 2 ustawy, jeżeli zgłoszenie zostało dokonane przed umożliwieniem przez świadczeniodawcę dokonywania przez świadczeniobiorcę zgłoszenia centralnego.

§ 3. Rozporządzenie wchodzi w życie z dniem następującym po dniu ogłoszenia. Minister Zdrowia: wz. T. Maciejewski

---

Przypisy:

1\) Minister Zdrowia kieruje działem administracji rządowej – zdrowie, na podstawie § 1 ust. 2 rozporządzenia Prezesa Rady Ministrów z dnia 25 lipca 2025 r. w sprawie szczegółowego zakresu działania Ministra Zdrowia (Dz. U. poz. 1004).
