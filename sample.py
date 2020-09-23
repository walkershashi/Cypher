from cypher import checkPassword, REQUIRED_CHARACTER
from cypher import encryptPassword

password = input("Enter your Password: ")
check_password = checkPassword()

passwordChecker = check_password.isStrong(password)

if passwordChecker:
    print("Strong Password")
    encryption_obj = encryptPassword()
    encryptedPassword = encryption_obj.encrypt(password)
    print("Encrypted Password : {}".format(encryptedPassword))

else:
    print("Weak Password!!")
    print("Characters Required: ")

    for char, required in REQUIRED_CHARACTER.items():
        if required:
            print(char)