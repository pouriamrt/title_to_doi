import requests
import pandas as pd
from tqdm import tqdm

def title_to_doi(title):
    headers = {"User-Agent": "TitleToDOI/1.0 (mailto:pouriamortezaagha7@gmail.com)"}
    params = {"query.bibliographic": title, "rows": 1}
    url = "https://api.crossref.org/works"
    try:
        resp = requests.get(url, params=params, headers=headers, timeout=15)
        if resp.status_code == 200:
            results = resp.json()["message"]["items"]
            if results:
                found_title = results[0]["title"][0].lower()
                if title.lower() in found_title or found_title in title.lower():
                    return results[0]["DOI"]
                else:
                    return results[0]["DOI"]
    except Exception as e:
        print(f"Error contacting CrossRef: {e}")
    return None


if __name__ == "__main__":
    df = pd.read_excel("../picos_compliance_results.xlsx", sheet_name="Sheet1")
    for index, row in tqdm(df.iterrows(), total=len(df)):
        doi = title_to_doi(row['Title'])
        df.at[index, 'DOI'] = doi
        
    df.to_excel("../picos_compliance_results_with_doi.xlsx", index=False)
