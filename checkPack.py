import sys
import subprocess


def check_packages():
    required_packages = ['pyvisa', 'numpy', 'pandas']

    missing_packages = []

    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))  # Handle packages
        except ImportError:
            missing_packages.append(package)

    if missing_packages:
        print(f"Missing packages: {missing_packages}")
        val = input("Would you like to install them now? (y/n): ")
        if val.lower() == 'y':
            for package in missing_packages:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print("Installations complete. Please restart the script.")
        sys.exit()
    else:
        print("Please install missing packages and try again.")
        sys.exit()

check_packages()
