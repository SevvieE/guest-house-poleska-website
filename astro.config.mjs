import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://www.guesthousepoleska.com',
  integrations: [sitemap()],
  build: { inlineStylesheets: 'auto' },
});
