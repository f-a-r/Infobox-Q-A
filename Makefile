Language: Python
(No external library needed)

Running:
Usage -
1. python run.py -key <Freebase API key> -q <query> -t <infobox | question>
2. python run.py -key <Freebase API key> -f <file of queries> -t <infobox | question>
where -
* <Freebase API key> is the Google account key for Freebase.
* -q <query> is the query. For infobox, it is a list of words in double quotes (e.x., “Bill Gates”). For question, it is a string that matches this patten “Who created [X]?”, where [X] is the target item. “W” and “w” is both accepted to our implementation, and “?” can be skipped. 
* -f <file of queries> is a text file with one query per line.
* -t <infobox | question> indicates the query type.

p.s.
If there is any error related to encode occurring (i.e., as ascii instead of unicode), please try to 
1) export LC_ALL=en_US.UTF-8
2) export LANG=en_US.UTF-8
3) export PYTHONIOENCODING=UTF-8
before running our code. Thanks.

