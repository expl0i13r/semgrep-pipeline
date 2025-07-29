import os

def run_command(user_input):
    # 🚨 Vulnerable to remote command execution!
    os.system(user_input)

if __name__ == "__main__":
    command = input("Enter command: ")
    run_command(command)
