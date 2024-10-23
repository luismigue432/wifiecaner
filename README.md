# Naranja_verder.py

## Descripción
`Naranja_verder.py` es un script de Python diseñado para escanear redes WiFi cercanas y mostrar información detallada sobre cada red disponible. Utiliza la biblioteca `pywifi` para realizar el escaneo y proporciona detalles como el SSID, la intensidad de la señal, la dirección MAC del punto de acceso, el canal utilizado y el fabricante del hardware de red.

## Funcionalidades
- Escaneo de redes WiFi disponibles en el entorno.
- Presentación clara y colorida de los resultados en la terminal.
- Identificación del fabricante de la dirección MAC utilizando un diccionario predefinido.

## Requisitos
- Python 3.x
- Bibliotecas necesarias:
  - `pywifi`
  - `termcolor`
  - `pyfiglet`

Puedes instalar las bibliotecas necesarias utilizando el siguiente comando:

```bash
pip install pywifi termcolor pyfiglet
