import demjson3 as demjson
import json
import re

# Reading the js file
with open(r'C:\Users\tmaga\OneDrive - NH Public Defender\quote\OneDrive_1_9-25-2023\shore\PhilosophicalQuotes.js', 'r', encoding='utf-8') as file:
    js_object_str = file.read()

# Extract the array assigned to 'const deeperPhilosophicalQuotes'
match = re.search(
    r'const philosophicalQuotes = (\[.*?\]);', js_object_str, re.DOTALL)
if match:
    js_array_str = match.group(1)
else:
    print("No 'const philosophicalQuotes =' declaration found.")
    js_array_str = '[]'

# Decode the JS array to a Python list
try:
    quote_data = demjson.decode(js_array_str)
except demjson.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")
    quote_data = []

duplicates = []
seen_items = set()

# Check for duplicates
for item in quote_data:
    if item in seen_items:
        duplicates.append(item)
    else:
        seen_items.add(item)

# Save duplicates to a file
with open(r'C:\Users\tmaga\OneDrive - NH Public Defender\quote\OneDrive_1_9-25-2023\shore\duplicate_quotes.js', 'w') as duplicate_file:
    duplicate_file.write('const duplicate_quotes = ')
    json.dump(duplicates, duplicate_file, indent=4)

# Convert seen_items set to a JavaScript array and save it to another file
seen_items_js = json.dumps(list(seen_items), indent=4)
with open(r'C:\Users\tmaga\OneDrive - NH Public Defender\quote\OneDrive_1_9-25-2023\shore\seen_items.js', 'w') as seen_items_file:
    seen_items_file.write(f'const seen_quotes = {seen_items_js};\n')

print("Seen items saved in 'seen_items.js'")
