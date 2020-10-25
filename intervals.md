# Intervals

+ [Non-overlapping Intervals](#non-overlapping-intervals)

[comment]: <> (Stop)

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

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