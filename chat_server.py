import paho.mqtt.client as mqtt

broker = "mosquitto"
port = 1883
topic = "chatroom"

def on_message(client, userdata, message):
    print(f"\nRecebido: {message.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message
client.connect(broker, port, 60)

client.subscribe(topic)

print("Servidor conectado ao broker. Digite 'sair' para parar.")
client.loop_start()
try:
    while True:
        pass
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
