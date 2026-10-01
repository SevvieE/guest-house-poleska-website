# Guest House Poleska: website

Static site built with [Astro](https://astro.build). No database, no server: `npm run build` produces plain files in `dist/` that any host can serve.

## Commands (run inside this folder)

| Command | What it does |
| --- | --- |
| `npm install` | Install dependencies (once) |
| `npm run dev` | Local preview at http://localhost:4321 with live reload |
| `npm run build` | Build the finished site into `dist/` |
| `npm run photos` | Re-create the web-sized photos from `../Foto's ` (run after adding or replacing photos) |

## Where things live

- `src/data/site.ts`: prices, guest numbers, contact details, menu. **Change facts here.**
- `src/data/photos.ts`: which photo is which, with the alt text and category used by the gallery.
- `src/pages/*.astro`: the pages and their text.
- `src/styles/global.css`: colours (top of the file), fonts and layout.
- `public/`: favicon, robots.txt, social preview image, and the generated `img/` folder.

## Still to fill in (marked TODO in the code)

1. `site.ts`: the `formEndpoint` of a form service (Formspree, Web3Forms, ...) so the contact form delivers to the hosts' inbox. No email address is shown on the site; the form service holds it. WhatsApp number is optional.
2. ~~`astro.config.mjs` and `public/robots.txt`: the real domain once it exists.~~ Done: www.guesthousepoleska.com.
3. Photos of the hosts and Raco (with the hosts' consent).
