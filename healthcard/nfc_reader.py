import time
from smartcard.System import readers
from smartcard.util import toHexString
from smartcard.Exceptions import NoCardException

def read_nfc():
    """Lit une carte NFC et retourne son UID."""
    try:
        r = readers()
        if not r:
            return {"status": "error", "message": "Aucun lecteur détecté."}

        reader = r[0].createConnection()
        reader.connect()

        GET_UID = [0xFF, 0xCA, 0x00, 0x00, 0x00]
        data, sw1, sw2 = reader.transmit(GET_UID)

        if sw1 == 0x90 and sw2 == 0x00:
            return {"status": "success", "uid": toHexString(data)}
        return {"status": "error", "message": f"Erreur de lecture : {sw1:02X} {sw2:02X}"}

    except NoCardException:
        return {"status": "error", "message": "Aucune carte détectée."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
