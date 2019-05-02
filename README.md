
DuckDuckgo Search API
=====

DuckDuckgo Search API is a python based library for searching various functionalities of DuckDuckgo.  It uses screen scraping to retrieve the results, and thus is unreliable if the way DuckDuckgo's web pages are returned change in the future.

*Disclaimer: This software uses screen scraping to retrieve search results from DuckDuckgo.com, and therefore this software may stop working at any given time.  Use this software at your own risk. I assume no responsibility for how this software API is used by others.*

**Table of Contents**

- [DuckDuckgo Search API](#DuckDuckgo-search-api)
  - [Installation](#installation)
  - [DuckDuckgo Web Search](#DuckDuckgo-web-search)


Installation
------------

The repo is structured like a package, so it can be installed from pip using
github clone url. From command line type:

```
pip install git+https://github.com/arthurbarros/DuckDuckgo-Search-API
```

To upgrade the package if you have already installed it:

```
pip install git+https://github.com/arthurbarros/DuckDuckgo-Search-API --upgrade
```

## DuckDuckgo Web Search
You can search DuckDuckgo web in the following way:

```python
from duckduckgo import duckduckgo
search_results = duckduckgo.search("This is my query")
```

`search_results` will contain a list of `DuckDuckgoResult` objects. num_page parameter is optional (default is 1 page)

```python
DuckDuckgoResult:
    self.name # The title of the link
    self.link # The external link
    self.description # The description of the link
```
