import os
import re
from termcolor import colored
from pyfiglet import figlet_format
import math

# Expresión regular para buscar redes WiFi en la salida de iwlist
wifi_regex = re.compile(r'Cell \d+ - Address: ([\dA-F:]+)\n.*?\n.*?ESSID:"(.*?)".*?Signal level=(-\d+) dBm', re.S)

# Calcular la distancia en metros a partir de la señal (dBm)
def calculate_distance(signal):
    frequency = 2400  # Suposición de 2.4 GHz
    distance = 10 ** ((27.55 - (20 * math.log10(frequency)) + abs(int(signal))) / 20)
    return distance

# Escanea redes WiFi usando iwlist
def scan_wifi():
    # Ejecutar el comando iwlist para escanear redes WiFi
    iwlist_output = os.popen('iwlist wlan0 scan').read()

    # Buscar todas las redes en la salida de iwlist
    networks = wifi_regex.findall(iwlist_output)

    # Abrir el archivo para escribir los resultados
    with open("resultados_wifi_termux.txt", "w") as archivo:
        archivo.write("Resultados del Escaneo de Redes WiFi:\n")
        archivo.write("=" * 50 + "\n")

        for bssid, ssid, signal in networks:
            distance = calculate_distance(signal)

            # Escribir los datos en el archivo
            archivo.write(f"Nombre: {ssid}\n")
            archivo.write(f"Señal: {signal} dBm\n")
            archivo.write(f"BSSID: {bssid}\n")
            archivo.write(f"Distancia: {round(distance, 2)} metros\n")
            archivo.write("-" * 50 + "\n")
            
            # Mostrar los resultados en pantalla
            print(f"SSID: {colored(ssid, 'cyan')}, Señal: {colored(signal, 'yellow')} dBm, "
                  f"BSSID: {colored(bssid, 'magenta')}, "
                  f"Distancia: {colored(round(distance, 2), 'red')} metros")
            print("-" * 50)

if __name__ == "__main__":
    print(colored(figlet_format("WiFi Scanner"), 'cyan'))
    print(colored("Hecho por: Luis Miguel de los Santos", 'yellow'))
    print("=" * 50)
    scan_wifi()

