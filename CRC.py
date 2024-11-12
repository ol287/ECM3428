class CRC:
    def __init__(self, message, generator_polynomial):
        """
        Initialize the CRC object with a message and generator polynomial.

        Parameters:
        message (str): Binary string representing the message.
        generator_polynomial (str): Binary string representing the generator polynomial.
        """
        self.message = message
        self.generator_polynomial = generator_polynomial
        self.r = len(generator_polynomial) - 1  # Order of polynomial (number of check bits)

    def calculate_crc(self):
        """
        Calculate the CRC check bits for the given message and generator polynomial.

        Returns:
        str: The CRC check bits as a binary string.
        """
        # Step 1: Append 'r' zeros to the end of the message to make room for CRC bits
        extended_message = self.message + '0' * self.r
        
        # Convert the extended message and generator polynomial to integer form
        # This allows us to use bitwise operations (like XOR and shifts)
        C = int(extended_message, 2)
        P = int(self.generator_polynomial, 2)
        
        # Get the total length of the extended message
        total_length = len(extended_message)

        # Perform the CRC calculation using the bitwise algorithm
        for i in range(len(self.message)):  # Only go through the original message length
            # Check if the leftmost bit in the current remainder (C) is 1
            if (C >> (total_length - i - 1)) & 1:
                # XOR C with the generator polynomial P aligned to the current position
                C ^= P << (total_length - self.r - i - 1)

        # Extract the CRC check bits (last r bits of C)
        crc_check_bits = C & ((1 << self.r) - 1)
        
        # Convert the CRC check bits to binary and return as a string
        return bin(crc_check_bits)[2:].zfill(self.r)

    def get_crc(self):
        """
        Public method to get the CRC check bits by calling the calculate_crc method.

        Returns:
        str: The CRC check bits.
        """
        return self.calculate_crc()

# Example usage
# Create a CRC object with a message and a generator polynomial
message = "11010011101100"  # Example binary message
generator_polynomial = "1101"  # Example binary generator polynomial (P(x) = 1101)

# Instantiate the CRC class
crc_calculator = CRC(message, generator_polynomial)

# Call the get_crc method to get the CRC check bits
crc_bits = crc_calculator.get_crc()
print("CRC Check Bits:", crc_bits)
