
def validate():
    import re
    while True:
        print(''''
        ****  Type Yes  to start the validation       ****
        ***** Type No  to show the emails in the files ****
        ***** Type Quit or stop to abort the service        ****''')
        Uservoice = input("Enter the your option: ")
        if Uservoice == "Yes":
            Emailcheck=(input("Entet the email to  vaildate: "))
            pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            val=re.match(pattern, Emailcheck)
            Vald = bool(val)
            if Vald:
                f = open("emailsss.txt", "a")
                f.write(Emailcheck + '\n')
                f.close()
            else:
                print("the mail id was wrong")
        elif Uservoice == "No":
            f = open("emailsss.txt", "r")
            v = f.read()
            print(v)
        elif Uservoice == "Stop":
            print("Thank you we are now Exiting from validation")
            break
        else:
            break
validate()