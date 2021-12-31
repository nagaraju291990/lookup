# To look up in input file the contents of master file.
## PYTHON

### To generate matched.txt and not-matched.txt
```
python3 lookup.py --i=inputfile --m=masterfile
```
Here both are assumed to be tab separated files.  

### To print zeroes and ones against each column of the inputfile against master/reference file
```
python3 lookup_multi_col.py --iinputfile --m=masterfile
```
#### Uniq program
```
python3 uniq.py -i=input.txt(tab separated)
```

## PERL
### For tab seperated file

```
	perl search.pl --input=[file1] --master=[file2]
```
### To matche entire line
```
	perl lookup.pl --input=[file1] --master=[file2]
```
