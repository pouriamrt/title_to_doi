# TitleToDOI

Tools for converting research paper titles into [DOI](https://www.doi.org/) (Digital Object Identifier) links using the [CrossRef REST API](https://www.crossref.org/services/metadata-delivery/rest-api/).

---

## Features

- 🔎 **Automatic DOI Lookup** – simple function for retrieving a DOI from a title.
- 🌐 **Web Interface** – `app.py` exposes a tiny Flask app for searching from the browser.
- 📑 **Batch Processing** – `program.py` demonstrates how to add DOIs to rows in an Excel sheet.
- 🤝 **Respectful API Usage** – every request sets a friendly User-Agent as recommended by CrossRef.

---

## Requirements

- Python 3.7+
- [`requests`](https://pypi.org/project/requests/) – required
- [`flask`](https://pypi.org/project/flask/) – for the web app
- [`pandas`](https://pypi.org/project/pandas/) and [`tqdm`](https://pypi.org/project/tqdm/) – for Excel processing

Install the packages you need with:

```bash
pip install requests flask pandas tqdm
```

---

## Usage

### Lookup a single title

Use the `title_to_doi` function directly in your own code:

```python
from program import title_to_doi

doi = title_to_doi("Attention Is All You Need")
print(doi)
```

### Run the web app

```bash
python app.py
```

Visit <http://localhost:8080> and enter a paper title. If a DOI is found it will be displayed and linked.

### Process an Excel sheet

`program.py` expects an Excel file named `picos_compliance_results.xlsx` in the parent directory.  For each row the script looks up the DOI and writes the results to `picos_compliance_results_with_doi.xlsx`.

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

Questions or suggestions?
Feel free to open an issue or contact [Pouria Mortezaagha](mailto:pouriamortezaagha7@gmail.com).

---

