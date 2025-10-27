import base64


# File path to the log file needs to be in the same directory as this script
with open('./a2V5bG9n.txt', 'r') as file:
    # List to store the decoded characters
    decoded_characters = []

    # Read from the file
    for line in file:
        # Strip any whitespace or newlines
        line = line.strip()
        if line:  # Check if the line is not empty
            # Decode the Base64 string and convert it to a string
            decoded_bytes = base64.b64decode(line)
            decoded_char = decoded_bytes.decode('utf-8')
            decoded_characters.append(decoded_char)

    with open('./Decoded_Log.txt', 'a') as output_file:
        # Print each character
        for char in decoded_characters:
            output_file.write(char)
            output_file.flush()
