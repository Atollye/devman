

### What's that script for

The script 
* turns long links into shortend links like 
```
ex. https://www.google.com/search?q=how+to+be+cool 
=> https://bit.ly/46lV7aP
```
* if the link already exists, the script returns, how many times people clicked on it
```
ex. Total clicks on https://bit.ly/46lV7aP:  11
```




### How to use it
1. [Make sure](../README.md#how-to-launch-the-code), you created a virtual environment and installed required packages there

2. Register at https://bitly.com and get personal token (*Settings > API > Generate token*)

3. Set environment token variable
To do so, execute 
`export BITLY_TOKEN='[your token from bitly]'`
before you run the script
