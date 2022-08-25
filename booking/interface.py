from datetime import datetime as dt

def getDate():
    date = dt.now()
    year = date.year
    month = date.month

    search_year = None
    search_month = None


    if month == 1:
        search_year = year - 1
        search_month = 12

    else:
        search_year = year
        search_month = month - 1

    return search_month, search_year