def ordenar_per_estrelles(llista_hotels):
    ll_hotels=llista_hotels.copy()
    ll_hotels.sort(key=lambda x: x[9])
    return ll_hotels