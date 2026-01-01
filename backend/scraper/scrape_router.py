import requests

def detect_source_type(url):
    """
    Decide how to scrape based on URL characteristics.
    Returns: 'api', 'static', or 'dynamic'
    """

    if "api" in url or url.endswith(".json"):
        return "api"

    try:
        response = requests.get(url, timeout=5)
        html = response.text.lower()

        # Heuristic: heavy JS frameworks
        js_indicators = ["react", "angular", "vue", "__next", "webpack"]

        if any(js in html for js in js_indicators):
            return "dynamic"

        return "static"

    except Exception:
        return "dynamic"
