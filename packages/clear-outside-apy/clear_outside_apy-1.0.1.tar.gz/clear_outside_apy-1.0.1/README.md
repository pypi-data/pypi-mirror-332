# ClearOutsideAPY

[![PyPI - Version](https://img.shields.io/pypi/v/clear-outside-apy?style=for-the-badge)](https://pypi.org/project/clear-outside-apy/)
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FTheElevatedOne%2FClearOutsideAPY%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&style=for-the-badge)

## Webscraper/API for ClearOutside.com

Python module for scraping and parsing data from [clearoutside.com](https://clearoutside.com)

Created using [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/), [requests](https://pypi.org/project/requests/) and [html5lib](https://pypi.org/project/html5lib/).

## Installation

From [PyPI](https://pypi.org/project/clear-outside-apy/):

```
pip install clear-outside-apy
```

From repo:

```
pip install git+https://github.com/TheElevatedOne/ClearOutsideAPY.git
```

## Usage

```python
from clear_outside_apy import ClearOutsideAPY

api = ClearOutsideAPY(lat: str, long: str, view: str = "midday")
api.update()
result = api.pull()
```

- `lat` -> latitude with two decimal places
- `long` -> longitude with two decimal places
  - ex. `lat = "43.16", long = "-75.84"` -> [New York](https://clearoutside.com/forecast/43.16/-75.84)  
- `view` -> string in three formats:
  - `midday` -> start at 12pm/12:00
  - `midnight` -> start at 12am/24:00
  - `current` -> start at current time

- `__init__` -> initializes the class, scrapes the website for the first time <br>
- `update()` -> scrapes the website <br>
- `pull()` -> parses and pulls the data; returns a giant dictionary

## Output Preview

### Units

**This Module outputs everything in Metric Units and European/Military time (24h)**

- Date format: dd/MM/yy,
- Sky Quality:
  - Brightness - millicandela per meter squared,
  - Artificial Brightness - candela per meter squared,
- Distance/Visibility: kilometers; (if showing 0.0, data is missing from the website),
- Rain: millimeters,
- Speed: kilometers per hour
- Temperature: degrees Celsius
- Pressure: millibars
- Ozone: Dobson Unit (du)

### Result

Showing a piece of resulting dictionary in json format.

The entire dictionary is around 4000 lines long in json format as it shows 17 types of information per hour in a day for 24 hours and 7 days.

If you want to see the entire file for some unknown reason, go here [example/example-result.json](https://github.com/TheElevatedOne/ClearOutsideAPY/blob/main/example/example-result.json).

```json
{
    "gen-info": {
        "last-gen": {
            "date": "19/02/25",
            "time": "20:26:52"
        },
        "forecast": {
            "from-day": "19/02/25",
            "to-day": "25/02/25"
        },
        "timezone": "UTC-5.00"
    },
    "sky-quality": {
        "magnitude": "21.3",
        "bortle_class": "4",
        "brightness": [
            "0.33",
            "mcd/m2"
        ],
        "artif-brightness": [
            "155.5",
            "cd/m2"
        ]
    },
    "forecast": {
        "day-0": {
            "date": {
                "long": "Wednesday",
                "short": "19"
            },
            "sun": {
                "rise": "06:51",
                "set": "17:40",
                "transit": "12:17",
                "civil-dark": [
                    "18:09",
                    "06:22"
                ],
                "nautical-dark": [
                    "18:42",
                    "05:49"
                ],
                "astro-dark": [
                    "19:15",
                    "05:16"
                ]
            },
            "moon": {
                "rise": "01:12",
                "set": "10:07",
                "phase": {
                    "name": "Waning Gibbous",
                    "percentage": "53%"
                }
            },
            "hours": {
                "12": {
                    "conditions": "bad",
                    "total-clouds": "91",
                    "low-clouds": "90",
                    "mid-clouds": "13",
                    "high-clouds": "18",
                    "visibility": "0.0",
                    "fog": "0",
                    "prec-type": "none",
                    "prec-probability": "0",
                    "prec-amount": "0",
                    "wind": {
                        "speed": "17.7",
                        "direction": "north-west"
                    },
                    "frost": "frost",
                    "temperature": {
                        "general": "-9",
                        "feels-like": "-14",
                        "dew-point": "-13"
                    },
                    "rel-humidity": "74",
                    "pressure": "1028",
                    "ozone": "375"
                },
                "13": {"..."},
                "..."
            }
        },
        "day-1": {"..."},
        "..."
    }
}
```
