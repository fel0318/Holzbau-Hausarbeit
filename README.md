# Holzbau-Hausarbeit – Semesteraufgabe B3 (TH Nürnberg)

Komplette statische Berechnung für die Semesteraufgabe B3 „Konstruktion im Holzbau:
Aufgabe 1 – Holzhaus" (Vorlesung Holzbau, Prof. Dr.-Ing. Jonas Schmidt).

## Abgabedokument

**`Hausarbeit_Holzbau_B3.pdf`** – fertiges Dokument (16 Seiten):

| Seite | Inhalt |
|---|---|
| 1 | Deckblatt (Name/Matrikel-Nr. eintragen!) |
| 2 | Inhaltsverzeichnis |
| 3–4 | Allgemeines: System, Normen, Material (C24 / GL24h), Beiwerte, NKL 1 |
| 5 | Lastannahmen inkl. Einzugsbreite Zweifeldträger (B = 1,25 · 4,0 = 5,0 m) |
| 6–7 | Pos. 1 Stütze 1: **KVH C24 12/12 cm** – Knicknachweis η = 0,68 |
| 8–12 | Pos. 2 Unterzug: **BSH GL24h 20/68 cm** – Biegung η = 0,86, Schub η = 0,81, Kippen (k_crit = 1,0), Auflagerpressung η = 0,81, Durchbiegung η ≤ 0,53 |
| 13 | Pos. 3 Stütze 2: **KVH C24 20/20 cm** – Knicken η = 0,26 (Größe aus Auflagerpressung) |
| 14 | Zusammenfassung, Bauteilliste, Hinweise für den Architekten |
| 15–16 | Zeichnungen (Ansicht M 1:50; Details/Querschnitte M 1:10 / 1:5) mit Plankopf |

**Wichtig:** Laut Aufgabenstellung sind die Zeichnungen als **Handzeichnung** abzugeben –
Blatt 15/16 dienen als maßstäbliche Vorlage zum Abzeichnen. Abgabe im Klarsichthefter A4.

## Dateien

- `statik/statische_berechnung.html` – Quelldokument (bearbeitbar, z. B. Name eintragen)
- `statik/build_pdf.js` – erzeugt die PDF: `node statik/build_pdf.js` (benötigt Playwright/Chromium)
- `statik/verifikation.py` – unabhängige Nachrechnung aller Zahlenwerte: `python3 statik/verifikation.py`

## Bemessungsgrundlagen (Kurzfassung)

- DIN EN 1995-1-1 (EC 5) + NA; γ_G = 1,35, γ_Q = 1,5, γ_M = 1,3; NKL 1, k_def = 0,6
- Maßgebende Kombination jeweils über max(E_d/k_mod) ermittelt → überall **G + Nutzlast**
  bzw. bei Stütze 1 **G + Schnee**
- Decke als Zweifeldträger → Mittelauflagerkraft 1,25 · w · ℓ → g = 12,5 + 0,6 = 13,1 kN/m,
  q = 10,0 kN/m auf den Unterzug; mittige Einzellast aus Stütze 1 (G = 10,25; S = 13; W = 2 kN)
