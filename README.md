# Code-breaker

###Hack Mr.Evil super secret lab and save the world!
![Mr. Evil](https://dl.dropboxusercontent.com/s/hb1maq55feqtat5/mr_evil.png) 

## Rules
* The password is composed by the following letters:
  * `R` `A` `M` `V` `I` `N`
* The system will generate a random password from the list of supported letters.
* It will return a `X` for each letters that match the password, and it will return a `*` for each letter that appear in the password but it doesn't match the position.

Some examples:
```code
input = RVMI
pass = AMVI
->
output = X**
```
```
input = RAMV
pass = VIMV
->
output = XX
```

## References
* Kata Code-Breaker, on [Solveet](http://www.solveet.com/exercises/Kata-CodeBreaker/14)
* I made my solution good-looking.
