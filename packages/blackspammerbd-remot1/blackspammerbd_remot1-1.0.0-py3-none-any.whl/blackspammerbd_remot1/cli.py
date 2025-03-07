#!/usr/bin/env python3
"""
CLI Module for blackspammerbd_remot Package

Available commands:
    start   : Generate secret code (if not exists) and start the TCP server.
    connect : Connect to remote server using secret code.
    off     : Disconnect from the connected device.
Usage:
    bsb start [--port <port>]
    bsb connect <secret_code> [host] [--port <port>]
    bsb off <secret_code> [host] [--port <port>]

In interactive mode, available commands: list, download <filename>, upload <filename>, exit
"""

import os
import sys
import random
import base64
import argparse
import socket
from colorama import Fore, Style

# File to store the secret code
SECRET_CODE_FILE = ".connection_code"
DEFAULT_PORT = 9000

def generate_secret_code() -> str:
    """Generates an 8-digit secret code."""
    return ''.join(str(random.randint(0, 9)) for _ in range(8))

def save_secret_code() -> None:
    """Generates and saves the secret code in a hidden file with restricted permissions."""
    code = generate_secret_code()
    try:
        with open(SECRET_CODE_FILE, "w", encoding="utf-8") as f:
            f.write(code)
        try:
            os.chmod(SECRET_CODE_FILE, 0o600)
        except Exception:
            pass
        print(Fore.GREEN + "Secret code generated and saved successfully.")
        print(Fore.CYAN + "Share this code only with trusted devices.")
        print(Fore.CYAN + f"Secret Code: {code}")
    except Exception as e:
        print(Fore.RED + f"Error saving secret code: {e}")

