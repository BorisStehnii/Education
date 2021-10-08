def make_country(country, capital, dict_={}):
    dict_.update({country: capital})
    print(dict_)
    return dict_


make_country("Ukrain", "Kiyv")
make_country("France", "Paris")
make_country("Moldova", "Kishinev")
