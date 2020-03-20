## CFRankScrapper

### Description

main.py uses the CF Contest Stadings API to get the results and then finds the ranks of those handles mentioned in the data.json and then tabulates and ranks the result in a table format

### Dependencies
- Bluesoup4 ( https://pypi.org/project/beautifulsoup4/)
  
  ``` pip3 install beautifulsoup4 ```
- Tabulate ( https://pypi.org/project/tabulate/ )

  ``` pip3 install tabulate ```
  
### Instructions
  
  ``` $ python3 ./main.py ```
  
  It will ask for the contest id. Contest ID for CodeForces contest is the number which you can find in the URL. 
  If the contest URL is ``` https://codeforces.com/contest/1326 ``` 
  Then the number 1326 is the contest ID. After you provide the contest ID it will take some time fecthing the data, and tabulating the results. The final ouput will be exported to the ``` results.txt ```

### To add another user ID
 The ``` data.json ``` file can be edited to insert more names and their respective user Id.
