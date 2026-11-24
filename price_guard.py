"""Price guard + 'left out' list. Plain code: the AI never decides price calls.

Rules
- usual price  = your own past price per unit (from order history), else the
  median price per unit of the comparable options found today (reference).
- over limit   = today's price per unit > usual * (1 + LIMIT).
- urgency:
    needed TODAY  -> never dropped silently. Status ASK with 3 options:
                     buy anyway (+Rs X), swap to named alternative, or order that meal instead.
    needed LATER  -> swap to the cheapest in-limit alternative if one exists, else HOLD
                     (re-check price tomorrow).
- out of stock  -> HOLD if later, ASK if today.
Every non-'added' decision goes on the left-out list with the numbers behind it.
"""
from statistics import median

LIMIT = 0.20

def decide(item, today):
    """item: {name, needed_for, needed_day, usual_per_unit|None, unit, options:[{label, per_unit, price, in_stock, spin, sku, qty}] , preferred: label|None}"""
    opts = [o for o in item["options"] if o["in_stock"]]
    ref = item.get("usual_per_unit") or (median(o["per_unit"] for o in item["options"]) if item["options"] else None)
    basis = "your usual" if item.get("usual_per_unit") else "today's median"
    today_need = item["needed_day"] == today
    if not opts:
        return dict(status="ASK" if today_need else "HOLD", pick=None, ref=ref, basis=basis,
                    reason="out of stock", options=[])
    first = next((o for o in opts if o["label"] == item.get("preferred")), None) or min(opts, key=lambda o: o["per_unit"])
    over = (first["per_unit"] - ref) / ref if ref else 0
    if over <= LIMIT:
        return dict(status="ADD", pick=first, ref=ref, basis=basis, over=over)
    in_limit = sorted([o for o in opts if (o["per_unit"] - ref) / ref <= LIMIT], key=lambda o: o["per_unit"])
    if today_need:
        return dict(status="ASK", pick=None, ref=ref, basis=basis, over=over, first=first,
                    options=[f"Buy anyway: {first['label']} (+{over:.0%})",
                             f"Swap: {in_limit[0]['label']}" if in_limit else "Swap: none within limit",
                             "Order tonight's meal instead"])
    if in_limit:
        return dict(status="SWAP", pick=in_limit[0], ref=ref, basis=basis, over=over, first=first)
    return dict(status="HOLD", pick=None, ref=ref, basis=basis, over=over, first=first, reason="re-check tomorrow")

def report(items, today):
    cart, left = [], []
    for it in items:
        d = decide(it, today)
        if d["pick"]:
            cart.append(dict(spinId=d["pick"]["spin"], skuId=d["pick"]["sku"], quantity=d["pick"]["qty"],
                             label=d["pick"]["label"], price=d["pick"]["price"] * d["pick"]["qty"], for_=it["needed_for"]))
        if d["status"] != "ADD":
            left.append(dict(item=it["name"], needed_for=it["needed_for"], status=d["status"], **{
                "usual": d["ref"], "basis": d["basis"], "unit": it["unit"],
                "today": d.get("first", {}).get("per_unit") if d.get("first") else None,
                "over": d.get("over"), "did": (f"Swapped to {d['pick']['label']}" if d["status"] == "SWAP"
                        else d.get("reason") or "; ".join(d.get("options", []))),
                "first_label": d.get("first", {}).get("label") if d.get("first") else None}))
    for it in items:  # skipped options worth showing (2x+ the pick), not decisions
        for o in it.get("notable_skips", []):
            left.append(dict(item=it["name"], needed_for=it["needed_for"], status="SKIPPED", usual=None, basis="",
                             unit=it["unit"], today=o["per_unit"], over=None, did=o["why"], first_label=o["label"]))
    return cart, left
