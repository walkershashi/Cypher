### Password Encrypter 

The package tells whether the password provided is strong or not and then encrypts the password.

#### Encryption.py 

This script encrypts the password provided and returns the encrypted password. The password is encrypted on the basis of a certain algorithm.

#### StrongPassword.py 

This script returns true if the password is strong and false is the password is weak.
The Password is considered to be strong if it consists:

<ul>
<li> Atleast one lowercase character: ['a-z'] </li>
<li> Atleast one uppercase character: ['A-Z'] </li>
<li> Atleast on digit: ['0-9'] </li>
<li> Atleast on special character: ['!@#$%^&*_'] </li>
</ul>

This script also has a <code>global dictionary</code> which has character names as key and bool as values which tells whether this chararter is missing or not.

#### main.py

This script calls both these modules and takes the input from the user and the passes to them.
This script call the global dictionary from the StrongPassword.py script and prints all the missing charater required in the password to make the password strong.
If the password is strong then it is encrypted and the encrypted password is then displayed on the screen.
