import urllib.request
import os

url = "https://raw.githubusercontent.com/rowanhogan/australian-states/refs/heads/master/states.geojson"
output_path = os.path.join('data', 'australia_states.geojson')

print("Downloading Australian state boundaries...")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response, open(output_path, 'wb') as out_file:
    out_file.write(response.read())

print(f"Successfully saved map to {output_path}")