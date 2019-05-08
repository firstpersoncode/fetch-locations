## Fetch all locations and their ids matched with Indonesian's identity card

#### Clone:
```
$ git clone git@github.com:firstpersoncode/fetch-locations.git
```
---
#### Run app:
```
$ python3 main.py

# * Serving Flask app "src" (lazy loading)
# * Debug mode: on
# * Running on http://127.0.0.1:6500/ (Press CTRL+C to quit)
```
---
#### Get the data with params page and limit:
```
$ curl http://localhost:6500/v1/locations/?page=1&limit=15
```
---
#### Response:
```json
{
    "data": [
        {
            "lid": "11",
            "name": "ACEH"
        },
        {
            "lid": "12",
            "name": "SUMATERA UTARA"
        },
        {
            "lid": "13",
            "name": "SUMATERA BARAT"
        },
        {
            "lid": "14",
            "name": "RIAU"
        },
        {
            "lid": "15",
            "name": "JAMBI"
        },
        {
            "lid": "16",
            "name": "SUMATERA SELATAN"
        },
        {
            "lid": "17",
            "name": "BENGKULU"
        },
        {
            "lid": "18",
            "name": "LAMPUNG"
        },
        {
            "lid": "19",
            "name": "KEPULAUAN BANGKA BELITUNG"
        },
        {
            "lid": "21",
            "name": "KEPULAUAN RIAU"
        },
        {
            "lid": "31",
            "name": "DKI JAKARTA"
        },
        {
            "lid": "32",
            "name": "JAWA BARAT"
        },
        {
            "lid": "33",
            "name": "JAWA TENGAH"
        },
        {
            "lid": "34",
            "name": "DI YOGYAKARTA"
        },
        {
            "lid": "35",
            "name": "JAWA TIMUR"
        }
    ]
}
```

> source data:
- [mining-locations](https://github.com/firstpersoncode/mining-locations)
- [rajaapi.com](https://rajaapi.com/)
