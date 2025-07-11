import requests

def title_to_doi(title):
    """
    Given a paper title, search CrossRef for its DOI.
    Returns the best match DOI or None if not found.
    """
    # CrossRef works best if you send a polite User-Agent
    headers = {"User-Agent": "TitleToDOI/1.0 (mailto:pouriamortezaagha7@gmail.com)"}
    params = {
        "query.bibliographic": title,
        "rows": 1  # Return the best match only
    }
    url = "https://api.crossref.org/works"
    resp = requests.get(url, params=params, headers=headers)
    if resp.status_code == 200:
        results = resp.json()["message"]["items"]
        if results:
            # Basic filter: return DOI if the title is a close match
            found_title = results[0]["title"][0].lower()
            if title.lower() in found_title or found_title in title.lower():
                return results[0]["DOI"]
            else:
                # Fallback: return the top result anyway
                return results[0]["DOI"]
    return None

if __name__ == "__main__":
    paper_title = input("Enter the paper title: ").strip()
    doi = title_to_doi(paper_title)
    if doi:
        print(f"DOI: {doi}")
    else:
        print("DOI not found.")
