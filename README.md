# TitleToDOI

A minimal Python script to retrieve the [DOI](https://www.doi.org/) (Digital Object Identifier) of a research paper from its title using the [CrossRef API](https://www.crossref.org/services/metadata-delivery/rest-api/).

---

## Features

- 🔎 **Automatic DOI Lookup**: Enter a paper’s title, and the script fetches its DOI from CrossRef.
- 🚦 **Best-Match Filtering**: Attempts to match the queried title with the CrossRef result for accuracy.
- 🛡️ **User-Friendly**: Simple, interactive command-line tool—no dependencies beyond `requests`.
- 🤝 **Respectful API Usage**: Includes a polite User-Agent as recommended by CrossRef.

---

## Requirements

- Python 3.7+
- `requests` library

Install dependencies with:

```bash
pip install requests
```

---

## Usage

```bash
python title_to_doi.py
```

You will be prompted to enter the paper title:

```text
Enter the paper title: Deep Learning for Healthcare: Review, Opportunities and Challenges
DOI: 10.1109/tbme.2018.2874532
```

If the DOI is not found, you’ll receive a friendly message.

---

## Example

```python
from title_to_doi import title_to_doi

doi = title_to_doi("Attention Is All You Need")
print(doi)  # Outputs: 10.5555/3295222.3295349
```

---

## How It Works

1. **Title Search:** Sends the given title as a query to the CrossRef REST API.
2. **Result Filtering:** Checks if the returned title closely matches the input; if so, returns the DOI.
3. **Fallback:** If the best match isn't perfect, still returns the top result’s DOI for convenience.
4. **Output:** Displays the found DOI or a “not found” message.

---

## Notes & Limitations

- Results depend on CrossRef’s indexing and may not be perfect for ambiguous or very short titles.
- For best results, use complete and exact paper titles.

---

## Acknowledgements

- Powered by the [CrossRef Metadata API](https://api.crossref.org/).
- Inspired by the need to quickly convert literature titles to persistent, citable links.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

Questions or suggestions?\
Feel free to open an issue or contact [Pouria Mortezaagha](mailto\:pouriamortezaagha7@gmail.com).

---

