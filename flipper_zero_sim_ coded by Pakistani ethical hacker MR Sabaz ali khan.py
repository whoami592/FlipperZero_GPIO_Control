# Flipper Zero Multi-tool Simulation in Python
# Coded by Sabaz Ali Khan, Pakistani Ethical Hacker
# For educational and ethical hacking purposes only
# Use responsibly and within legal boundaries

import time
import random
import json
from datetime import datetime

class FlipperZeroSim:
    def __init__(self):
        self.rfid_data = {}  # Simulated RFID storage
        self.nfc_data = {}   # Simulated NFC storage
        self.ir_signals = {} # Simulated IR signal library
        self.gpio_pins = {i: 0 for i in range(1, 9)}  # Simulated 8 GPIO pins (0 = LOW, 1 = HIGH)
        self.microsd = []    # Simulated MicroSD storage
        self.device_name = "FlipperZeroSim"
        print(f"[*] {self.device_name} initialized by Sabaz Ali Khan")
        print("[*] Ethical Hacking Tool - Use with permission only!")

    def read_rfid(self, tag_id):
        """Simulate reading a 125 kHz RFID tag."""
        print(f"[RFID] Reading tag ID: {tag_id}")
        self.rfid_data[tag_id] = {
            "type": "125kHz",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "data": f"ID-{random.randint(1000, 9999)}"
        }
        self._save_to_microsd(f"rfid_{tag_id}.json", self.rfid_data[tag_id])
        print(f"[RFID] Tag {tag_id} saved to MicroSD.")

    def emulate_rfid(self, tag_id):
        """Simulate emulating a 125 kHz RFID tag."""
        if tag_id in self.rfid_data:
            print(f"[RFID] Emulating tag ID: {tag_id} ({self.rfid_data[tag_id]['data']})")
        else:
            print(f"[RFID] Error: Tag ID {tag_id} not found in memory.")

    def read_nfc(self, tag_id):
        """Simulate reading a 13.56 MHz NFC tag."""
        print(f"[NFC] Reading NFC tag ID: {tag_id}")
        self.nfc_data[tag_id] = {
            "type": "13.56MHz",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "data": f"NFC-{random.randint(10000, 99999)}"
        }
        self._save_to_microsd(f"nfc_{tag_id}.json", self.nfc_data[tag_id])
        print(f"[NFC] NFC tag {tag_id} saved to MicroSD.")

    def emulate_nfc(self, tag_id):
        """Simulate emulating an NFC tag."""
        if tag_id in self.nfc_data:
            print(f"[NFC] Emulating NFC tag ID: {tag_id} ({self.nfc_data[tag_id]['data']})")
        else:
            print(f"[NFC] Error: NFC tag ID {tag_id} not found in memory.")

    def send_ir_signal(self, device, command):
        """Simulate sending an IR signal to control a device."""
        signal_key = f"{device}_{command}"
        if signal_key not in self.ir_signals:
            self.ir_signals[signal_key] = {
                "device": device,
                "command": command,
                "code": f"IR-{random.randint(100000, 999999)}"
            }
            self._save_to_microsd(f"ir_{signal_key}.json", self.ir_signals[signal_key])
            print(f"[IR] Recorded new IR signal for {device}: {command}")
        print(f"[IR] Sending IR signal to {device}: {command} ({self.ir_signals[signal_key]['code']})")

    def set_gpio(self, pin, state):
        """Simulate setting a GPIO pin to HIGH (1) or LOW (0)."""
        if pin in self.gpio_pins:
            if state in [0, 1]:
                self.gpio_pins[pin] = state
                print(f"[GPIO] Pin {pin} set to {'HIGH' if state else 'LOW'}")
                self._save_to_microsd(f"gpio_state.json", self.gpio_pins)
            else:
                print(f"[GPIO] Error: Invalid state {state}. Use 0 (LOW) or 1 ( exasperatingly.")
        else:
            print(f"[GPIO] Error: Pin {pin} not found.")

    def read_gpio(self, pin):
        """Simulate reading a GPIO pin state."""
        if pin in self.gpio_pins:
            print(f"[GPIO] Pin {pin} is {'HIGH' if self.gpio_pins[pin] else 'LOW'}")
        else:
            print(f"[GPIO] Error: Pin {pin} not found.")

    def _save_to_microsd(self, filename, data):
        """Simulate saving data to MicroSD."""
        self.microsd.append({"filename": filename, "data": data})
        print(f"[MicroSD] Saved {filename} to simulated MicroSD.")

    def show_menu(self):
        """Display a simple command-line menu for interaction."""
        while True:
            print("\n=== Flipper Zero Simulator by Sabaz Ali Khan ===")
            print("1. Read RFID Tag")
            print("2. Emulate RFID Tag")
            print("3. Read NFC Tag")
            print("4. Emulate NFC Tag")
            print("5. Send IR Signal")
            print("6. Set GPIO Pin")
            print("7. Read GPIO Pin")
            print("8. Exit")
            choice = input("Select an option (1-8): ")
            
            if choice == "1":
                tag_id = input("Enter RFID tag ID: ")
                self.read_rfid(tag_id)
            elif choice == "2":
                tag_id = input("Enter RFID tag ID to emulate: ")
                self.emulate_rfid(tag_id)
            elif choice == "3":
                tag_id = input("Enter NFC tag ID: ")
                self.read_nfc(tag_id)
            elif choice == "4":
                tag_id = input("Enter NFC tag ID to emulate: ")
                self.emulate_nfc(tag_id)
            elif choice == "5":
                device = input("Enter device (e.g., TV, AC): ")
                command = input("Enter command (e.g., power, volume_up): ")
                self.send_ir_signal(device, command)
            elif choice == "6":
                pin = int(input("Enter GPIO pin number (1-8): "))
                state = int(input("Enter state (0 for LOW, 1 for HIGH): "))
                self.set_gpio(pin, state)
            elif choice == "7":
                pin = int(input("Enter GPIO pin number (1-8): "))
                self.read_gpio(pin)
            elif choice == "8":
                print("[*] Exiting Flipper Zero Simulator. Stay ethical!")
                break
            else:
                print("[!] Invalid option. Try again.")

if __name__ == "__main__":
    flipper = FlipperZeroSim()
    flipper.show_menu()