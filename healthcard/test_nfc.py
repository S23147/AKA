from smartcard.System import readers
from smartcard.util import toHexString

def lire_carte_nfc():
    r = readers()

    if not r:
        print("⚠ Aucun lecteur NFC détecté.")
        return

    try:
        reader = r[0].createConnection()
        reader.connect()

        GET_UID = [0xFF, 0xCA, 0x00, 0x00, 0x00]  # Commande pour lire l'UID de la carte
        data, sw1, sw2 = reader.transmit(GET_UID)

        if sw1 == 0x90 and sw2 == 0x00:
            print("✁EUID de la carte NFC :", toHexString(data))
        else:
            print(f"⚠ Erreur de lecture : {sw1:02X} {sw2:02X}")
    except Exception as e:
        print(f"❁EErreur lors de la lecture : {e}")

if __name__ == "__main__":
    lire_carte_nfc()
