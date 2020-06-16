REQUIRED_CHARACTER = {} # Dictionary to store missing characters from the password which are required to make the passworrd strong

class checkPassword:

    """
    Class for checking whether a password(string) provided is strong or not

    Attributes:
        None

    """
    
    def __init__(self):
        pass
        
    def isStrong(self, password):

        """Function to check password is strong or not 
        Args:
            password (string): The password entered by the user
                               Password must be of length 6 with atleast one uppercase, lowercase, digit and special characters
                               uppercase = 'A-Z'
                               lowercase = 'a-z'
                               digits = '0-9'
                               special characters = '!@#$%^&*_'
        
        Returns:
            bool: False for Weak Password
                  True for string Password
        """

        size = 0
        if len(password) < 6:
            size = 6 - len(password)

        cnt = 0
        password = set(password)
        number = set(map(str, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        lower_case = set("abcdefghijklmnopqrstuvwxyz")
        upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        sp_char = set("!@#$%^&*_")

        if len(password.intersection(number)) == 0:
            cnt += 1
            REQUIRED_CHARACTER['number'] = True

        if len(password.intersection(lower_case)) == 0:
            cnt += 1
            REQUIRED_CHARACTER['lower character'] = True

        if len(password.intersection(upper_case)) == 0:
            cnt += 1
            REQUIRED_CHARACTER['upper character'] = True

        if len(password.intersection(sp_char)) == 0:
            cnt += 1
            REQUIRED_CHARACTER['special character'] = True

        res = max(cnt, size)
        if res != 0:          
            return False #("Weak Password") 
        else:
            return True #("Strong Password")
