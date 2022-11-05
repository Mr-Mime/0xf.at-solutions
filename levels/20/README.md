For this cracking challenge the haslib module has been used.  
Hashlib implements various hash algorithms, including MD5.  

We know that the hash was calculated by combining two words of the given wordlist.  
Thus we need to check every possible combination and have a nested loop iterating through the words of the word list.

For each combination the hash is calculated and checked against the given hash.
If it maches we leave the for loops, print the solution and close the the files

It took 06:31 minutes with python to find the solution.


```
solution.py 37cf3ec60e9a693df97b075019c7d1fb wordlist.txt

> awakensfaster
```