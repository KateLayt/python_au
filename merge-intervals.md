# Intervals

+ [Merge Intervals](#merge-intervals)

[comment]: <> (Stop)

## Merge Intervals

https://leetcode.com/problems/merge-intervals/

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
