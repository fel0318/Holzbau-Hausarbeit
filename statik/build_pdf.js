// Erzeugt die Abgabe-PDF aus statische_berechnung.html (Chromium/Playwright)
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(__dirname, 'statische_berechnung.html'));
  await page.waitForTimeout(300);

  // Ueberlauf-Kontrolle: jede .page darf nicht hoeher sein als ihr Rahmen
  const overflow = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('.page').forEach((p, i) => {
      if (p.scrollHeight > p.clientHeight + 1) {
        out.push(`Seite ${i + 1}: scroll=${p.scrollHeight}px client=${p.clientHeight}px`);
      }
    });
    return out;
  });
  if (overflow.length) {
    console.log('UEBERLAUF:\n' + overflow.join('\n'));
  } else {
    console.log('Kein Seitenueberlauf.');
  }

  await page.pdf({
    path: path.resolve(__dirname, '..', 'Hausarbeit_Holzbau_B3.pdf'),
    format: 'A4',
    printBackground: true,
    margin: { top: 0, bottom: 0, left: 0, right: 0 },
  });
  await browser.close();
  console.log('PDF erzeugt: Hausarbeit_Holzbau_B3.pdf');
})();
