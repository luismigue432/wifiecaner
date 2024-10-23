import pywifi
import time
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
        channel = network.freq  # Canal en el que opera la red
        
        # Obtener el fabricante
        manufacturer = get_manufacturer(bssid)

        print(f"SSID: {colored(ssid, 'cyan')}, Señal: {colored(signal, 'yellow')} dBm, "
              f"BSSID: {colored(bssid, 'magenta')}, Canal: {colored(channel, 'blue')}, "
              f"Fabricante: {colored(manufacturer, 'white')}")
        print("-" * 50)

if __name__ == "__main__":
    print(colored(figlet_format("WiFi Scanner"), 'cyan'))
    print(colored("Hecho por: Luis Miguel de los Santos", 'yellow'))
    print("=" * 50)
    scan_wifi()
