# Introducción
Muchas de las empresas auditoras y bancarias actualmente trabajaban con datos financieros que no son facilmente accesibles. Una de ellas es el tipo de cambio del dolar frente al sol. Por lo que este proyecto **TC Sunat** se realiazó, con la intención de poder automatizar la adquisión de los precios de compra y venta del tipo de cambio mensual del mes anterior.

### Características

- El mes obtenido es el mes anterior a la fecha actual en la que te encuentras
- Se obtiene todos los dias del mes
- Los valores vacíos son aquellos en las que no hubo valor asignado al tipo de cambio
- Solo es utilizable en navegador Edge
- La obtención de los datos se da con el navegador expandido
- La devolución de los datos se da en un archivo Excel con extensión *.xlsx*
- La última versión es el 0.1.1

# TC Sunat

![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)

![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)


### Archivos necesarias

- En la carpeta raiz del proyecto  debemos crear el archivo **.env**, este archivo contendrá:
	- La variable **WEB=** , que contendrá la url(string) de la web a la que realizaremos WebScraping, por defecto [TC Página](https://e-consulta.sunat.gob.pe/cl-at-ittipcam/tcS01Alias "TC Página")
	- La variable **PATH_EDGE =** , que contendrá la dirección(path) del webdriver del navegador Edge. Lista de webdriver de Edge [aquí](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ "aquí")
	- La variable **PATH_CHROME =** , que contendrá la dirección(path) del webdriver del navegador de Chrome. Lista de webdriver de Chrome [aquí](https://chromedriver.chromium.org/ "aquí")

### Requerimientos
|  Librería | Versión  |
| :------------ | :------------ |
| numpy   | 1.23.2  |
| pandas   |  1.4.3 |
| pip  | 22.0.4  |
| selenium  | 4.3.0  |
| urllib3  | 1.26.11  |
