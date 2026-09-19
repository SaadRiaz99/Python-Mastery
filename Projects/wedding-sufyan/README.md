# M Sufyan — Pakistani wedding invitation

An original ivory, maroon and antique-gold invitation with an arch border, Bismillah, Urdu invitation, family names, Mehndi, Nikah / Barat, Walima and RSVP. Mobile-friendly, keyboard-accessible and printable. No paid services, dependencies, tracking or database.

## Open locally (Windows / PowerShell)

From your Python-Mastery repository:

```powershell
cd Projects/wedding-sufyan
python -m http.server 8000
```

Open http://localhost:8000. Stop with Ctrl+C. You can also open index.html directly; use the local server for the most reliable personalised HTML download.

## Add real wedding details

Only the groom's name, **M Sufyan**, was supplied. Bride, family, dates, times, addresses and RSVP are clearly marked placeholders, not real event details.

1. Open **Personalise this invitation** and fill the fields.
2. Check every name, venue and time.
3. Choose **Download personalised card** for a standalone HTML file with embedded styles; this export needs no other files and has no editing controls.
4. Choose **Print / Save PDF** for a printable invitation. Use A4, 100% scale, background graphics enabled, and browser headers/footers disabled. Long custom text may require reducing the print scale.

Edits live only in the open page until downloaded/printed. They are not uploaded or saved to the original source. To change permanent defaults, edit the text inside the `data-field` elements in index.html. The exported card can be shared as a file; no live website is deployed by this project. RSVP is contact information, not an online submission form.

## Files

- `index.html`: invitation text and structure.
- `styles.css`: theme, responsive layout and print styling.
- `card.js`: live text editing and portable HTML export.

## Design research

Reference collection reviewed before creating this original design:
- [Little Letter Company — Pakistani wedding invitations](https://www.littlelettercompany.com/collections/wedding-invitations): Pearl & Gold, Royal Botanical and neutral colour directions.
- [Muslim invitation reference board](https://in.pinterest.com/weddings0180/muslim-wedding-invitations/): arch and Nikah / Walima invitation ideas.

No third-party artwork or template was copied. Ornamentation uses CSS and typographic flourishes; system fonts keep the card independent of external font services. Arabic/Urdu appearance depends on installed fonts.

All existing repository projects are preserved. This project is entirely contained in `Projects/wedding-sufyan/`.

## Individual invitation cards

- [Nikah / Barat card](nikah-barat.html): maroon, ivory and gold, with only Nikah / Barat date, timings and venue.
- [Walima card](walima.html): sage, ivory and gold, with only Walima date, reception / dinner timings and venue.
- [Combined card](index.html): the original multi-event invitation remains available.

Choose a card from the links above the invitation, or open its HTML file. Each individual card has its own editable family names and RSVP and its own download filename. Download or print each card separately. Edits do not transfer between cards and must be saved before navigating to another card.
