class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I") # Chuyển "J" thành "I" trong khóa
        key = key.upper()
        
        # ĐÃ SỬA LỖI: Lọc bỏ các ký tự bị trùng lặp trong từ khóa (ví dụ: chữ H thứ 2 trong HUTECH)
        matrix = []
        for char in key:
            if char not in matrix:
                matrix.append(char)
                
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        
        # Thêm các chữ cái còn lại trong bảng chữ cái vào ma trận
        for letter in alphabet:
            if letter not in matrix:
                matrix.append(letter)
                if len(matrix) == 25:
                    break

        # Cắt thành ma trận 5x5
        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text, matrix):
        # Chuyển "J" thành "I" trong văn bản đầu vào
        plain_text = plain_text.replace("J", "I")
        plain_text = plain_text.upper()
        encrypted_text = ""

        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i+2]
            if len(pair) == 1:  # Xử lý nếu số lượng ký tự lẻ
                pair += "X"
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
                
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        # Xóa chữ 'X' ở cuối cùng nếu nó được tự động thêm vào lúc mã hóa vì lẻ ký tự
        if decrypted_text.endswith("X"):
            decrypted_text = decrypted_text[:-1]

        return decrypted_text