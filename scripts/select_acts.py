"""Selection of acts to publish.

The Sejm ELI search endpoint is queried for every act of Dziennik Ustaw that the API
flags as in force (inForce=1), per type.  Result pages are cached in
<raw>/search/<type>.json.  The Constitution (DU/1997/483) is always included.
"""
import json
import os
import sys
import time

import requests

API = "https://api.sejm.gov.pl/eli"
UA = "LawCodex/1.0 (+https://github.com/LawCodex)"

# API type name -> our category key
TYPES = {
    "Ustawa": "ustawa",
    "Dekret": "dekret",
    "Rozporządzenie": "rozporzadzenie",
}
CONSTITUTION = "DU/1997/483"
# Statuses not published even when the API flags the act inForce: amending acts whose
# content is already merged into another act's consolidated text, and inconsistent records.
SKIP_STATUS = {"akt objęty tekstem jednolitym", "uchylony", "wygaśnięcie aktu"}


def _get(url, params):
    delay = 2
    for i in range(8):
        try:
            r = requests.get(url, params=params, headers={"User-Agent": UA}, timeout=300)
            if r.status_code == 200:
                return r.json()
            err = f"HTTP {r.status_code}"
        except (requests.RequestException, ValueError) as e:
            err = str(e)
        print(f"  retry {i+1} search {params}: {err}", file=sys.stderr, flush=True)
        time.sleep(delay)
        delay = min(delay * 2, 120)
    raise RuntimeError(f"search failed {params}")


def search_type(raw, api_type, refresh=False):
    path = os.path.join(raw, "search", TYPES[api_type] + ".json")
    if os.path.exists(path) and not refresh:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    items, offset, total = [], 0, None
    while total is None or offset < total:
        d = _get(f"{API}/acts/search", {"publisher": "DU", "type": api_type, "inForce": 1,
                                        "limit": 500, "offset": offset})
        total = d["totalCount"]
        items.extend(d["items"])
        offset += 500
        print(f"search {api_type}: {len(items)}/{total}", flush=True)
        if not d["items"]:
            break
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False)
    return items


def category(item):
    if item["ELI"] == CONSTITUTION:
        return "konstytucja"
    return TYPES.get(item["type"])


def selected_items(raw, types=None, refresh=False):
    """List of search items (dicts with ELI, title, type, status...) to publish."""
    out, seen = [], set()
    for api_type, key in TYPES.items():
        if types and key not in types:
            continue
        for it in search_type(raw, api_type, refresh):
            if it["ELI"] in seen or it.get("status") in SKIP_STATUS:
                continue
            seen.add(it["ELI"])
            out.append(it)
    if CONSTITUTION not in seen and (not types or "konstytucja" in types or "ustawa" in types):
        out.append({"ELI": CONSTITUTION, "type": "Ustawa", "title": "Konstytucja Rzeczypospolitej Polskiej"})
    return out
