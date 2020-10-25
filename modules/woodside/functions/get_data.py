import requests

def brent_crude():
    try:
        resp = requests.get('https://fred.stlouisfed.org/graph/fredgraph.csv?id=WCOILBRENTEU&fq=Weekly')
        resp.raise_for_status()
        csv_file = open('./data/brent.csv', 'wb')
        csv_file.write(resp.content)
        csv_file.close()
        return 0
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)