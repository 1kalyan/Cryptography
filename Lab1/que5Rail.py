def encrypt(input_text, depth):
    if depth == 1:
        return input_text

    rail = [['' for _ in range(len(input_text))] for _ in range(depth)]

    direction_down = False
    row, col = 0, 0

    for char in input_text:
        rail[row][col] = char
        col += 1

        if row == 0 or row == depth - 1:
            direction_down = not direction_down

        if direction_down:
            row += 1
        else:
            row -= 1

    # Read the characters from the rail matrix row by row
    encrypted_text = []
    for i in range(depth):
        for j in range(len(input_text)):
            if rail[i][j] != '':
                encrypted_text.append(rail[i][j])

    return ''.join(encrypted_text)

def decrypt(encrypted_text, depth):
    if depth == 1:
        return encrypted_text

    rail = [['' for _ in range(len(encrypted_text))] for _ in range(depth)]

    direction_down = None
    row, col = 0, 0

    for i in range(len(encrypted_text)):
        if row == 0:
            direction_down = True
        if row == depth - 1:
            direction_down = False

        # Mark the positions with '*'
        rail[row][col] = '*'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(depth):
        for j in range(len(encrypted_text)):
            if rail[i][j] == '*' and index < len(encrypted_text):
                rail[i][j] = encrypted_text[index]
                index += 1

    decrypted_text = []
    row, col = 0, 0
    for i in range(len(encrypted_text)):
        if row == 0:
            direction_down = True
        if row == depth - 1:
            direction_down = False

        if rail[row][col] != '':
            decrypted_text.append(rail[row][col])
            col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    return ''.join(decrypted_text)

def main():
    input_text = input("Enter the text: ").replace(" ", "")  # Remove spaces from the input text
    depth = int(input("Enter the depth: "))
    choice = input("Type 'encode' to encrypt or 'decode' to decrypt: ").strip().lower()

    if choice == 'encode':
        encrypted_text = encrypt(input_text, depth)
        print(f"Encrypted text: {encrypted_text}")
    elif choice == 'decode':
        decrypted_text = decrypt(input_text, depth)
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Error! Invalid choice. Please type 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
