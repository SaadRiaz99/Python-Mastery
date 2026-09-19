// All editable invitation text is rendered with textContent, never HTML.
const labels = {
  groom: 'Groom’s name', bride: 'Bride’s name', hosts: 'Inviting family / parents',
  mehndiDate: 'Mehndi date & time', mehndiVenue: 'Mehndi venue & address',
  baratDate: 'Nikah / Barat date', baratTime: 'Nikah, arrival & dinner timings',
  baratVenue: 'Nikah / Barat venue & address', walimaDate: 'Walima date & time',
  walimaTime: 'Walima reception & dinner timings', walimaVenue: 'Walima venue & address', rsvp: 'RSVP contact name & phone'
};
const fields = document.getElementById('fields');
for (const [key, labelText] of Object.entries(labels)) {
  const target = document.querySelector(`[data-field="${key}"]`);
  if (!target) continue; // Individual cards only edit their own event fields.
  const fallback = target.textContent;
  const label = document.createElement('label');
  label.textContent = labelText;
  const input = document.createElement('input');
  input.name = key;
  input.maxLength = 180;
  input.value = fallback.startsWith('[') ? '' : fallback;
  input.placeholder = fallback;
  input.addEventListener('input', () => {
    target.textContent = input.value.trim() || fallback;
  });
  label.append(input);
  fields.append(label);
}
document.getElementById('details-form').addEventListener('submit', event => event.preventDefault());
document.getElementById('print').addEventListener('click', () => window.print());
document.getElementById('download').addEventListener('click', async () => {
  const status = document.getElementById('status');
  try {
    // Embed the stylesheet so the exported invitation is a single portable file.
    let css = '';
    for (const sheet of document.styleSheets) {
      for (const rule of sheet.cssRules) css += rule.cssText + '\n';
    }
    const copy = document.documentElement.cloneNode(true);
    copy.querySelectorAll('.editor, .toolbar, .intro, .note, script, link[rel="stylesheet"]').forEach(node => node.remove());
    const style = document.createElement('style');
    style.textContent = css;
    copy.querySelector('head').append(style);
    const blob = new Blob(['<!doctype html>\n' + copy.outerHTML], {type:'text/html;charset=utf-8'});
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = document.body.dataset.downloadName || 'M-Sufyan-Wedding-Invitation.html';
    link.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    status.textContent = 'Personalised card downloaded. Open it in a browser, or use Ctrl+P to save a PDF.';
  } catch {
    status.textContent = 'Please run the local server described in README.md, then download again. You can also use Print / Save PDF.';
  }
});
