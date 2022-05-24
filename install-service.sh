#!/bin/bash
sudo cp octopi-button.service /etc/systemd/system/octopi-button.service
sudo chown root:root /etc/systemd/system/octopi-button.service
sudo chmod 644 /etc/systemd/system/octopi-button.service

sudo systemctl daemon-reload
sudo systemctl start octopi-button.service
sudo systemctl enable octopi-button.service
