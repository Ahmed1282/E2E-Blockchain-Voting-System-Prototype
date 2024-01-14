from flask import Flask, render_template, request, redirect, url_for
import requests
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import json
import base64

app = Flask(__name__)

def generate_aes_key():
    return get_random_bytes(16)  # 128-bit key for AES

def encrypt_aes(data, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return {'ciphertext': ciphertext, 'tag': tag, 'nonce': cipher.nonce}

@app.route('/')
def index():
    return render_template('client.html')
@app.route('/submit_vote', methods=['POST'])
def submit_vote():
    vote_data = request.form.get('vote')

    # Generate AES key
    aes_key = generate_aes_key()

    # Encrypt vote data with AES
    encrypted_vote = encrypt_aes(vote_data, aes_key)

    # Convert bytes to base64 for JSON serialization
    encrypted_vote_base64 = {
        'ciphertext': base64.b64encode(encrypted_vote['ciphertext']).decode('utf-8'),
        'tag': base64.b64encode(encrypted_vote['tag']).decode('utf-8'),
        'nonce': base64.b64encode(encrypted_vote['nonce']).decode('utf-8')
    }

    # Send encrypted vote and AES key (hex representation) to the server
    requests.post('http://localhost:5001/receive_vote', json={'vote': encrypted_vote_base64, 'key': aes_key.hex()})
    print(f"Sent encrypted vote: {encrypted_vote_base64}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
