def lzw_encoding(input_string, initial_dictionary):
    """
    Perform LZW encoding on an input string.

    Parameters:
    input_string (str): The string to be encoded.
    initial_dictionary (dict): A dictionary with initial characters mapped to their codewords.

    Returns:
    list: A list of codewords representing the encoded input string.
    """
    # Initialize variables
    n = len(input_string)
    dictionary = initial_dictionary.copy()  # Copy the initial dictionary
    codewords = []  # List to store output codewords
    w = ""  # Current sequence being processed

    # Loop through the input string
    for i in range(n):
        k = input_string[i]  # Current character
        if w + k in dictionary:  # Check if the sequence exists in the dictionary
            w += k  # Extend the current sequence
        else:
            # Add new sequence to the dictionary
            dictionary[w + k] = len(dictionary) + 1
            # Output the codeword for the current sequence
            codewords.append(dictionary[w])
            # Update w to the current character
            w = k

    # Output the final codeword for the remaining sequence
    if w:
        codewords.append(dictionary[w])

    return codewords


# Example Usage
if __name__ == "__main__":
    # Input string and initial dictionary
    input_string = "ABABABA"
    initial_dictionary = {"A": 1, "B": 2}

    # Perform LZW encoding
    encoded_output = lzw_encoding(input_string, initial_dictionary)

    print("Encoded Output:", encoded_output)
