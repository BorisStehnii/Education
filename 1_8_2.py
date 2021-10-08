def country_dict(country, capital, dict_={}):
    dict_.update({country: capital})
    print(dict_)
    return dict_


country_dict("Ukrain", "Kiyv")
country_dict("France", "Paris")
country_dict("Moldova", "Kishinev")
