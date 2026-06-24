import json

with open("neighborhoods.geojson", "r", encoding="utf-8") as f:
    geojson = json.load(f)

names = sorted(
    {
        feature["properties"]["pri_neigh"]
        for feature in geojson["features"]
        if "pri_neigh" in feature["properties"]
    }
)

for name in names:
    print(name)