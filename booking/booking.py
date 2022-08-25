from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.options import Options

from datetime import datetime as dt
import os
import pandas as pd

path = 'C:/Program Files (x86)/Microsoft/Edge/Application/webdriver-edge/msedgedriver.exe'
web = 'https://e-consulta.sunat.gob.pe/cl-at-ittipcam/tcS01Alias'

class Booking():
    def __init__(self, driver_path=path, teardown=False):
        self.teardown = teardown
        self.driver_edge= driver_path

    def __enter__(self):
        self.service = Service(executable_path=self.driver_edge)

        options = Options()
        options.headless = False # Con True me causa error no solucionado

        self.driver = webdriver.Edge(service=self.service, options=options)
        self.driver.maximize_window()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def land_first_page(self):
        self.driver.implicitly_wait(15)
        self.driver.get(web)

    def month_year(self, month, go_year):

        self.month = month
        self.go_year = go_year

        click_search = self.driver.find_element("xpath", "//div[@id='fecAsistenciaBusqDiv']//span[@class='input-group-addon']")
        click_search.click()

        WebDriverWait(self.driver, 4)

        select_year = self.driver.find_element("xpath", '//th[@title="Seleccione Año"]')
        select_year.click()

        WebDriverWait(self.driver, 4)

        datepickers = self.driver.find_elements("xpath", '//div[@class="datepicker"]/div')

        for datepi in datepickers:

            picker = datepi.get_attribute("class")

            if picker == "datepicker-years":
                pic_year = datepi.find_element("xpath", f"./table/tbody/tr/td/span[text()='{go_year}']")
                pic_year.click()

                WebDriverWait(self.driver, 4)

                pic_month = self.driver.find_element("xpath", f'//*[@id="fecAsistenciaBusqDiv"]/div/ul/li[1]/div/div[2]/table/tbody/tr/td/span[{month}]')
                pic_month.click()
                break
                
            else:
                print("No se encontro el atributo del año")               


    def search(self):

        element = self.driver.find_element("xpath", "//button[@id='btnBuscarAsistencias']")
        element.click()

    def values_money(self):

        days = []
        buys = []
        sells = []

        day_weeks = self.driver.find_elements("xpath", '//div/table/tbody/tr/td')

        WebDriverWait(self.driver, 4)

        for day_week in day_weeks:

            # Obteniendo los dias del mes

            try:
                num_day = day_week.find_element("xpath", './div[1]').text
                WebDriverWait(self.driver, 5)

                day_int = int(num_day)
                days.append(day_int)
                print("Se agrego con exito el día")
            except:
                days.append("")
                print("No se encontro el día")

            # Obteniendo el precio de compra del mes
            try:
                buy = day_week.find_element("xpath", './div[2]').text
                WebDriverWait(self.driver, 5)

                buy_strip = buy.strip("Compra ")
                buy_int = float(buy_strip)
                buys.append(buy_int)
                print("Se agrego con exito el TC de compra")
            except:
                buys.append("")
                print("No se encontro el precio de compra")

            # Obteniendo el precio de venta del mes
            try:
                sell = day_week.find_element("xpath", './div[3]').text
                WebDriverWait(self.driver, 5)

                sell_strip = sell.strip("Venta ")
                sell_float = float(sell_strip)
                sells.append(sell_float)
                print("Se agrego con exito el TC de venta")
            except:
                sells.append("")
                print("No se encontro el precio de venta")

        # Guardando los datos en un dataframe y luego en un excel

        print("Paso la valla mencionada")

        date = dt(self.go_year, self.month, 4)
        date_new = date.strftime("%B-%Y")

        data_sell_buy = pd.DataFrame({
            "Día": days,
            "Compra": buys,
            "Venta": sells
        })

        # Generando la ruta para guardarlo en la carpeta documentos
        rootUser= os.environ["USERPROFILE"]
        rootDic = os.path.join(rootUser, "Documents", "TC_Sunat")
        rootFile = os.path.join(rootDic, f"TC {date_new}.xlsx")
        
        # Crear la carpeta antes de unirlo

        try:
            os.mkdir(rootDic)

        except OSError as err:
            print("La carpeta ya esta creada")

        finally:
            data_sell_buy.to_excel(rootFile, index=False)

        

        print("Se guardo de forma exitosa")

            







        


        