from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher

app = Flask(__name__)

# Khởi tạo các đối tượng mã hóa
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
playfair_cipher = PlayFairCipher()
railfence_cipher = RailFenceCipher()

# ================= RENDER TEMPLATES (CHUYỂN TRANG) =================
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar_page():
    return render_template('caesar.html')

@app.route("/vigenere")
def vigenere_page():
    return render_template('vigenere.html')

@app.route("/playfair")
def playfair_page():
    return render_template('playfair.html')

@app.route("/railfence")
def railfence_page():
    return render_template('railfence.html')


# ================= CAESAR ROUTES =================
@app.route("/caesar_encrypt", methods=['POST'])
def caesar_encrypt_web():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain']) # Ép kiểu số nguyên
    encrypted_text = caesar_cipher.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/caesar_decrypt", methods=['POST'])
def caesar_decrypt_web():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# ================= VIGENERE ROUTES =================
@app.route("/vigenere_encrypt", methods=['POST'])
def vigenere_encrypt_web():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain'] # Vigenere key là chữ (string)
    encrypted_text = vigenere_cipher.vigenere_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere_decrypt", methods=['POST'])
def vigenere_decrypt_web():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    decrypted_text = vigenere_cipher.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# ================= PLAYFAIR ROUTES =================
@app.route("/playfair_encrypt", methods=['POST'])
def playfair_encrypt_web():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    # Playfair cần tạo ma trận trước khi mã hóa
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/playfair_decrypt", methods=['POST'])
def playfair_decrypt_web():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# ================= RAIL FENCE ROUTES =================
@app.route("/playfair_creatematrix", methods=['POST'])
def playfair_creatematrix_web():
    key = request.form['inputKeyMatrix']
    matrix = playfair_cipher.create_playfair_matrix(key)
    
    # Định dạng ma trận để in ra web cho đẹp
    matrix_display = "<br/>".join([str(row) for row in matrix])
    
    return f"Key: {key}<br/><br/><b>Playfair Matrix:</b><br/>{matrix_display}"
@app.route("/railfence_encrypt", methods=['POST'])
def railfence_encrypt_web():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain']) # Rail Fence key là số (int)
    encrypted_text = railfence_cipher.rail_fence_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence_decrypt", methods=['POST'])
def railfence_decrypt_web():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# ================= MAIN FUNCTION =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)