def load_secret_code() -> str:
    """Loads the secret code from the hidden file."""
    if not os.path.exists(SECRET_CODE_FILE):
        return ""
    try:
        with open(SECRET_CODE_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        print(Fore.RED + f"Error reading secret code: {e}")
        return ""

def get_server_ip() -> str:
    """Automatically determines the server's active IP address."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except Exception:
        ip = "127.0.0.1"
    return ip

def start_server(port: int) -> None:
    """Starts a TCP server to handle client connections and interactive sessions."""
    code = load_secret_code()
    if not code:
        print(Fore.RED + "Secret code not found. Run 'bsb start' first to generate it.")
        return

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_sock.bind(('', port))
        server_sock.listen(1)
    except Exception as e:
        print(Fore.RED + f"Error starting server: {e}")
        return

    server_ip = get_server_ip()
    print(Fore.CYAN + f"Server IP Address: {server_ip}")
    print(Fore.CYAN + f"Waiting for incoming connections on port {port}...")

    conn, addr = server_sock.accept()
    print(Fore.CYAN + f"Connection established from: {addr}")

    # Authenticate client using the secret code
    try:
        received = conn.recv(1024).decode().strip()
    except Exception as e:
        print(Fore.RED + f"Error receiving data: {e}")
        conn.close()
        server_sock.close()
        return

    if received != code:
        conn.sendall("ERROR: Invalid connection code.\n".encode())
        print(Fore.RED + "Invalid secret code. Closing connection.")
        conn.close()
        server_sock.close()
        return
    else:
        conn.sendall("OK\n".encode())
        print(Fore.GREEN + "Client authenticated successfully.")

    # Interactive session for file transfer
    print(Fore.CYAN + "Entering interactive mode. Available commands: list, download <filename>, upload <filename>, exit")
    while True:
        try:
            data = conn.recv(4096).decode().strip()
            if not data:
                break
            parts = data.split(" ", 2)
            command = parts[0].lower()
            if command == "list":
                items = os.listdir('.')
                response = "\n".join(items) if items else "No files found."
                conn.sendall((response + "\n").encode())
            elif command == "download":
                if len(parts) < 2:
                    conn.sendall("ERROR: Filename not provided.\n".encode())
                    continue
                filename = parts[1]
                if not os.path.exists(filename):
                    conn.sendall(f"ERROR: File '{filename}' not found.\n".encode())
                    continue
                try:
                    with open(filename, "rb") as f:
                        content = f.read()
                    encoded = base64.b64encode(content).decode()
                    conn.sendall(f"DATA {encoded}\n".encode())
                except Exception as e:
                    conn.sendall(f"ERROR: Failed to read file: {e}\n".encode())
            elif command == "upload":
                if len(parts) < 3:
                    conn.sendall("ERROR: Filename or data not provided.\n".encode())
                    continue
                filename = parts[1]
                b64data = parts[2]
                try:
                    file_data = base64.b64decode(b64data)
                    out_filename = "uploaded_" + filename
                    with open(out_filename, "wb") as f:
                        f.write(file_data)
                    conn.sendall(f"File '{filename}' uploaded as '{out_filename}'.\n".encode())
                except Exception as e:
                    conn.sendall(f"ERROR: Failed to upload file: {e}\n".encode())
            elif command in ["exit", "off"]:
                conn.sendall("Goodbye!\n".encode())
                break
            else:
                conn.sendall("ERROR: Unknown command.\n".encode())
        except Exception as e:
            conn.sendall(f"ERROR: {e}\n".encode())
    conn.close()
    server_sock.close()
    print(Fore.CYAN + "Connection closed. Server shutting down.")

def start_client(provided_code: str, host: str, port: int, interactive: bool = True, immediate_disconnect: bool = False) -> None:
    """
    Connects to the server using the provided secret code.
    If immediate_disconnect is True, sends a disconnect command right after authentication.
    Otherwise, enters interactive mode.
    """
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_sock.connect((host, port))
    except Exception as e:
        print(Fore.RED + f"Error connecting to server: {e}")
        return

    # Send secret code for authentication
    client_sock.sendall((provided_code + "\n").encode())
    try:
        response = client_sock.recv(1024).decode().strip()
    except Exception as e:
        print(Fore.RED + f"Error receiving authentication response: {e}")
        client_sock.close()
        return

    if response != "OK":
        print(Fore.RED + f"Authentication failed: {response}")
        client_sock.close()
        return

    print(Fore.GREEN + "Authenticated successfully.")

    if immediate_disconnect:
        client_sock.sendall("exit\n".encode())
        data = client_sock.recv(1024).decode().strip()
        print(data)
        client_sock.close()
        return

    print(Fore.CYAN + "Entering interactive mode. Available commands: list, download <filename>, upload <filename>, exit")
    while True:
        try:
            command = input(">> ").strip()
            if not command:
                continue
            if command.lower().startswith("upload"):
                parts = command.split(" ", 1)
                if len(parts) < 2:
                    print(Fore.RED + "Error: Filename not provided for upload.")
                    continue
                filename = parts[1]
                if not os.path.exists(filename):
                    print(Fore.RED + f"Error: File '{filename}' not found.")
                    continue
                try:
                    with open(filename, "rb") as f:
                        content = f.read()
                    b64data = base64.b64encode(content).decode()
                    full_command = f"upload {filename} {b64data}"
                    client_sock.sendall((full_command + "\n").encode())
                except Exception as e:
                    print(Fore.RED + f"Error reading file: {e}")
                    continue
            else:
                client_sock.sendall((command + "\n").encode())
            data = client_sock.recv(4096).decode()
            if data.startswith("DATA "):
                # Download response: decode and save the file
                encoded = data[5:].strip()
                parts = command.split(" ", 1)
                if len(parts) < 2:
                    print(Fore.RED + "Error: Filename missing for download.")
                    continue
                filename = parts[1]
                out_filename = "downloaded_" + filename
                try:
                    file_data = base64.b64decode(encoded)
                    with open(out_filename, "wb") as f:
                        f.write(file_data)
                    print(Fore.GREEN + f"File '{filename}' downloaded and saved as '{out_filename}'.")
                except Exception as e:
                    print(Fore.RED + f"Error decoding file data: {e}")
            else:
                print(data.strip())
            if command.lower() in ["exit", "off"]:
                break
        except Exception as e:
            print(Fore.RED + f"Error: {e}")
            break
    client_sock.close()

def main():
    parser = argparse.ArgumentParser(
        description="BlackSpammerBD_Tool CLI - Professional Edition for Secure Device Connection and File Transfer",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Server mode: 'start' command
    start_parser = subparsers.add_parser("start", aliases=["-start"],
                                          help="Generate secret code (if not exists) and start server mode")
    start_parser.add_argument("--port", "-p", type=int, default=DEFAULT_PORT,
                              help="Port to listen on (default: 9000)")

    # Client mode: 'connect' command
    connect_parser = subparsers.add_parser("connect", aliases=["-connect"],
                                            help="Connect to remote server using secret code")
    connect_parser.add_argument("code", help="Secret code for authentication")
    connect_parser.add_argument("host", nargs="?", default=None,
                                help="Server IP address (if not provided, you will be prompted)")
    connect_parser.add_argument("--port", "-p", type=int, default=DEFAULT_PORT,
                                help="Server port (default: 9000)")

    # Disconnect mode: 'off' command (immediate disconnect)
    off_parser = subparsers.add_parser("off", aliases=["-off"],
                                        help="Disconnect from the connected device")
    off_parser.add_argument("code", help="Secret code for authentication")
    off_parser.add_argument("host", nargs="?", default=None,
                            help="Server IP address (if not provided, you will be prompted)")
    off_parser.add_argument("--port", "-p", type=int, default=DEFAULT_PORT,
                            help="Server port (default: 9000)")

    args = parser.parse_args()

    if args.command in ["start", "-start"]:
        if not os.path.exists(SECRET_CODE_FILE):
            save_secret_code()
        else:
            print(Fore.CYAN + "Secret code already exists.")
        start_server(args.port)
    elif args.command in ["connect", "-connect"]:
        if not args.host:
            args.host = input("Enter server IP address: ").strip()
        start_client(args.code, args.host, args.port, interactive=True, immediate_disconnect=False)
    elif args.command in ["off", "-off"]:
        if not args.host:
            args.host = input("Enter server IP address: ").strip()
        # Immediately disconnect by connecting and sending the exit command
        start_client(args.code, args.host, args.port, interactive=False, immediate_disconnect=True)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
