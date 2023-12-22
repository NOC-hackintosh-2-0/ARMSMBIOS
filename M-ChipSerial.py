import random
import time
import sys

# Function to display a progress bar
def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

# Function to simulate computation time
def compute_serial_progress():
    for i in range(101):
        print_progress_bar(i, 100, prefix='Generating Serial:', suffix='Complete', length=30)
        time.sleep(0.05)  # Simulating computation time
    print()

# Function to generate a serial
def generate_serial():
    compute_serial_progress()
    return ''.join(random.choices('0123456789ABCDEF', k=8))

# Function to display a menu of Mac models
def display_mac_models():
    mac_models = [
        'iMac', 'MacBook Pro', 'MacBook Air', 'Mac mini', 'Mac Studio', 'Mac Pro', 'Go back to main menu'
    ]
    print("=== Mac Models ===")
    for idx, model in enumerate(mac_models, start=1):
        print(f"{idx}. {model}")
    return input("Enter the number of the Mac model or 'Q' to go back: ")

def generate_serial_with_model(chip, model, mac_model):
    print("Generating Serial...")
    generated_serial = generate_serial()
    print(f"Generated {chip} Serial for {model} {mac_model}: {generated_serial}")
    input("Press Enter to return to the main menu...")

def main():
    base_serials = {
        'M1': {
            'M1': ['M1BASE1111', 'M1BASE2222', 'M1BASE3333', 'M1BASE4444'],
            'M1 Pro': ['M1PRO1111', 'M1PRO2222', 'M1PRO3333', 'M1PRO4444'],
            'M1 Max': ['M1MAX1111', 'M1MAX2222', 'M1MAX3333', 'M1MAX4444'],
            'M1 Ultra': ['M1ULTRA1111', 'M1ULTRA2222', 'M1ULTRA3333', 'M1ULTRA4444']
        },
        'M2': {
            'M2': ['M2BASE1111', 'M2BASE2222', 'M2BASE3333', 'M2BASE4444'],
            'M2 Pro': ['M2PRO1111', 'M2PRO2222', 'M2PRO3333', 'M2PRO4444'],
            'M2 Max': ['M2MAX1111', 'M2MAX2222', 'M2MAX3333', 'M2MAX4444'],
            'M2 Ultra': ['M2ULTRA1111', 'M2ULTRA2222', 'M2ULTRA3333', 'M2ULTRA4444']
        },
        'M3': {
            'M3': ['M3BASE1111', 'M3BASE2222', 'M3BASE3333', 'M3BASE4444'],
            'M3 Pro': ['M3PRO1111', 'M3PRO2222', 'M3PRO3333', 'M3PRO4444'],
            'M3 Max': ['M3MAX1111', 'M3MAX2222', 'M3MAX3333', 'M3MAX4444'],
            'M3 Ultra': ['M3ULTRA1111', 'M3ULTRA2222', 'M3ULTRA3333', 'M3ULTRA4444']
        }
        # Add more base serials as needed for other chip models
    }

    mac_models_chip_versions = {
        'iMac': ['M1', 'M3'],
        'MacBook Pro': ['M1', 'M1 Pro', 'M1 Max', 'M2', 'M2 Pro', 'M2 Max', 'M3', 'M3 Pro', 'M3 Max'],
        'MacBook Air': ['M1', 'M2'],
        'Mac mini': ['M1', 'M1 Pro', 'M2', 'M2 Pro'],
        'Mac Studio': ['M2 Max', 'M2 Ultra'],
        'Mac Pro': ['M2 Ultra']
    }

    while True:
        print("=== Main Menu ===")
        print("1. Choose Chip Type")
        print("2. Choose Mac Model")
        print("Q. Quit")
        choice = input("Enter your choice: ").lower()

        if choice == 'q':
            break

        if choice == '1':
            print("=== Chip Menu ===")
            chip_models = list(base_serials.keys())
            for idx, chip in enumerate(chip_models, start=1):
                print(f"{idx}. {chip}")
            chip_idx = int(input("Enter the number of the chip type: ")) - 1
            chosen_chip = chip_models[chip_idx]

            print(f"=== {chosen_chip} Versions ===")
            sub_menu = list(base_serials[chosen_chip].keys()) + ['Go back to main menu']
            for idx, version in enumerate(sub_menu, start=1):
                print(f"{idx}. {version}")
            model_idx = int(input(f"Enter the number of the {chosen_chip} version: ")) - 1
            chosen_model = sub_menu[model_idx]

            mac_model_choice = display_mac_models()
            if mac_model_choice.lower() == 'q':
                continue
            elif mac_model_choice == str(len(mac_models_chip_versions) + 1):
                continue  # Go back to main menu
            else:
                mac_model_idx = int(mac_model_choice) - 1
                chosen_mac_model = list(mac_models_chip_versions.keys())[mac_model_idx]
                
                available_versions = mac_models_chip_versions[chosen_mac_model]
                if chosen_model not in available_versions:
                    print(f"{chosen_mac_model} does not support {chosen_model} chip.")
                    continue

                generate_serial_with_model(chosen_chip, chosen_model, chosen_mac_model)

        elif choice == '2':
            mac_model_choice = display_mac_models()
            if mac_model_choice.lower() == 'q':
                continue
            elif mac_model_choice == str(len(mac_models_chip_versions) + 1):
                continue  # Go back to main menu
            else:
                mac_model_idx = int(mac_model_choice) - 1
                chosen_mac_model = list(mac_models_chip_versions.keys())[mac_model_idx]

                print("=== Chip Menu ===")
                chip_models = list(base_serials.keys())
                for idx, chip in enumerate(chip_models, start=1):
                    print(f"{idx}. {chip}")
                chip_idx = int(input("Enter the number of the chip type: ")) - 1
                chosen_chip = chip_models[chip_idx]

                available_versions = mac_models_chip_versions[chosen_mac_model]
                if chosen_chip not in available_versions:
                    print(f"{chosen_mac_model} does not support {chosen_chip} chip.")
                    continue

                print(f"=== {chosen_chip} Versions ===")
                sub_menu = list(base_serials[chosen_chip].keys()) + ['Go back to main menu']
                for idx, version in enumerate(sub_menu, start=1):
                    print(f"{idx}. {version}")
                model_idx = int(input(f"Enter the number of the {chosen_chip} version: ")) - 1
                chosen_model = sub_menu[model_idx]

                generate_serial_with_model(chosen_chip, chosen_model, chosen_mac_model)

        else:
            print("Invalid input. Please enter a valid option.")

if __name__ == '__main__':
    main()
