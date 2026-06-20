#!/usr/bin/env node
// Screenshot capture template for product/app READMEs.
// dustjacket adapts BASE_URL and SHOTS to the real app; you run it to produce real pixels.
//
//   npm i -D playwright && npx playwright install chromium
//   node scripts/capture-screenshots.mjs
//
// Output: light/dark pairs under docs/assets/, ready for a <picture> block.

import { chromium } from "playwright";
import { mkdir } from "node:fs/promises";

const BASE_URL = process.env.BASE_URL ?? "http://localhost:3000";
const OUT_DIR = "docs/assets";

// One entry per screenshot. `selector` is optional — omit for a full-page shot.
const SHOTS = [
  { name: "hero", path: "/", selector: undefined },
];

async function shoot(browser, scheme) {
  const context = await browser.newContext({
    colorScheme: scheme,
    viewport: { width: 1600, height: 1000 },
    deviceScaleFactor: 2,
  });
  const page = await context.newPage();
  for (const { name, path, selector } of SHOTS) {
    await page.goto(`${BASE_URL}${path}`, { waitUntil: "networkidle" });
    const target = selector ? page.locator(selector) : page;
    const file = `${OUT_DIR}/${name}-${scheme}.png`;
    await target.screenshot({ path: file });
    console.log(`wrote ${file}`);
  }
  await context.close();
}

const browser = await chromium.launch();
await mkdir(OUT_DIR, { recursive: true });
for (const scheme of ["light", "dark"]) await shoot(browser, scheme);
await browser.close();
console.log("\nEmbed with a <picture> block — see references/helpers.md.");
