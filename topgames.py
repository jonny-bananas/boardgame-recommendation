#Citation for xml data parsing:
#Code based on/modified from: xml.etree.ElementTree - The ElementTree XML API
#       from python.org
#URL: https://docs.python.org/3/library/xml.etree.elementtree.html
#Date: 2/23/2024

#Citation for Python sockets:
#Code based on/modified from: Socket Programming HOWTO
#       from python.org
#URL: https://docs.python.org/3/howto/sockets.html
#Date: 2/24/2024


import socket
import requests
import xml.etree.ElementTree as ET

#set up listener socket to wait for client to request data
server_port = 32000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', server_port))
server_socket.listen(1)


while True:
    print("Waiting for client to connect...")
    connected, address = server_socket.accept()
    
    while True:
        data = connected.recv(1024).decode()

        if data == "get_top_50":
            bgg_api = "https://www.boardgamegeek.com/xmlapi2/hot?boardgame"
            response = requests.get(bgg_api)
            xml_str = response.text
            root = ET.fromstring(xml_str)

            hottness = ''
            for item in root.findall("item"):
                rank = item.get("rank")
                name = item.find("name").get("value")
                hottness = hottness + f"{rank}. {name}\n"

            connected.send(hottness.encode())
            print("Data has been sent")
        elif data == "quit":
            print("Client requested to quit")
            break
        else:
            print("Invalid request from the client")

    connected.close()
    print("Connection closed")

