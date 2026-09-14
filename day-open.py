# Records the day's opening metal prices into open.json.
# Run once a day at 00:05 UTC by .github/workflows/day-open.yml
import json, urllib.request, datetime
SYMBOLS = ["XAU", "XAG", "XPT", "XPD", "HG"]
prices = {s: json.load(urllib.request.urlopen("https://api.gold-api.com/price/" + s))["price"] for s in SYMBOLS}
day = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
open("open.json", "w").write(json.dumps({"day": day, "prices": prices}, indent=2) + "\n")
print(day, prices)
