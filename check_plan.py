# Weekly plan check (vegetarian). Nutrition per 100 g / 100 ml, typical values
# (USDA FoodData Central / IFCT 2017). Packaged items: the pack label overrides.
N = {  # kcal, protein g
 "soya chunks": (345, 52.0), "paneer": (265, 18.3), "tofu": (110, 12.0), "greek yoghurt": (73, 10.0),
 "toned milk": (58, 3.1), "besan": (387, 22.4), "moong dal": (347, 24.0), "rajma": (333, 23.6),
 "oats": (389, 16.9), "atta": (340, 13.2), "rice": (365, 7.1), "ww bread": (247, 13.0),
 "mixed veg": (35, 2.0), "greens": (25, 3.0), "onion tomato": (30, 1.0), "oil": (884, 0.0), "almonds": (579, 21.2),
}
def cooked(name, items):
    k = sum(N[f][0]*g/100 for f, g in items.items()); p = sum(N[f][1]*g/100 for f, g in items.items())
    return dict(name=name, kind="cook", kcal=round(k), protein=round(p, 1), items=items)
def ordered(name, kcal, protein):  # restaurant dish: estimate, labelled as such
    return dict(name=name, kind="order (estimate)", kcal=kcal, protein=protein, items={})

B_oats  = cooked("Overnight oats: Greek yoghurt + milk", {"oats": 50, "greek yoghurt": 200, "toned milk": 150})
B_chil  = cooked("Besan chilla x3 + Greek yoghurt", {"besan": 90, "onion tomato": 80, "oil": 8, "greek yoghurt": 150})
B_toast = cooked("Paneer bhurji on 2 ww toast + Greek yoghurt", {"paneer": 100, "ww bread": 60, "onion tomato": 60, "oil": 5, "greek yoghurt": 150})
SN      = cooked("Soya chaat + Greek yoghurt", {"soya chunks": 70, "onion tomato": 50, "greek yoghurt": 150})
MK      = cooked("Glass of milk", {"toned milk": 300})
D_soya  = cooked("Soya-paneer bhurji, 2 roti", {"soya chunks": 50, "paneer": 100, "onion tomato": 100, "atta": 60, "oil": 10})
D_tofu  = cooked("Air-fryer tofu tikka, 2 roti, sabzi", {"tofu": 200, "soya chunks": 40, "atta": 60, "mixed veg": 150, "oil": 10})
D_dal   = cooked("Moong dal with greens, rice, soya", {"moong dal": 60, "greens": 100, "soya chunks": 60, "rice": 50, "oil": 8})
D_raj   = cooked("Rajma chawal + air-fryer paneer tikka", {"rajma": 60, "rice": 60, "paneer": 100, "soya chunks": 40, "onion tomato": 80, "oil": 8})
L_bowl  = cooked("Soya pulao bowl (weekend)", {"soya chunks": 80, "rice": 70, "mixed veg": 150, "oil": 8})
O_sub   = ordered("Subway: footlong paneer tikka, no mayo", 700, 32)
O_pan   = ordered("Paneer tikka + 2 roti (restaurant)", 650, 35)
O_bur   = ordered("Burger Farm: spicy paneer burger", 550, 22)

week = {
 "Tue": [B_chil, O_pan, SN, D_soya],  "Wed": [B_oats, O_sub, SN, D_tofu, MK],
 "Thu": [B_toast, O_pan, SN, D_dal, MK],  "Fri": [B_oats, O_sub, SN, D_raj],
 "Sat": [B_chil, L_bowl, SN, O_pan, MK],  "Sun": [B_toast, L_bowl, SN, O_pan, MK],
 "Mon": [B_oats, O_pan, SN, D_tofu, MK],
}
LO, HI, PMIN = 2300, 2400, 180
fails = 0
print("Day | kcal | protein | check")
for d, meals in week.items():
    k = sum(m["kcal"] for m in meals); p = sum(m["protein"] for m in meals)
    ok = (LO - 100 <= k <= HI + 100) and p >= PMIN - 10; fails += not ok
    print(f"{d} | {k} | {p:.0f} g | {'OK' if ok else 'FLAG'}")
print(f"{7 - fails}/7 days pass")
