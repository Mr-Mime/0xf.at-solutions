And once again we open the developer tools and search for the `script` tag.

Ther intersting line is this one:  
`if(el.value==unescape("r%20i%20g%20h%20t%20")+""+"p"+"w"+""+"a6e3efefd")`

Entering the right part of the comparison into the javascript console gives us the solution:
![image](https://user-images.githubusercontent.com/37423773/200136580-f504ce6d-1b12-478c-9c4b-b1c76efb7e8a.png)
