# Agent 4: Weekly Grocery Agent (12 agents in 12 weeks)

Tell it which meals you'll cook and which you'll order. It plans the week to your calorie and protein targets, fills your **Swiggy Instamart** cart, and shows you everything it **left out** and why. It stops at the cart: you check out and pay.

## How it works
| Step | Who does it |
|---|---|
| Ask which meals you cook vs order | Claude |
| Draft the meal plan | Claude |
| Check every day hits calories (±100 kcal) and protein (≥170 g) | `check_plan.py` (code) |
| Search Instamart for each item | Claude via the official Swiggy MCP |
| Price guard: usual price vs today's, per unit | `price_guard.py` (code) |
| Fill the cart (merge, never overwrite) | Claude via MCP |
| Checkout and payment | **You** |

## The price guard (`price_guard.py`)
- **Usual price** = what you paid before, per unit (`data/price_log.csv`, seeded from your order emails). With no history, it uses the median of today's comparable options.
- **More than 20% above usual:**
  - needed **today**: it is never dropped quietly. It asks you: buy anyway (+₹X), swap to a named alternative, or order that meal instead.
  - needed **later**: it swaps to the cheapest option within the limit, or holds the item and re-checks tomorrow.
- **Out of stock** (including items that sell out between search and cart): replaced within the limit, or put on hold.
- Everything that isn't simply added goes on the **Left out** list, with the numbers behind it.

The left-out list came from a reader's comment: *"I'd trust it more if I could see what it left out of my cart for being too expensive, especially if it was dinner for tonight."*

## Setup (about 15 minutes)
1. In Claude: Settings → Connectors → Add custom connector → `https://mcp.swiggy.com/instamart` (and `https://mcp.swiggy.com/food` if you order meals). Sign in with Swiggy.
2. Add `skill/weekly-grocery-agent` as a Claude skill, together with `price_guard.py`, `check_plan.py` and `data/`.
3. Optional history: `n8n/order-email-scan.json` reads Instamart order emails in Gmail (read-only) and outputs item and price rows for `data/price_log.csv`.
4. Edit your targets, diet rules (`preferences.md`) and nutrition table in `check_plan.py`. Then say: "plan my week".

## First real run (24 Nov 2026, Gurugram, vegetarian week)
- Meal plan: 7/7 days pass the check (2,321 to 2,468 kcal, 175 to 190 g protein).
- Cart: 13 lines, ₹1,562 to pay. Checkout not called.
- Left out / changed: baby spinach at ₹63 for 125 g → swapped to sarson saag at ₹13 for 250 g. Morinaga tofu at 4.6x the pick → skipped.
- Sold out in the seconds between search and cart: oats (replaced by Quaker, within the limit) and two Greek yoghurt packs (900 g short, on hold).
- My usual items with price history were within 20%: milk +11%, Greek yoghurt +6%.
- Greek yoghurt was 41% of the bill. Per gram of protein it costs about 15x more than soya chunks (₹4.70 vs ₹0.32).
- Run files: `runs/2026-11-24_*`. Tests: `python3 test_price_guard.py` (7/7). Plan check: `python3 check_plan.py` (7/7).

Only Instamart for now: it's the only quick-commerce app with an official MCP. Store-specific calls stay in the skill, so Blinkit or Zepto can be added when they launch official ones.
