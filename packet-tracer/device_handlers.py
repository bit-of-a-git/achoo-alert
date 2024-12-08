import json
from gpio import *

def control_ac(action):
    if action == "on":
        digitalWrite(1, HIGH)
        return {"status": "success", "message": "Turning AC ON"}
    elif action == "off":
        digitalWrite(1, LOW)
        return {"status": "success", "message": "Turning AC OFF"}
    else:
        return {"status": "error", "message": "Unknown AC action: " + action}

def control_humidifier(action):
    if action == "on":
        customWrite(0, 1)
        return {"status": "success", "message": "Turning Humidifier ON"}
    elif action == "off":
        customWrite(0, 0)
        return {"status": "success", "message": "Turning Humidifier OFF"}
    else:
        return {"status": "error", "message": "Unknown Humidifier action: " + action}

def handle_command(json_data):
    try:
        command = json.loads(json_data)
        device = command.get("device")
        action = command.get("action")

        if device == "ac":
            return control_ac(action)
        elif device == "humidifier":
            return control_humidifier(action)
        else:
            return {"status": "error", "message": "Unknown device: " + device}
    except json.JSONDecodeError:
        return {"status": "error", "message": "Invalid JSON received"}
    except Exception as e:
        return {"status": "error", "message": "Error handling command: " + str(e)}
