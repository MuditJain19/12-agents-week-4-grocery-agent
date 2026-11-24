---
name: weekly-grocery-agent
description: Plan my week's meals to my calorie and protein targets, then fill my Swiggy Instamart cart with a price guard and a "left out" list. Use when I say "plan my week", "do my groceries", or dictate which meals I cook vs order.
---

# Weekly grocery agent

Needs the official Swiggy MCP connectors in Claude: Instamart (https://mcp.swiggy.com/instamart) and, for ordered meals, Swiggy Food (https://mcp.swiggy.com/food).

## Hard rules
- NEVER call `checkout` (Instamart) or `place_food_order` (Food). You fill carts; the human checks out and pays.
- `update_cart` REPLACES the whole cart. Always `get_cart` first and send the merged list. After every update, read the response: items can go out of stock between search and cart. Replace them with the next in-limit option or put them on the left-out list.
- The AI does not decide calories, protein or price calls. Code does: `check_plan.py` and `price_guard.py`.

## Each week
1. **Ask what I'm cooking vs ordering**, day by day. Read `preferences.md` (diet rules and swaps I made before). Never plan, search or add anything that breaks the diet rules.
2. **Draft the plan**, then run `check_plan.py`. Every day must land within the calorie range ±100 kcal and at least 170 g protein (target 180 g). Fix failing days and re-run. Restaurant meals are labelled as estimates.
3. **Show me the plan.** I approve or swap; append every swap to `preferences.md`.
4. **Shopping list** = cooked meals minus pantry staples I have. Tag each item with the day it's first needed.
5. **Search Instamart** for each item at my address. Pass every in-stock option with price per unit (`unitLevelPrice`) into `price_guard.py`, together with my usual price per unit from `data/price_log.csv` (seeded from my order emails).
6. **Apply the decisions**: ADD / SWAP go in the cart. HOLD and ASK don't.
   - ASK (needed today and over the limit, or out of stock): stop and ask me: buy anyway (+₹X) / named swap / order tonight's meal instead.
7. **Report**: plan, cart total, and the LEFT OUT list (item, needed for, usual vs today's price, what you did). End with: "Cart ready. Nothing is ordered until you check out."
8. Append today's prices to `data/price_log.csv`.
