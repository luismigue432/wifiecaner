
import pywifi
import time
import math
from termcolor import colored
from pyfiglet import figlet_format

# Diccionario de fabricantes de direcciones MAC (ejemplo reducido)
mac_vendors = {
    '00:1A:2B': 'Vendor A',
    '00:1A:3C': 'Vendor B',
    '68:9F:F0': 'Vendor C',
    'E2:16:DA': 'Vendor D',
    'B4:0F:3B': 'Vendor E',
}

# Obtener el fabricante de la dirección MAC
def get_manufacturer(bssid):
    mac_prefix = ':'.join(bssid.split(':')[:3]).upper()  # Convertir a mayúsculas
    return mac_vendors.get(mac_prefix, 'Desconocido')

# Calcular la distancia en metros a partir de la señal (dBm)
def calculate_distance(signal, frequency):
    # Convertir la frecuencia a MHz
    frequency_mhz = frequency / 1000.0  # La frecuencia se proporciona en kHz
    # Aplicar la fórmula
    distance = 10 ** ((27.55 - (20 * math.log10(frequency_mhz)) + abs(signal)) / 20)
    return distance

# Inicializa el escáner WiFi
def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Selecciona la interfaz de red (WiFi)

    iface.scan()  # Inicia el escaneo de redes
    time.sleep(2)  # Espera unos segundos para obtener los resultados

    results = iface.scan_results()
    print(colored("Resultados del Escaneo de Redes WiFi:", 'green'))
    print("=" * 50)
    
    for network in results:
        ssid = network.ssid  # Nombre de la red (SSID)
        signal = network.signal  # Intensidad de la señal
        bssid = network.bssid  # Dirección MAC del punto de acceso
        frequency = network.freq  # Canal en el que opera la red
        
        # Obtener el fabricante
        manufacturer = get_manufacturer(bssid)
        
        # Calcular la distancia
        distance = calculate_distance(signal, frequency)

        print(f"SSID: {colored(ssid, 'cyan')}, Señal: {colored(signal, 'yellow')} dBm, "
              f"BSSID: {colored(bssid, 'magenta')}, Canal: {colored(frequency, 'blue')} MHz, "
              f"Fabricante: {colored(manufacturer, 'white')}, Distancia: {colored(round(distance, 2), 'red')} metros")
        print("-" * 50)

if __name__ == "__main__":
    print(colored(figlet_format("WiFi Scanner"), 'cyan'))
    print(colored("Hecho por: Luis Miguel de los Santos", 'yellow'))
    print("=" * 50)
    scan_wifi()
