As in level 1 we once again need the developer tools and need to search for the `<script>` tag.
We see the following function wich checks the password:
```
function checkPW() {
  var pw = "%63%38%34%62%34";
  var el = document.getElementById('pw');
  if(el.value==unescape(pw))
    window.location.href="?pw="+el.value;
  else alert("Wrong password");
}
```

The entered password is checked against the unescaped `pw` variable.

The easiest way to get the unescaped value is to use the javascript console of the browser:  
![image](https://user-images.githubusercontent.com/37423773/200136323-682e6390-e19a-47a4-a119-3975b1839e4f.png)

And there we have the password.
