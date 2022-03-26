# office_coincidence

## Solution #1 (coincidence.py)

In this solution i used a structured programming approche. 

### Design and Architecture 

Because we need pairs of employees, I needed to implement a nested loop over the data already cleaned and convereted to pick the name of the employee and compare the time the were in the office. 

I used Python dictionaries to store both, the cleaned data and the pairs to be returned by the program, for their capabilities to hold key-value pairs. Although a list could be used for the cleaned data, decided for a dictionary for it's time efficiency.

As the program is counting the pairs twice (name1-name2 and name2-name1) i needed to  floor devide the occurencies by 2.


### Usage

To use the program call it's name preceeded by the interprete;s name, and followed by the name of the text file where the data is contrained.

```bash
python coincidence.py schedule.txt
```

## Solution #2 (coincidence2.py)

In this solution i used a Object Oriented Programming approche. 

### Design and Architecture 

With this solution i focused more on the schedules themselves and their coincidences. I created a class which contains the data needed to compare each worked schedule.

After reading and converting the data coming from the .txt file into the appropiate type (string and datetime), an instance of the Schedule class is created. At it's creation and instance method compares to all instances already created and if schedules coincide to another, it is added to coincidence python dictionary.

A class level method is called in which each in which coincidences are printed. 

pairs to be returned are stored using a python dictionary.


### Usage

To use the program call it's name preceeded by the interprete;s name, and followed by the name of the text file where the data is contrained.

```bash
python coincidence2.py schedule.txt
