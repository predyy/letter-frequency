import argparse
import yaml
import json

def count_chars(filename, language = "english", ascii = False):
    """Counts the occurrences of each character and character pair in a given text."""
    language_data = get_language_data(language)
    alphabet = language_data["alphabet"]

    if ("ascii_mappings" in language_data):
        ascii_mappings = language_data["ascii_mappings"]
    else:
        print("No ASCII mappings found for this language.")
        ascii_mappings = {}
   
    counts = {char: 0 for char in alphabet}
    if ascii:
        for char in ascii_mappings:
            del counts[char]

    pair_counts = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            for i in range(len(line) - 1):
                pair = line[i:i+2]
                pair = pair.lower()

                if ascii:
                    if pair[0] in ascii_mappings:
                        pair = ascii_mappings[pair[0]] + pair[1]
                    if pair[1] in ascii_mappings:
                        pair = pair[0] + ascii_mappings[pair[1]]

                if pair[0] not in alphabet or pair[1] not in alphabet:
                    continue
                
                counts[pair[0]] += 1

                if pair in pair_counts:                    
                    pair_counts[pair] += 1
                else:
                    pair_counts[pair] = 1

    total_chars = sum(counts.values())
    total_pairs = sum(pair_counts.values())
    counts = {char: count / total_chars for char, count in counts.items()}
    pair_counts = {pair: count / total_pairs for pair, count in pair_counts.items()}

    return (counts, pair_counts)

def get_language_data(language = "english"):
    """Returns the language data for a given language."""

    with open(f"data/alphabets/{language}.yaml", "r") as file:
        data = yaml.safe_load(file)
        if (data is None):
            raise ValueError(f"Alphabet for language '{language}' not found.")

        return(data) 

parser = argparse.ArgumentParser(description='Get the frequency of characters and pairs of characters from a text file.')
parser.add_argument('filepath', type=str, help='The path to the file to process')
parser.add_argument('--language', type=str, help='Select language', default="english")
parser.add_argument('--ascii', action='store_true', help='Turn on ASCII-only mode; this will attempt to convert non-ASCII characters to ASCII.')
parser.add_argument('--yaml', action='store_true', help='Add YAML output')
parser.add_argument('--json', action='store_true', help='Add JSON output')
args = parser.parse_args()

results = count_chars(args.filepath, args.language, args.ascii)

for table in results:
    for char, value in table.items():
        print(f"{char}: {value}")
  
if (args.json):
    with open("out_single.json", 'w') as file:
        json.dump(results[0], file)
    with open("out_pairs.json", 'w') as file:
        json.dump(results[1], file)

if (args.yaml):
    with open("out_single.yaml", 'w') as file:
        yaml.dump(results[0], file)
    with open("out_pairs.yaml", 'w') as file:
        yaml.dump(results[1], file)