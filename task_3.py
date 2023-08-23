import re
import subprocess
def validate():
    while True:
        print('''
        ****  Type Yes to start the validation       ****
        ***** Type No to show the emails in the files ****
        ***** Type Quit or Stop to abort the service  ****''')
        user_choice = input("Enter your option: ").lower()

        if user_choice == "yes":
            ip_check = input("Enter the IP address to validate: ")
            ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
            is_valid_ip = re.match(ip_pattern, ip_check)

            if is_valid_ip:
                result = subprocess.run(["ping",ip_check], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if result.returncode == 0:
                    with open("pingip.txt", "a") as f:
                        f.write(ip_check + '\n')
                    print("added to file, its pingig")
                else:
                    with open("unpingip.txt", "a") as f:
                        f.write(ip_check + '\n')
                    print("added to file, its not pingig")
            else:
                print("The IP address was invalid")

        elif user_choice == "no":
            with open("pingip.txt", "r") as f:
                pingable_ips = f.read()
            with open("unpingip.txt", "r") as f:
                unpingable_ips = f.read()
            print("Pingable IP addresses:")
            print(pingable_ips)
            print("Non-pingable IP addresses:")
            print(unpingable_ips)

        elif user_choice == "quit" or user_choice == "stop":
            print("Thank you. Exiting from validation.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

validate()
