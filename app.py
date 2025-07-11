from flask import Flask, render_template_string, request, jsonify
import requests

app = Flask(__name__)

def title_to_doi(title):
    headers = {"User-Agent": "TitleToDOI/1.0 (mailto:pouriamortezaagha7@gmail.com)"}
    params = {"query.bibliographic": title, "rows": 1}
    url = "https://api.crossref.org/works"
    resp = requests.get(url, params=params, headers=headers)
    if resp.status_code == 200:
        results = resp.json()["message"]["items"]
        if results:
            found_title = results[0]["title"][0].lower()
            if title.lower() in found_title or found_title in title.lower():
                return results[0]["DOI"]
            else:
                return results[0]["DOI"]
    return None

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Paper Title to DOI</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f4f6f8;}
        .container { background: #fff; padding: 30px 40px; border-radius: 10px; box-shadow: 0 2px 8px #ddd; max-width: 500px; margin: auto;}
        h2 { text-align: center; color: #2d3846;}
        input, button { font-size: 1.1em; }
        #result { margin-top: 20px; font-size: 1.1em;}
        .doi { color: green; font-weight: bold;}
        .notfound { color: #d22;}
    </style>
</head>
<body>
    <div class="container">
        <h2>Find DOI by Paper Title</h2>
        <form id="doiForm" autocomplete="off">
            <input type="text" id="title" name="title" placeholder="Enter paper title" style="width: 90%;" required>
            <button type="submit">Search DOI</button>
        </form>
        <div id="result"></div>
    </div>
<script>
document.getElementById('doiForm').onsubmit = async function(e) {
    e.preventDefault();
    let title = document.getElementById('title').value.trim();
    document.getElementById('result').innerHTML = "Searching...";
    let resp = await fetch('/doi', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title })
    });
    let data = await resp.json();
    if (data.doi) {
        document.getElementById('result').innerHTML = '<span class="doi">DOI: <a href="https://doi.org/' + data.doi + '" target="_blank">' + data.doi + '</a></span>';
    } else {
        document.getElementById('result').innerHTML = '<span class="notfound">DOI not found.</span>';
    }
};
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(TEMPLATE)

@app.route("/doi", methods=["POST"])
def get_doi():
    title = request.json.get("title")
    if not title:
        return jsonify({"doi": None})
    doi = title_to_doi(title)
    return jsonify({"doi": doi})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
