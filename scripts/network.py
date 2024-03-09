import socket

def connect(record):
    try:
        socket.create_connection((record, 25), timeout=10)
        print("Successfully connected to the SMTP server.")
    except Exception as e:
        print(f"Error connecting to SMTP server: {e}")

connect('hotmail-com.olc.protection.outlook.com')