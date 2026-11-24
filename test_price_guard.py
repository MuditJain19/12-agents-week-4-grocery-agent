from price_guard import decide
o = lambda l, p, s=True: dict(label=l, per_unit=p, price=p, in_stock=s, spin=l, sku=l, qty=1)
T = "Tue"
def t(name, **kw): return dict(name=name, needed_for="x", unit="/100g", options=kw.pop("opts"), **kw)
# 1 within limit -> ADD
assert decide(t("a", needed_day="Wed", usual_per_unit=10, opts=[o("A", 11)]), T)["status"] == "ADD"
# 2 over limit, needed later, cheaper in-limit option -> SWAP
r = decide(t("b", needed_day="Wed", usual_per_unit=10, preferred="A", opts=[o("A", 13), o("B", 11.5)]), T)
assert r["status"] == "SWAP" and r["pick"]["label"] == "B"
# 3 over limit, needed TONIGHT -> ASK, never silent drop or silent swap
r = decide(t("c", needed_day="Tue", usual_per_unit=10, preferred="A", opts=[o("A", 13), o("B", 11.5)]), T)
assert r["status"] == "ASK" and r["pick"] is None and len(r["options"]) == 3
# 4 over limit later, nothing in limit -> HOLD
assert decide(t("d", needed_day="Fri", usual_per_unit=10, opts=[o("A", 15)]), T)["status"] == "HOLD"
# 5 out of stock tonight -> ASK; later -> HOLD
assert decide(t("e", needed_day="Tue", usual_per_unit=10, opts=[o("A", 9, False)]), T)["status"] == "ASK"
assert decide(t("f", needed_day="Fri", usual_per_unit=10, opts=[o("A", 9, False)]), T)["status"] == "HOLD"
# 6 no history -> median of today's options is the reference
r = decide(t("g", needed_day="Wed", usual_per_unit=None, opts=[o("A", 10), o("B", 12), o("C", 30)]), T)
assert r["status"] == "ADD" and r["basis"] == "today's median"
print("price guard: 7/7 checks passed")
