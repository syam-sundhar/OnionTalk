#!/bin/bash

set -e

echo "[+] Updating system"
sudo apt update -y

echo "[+] Installing dependencies"
sudo apt install -y tor python3 python3-pip netcat-openbsd

echo "[+] Configuring Tor Hidden Service"

HS_DIR="/var/lib/tor/terminal_chat"

sudo mkdir -p $HS_DIR
sudo chown -R debian-tor:debian-tor $HS_DIR
sudo chmod 700 $HS_DIR

TORRC="/etc/tor/torrc"

if ! grep -q "terminal_chat" "$TORRC"; then
sudo bash -c "cat >> $TORRC <<EOF

HiddenServiceDir $HS_DIR/
HiddenServicePort 5555 127.0.0.1:5555
EOF"
fi

echo "[+] Restarting Tor"
sudo systemctl enable tor
sudo systemctl restart tor

sleep 5

echo "[+] Your .onion address:"
sudo cat $HS_DIR/hostname

echo "[✓] Setup complete"
