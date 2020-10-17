+ [Non-overlapping Intervals](#non-overlapping-intervals)

+ [Merge Intervals](#merge-intervals)

+ [Insert Interval](#insert-interval)

[comment]: <> (Stop)

# Insert Interval

Problem 57. <a href="https://leetcode.com/problems/insert-interval/">Link to the page </a>

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
# Merge Intervals

Problem 56. <a href="https://leetcode.com/problems/merge-intervals/">Link to the page </a>

``` python 
 def merge(self, Intervals):
    MergedIntervals = []
    AlreadyMerged = []
    for interval_1 in Intervals:
        if Intervals.index(interval_1) in AlreadyMerged:
            continue
        for interval_2 in Intervals:
            if Intervals.index(interval_2) in AlreadyMerged:
                continue
            if (interval_1[0] == interval_2[0]) and (interval_1[1] == interval_2[1]) and (Intervals.index(interval_1) != Intervals.index(interval_2)) and not (interval_2 in MergedIntervals):
                MergedIntervals.append(interval_1)
                AlreadyMerged.append(Intervals.index(interval_1))
                AlreadyMerged.append(Intervals.index(interval_2))
                break
            elif (interval_1[0] == interval_2[1]) and not([interval_2[0],interval_1[1]] in MergedIntervals):
                MergedIntervals.append([interval_2[0], interval_1[1]])
                AlreadyMerged.append(Intervals.index(interval_1))
                AlreadyMerged.append(Intervals.index(interval_2))
                break
            elif (interval_1[1] == interval_2[0]) and not([interval_1[0],interval_2[1]] in MergedIntervals):
                MergedIntervals.append([interval_1[0], interval_2[1]])
                AlreadyMerged.append(Intervals.index(interval_1))
                AlreadyMerged.append(Intervals.index(interval_2))
                break
            elif (interval_1[0] > interval_2[0]) and (interval_1[0] < interval_2[1]):
                if (interval_1[1] <= interval_2[1]) and not(interval_2 in MergedIntervals):
                    MergedIntervals.append(interval_2)
                    AlreadyMerged.append(Intervals.index(interval_1))
                    AlreadyMerged.append(Intervals.index(interval_2))
                    break
                if (interval_1[1] > interval_2[1]) and not([interval_2[0], interval_1[1]] in MergedIntervals):
                    MergedIntervals.append([interval_2[0], interval_1[1]])
                    AlreadyMerged.append(Intervals.index(interval_1))
                    AlreadyMerged.append(Intervals.index(interval_2))
                    break
            elif (interval_1[1] > interval_2[0]) and (interval_1[1] < interval_2[1]):
                if interval_1[0] >= interval_2[0] and not(interval_2 in MergedIntervals):
                    MergedIntervals.append(interval_2)
                    AlreadyMerged.append(Intervals.index(interval_1))
                    AlreadyMerged.append(Intervals.index(interval_2))
                    break
                if (interval_1[0] < interval_2[0]) and not([interval_1[0],interval_2[1]] in MergedIntervals):
                    MergedIntervals.append([interval_1[0],interval_2[1]])
                    AlreadyMerged.append(Intervals.index(interval_1))
                    AlreadyMerged.append(Intervals.index(interval_2))
                    break
        if not(Intervals.index(interval_1) in AlreadyMerged):
            MergedIntervals.append(interval_1)
            AlreadyMerged.append(Intervals.index(interval_1))
    for merginterval_1 in MergedIntervals:
        for merginterval_2 in MergedIntervals:
            if (merginterval_1[0] > merginterval_2[0]) and (merginterval_1[0] < merginterval_2[1]):
                return merging(MergedIntervals)
            if (merginterval_1[1] > merginterval_2[0]) and (merginterval_1[1] < merginterval_2[1]):
                return merging(MergedIntervals)
            if ((merginterval_1[0] == merginterval_2[0]) or (merginterval_1[1] == merginterval_2[0]) or (merginterval_1[0] == merginterval_2[1]) or (merginterval_1[1] == merginterval_2[1])) and (Intervals.index(interval_1) != Intervals.index(interval_2)):
                return merging(MergedIntervals)
    return MergedIntervals
 ```
# Non-overlapping Intervals

Problem 435. <a href="https://leetcode.com/problems/non-overlapping-intervals/">Link to the page </a>

``` python 
 def eraseOverlapIntervals(self, Intervals) -> int:
    Num_of_deleted = 0
    max_num = [0,-1]
    IfOverlap = False
    Num_of_overs = [0]*len(Intervals)
    for interval_1 in Intervals:
        for interval_2 in Intervals:
            if (interval_1[0] == interval_2[0]) and (interval_1[1] == interval_2[1]):
                Num_of_overs[Intervals.index(interval_1)] += 1
            elif (interval_1[0] > interval_2[0]) and (interval_1[0] < interval_2[1]):
                Num_of_overs[Intervals.index(interval_1)] += 1
            elif (interval_1[1] > interval_2[0]) and (interval_1[1] < interval_2[1]):
                Num_of_overs[Intervals.index(interval_1)] += 1
            elif (interval_2[0] > interval_1[0]) and (interval_2[0] < interval_1[1]):
                Num_of_overs[Intervals.index(interval_1)] += 1
            elif (interval_2[1] > interval_1[0]) and (interval_2[1] < interval_1[1]):
                Num_of_overs[Intervals.index(interval_1)] += 1
    for num in Num_of_overs:
        num -= 1 
        if num > 0:
            IfOverlap = True    
    while IfOverlap == True:
        for num in Num_of_overs:
            if num > max_num[0]:
                max_num[0] = num
                max_num[1] = Num_of_overs.index(num)
        del Num_of_overs[max_num[1]]
        del Intervals[max_num[1]]
        max_num = [0,-1]
        Num_of_deleted += 1
        Num_of_overs = [0]*len(Intervals)
        IfOverlap = False
        for interval_1 in Intervals:
            for interval_2 in Intervals:
                if (interval_1[0] == interval_2[0]) and (interval_1[1] == interval_2[1]):
                    Num_of_overs[Intervals.index(interval_1)] += 1
                elif (interval_1[0] > interval_2[0]) and (interval_1[0] < interval_2[1]):
                    Num_of_overs[Intervals.index(interval_1)] += 1
                elif (interval_1[1] > interval_2[0]) and (interval_1[1] < interval_2[1]):
                    Num_of_overs[Intervals.index(interval_1)] += 1
                elif (interval_2[0] > interval_1[0]) and (interval_2[0] < interval_1[1]):
                    Num_of_overs[Intervals.index(interval_1)] += 1
                elif (interval_2[1] > interval_1[0]) and (interval_2[1] < interval_1[1]):
                    Num_of_overs[Intervals.index(interval_1)] += 1
        for num in Num_of_overs:
            num -= 1
            if num > 0:
                IfOverlap = True        
    return(Num_of_deleted)                                                                                              
 ```
