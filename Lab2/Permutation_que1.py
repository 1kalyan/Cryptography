# Initial Permutation Table
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Final Permutation Table
FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

def permute(block, table):
    """
    Permute the input block using the specified table.
    """
    return ''.join([block[table[i] - 1] for i in range(len(table))])

def hex_to_bin(hex_string):
    """
    Convert a hex string to a binary string.
    """
    return bin(int(hex_string, 16))[2:].zfill(64)

def bin_to_hex(bin_string):
    """
    Convert a binary string to a hex string.
    """
    return hex(int(bin_string, 2))[2:].upper().zfill(16)

def main():
    # Example 64-bit block (in hexadecimal)
    hex_input = input("Enter the hexadecimal (16 characters): ")
    print(f"Input (hex): {hex_input}")

    # Convert hex input to binary
    bin_input = hex_to_bin(hex_input)
    print(f"Input (binary): {bin_input}")

    # Apply initial permutation
    ip_output = permute(bin_input, IP)
    print(f"After Initial Permutation (binary): {ip_output}")
    print(f"After Initial Permutation (hex): {bin_to_hex(ip_output)}")

    # Apply final permutation
    fp_output = permute(ip_output, FP)
    print(f"After Final Permutation (binary): {fp_output}")
    print(f"After Final Permutation (hex): {bin_to_hex(fp_output)}")

if __name__ == "__main__":
    main()
