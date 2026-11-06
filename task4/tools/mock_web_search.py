import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "company_data.json"


def search_company(name):

    with open(
        DATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        company_data = json.load(file)

    if name in company_data:
        return company_data[name]

    return {
        "news": "No news available.",
        "products": [],
        "pain_points": []
    }