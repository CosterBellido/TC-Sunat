from booking import interface

import time
from booking.booking import Booking
from datetime import datetime as dt

# Creando la interfas de usuario

# Creando la fecha de adquisición

month_get, year_get = interface.getDate()

# A las funciones de conexión
with Booking(teardown=True) as bot:
    bot.land_first_page()

    time.sleep(2)

    bot.month_year(month_get, year_get)

    time.sleep(1)

    bot.search()

    time.sleep(4)

    bot.values_money()









