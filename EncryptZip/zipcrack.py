from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False

def main():
    print("[+] Beginning brute force")
    with ZipFile('aaa.zip') as zf:
        with open('rockyou.txt', 'r') as f:
            for line in f:
                password = line.strip().encode()  # Convert password to bytes
                if attempt_extract(zf, password):
                    print("[+] Correct password: %s" % password.decode())  # Decode for readability
                    exit(0)
                else:
                    print("[-] Incorrect password: %s" % password.decode())

    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
