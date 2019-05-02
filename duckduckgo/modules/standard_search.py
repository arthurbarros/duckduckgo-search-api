from .utils import _get_search_url, get_html
from bs4 import BeautifulSoup


class DuckDuckGoResult:
    """Represents a DuckDuckGo search result."""
    name = None
    link = None
    description = None


# PUBLIC
def search(query):
    """Returns a list of DuckDuckGoResult.

    Args:
        query: String to search in DuckDuckGo.

    TODO: add support to get the DuckDuckGo results.
    Returns:
        A DuckDuckGoResult object."""

    results = []
    url = _get_search_url(query)
    html = get_html(url)

    if html:
        soup = BeautifulSoup(html, "html.parser")
        divs = soup.findAll("div", attrs={"class": "web-result"})

        for li in divs:
            res = DuckDuckGoResult()

            res.name = _get_name(li)
            res.description = _get_description(li)
            res.link = _get_link(li)

            results.append(res)
    return results


# PRIVATE
def _get_name(li):
    """Return the name of a duckduckgo search."""
    a = li.find("a")
    # return a.text.encode("utf-8").strip()
    if a is not None:
        return a.text.strip()
    return None


def _get_link(li):
    """Return external link from a search."""
    try:
        a = li.find("a")
        link = a["href"]
    except Exception:
        return None
    return link


def _get_description(li):
    """Return the description of a duckduckgo search.

    TODO: There are some text encoding problems to resolve."""

    sdiv = li.find("div", attrs={"class": "result__body"})
    if sdiv:
        stspan = sdiv.find("a", attrs={"class": "result__snippet"})
        if stspan is not None:
            # return stspan.text.encode("utf-8").strip()
            return stspan.text.strip()
    else:
        return None

