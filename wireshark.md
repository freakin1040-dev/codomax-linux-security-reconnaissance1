# Wireshark — Local Packet Analysis

**Purpose:** Wireshark captures and analyses network packets and protocol behaviour.

## Install
Use the official installer: https://www.wireshark.org/download.html  
During Windows installation, Npcap may be offered; follow the official installer guidance. You can capture on the Windows loopback adapter (Npcap Loopback Adapter) or a suitable WSL interface depending on your setup.

## Safe capture exercise
1. Start the local app with `bash scripts/start_lab.sh`.
2. Open Wireshark and select the loopback interface appropriate to your browser/app traffic.
3. Start a capture.
4. Visit `http://127.0.0.1:8000/` and `http://127.0.0.1:8000/hello`.
5. Stop capture.
6. Try display filter `tcp.port == 8000` (if the selected capture interface exposes that traffic).
7. Select a packet and inspect the packet details pane.
8. Save a `.pcapng` only if it contains no sensitive traffic.

If localhost traffic is not visible on the selected interface, consult the Wireshark/Npcap documentation and select the correct loopback interface. Do not capture other people's traffic.

Evidence to record:
- Interface name
- Capture filter (if any)
- Display filter
- Protocols observed
- A screenshot showing packet details with sensitive data excluded
