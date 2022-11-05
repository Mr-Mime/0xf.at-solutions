Once again the solution lays in the javascript code.

The function checks the entered password against the length of the `pwinfo` variable.
```
function checkPW() {
  var el = document.getElementById("pw");
  var pwinfo = "0a2bfaccd3a ebaaceba45e43aaa43aeb2c5fe4eaaddc35cfff b14b5cc52 bce55fa55d2b50dc2251e 3 15cb3 52444";
  if(el.value==pwinfo.length)
    window.location.href="?pw="+el.value;
  else alert("Wrong password");
}
```

Thus the solution is the length of the `pwinfo` string.
![image](https://user-images.githubusercontent.com/37423773/200136807-80cbeaf1-6ba7-4d1b-99e5-be367ab68ca5.png)
