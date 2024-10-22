import bibtexparser
import json


def bibtex_to_json(bibtex_file):
    with open(bibtex_file, "r") as file:
        bibtex_data = bibtexparser.load(file)

    entries_json = []

    for entry in bibtex_data.entries:
        entry_json = {
            "type": entry.get("ENTRYTYPE", ""),
            "key": entry.get("ID", ""),
            "author": entry.get("author", ""),
            "title": entry.get("title", ""),
            "journal": entry.get("journal", ""),
            "booktitle": entry.get("booktitle", ""),
            "month": entry.get("month", ""),
            "year": entry.get("year", ""),
            "abbr": entry.get("journal", "").split()[-1] if "journal" in entry else "",
        }
        entries_json.append(entry_json)

    return json.dumps(entries_json, indent=4)


# Example usage
bibtex_file = "../_bibliography/papers.bib"  # replace with your file path
json_output = bibtex_to_json(bibtex_file)
with open("output.json", "w") as fd:
    fd.write(json_output)
