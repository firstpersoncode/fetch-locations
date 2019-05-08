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
---
#### Get the data with specific location (provinsi, kabupaten, kecamatan, kelurahan):
```
$ curl http://localhost:6500/v1/locations/kecamatan?page=2&limit=15
```
---
#### Response:
```json
{
    "data": [
        {
            "lid": "1102030",
            "name": "SIMPANG KANAN"
        },
        {
            "lid": "1102031",
            "name": "GUNUNG MERIAH"
        },
        {
            "lid": "1102032",
            "name": "DANAU PARIS"
        },
        {
            "lid": "1102033",
            "name": "SURO"
        },
        {
            "lid": "1102042",
            "name": "SINGKOHOR"
        },
        {
            "lid": "1102043",
            "name": "kota BAHARU"
        },
        {
            "lid": "1103010",
            "name": "TRUMON"
        },
        {
            "lid": "1103011",
            "name": "TRUMON TIMUR"
        },
        {
            "lid": "1103012",
            "name": "TRUMON TENGAH"
        },
        {
            "lid": "1103020",
            "name": "BAKONGAN"
        },
        {
            "lid": "1103021",
            "name": "BAKONGAN TIMUR"
        },
        {
            "lid": "1103022",
            "name": "kota BAHAGIA"
        },
        {
            "lid": "1103030",
            "name": "KLUET SELATAN"
        },
        {
            "lid": "1103031",
            "name": "KLUET TIMUR"
        },
        {
            "lid": "1103040",
            "name": "KLUET UTARA"
        }
    ]
}
```
---
> source data:
- [mining-locations](https://github.com/firstpersoncode/mining-locations)
- [docs.rajaapi.com](https://docs.rajaapi.com/)
