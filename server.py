from flask import Flask, render_template, request, jsonify
import hashlib
import json
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
import base64

app = Flask(__name__)

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash, signature=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data  
        self.hash = hash
        self.signature = signature

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

blockchain = [create_genesis_block()]

def decrypt_aes(encrypted_data, key):
    # Convert base64 to bytes for decryption
    encrypted_data_bytes = {
        'ciphertext': base64.b64decode(encrypted_data['ciphertext']),
        'tag': base64.b64decode(encrypted_data['tag']),
        'nonce': base64.b64decode(encrypted_data['nonce'])
    }

    cipher = AES.new(key, AES.MODE_GCM, nonce=encrypted_data_bytes['nonce'])
    decrypted_data = cipher.decrypt_and_verify(encrypted_data_bytes['ciphertext'], encrypted_data_bytes['tag'])
    return decrypted_data.decode('utf-8')

voting_results = {"Red": 0, "Yellow": 0, "Blue": 0, "Green": 0}

@app.route('/receive_vote', methods=['POST'])
def receive_vote():
    encrypted_vote = request.json['vote']
    aes_key_hex = request.json['key']

    # Convert AES key from hex
    aes_key = bytes.fromhex(aes_key_hex)

    previous_block = blockchain[-1]
    index = previous_block.index + 1
    timestamp = int(time.time())
    previous_hash = previous_block.hash

    # Decrypt vote data on the server
    decrypted_vote = decrypt_aes(encrypted_vote, aes_key)

    new_block = Block(index, previous_hash, timestamp, decrypted_vote, calculate_hash(index, previous_hash, timestamp, decrypted_vote))
    blockchain.append(new_block)
    voting_results[decrypted_vote] += 1
    print(f"Received encrypted vote: {encrypted_vote}")
    print(f"Decrypted vote: {decrypted_vote}")

    return jsonify({'message': 'Vote received'}), 200

@app.route('/')
def server():
    return render_template('server.html', blockchain=blockchain, voting_results=voting_results)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
