

###### What the scipt does:

The script 
1). turns long links into shortend links like 
```
ex. https://www.google.com/search?q=how+to+be+cool 
=> https://bit.ly/46lV7aP
```
2). if the link already exists, the script returns how many times people clicked on it
```
ex. Total clicks on https://bit.ly/46lV7aP:  11
```

###### How to use it
1. Register at https://bitly.com and get personal token (Settings > API > Generate token)

2. Set environment token variable
To do so, execute 
`export BITLY_TOKEN='[your token from bitly]'`
before you run the script