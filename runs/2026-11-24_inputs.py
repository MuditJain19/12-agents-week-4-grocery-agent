# Real Instamart search results, 24 Nov 2026, Gurugram. per_unit = Rs per 100 g, 100 ml or pack.
def o(label, per_unit, price, spin, sku, qty=1, in_stock=True): return dict(label=label, per_unit=per_unit, price=price, spin=spin, sku=sku, qty=qty, in_stock=in_stock)
TODAY = "Tue"
ITEMS = [
 dict(name="Paneer 400 g", needed_for="Tonight + 3 more meals", needed_day="Tue", unit="/100 g", usual_per_unit=None, preferred=None, options=[
   o("NOICE Fresh Malai Paneer 200 g x2", 37.5, 75, "TDF8TT5DOR", "HYO15RSI66", qty=2), o("Amul Fresh Paneer 200 g", 47.5, 95, "2C6V5PBANE", "GYG2TF8M36"),
   o("Mother Dairy Paneer 200 g", 50, 100, "SIN3I7HTTZ", "7H8GGBD2CK"), o("Milky Mist Paneer 200 g", 50.5, 101, "UYVXDKB0SY", "NKZBR2S4AU"),
   o("Milky Mist High Protein Paneer 200 g", 46, 92, "3VJIVWSGN3", "DYCR3MJWTS"), o("Heritage High Protein Paneer 240 g", 44.2, 106, "TAN24Z461J", "F3LZXQP7WB"),
   o("Ananda Premium Paneer 200 g", 52.5, 105, "ZK2EXJ1F2J", "Q39PWML3DW"), o("NOICE High Protein Paneer 200 g", 57.5, 115, "J6K2GFOHL3", "8AXYQ4AALV"),
   o("Country Delight Paneer 180 g", 63.9, 115, "5JH8S7X14M", "8X0GUQJKVN"), o("Epigamia High Protein Paneer 200 g", 77.5, 155, "V38SFXK99P", "0F0DOBMR5I"),
   o("Pride of Cows Paneer 200 g", 79.5, 159, "KSHN0XPKD6", "R64RXBRHSG")]),
 dict(name="Soya chunks", needed_for="Tonight: paneer-soya bhurji", needed_day="Tue", unit="/100 g", usual_per_unit=None, options=[
   o("Supreme Harvest Soya Chunks 200 g", 18, 36, "FAL163U6JD", "XW9RMMMUU5"), o("Fortune Soya Chunk 200 g", 24.5, 49, "9BX0IKWVJG", "UKQKKY279R"),
   o("Nutrela Soya Chunks 200 g", 26, 52, "QYVM8SZTHH", "PTAMJ7K9JG"), o("Saffola Mealmaker 200 g", 28.5, 57, "KYHB6SCXAT", "GCA27CH76V"),
   o("Aashirvaad Soya Chunks 200 g", 20.5, 41, "1N3L1TTW4L", "IMU6FWRNOR")]),
 dict(name="Onion 1 kg", needed_for="Tonight + week", needed_day="Tue", unit="/100 g", usual_per_unit=None, options=[
   o("Onion 1 kg", 6.6, 66, "FG8WDTXSUN", "02KZ302FU7"), o("Organic Onion 1 kg", 9.5, 95, "69CV6JQ52I", "QSTPRQQN2A")]),
 dict(name="Tomato 500 g", needed_for="Tonight + week", needed_day="Tue", unit="/100 g", usual_per_unit=None, options=[
   o("Indian Tomato 500 g", 4.4, 22, "0GWBSRKMYQ", "2FVH2A4HU0"), o("Hybrid Tomato 500 g", 4.4, 22, "TOXY8MIG4N", "3QK6PBKT7R"),
   o("Organic Hybrid Tomato 500 g", 7.4, 37, "RBCL4S5JU7", "021H5NU8FP")]),
 dict(name="Soya chunks 1 kg", needed_for="Daily snack + dinners", needed_day="Wed", unit="/100 g", usual_per_unit=None, options=[
   o("Fortune Soya Chunks 1 kg", 16.6, 166, "5AKPD3J08Q", "9VRA2GJWAJ"), o("Fortune Soya Chunk 200 g", 24.5, 49, "9BX0IKWVJG", "UKQKKY279R"),
   o("Nutrela Soya Chunks 200 g", 26, 52, "QYVM8SZTHH", "PTAMJ7K9JG"), o("Aashirvaad Soya Chunks 200 g", 20.5, 41, "1N3L1TTW4L", "IMU6FWRNOR")]),
 dict(name="Tofu 400 g", needed_for="Wed & Mon dinners", needed_day="Wed", unit="/100 g", usual_per_unit=None, options=[
   o("Pro Plant Tofu 200 g x2", 28, 112, "BXETSXD06K", "9NFBUA3FUN"), o("Health on Plants Organic Tofu 200 g", 52.5, 105, "RBZ4ASR1FF", "VHUNSR3G9G"),
   o("Mooz Formaggio Vegetable Tofu 200 g", 54, 108, "7YMUYAB6U3", "MUS87MUJQ6"), o("Mooz Fresh & Firm Tofu 200 g", 49.5, 99, "TYYCQLY2JD", "IG8HYCF90T"),
   o("Morinaga Tofu Extra Firm 308 g", 129.5, 399, "EYVFWGR6V3", "VLFVF00L7H")],
   notable_skips=[dict(label="Morinaga Tofu Extra Firm 308 g", per_unit=129.5, why="Skipped: 4.6x the price of the pick")]),
 dict(name="Greek yoghurt", needed_for="Snacks + breakfasts", needed_day="Wed", unit="/100 g", usual_per_unit=44.4, preferred="Milky Mist Greek Yoghurt 225 g x5 + x3", options=[
   o("Milky Mist Greek Yoghurt 225 g x5 + x3", 47.1, 848, "KJ0EZBGDF4+HEINCJ2T0T", "L4JBZ3NB8A+X1P6481CPA"),
   o("Epigamia Greek Yogurt Natural 400 g", 56.3, 225, "EDJ0N0BVPX", "RBRO6NXDNQ")]),
 dict(name="Milk 2 L", needed_for="Overnight oats + nightly glass", needed_day="Wed", unit="/100 ml", usual_per_unit=5.6, preferred="Amul Taaza 500 ml x4", options=[
   o("Amul Taaza 500 ml x4", 6.2, 124, "D9PNFAT8MI", "L6GF8F99SQ"), o("Amul Moti Toned 450 ml x2", 7.3, 66, "LG3284WMD5", "YIRM55TWKF"),
   o("Amul Taaza Toned 1 L", 7.7, 77, "HH5FTSMTW0", "33SP4N1D1Y")]),
 dict(name="Whole-wheat bread", needed_for="Paneer toast breakfasts", needed_day="Wed", unit="/100 g", usual_per_unit=None, options=[
   o("The Health Factory Whole Wheat 350 g", 18.6, 65, "YL7ZNQ4NVF", "CZWVJZ8IBX"), o("The Health Factory Whole Wheat 250 g", 22, 55, "N3DHY2LMT1", "I0U80BV1U0")]),
 dict(name="Mixed veg 500 g", needed_for="Tofu tikka sabzi", needed_day="Wed", unit="/100 g", usual_per_unit=None, options=[
   o("Safal Frozen Mixed Vegetables 500 g", 15.2, 76, "1VJN27TW4M", "ROD9MBR0SB")]),
 dict(name="Spinach / greens", needed_for="Thu dal", needed_day="Thu", unit="/100 g", usual_per_unit=None, preferred="Baby Spinach 125 g", options=[
   o("Baby Spinach 125 g", 50.4, 63, "ZRH8VAC3LY", "0WA82VLG26"), o("Methi 1 bunch (~150 g)", 14, 21, "WPZ8FWD02N", "I3YDWX938G"),
   o("Sarson Saag 250 g", 5.2, 13, "JG75C8UARK", "IPZAF1NF1Q")]),
 dict(name="Oats", needed_for="Oats breakfasts", needed_day="Wed", unit="/100 g", usual_per_unit=None, options=[
   o("Quaker High Protein Oats 400 g", 20.8, 83, "UUU62HXTSA", "ORBNNMCRGV"), o("Saffola Oats 460 g", 19.6, 90, "MCNIWG4OC3", "ABJ1RS1SG1"),
   o("True Elements Rolled Oats 500 g", 28.4, 142, "KDYRCJ7QH2", "60DXSVHPMP"), o("Yogabar Rolled Oats 400 g", 37.3, 149, "CHWQGUJ049", "VZNSJLUMQU")]),
]
