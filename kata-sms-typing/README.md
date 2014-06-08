SMS-like typing
===============

Write your SMS as you would do it on a old phone keypad.

This is the pad:

|  C   |  ←   |   →   |
| :--: | :--: | :---: |
| .; 1 | abc2  | def3 |
| ghi4 | jkl5  | mno6 | 
| pqrs7| tuv8  | wxyz9|
|      | -_:0 |       | 
*Note that key '1' contains a blank space

## Rules
### Decode
* The input will be a sequence of numbers that can be separated by blank spaces or not
* It is cyclic i.e.: 33333 would be decoded as 'd'
* Some examples of how can be the input (hello):
  * 44 33 555 555 666
  * 4433555 555666
  * 444444 33 555 555666

### Encode
* The input is a **valid** string.
* The output is the sequence of numbers -separated by a space blank- that produce that string.
* Example:
  * hello -> 44 33 555 555 666
  * sms -> 7777 6 7777

## License
[MIT License](LICENSE)
