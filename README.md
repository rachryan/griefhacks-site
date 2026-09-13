# GriefHacks

A static website for practical tools and personal writing about grief. HTML, CSS, and a small navigation script; no build step or package installation is needed.

## Preview locally

From this directory, run `python3 -m http.server 8080`, then open `http://localhost:8080` in a browser. Check the homepage, collection, framework, and one article at desktop and phone widths.

## Edit

- `index.html`: homepage and the single Buttondown signup form.
- `blog/index.html`: all stories and tools, grouped by reader need.
- `blog/*.html`: article bodies and metadata. Keep published filenames so existing links continue to work.
- `framework.html`: paid guide information. The contents list must match the actual product.
- `styles.css`: shared responsive design and print styles.
- `script.js`: accessible mobile navigation and footer year.
- `images/`: existing site illustrations.

Headers and footers are static HTML so they remain available without JavaScript. When changing shared navigation, apply the same change to all 16 pages. Keep labels, canonical URLs, page titles, and descriptions aligned with the article content.

## Verify before publishing

Run `python3 scripts/check_site.py` to check page structure, assets, links, and anchors. Run `node --check script.js` for JavaScript syntax.

In a browser, also check:

- Narrow and wide layouts, including 320px and 390px phone widths.
- Keyboard focus, the skip link, mobile menu, Escape to close, and navigation after resizing.
- The support kit checkboxes and navigation with JavaScript disabled.
- Newsletter required-email validation. Do not submit a real signup without permission.

The main signup uses the existing Buttondown address. It has not been verified by sending a subscription. Purchasing and delivery remain on Gumroad. No price is hard-coded.

## Redesign review

The redesign branch is a draft. Local-browser preview access was blocked in the editing environment, so rendered visual and interaction checks remain required before merging. Automated link and structure checks, JavaScript syntax, and primary text contrast pairs were checked.

The guide's published chapter titles are retained to avoid misrepresenting the purchased product. Any proposed renaming should be coordinated with the guide itself. The author introduction uses Rachel and the existing Momma R byline, without adding private family details.

## September follow-up

The first redesign is live. The follow-up branch adds larger supporting text, a shorter hero, a direct support-kit link, practical tools nearer the top, related-article links, a clearer About section, support/privacy/contact pages, and complete social metadata plus sitemap/robots files.

Resource details were checked on 13 September 2026 against BC Bereavement Helpline, GRASP, AboutGrief.ca, and 988.ca. Provider information is linked directly on the support/privacy pages.

The contact form reuses the original Formspree endpoint found in repository history (commit 13ecbe3). Its availability and delivery remain unverified: a read-only request returned HTTP 403. Verify this endpoint in the owner's Formspree account and perform an authorised test before publishing the contact form. No test message or newsletter subscription was sent.

The live homepage was visually inspected. The updated local draft still requires desktop/mobile visual checks because local URLs are blocked by the browser policy.
