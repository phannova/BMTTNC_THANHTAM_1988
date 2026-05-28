from flask import Flask, render_template, request, session, redirect
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)
# Tạo một "chìa khóa" bí mật để sử dụng tính năng ghi nhớ (session)
app.secret_key = 'hutech_security_lab'

# Khởi tạo các đối tượng mã hóa
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
playfair_cipher = PlayFairCipher()
railfence_cipher = RailFenceCipher()
transposition_cipher = TranspositionCipher()

# ================= RENDER TEMPLATES =================
@app.route("/")
def home():
    return render_template('index.html')


# ================= CAESAR ROUTES =================
@app.route("/caesar")
def caesar_page():
    return render_template('caesar.html',
        enc_result=session.get('c_enc_result'), enc_text=session.get('c_enc_text'), enc_key=session.get('c_enc_key'),
        dec_result=session.get('c_dec_result'), dec_text=session.get('c_dec_text'), dec_key=session.get('c_dec_key')
    )

@app.route("/caesar_encrypt", methods=['POST'])
def caesar_encrypt_web():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    session['c_enc_text'] = text
    session['c_enc_key'] = key
    session['c_enc_result'] = caesar_cipher.encrypt_text(text, key)
    return redirect('/caesar')

@app.route("/caesar_decrypt", methods=['POST'])
def caesar_decrypt_web():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    session['c_dec_text'] = text
    session['c_dec_key'] = key
    session['c_dec_result'] = caesar_cipher.decrypt_text(text, key)
    return redirect('/caesar')


# ================= VIGENERE ROUTES =================
@app.route("/vigenere")
def vigenere_page():
    return render_template('vigenere.html',
        enc_result=session.get('v_enc_result'), enc_text=session.get('v_enc_text'), enc_key=session.get('v_enc_key'),
        dec_result=session.get('v_dec_result'), dec_text=session.get('v_dec_text'), dec_key=session.get('v_dec_key')
    )

@app.route("/vigenere_encrypt", methods=['POST'])
def vigenere_encrypt_web():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    session['v_enc_text'] = text
    session['v_enc_key'] = key
    session['v_enc_result'] = vigenere_cipher.vigenere_encrypt(text, key)
    return redirect('/vigenere')

@app.route("/vigenere_decrypt", methods=['POST'])
def vigenere_decrypt_web():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    session['v_dec_text'] = text
    session['v_dec_key'] = key
    session['v_dec_result'] = vigenere_cipher.vigenere_decrypt(text, key)
    return redirect('/vigenere')


# ================= PLAYFAIR ROUTES =================
@app.route("/playfair")
def playfair_page():
    return render_template('playfair.html',
        matrix_result=session.get('p_matrix_result'), matrix_key=session.get('p_matrix_key'),
        enc_result=session.get('p_enc_result'), enc_text=session.get('p_enc_text'), enc_key=session.get('p_enc_key'),
        dec_result=session.get('p_dec_result'), dec_text=session.get('p_dec_text'), dec_key=session.get('p_dec_key')
    )

@app.route("/playfair_creatematrix", methods=['POST'])
def playfair_creatematrix_web():
    key = request.form['inputKeyMatrix']
    matrix = playfair_cipher.create_playfair_matrix(key)
    session['p_matrix_key'] = key
    session['p_matrix_result'] = "<br/>".join([str(row) for row in matrix])
    return redirect('/playfair')

@app.route("/playfair_encrypt", methods=['POST'])
def playfair_encrypt_web():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    matrix = playfair_cipher.create_playfair_matrix(key)
    session['p_enc_text'] = text
    session['p_enc_key'] = key
    session['p_enc_result'] = playfair_cipher.playfair_encrypt(text, matrix)
    return redirect('/playfair')

@app.route("/playfair_decrypt", methods=['POST'])
def playfair_decrypt_web():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    matrix = playfair_cipher.create_playfair_matrix(key)
    session['p_dec_text'] = text
    session['p_dec_key'] = key
    session['p_dec_result'] = playfair_cipher.playfair_decrypt(text, matrix)
    return redirect('/playfair')


# ================= RAIL FENCE ROUTES =================
@app.route("/railfence")
def railfence_page():
    return render_template('railfence.html',
        enc_result=session.get('r_enc_result'), enc_text=session.get('r_enc_text'), enc_key=session.get('r_enc_key'),
        dec_result=session.get('r_dec_result'), dec_text=session.get('r_dec_text'), dec_key=session.get('r_dec_key')
    )

@app.route("/railfence_encrypt", methods=['POST'])
def railfence_encrypt_web():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    session['r_enc_text'] = text
    session['r_enc_key'] = key
    session['r_enc_result'] = railfence_cipher.rail_fence_encrypt(text, key)
    return redirect('/railfence')

@app.route("/railfence_decrypt", methods=['POST'])
def railfence_decrypt_web():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    session['r_dec_text'] = text
    session['r_dec_key'] = key
    session['r_dec_result'] = railfence_cipher.rail_fence_decrypt(text, key)
    return redirect('/railfence')


# ================= TRANSPOSITION ROUTES =================
@app.route("/transposition")
def transposition_page():
    return render_template('transposition.html',
        enc_result=session.get('t_enc_result'), enc_text=session.get('t_enc_text'), enc_key=session.get('t_enc_key'),
        dec_result=session.get('t_dec_result'), dec_text=session.get('t_dec_text'), dec_key=session.get('t_dec_key')
    )

@app.route("/transposition_encrypt", methods=['POST'])
def transposition_encrypt_web():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    session['t_enc_text'] = text
    session['t_enc_key'] = key
    session['t_enc_result'] = transposition_cipher.encrypt(text, key)
    return redirect('/transposition')

@app.route("/transposition_decrypt", methods=['POST'])
def transposition_decrypt_web():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    session['t_dec_text'] = text
    session['t_dec_key'] = key
    session['t_dec_result'] = transposition_cipher.decrypt(text, key)
    return redirect('/transposition')

# ================= MAIN FUNCTION =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)