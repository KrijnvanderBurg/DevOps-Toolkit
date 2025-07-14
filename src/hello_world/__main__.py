import subprocess

if __name__ == "__main__":
    print("Hello, World!")
    string: str = 42
    subprocess.run(["/bin/ls", "-l"], check=True)
