import subprocess

def list_installed_packages():
    try:
        installed_packages = subprocess.check_output(['pip', 'freeze']).decode('utf-8')
        
        with open('requirements.txt', 'w') as file:
            file.write(installed_packages)
            
        print("The installed packages have been listed in requirements.txt")
        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while listing the packages: {e}")

if __name__ == "__main__":
    list_installed_packages()
