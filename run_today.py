import json, importlib.util, sys
from price_guard import report
spec = importlib.util.spec_from_file_location("inp", "runs/2026-11-24_inputs.py"); inp = importlib.util.module_from_spec(spec); spec.loader.exec_module(inp)
cart, left = report(inp.ITEMS, inp.TODAY)
print("CART")
for c in cart: print(f"  {c['label']:45} x{c['quantity']}  Rs{c['price']:>5}  ({c['for_']})")
print(f"  TOTAL items Rs{sum(c['price'] for c in cart)}")
print("\nLEFT OUT / CHANGED")
for l in left:
    u = f"usual Rs{l['usual']:.1f}{l['unit']} ({l['basis']})" if l["usual"] else ""
    t = f"today Rs{l['today']}{l['unit']}" if l["today"] else ""
    ov = f"+{l['over']:.0%}" if l.get("over") else ""
    print(f"  [{l['status']}] {l['item']} — for {l['needed_for']} | {l.get('first_label') or ''} {t} {u} {ov} → {l['did']}")
json.dump(dict(cart=cart, left=left), open("runs/2026-11-24_result.json", "w"), indent=1, default=str)
