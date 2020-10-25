# Intervals

+ [Insert Interval](#insert-interval)

[comment]: <> (Stop)

## Insert Interval

https://leetcode.com/problems/insert-interval/

``` python 
 def insert(self, Intervals, NewInterval):
    ShallBeRemoved = []
    for interval in Intervals:
        if (interval[0] <= NewInterval[0]) and (NewInterval[1] <= interval[1]):
            NewInterval = interval
            ShallBeRemoved.append(interval)
        elif (NewInterval[0] <= interval[0]) and (interval[1] <= NewInterval[1]):
            ShallBeRemoved.append(interval)
        elif (interval[0] == NewInterval[1]):
            NewInterval = [NewInterval[0], interval[1]]
            ShallBeRemoved.append(interval)
        elif (interval[1] == NewInterval[0]):
            NewInterval = [NewInterval[1], interval[0]]
            ShallBeRemoved.append(interval)
        elif (interval[0] > NewInterval[0]) and (interval[0] < NewInterval[1]):
            NewInterval = [NewInterval[0], interval[1]]
            ShallBeRemoved.append(interval)
        elif (interval[1] > NewInterval[0]) and (interval[1] < NewInterval[1]):
            NewInterval = [interval[0], NewInterval[1]]
            ShallBeRemoved.append(interval)
    for interval in ShallBeRemoved:
        Intervals.remove(interval)   
    if len(Intervals) == 0:
        return([NewInterval])
    New_Intervals = []
    New_Intervals.append(NewInterval)
    New_Intervals += Intervals
    New_Intervals = sorted(New_Intervals)
    return(New_Intervals)   
 ```
