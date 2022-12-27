import requests
# es como la version de axios para python.


def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    # print(r.text)
    categories = r.json()
    for categorie in categories:
        print(categorie['id'], " = ", categorie['name'])
