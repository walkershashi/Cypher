import math

class encryptPassword:

    """
    Class to encrypt the password, if the password is strong

    Attributes:
        None
    """

    def __init__(self):
        pass

    def encrypt(self, password):

        """
        Function to encrypt the password 

        Args:
            password (string): Passwword provided

        Returns:
            encrypted_password (string)
        """

        res = []
        size = len(password)

        str_size = str(math.sqrt(size))
        
        if len(str_size) == 3:
            row = int(math.sqrt(size))
            col = int(math.sqrt(size))

        else:
            row = int(math.sqrt(size))
            col = int(math.sqrt(size) + 1)

        if row*col < size:
            row += 1
        
        i = 0
        for it in range(size//col):
            res.append(password[i: col+i])
            i += col
        
        if size//col != row:
            left_str = size - col * (size//col)
            string =password[-left_str:]
            space_len = col - len(string)
            
            for i in range(space_len):
                string += ' '

            res.append(string)
        
        encrypted_string = []

        for i in range(len(res[0])):
            password = ''
            for word in res:
                password += word[i]
            encrypted_string.append(password.replace(" ", ""))

        return ("".join(encrypted_string))
