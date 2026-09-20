const editing = new URLSearchParams(window.location.search).get('edit') === '1';
document.documentElement.classList.toggle('editing', editing);
document.querySelectorAll('.card-nav a').forEach(link => {
  if (new URL(link.href).pathname === window.location.pathname) link.setAttribute('aria-current', 'page');
  if (editing) link.search = '?edit=1';
});
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
document.getElementById('print').addEventListener('click', async () => { await document.fonts.ready; window.print(); });
document.getElementById('download').addEventListener('click', async () => {
  const status = document.getElementById('status');
  try {
    await document.fonts.ready;
    // Embed the stylesheet so the exported invitation is a single portable file.
    let css = '';
    for (const sheet of document.styleSheets) {
      for (const rule of sheet.cssRules) css += rule.cssText + '\n';
    }
    const copy = document.documentElement.cloneNode(true);
    copy.querySelectorAll('.editor, .toolbar, .intro, .note, .share-actions, .share-status, .guest-note, script, link[rel="stylesheet"]').forEach(node => node.remove());
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

if (!editing) {
  const defaults = {
    bride: 'Bride’s name to be announced',
    hosts: 'Together with our families',
    mehndiDate: 'Date & time to be announced',
    mehndiVenue: 'Venue details to follow',
    baratDate: 'Date to be announced',
    baratTime: 'Nikah, arrival & dinner timings to follow',
    baratVenue: 'Venue details to follow',
    walimaDate: 'Date to be announced',
    walimaTime: 'Reception & dinner timings to follow',
    walimaVenue: 'Venue details to follow',
    rsvp: 'Contact details to follow'
  };
  let incomplete = false;
  document.querySelectorAll('[data-field]').forEach(node => {
    if (node.textContent.trim().startsWith('[')) {
      incomplete = true;
      if (node.dataset.field === 'bride') {
        node.hidden = true;
        const joining = document.querySelector('.joining');
        if (joining) joining.hidden = true;
      } else node.textContent = defaults[node.dataset.field] || 'Details to be announced';
    }
  });
  if (incomplete) {
    const note = document.createElement('p');
    note.className = 'guest-note';
    note.textContent = 'Wedding details will be announced soon. We look forward to celebrating with you.';
    document.querySelector('main').append(note);
  }
}
const shareButton = document.getElementById('share');
if (shareButton) shareButton.addEventListener('click', async () => {
  const status = document.getElementById('share-status');
  if (!/^https?:$/.test(window.location.protocol) || ['localhost', '127.0.0.1'].includes(window.location.hostname)) {
    status.textContent = 'A shareable link will be available after deployment.';
    return;
  }
  const url = new URL(window.location.href);
  url.search = '';
  url.hash = '';
  try {
    if (navigator.share) await navigator.share({title: document.title, text: 'With love, you are invited to M Sufyan’s wedding celebration.', url: url.href});
    else if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(url.href);
      status.textContent = 'Invitation link copied.';
    } else status.textContent = 'Copy this invitation link: ' + url.href;
  } catch (error) {
    if (error.name !== 'AbortError') status.textContent = 'Copy this invitation link: ' + url.href;
  }
});
