from flask import Flask, request, send_from_directory
import requests
import pyaes

def encrypt():
  pass

def decrypt():
  pass

server = Flask(__name__)

load = lambda file: open(file).read()

def ip(req):
  print("[IP] IP Address: " + req.remote_addr)

def log(text, level=""):
  if level == "":
    print(f"[INFO] {str(text)}")
  else:
    print(f"[{level.upper()}] {str(text)}")
 
@app.route('/get', methods=["POST"])
def form():
  ip(request)
  log("REQUEST", request.form)
  text = requests.get(request.url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}).text
  
