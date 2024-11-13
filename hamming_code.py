def calculate_parity_bits(m):
    # Calculate the number of parity bits required
    for i in range(m):
        if 2**i >= m + i + 1:
            return i

def hamming_encode(data):
    """
    Encode the given binary data using Hamming code.
    :param data: Input data string (binary format, e.g., '1011')
    :return: Encoded data with parity bits
    """
    m = len(data)
    r = calculate_parity_bits(m)

    # Initialize the encoded data array
    total_length = m + r
    encoded = ['0'] * total_length

    # Position the data bits (skip parity positions)
    j = 0
    for i in range(1, total_length + 1):
        if i & (i - 1) == 0:  # Power of 2 positions are parity bits
            continue
        encoded[i - 1] = data[j]
        j += 1

    # Calculate parity bits
    for i in range(r):
        parity_position = 2**i
        parity = 0
        for j in range(1, total_length + 1):
            if j & parity_position and encoded[j - 1] == '1':
                parity ^= 1
        encoded[parity_position - 1] = str(parity)

    return ''.join(encoded)

def hamming_decode(encoded):
    """
    Decode the given Hamming encoded data, correcting any single-bit error.
    :param encoded: Encoded data string (binary format, e.g., '1010110')
    :return: Decoded data and error position (0 if no error)
    """
    n = len(encoded)
    r = calculate_parity_bits(n)

    # Detect error position
    error_position = 0
    for i in range(r):
        parity_position = 2**i
        parity = 0
        for j in range(1, n + 1):
            if j & parity_position and encoded[j - 1] == '1':
                parity ^= 1
        if parity:
            error_position += parity_position

    # Correct the error if found
    if error_position:
        error_index = error_position - 1
        encoded = list(encoded)
        encoded[error_index] = '1' if encoded[error_index] == '0' else '0'
        encoded = ''.join(encoded)

    # Extract original data (skip parity positions)
    decoded = []
    for i in range(1, n + 1):
        if i & (i - 1) == 0:  # Skip parity positions
            continue
        decoded.append(encoded[i - 1])

    return ''.join(decoded), error_position

# Example usage
data = "1011"
encoded_data = hamming_encode(data)
print(f"Encoded Data: {encoded_data}")

decoded_data, error_position = hamming_decode(encoded_data)
print(f"Decoded Data: {decoded_data}, Error Position: {error_position}")

# Introduce an error for testing
error_encoded_data = list(encoded_data)
error_encoded_data[2] = '0' if error_encoded_data[2] == '1' else '1'
error_encoded_data = ''.join(error_encoded_data)
print(f"Encoded Data with Error: {error_encoded_data}")

decoded_data, error_position = hamming_decode(error_encoded_data)
print(f"Decoded Data: {decoded_data}, Error Position: {error_position}")
