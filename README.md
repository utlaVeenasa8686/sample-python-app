
# Haswitha Academy - Sample DevOps App

A simple **Flask-based Python web app** to demonstrate DevOps concepts.

## Features
- 🚀 Homepage with DevOps course info
- 🖼️ Images + text using Bootstrap cards
- 🔧 Built with Flask, ready for Docker/Kubernetes CI/CD demos


# Install python in local laptop
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
# Run compute instance or ec2 instance
```
sudo apt install -y python3 python3-pip
sudo apt install -y python3.13-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=5000
```
# Note: if you want to access through browser then  5000 port need to open in firewall

