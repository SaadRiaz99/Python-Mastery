# M Sufyan — Pakistani wedding invitation

An original smokey-white, silver-grey and charcoal invitation with an arch border, Bismillah, Urdu invitation, family names, Mehndi, Nikah / Barat, Walima and RSVP. Mobile-friendly, keyboard-accessible and printable. No paid services, dependencies, tracking or database.

## Open locally (Windows / PowerShell)

From your Python-Mastery repository:

```powershell
cd Projects/wedding-sufyan
python -m http.server 8000
```

Open http://localhost:8000. Stop with Ctrl+C. You can also open index.html directly; use the local server for the most reliable personalised HTML download.

## Add real wedding details

Only the groom's name, **M Sufyan**, was supplied. Bride, family, dates, times, addresses and RSVP are clearly marked placeholders, not real event details.

1. Open the relevant card with `?edit=1` (for example `nikah-barat.html?edit=1`) to reveal **Personalise this invitation**, then fill the fields.
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

No third-party artwork or template was copied. Individual cards use original AI-generated floral artwork embedded in the CSS; the combined card retains its earlier typographic ornamentation. Embedded Latin Modern-derived fonts keep English typography consistent without external font services. Arabic/Urdu appearance depends on installed fonts.

All existing repository projects are preserved. This project is entirely contained in `Projects/wedding-sufyan/`.

## Individual invitation cards

- [Nikah / Barat card](nikah-barat.html): smokey white with silver-grey borders and charcoal text, with only Nikah / Barat date, timings and venue.
- [Walima card](walima.html): smokey white with silver-grey borders and charcoal text, with only Walima date, reception / dinner timings and venue.
- [Combined card](index.html): the original multi-event invitation remains available.

Choose a card from the links above the invitation, or open its HTML file. Each individual card has its own editable family names and RSVP and its own download filename. Download or print each card separately. Edits do not transfer between cards and must be saved before navigating to another card.

## Floral design update

The separate Nikah / Barat and Walima cards now use smokey-white botanical stationery: ivory roses, pale grey-green leaves, a thin silver double frame, and italic name lettering. The combined card remains unchanged in layout.

Style reference requested: [Hand-drawing floral wedding invitation](https://www.magnific.com/free-vector/beautiful-hand-drawing-wedding-invitation-floral-card-template_11171436.htm). The page was readable but its full reference image could not be retrieved; this is an original floral interpretation, not an exact reproduction.

The built-in image-generation tool created the background. It is embedded as an optimised WebP data URI in `styles.css`, so personalised HTML exports contain the artwork without external files or network access. Enable background graphics when printing.

Artwork brief: “Portrait smokey-white wedding stationery, delicate hand-drawn ivory roses, silver-grey blossoms, pale grey-green eucalyptus, fine graphite outlines and light watercolor washes; asymmetric upper-left and lower-right arrangements; empty central area for editable text; flat front view; no text, logos, watermark or border.”

## Family invitation structure (ready for final details)

The individual cards now use smokey pearl, champagne borders and muted sage lettering. English names use an embedded italic display font; body text uses an embedded book serif. Both are renamed Latin Modern subsets. See FONT-LICENSE.txt. Urdu and Arabic retain local font fallbacks.

- Gentle one-time card and name entrance animations, subtle button hover movement.
- Reduced-motion preferences respected; print output is static.
- Guest mode hides editing controls and shows friendly “to be announced” wording for missing details. The missing bride name is hidden.
- Add `?edit=1` to a card URL to access the local editor. This is a local editing convenience, not authentication or a server admin panel.
- Share invitation uses native device sharing where supported, otherwise copies or displays the clean URL. Sharing is initiated only by the visitor.
- Fonts and flowers stay embedded in standalone downloads.
- No deployment has been made for this structure. Supply the final names, dates, venues, family names and RSVP before publishing the real invitation. An HTML download does not change the deployed invitation; final details must be committed in the source.
