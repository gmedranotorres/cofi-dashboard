import json
from difflib import get_close_matches

# 1. Read GeoJSON names
with open("neighborhoods.geojson", "r", encoding="utf-8") as f:
    geojson = json.load(f)

geojson_names = sorted({
    feature["properties"].get("pri_neigh", "").strip()
    for feature in geojson["features"]
    if feature["properties"].get("pri_neigh")
})

# 2. Put your Google Sheets community names here
sheet_names = sorted({
    "North Lawndale",
    "Douglass Park",
    "Humboldt Park",
    "Little Village",
    "Auburn Gresham",
    "Gage Park",
    "Greater Grand Crossing",
    "East Garfield Park",
})

# 3. Compare
print("\nMATCH RESULTS\n")

for sheet_name in sheet_names:
    if sheet_name in geojson_names:
        print(f"✅ {sheet_name} -> exact match")
    else:
        suggestions = get_close_matches(sheet_name, geojson_names, n=3, cutoff=0.5)
        print(f"❌ {sheet_name} -> no exact match")
        print(f"   Suggestions: {suggestions}")

# 4. Optional: save all GeoJSON names
with open("pri_neigh_names.txt", "w", encoding="utf-8") as f:
    for name in geojson_names:
        f.write(name + "\n")

print("\nSaved GeoJSON names to pri_neigh_names.txt")