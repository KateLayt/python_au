<h2> Intervals

---

<h5> Задача 1. <font size = "2"><a href="https://leetcode.com/problems/non-overlapping-intervals/">Ссылка на условие </a></font><br><br></h5> 

<pre>
<font color="grey"># -*- coding: utf-8 -*-</font><br>
<font color="blue">def</font> <b>eraseOverlapIntervals</b>():<br>
    <font color="blue">print</font>(<font color="green">'Введите массив интервалов:'</font>)<br>
    Intervals =[]<br>
    a = <font color="darkred">0</font><br>
    b = <font color="darkred">0</font><br>
    StrIntervals = input()<br>
    StrIntervals = StrIntervals[<font color="darkred">2</font> : len(StrIntervals) - <font color="darkred">2</font>].replace('[', ' ').replace(']', ' ').split(' , ')<br>
    <font color="blue">for</font> pairs <font color="blue">in</font> StrIntervals:<br>
        a, b = (pairs.split(','))<br>
        Intervals.append([int(a),int(b)])<br>
    Num_of_deleted = <font color="darkred">0</font><br>
    max_num = [<font color="darkred">0</font>,<font color="darkred">-1</font>]<br>
    IfOverlap = <font color="blue">False</font><br>
    <font color="blue">for</font> interval <font color="blue">in</font> Intervals:<br>
        if interval[<font color="darkred">0</font>] > interval[<font color="darkred">1</font>]:<br>
            <font color="blue">print</font>(<font color="green">'Некорректно введён интервал '</font>, interval)<br>
            <font color="blue">return</font>(<font color="darkred">-1</font>)<br>
    Num_of_overs = [<font color="darkred">0</font>]*len(Intervals)<br>
    <font color="blue">for</font> interval_1 <font color="blue">in</font> Intervals:<br>
        <font color="blue">for</font> interval_2 <font color="blue">in</font> Intervals:<br>
            <font color="blue">if</font> (interval_1[<font color="darkred">0</font>] == interval_2[<font color="darkred">0</font>]) <font color="blue">and</font> (interval_1[<font color="darkred">1</font>] == interval_2[<font color="darkred">1</font>]):<br>
                Num_of_overs[Intervals.index(interval_1)] += <font color="darkred">1</font><br>
            <font color="blue">elif</font> (interval_1[<font color="darkred">0</font>] > interval_2[<font color="darkred">0</font>]) <font color="blue">and</font> (interval_1[<font color="darkred">0</font>] < interval_2[<font color="darkred">1</font>]):<br>
                Num_of_overs[Intervals.index(interval_1)] += <font color="darkred">1</font><br>
            <font color="blue">elif</font> (interval_1[<font color="darkred">1</font>] > interval_2[<font color="darkred">0</font>]) <font color="blue">and</font> (interval_1[<font color="darkred">1</font>] < interval_2[<font color="darkred">1</font>]):<br>
                Num_of_overs[Intervals.index(interval_1)] += <font color="darkred">1</font><br>
            <font color="blue">elif</font> (interval_2[<font color="darkred">0</font>] > interval_1[<font color="darkred">0</font>]) <font color="blue">and</font> (interval_2[<font color="darkred">0</font>] < interval_1[<font color="darkred">1</font>]):<br>
                Num_of_overs[Intervals.index(interval_1)] += <font color="darkred">1</font><br>
            <font color="blue">elif</font> (interval_2[<font color="darkred">1</font>] > interval_1[<font color="darkred">0</font>]) <font color="blue">and</font> (interval_2[<font color="darkred">1</font>] < interval_1[<font color="darkred">1</font>]):<br>
                Num_of_overs[Intervals.index(interval_1)] += <font color="darkred">1</font><br>
    <font color="blue">for</font> num <font color="blue">in</font> Num_of_overs:<br>
        num -= <font color="darkred">1</font><br>
        <font color="blue">if</font> num > <font color="darkred">0</font>:<br>
            IfOverlap = <font color="blue">True</font><br>  
    <font color="blue">while</font> IfOverlap == <font color="blue">True</font>:<br>
        <font color="blue">for</font> num <font color="blue">in</font> Num_of_overs:<br>
            <font color="blue">if</font> num > max_num[<font color="darkred">0</font>]:<br>
                max_num[<font color="darkred">0</font>] = num<br>
                max_num[<font color="darkred">1</font>] = Num_of_overs.index(num)<br>
        <font color="blue">del</font> Num_of_overs[max_num[<font color="darkred">1</font>]]<br>
        <font color="blue">del</font> Intervals[max_num[<font color="darkred">1</font>]]<br>
        max_num = [<font color="darkred">0</font>,<font color="darkred">-1</font>]<br>
        Num_of_deleted += <font color="darkred">1</font><br>
        Num_of_overs = [<font color="darkred">0</font>]*len(Intervals)<br>
        IfOverlap = <font color="blue">False</font><br>
        <font color="blue">for</font> interval_1 <font color="blue">in</font> Intervals:<br>
            <font color="blue">for</font> interval_2 <font color="blue">in</font> Intervals:<br>
                <font color="blue">if</font> (interval_1[<font color="darkred">0</font>] == interval_2[<font color="darkred">0</font>]) <font color="blue">and</font> (interval_1[<font color="darkred">1</font>] == interval_2[<font color="darkred">1</font>]):<br>
                    Num_of_overs[Intervals.index(interval_1)] += <font color="darkred">1</font><br>
                <font color="blue">elif</font> (interval_1[<font color="darkred">0</font>] > interval_2[<font color="darkred">0</font>]) <font color="blue">and</font> (interval_1[<font color="darkred">0</font>] < interval_2[<font color="darkred">1</font>]):<br>
                    Num_of_overs[Intervals.index(interval_1)] += <font color="darkred">1</font><br>
                <font color="blue">elif</font> (interval_1[<font color="darkred">1</font>] > interval_2[<font color="darkred">0</font>]) <font color="blue">and</font> (interval_1[<font color="darkred">1</font>] < interval_2[<font color="darkred">1</font>]):<br>
                    Num_of_overs[Intervals.index(interval_1)] += <font color="darkred">1</font><br>
                <font color="blue">elif</font> (interval_2[<font color="darkred">0</font>] > interval_1[<font color="darkred">0</font>]) <font color="blue">and</font> (interval_2[<font color="darkred">0</font>] < interval_1[<font color="darkred">1</font>]):<br>
                    Num_of_overs[Intervals.index(interval_1)] += <font color="darkred">1</font><br>
                <font color="blue">elif</font> (interval_2[<font color="darkred">1</font>] > interval_1[<font color="darkred">0</font>]) <font color="blue">and</font> (interval_2[<font color="darkred">1</font>] < interval_1[<font color="darkred">1</font>]):<br>
                    Num_of_overs[Intervals.index(interval_1)] += <font color="darkred">1</font><br>
        <font color="blue">for</font> num <font color="blue">in</font> Num_of_overs:<br>
            num -= <font color="darkred">1</font><br>
            <font color="blue">if</font> num > <font color="darkred">0</font>:<br>
                IfOverlap = <font color="blue">True</font><br>   
    <font color="blue">return</font>(Num_of_deleted)<br>
<font color="blue">print</font>(eraseOverlapIntervals())
</pre>

---

<h5> Задача 2. <font size = "2"><a href="https://leetcode.com/problems/merge-intervals/">Ссылка на условие </a></font><br><br></h5> 
<pre>
<font color="grey"># -*- coding: utf-8 -*-</font><br>
<font color="blue">def</font> <b>merged</b>():<br>
    <font color="blue">print</font>(<font color="green">'Введите массив интервалов:'</font>)<br>
    Intervals =[]<br>
    a = <font color="darkred">0</font><br>
    b = <font color="darkred">0</font><br>
    StrIntervals = input()<br>
    StrIntervals = StrIntervals[<font color="darkred">2</font> : len(StrIntervals) - <font color="darkred">2</font>].replace(<font color="green">'['</font>, <font color="green">' '</font>).replace(<font color="green">']'</font>, <font color="green">' '</font>).split(<font color="green">' , '</font>)<br>
    <font color="blue">for</font> pairs <font color="blue">in</font> StrIntervals:<br>
        a, b = (pairs.split(<font color="green">','</font>))<br>
        Intervals.append([int(a),int(b)])<br>
    <font color="blue">for</font> interval <font color="blue">in</font> Intervals:<br>
        <font color="blue">if</font> interval[<font color="darkred">0</font>] > interval[<font color="darkred">1</font>]:<br>
            <font color="blue">print</font>(<font color="green">'Некорректно введён интервал '</font>, interval)<br>
            <font color="blue">return</font>(<font color="darkred">-1</font>)<br>
    <font color="blue">def</font> <b>merging</b>(Intervals):<br>
        MergedIntervals = []<br>
        AlreadyMerged = []<br>
        <font color="blue">for</font> interval_1 <font color="blue">in</font> Intervals:<br>
            <font color="blue">if</font> Intervals.index(interval_1) <font color="blue">in</font> AlreadyMerged:<br>
                <font color="blue">continue</font><br>
            <font color="blue">for</font> interval_2 <font color="blue">in</font> Intervals:<br>
                <font color="blue">if</font> Intervals.index(interval_2) <font color="blue">in</font> AlreadyMerged:<br>
                    <font color="blue">continue</font><br>
                <font color="blue">if</font> (interval_1[<font color="darkred">0</font>] == interval_2[<font color="darkred">0</font>]) <font color="blue">and</font> (interval_1[<font color="darkred">1</font>] == interval_2[<font color="darkred">1</font>]) <font color="blue">and</font> (Intervals.index(interval_1) != Intervals.index(interval_2)) <font color="blue">and not</font> (interval_2 <font color="blue">in</font> MergedIntervals):<br>
                    MergedIntervals.append(interval_1)<br>
                    AlreadyMerged.append(Intervals.index(interval_1))<br>
                    AlreadyMerged.append(Intervals.index(interval_2))<br>
                    <font color="blue">break</font><br>
                <font color="blue">elif</font> (interval_1[<font color="darkred">0</font>] == interval_2[<font color="darkred">1</font>]) <font color="blue">and not</font>([interval_2[<font color="darkred">0</font>],interval_1[<font color="darkred">1</font>]] <font color="blue">in</font> MergedIntervals):<br>
                    MergedIntervals.append([interval_2[<font color="darkred">0</font>], interval_1[<font color="darkred">1</font>]])<br>
                    AlreadyMerged.append(Intervals.index(interval_1))<br>
                    AlreadyMerged.append(Intervals.index(interval_2))<br>
                    <font color="blue">break</font><br>
                <font color="blue">elif</font> (interval_1[<font color="darkred">1</font>] == interval_2[<font color="darkred">0</font>]) <font color="blue">and not</font>([interval_1[<font color="darkred">0</font>],interval_2[<font color="darkred">1</font>]] <font color="blue">in</font> MergedIntervals):<br>
                    MergedIntervals.append([interval_1[<font color="darkred">0</font>], interval_2[<font color="darkred">1</font>]])<br>
                    AlreadyMerged.append(Intervals.index(interval_1))<br>
                    AlreadyMerged.append(Intervals.index(interval_2))<br>
                    <font color="blue">break</font><br>
                <font color="blue">elif</font> (interval_1[<font color="darkred">0</font>] > interval_2[<font color="darkred">0</font>]) <font color="blue">and</font> (interval_1[<font color="darkred">0</font>] < interval_2[<font color="darkred">1</font>]):<br>
                    <font color="blue">if</font> (interval_1[<font color="darkred">1</font>] <= interval_2[<font color="darkred">1</font>]) <font color="blue">and not</font>(interval_2 <font color="blue">in</font> MergedIntervals):<br>
                        MergedIntervals.append(interval_2) <br>
                        AlreadyMerged.append(Intervals.index(interval_1))<br>
                        AlreadyMerged.append(Intervals.index(interval_2))<br>
                        <font color="blue">break</font><br>
                    <font color="blue">if</font> (interval_1[<font color="darkred">1</font>] > interval_2[<font color="darkred">1</font>]) <font color="blue">and not</font>([interval_2[<font color="darkred">0</font>], interval_1[<font color="darkred">1</font>]] <font color="blue">in</font> MergedIntervals):<br>
                        MergedIntervals.append([interval_2[<font color="darkred">0</font>], interval_1[<font color="darkred">1</font>]]) <br> 
                        AlreadyMerged.append(Intervals.index(interval_1))<br>
                        AlreadyMerged.append(Intervals.index(interval_2))<br>
                        <font color="blue">break</font><br>
                <font color="blue">elif</font> (interval_1[<font color="darkred">1</font>] > interval_2[<font color="darkred">0</font>]) <font color="blue">and</font> (interval_1[<font color="darkred">1</font>] < interval_2[<font color="darkred">1</font>]):<br>
                    <font color="blue">if</font> interval_1[<font color="darkred">0</font>] >= interval_2[<font color="darkred">0</font>] <font color="blue">and not</font>(interval_2 <font color="blue">in</font> MergedIntervals):<br>
                        MergedIntervals.append(interval_2) <br>
                        AlreadyMerged.append(Intervals.index(interval_1))<br>
                        AlreadyMerged.append(Intervals.index(interval_2))<br>
                        <font color="blue">break</font><br>
                    <font color="blue">if</font> (interval_1[<font color="darkred">0</font>] < interval_2[<font color="darkred">0</font>]) <font color="blue">and not</font>([interval_1[<font color="darkred">0</font>],interval_2[<font color="darkred">1</font>]] <font color="blue">in</font> MergedIntervals):<br>
                        MergedIntervals.append([interval_1[<font color="darkred">0</font>],interval_2[<font color="darkred">1</font>]]) <br>
                        AlreadyMerged.append(Intervals.index(interval_1))<br>
                        AlreadyMerged.append(Intervals.index(interval_2))<br>
                        <font color="blue">break</font><br>
            <font color="blue">if not</font>(Intervals.index(interval_1) <font color="blue">in</font> AlreadyMerged):<br>
                MergedIntervals.append(interval_1)<br>
                AlreadyMerged.append(Intervals.index(interval_1))<br>
        <font color="blue">for</font> merginterval_1 <font color="blue">in</font> MergedIntervals:<br>
            <font color="blue">for</font> merginterval_2 <font color="blue">in</font> MergedIntervals:<br>
                <font color="blue">if</font> (merginterval_1[<font color="darkred">0</font>] > merginterval_2[<font color="darkred">0</font>]) <font color="blue">and</font> (merginterval_1[<font color="darkred">0</font>] < merginterval_2[<font color="darkred">1</font>]):<br>
                    <font color="blue">return</font> merging(MergedIntervals)<br>
                <font color="blue">if</font> (merginterval_1[<font color="darkred">1</font>] > merginterval_2[<font color="darkred">0</font>]) <font color="blue">and</font> (merginterval_1[<font color="darkred">1</font>] < merginterval_2[<font color="darkred">1</font>]):<br>
                    <font color="blue">return</font> merging(MergedIntervals)<br>
                <font color="blue">if</font> ((merginterval_1[<font color="darkred">0</font>] == merginterval_2[<font color="darkred">0</font>]) <font color="blue">or</font> (merginterval_1[<font color="darkred">1</font>] == merginterval_2[<font color="darkred">0</font>]) <font color="blue">or</font> (merginterval_1[<font color="darkred">0</font>] == merginterval_2[<font color="darkred">1</font>]) <font color="blue">or</font> (merginterval_1[<font color="darkred">1</font>] == merginterval_2[<font color="darkred">1</font>])) <font color="blue">and</font> (Intervals.index(interval_1) != Intervals.index(interval_2)):<br>
                    <font color="blue">return</font> merging(MergedIntervals)<br>
        <font color="blue">return</font> MergedIntervals<br>
    <font color="blue">return</font> merging(Intervals)<br>
<font color="blue">print</font>(merged())
</pre>

---

<h5> Задача 3. <font size = "2"><a href="https://leetcode.com/problems/insert-interval/">Ссылка на условие </a></font><br><br></h5>

<pre>
<font color="grey"># -*- coding: utf-8 -*-</font><br>
<font color="blue">def</font> <b>insert</b>():<br>
    <font color="blue">print</font>(<font color="green">'Введите массив интервалов:'</font>)<br>
    Intervals = []<br>
    a = <font color="darkred">0</font><br>
    b = <font color="darkred">0</font><br>
    StrIntervals = input()<br>
    StrIntervals = StrIntervals[<font color="darkred">2</font> : len(StrIntervals) - <font color="darkred">2</font>].replace(<font color="green">'['</font>, <font color="green">' '</font>).replace(<font color="green">']'</font>, <font color="green">' '</font>).split(<font color="green">' , '</font>)<br>
    <font color="blue">for</font> pairs <font color="blue">in</font> StrIntervals:<br>
        a, b = (pairs.split(<font color="green">','</font>))<br>
        Intervals.append([int(a),int(b)])<br>
    <font color="blue">for</font> interval <font color="blue">in</font> Intervals:<br>
        <font color="blue">if</font> interval[<font color="darkred">0</font>] > interval[<font color="darkred">1</font>]:<br>
            <font color="blue">print</font>(<font color="green">'Некорректно введён интервал '</font>, interval)<br>
            <font color="blue">return</font>(<font color="darkred">-1</font>)<br>
    <font color="blue">print</font>(<font color="green">'Введите новый интервал: '</font>)<br>
    NewInterval = input()<br>
    NewInterval = NewInterval[<font color="darkred">1</font> : len(NewInterval) - <font color="darkred">1</font>].split(<font color="green">','</font>)<br>
    NewInterval[<font color="darkred">0</font>] = int(NewInterval[<font color="darkred">0</font>])<br>
    NewInterval[<font color="darkred">1</font>] = int(NewInterval[<font color="darkred">1</font>])<br>
    New_Intervals = []<br>
    ShallBeRemoved = []<br>
    <font color="blue">for</font> interval <font color="blue">in</font> Intervals:<br>
        <font color="blue">if</font> (interval[<font color="darkred">0</font>] <= NewInterval[<font color="darkred">0</font>]) <font color="blue">and</font> (NewInterval[<font color="darkred">1</font>] <= interval[<font color="darkred">1</font>]):<br>
            NewInterval = interval<br>
            ShallBeRemoved.append(interval)<br>
        <font color="blue">elif</font> (NewInterval[<font color="darkred">0</font>] <= interval[<font color="darkred">0</font>]) <font color="blue">and</font> (interval[<font color="darkred">1</font>] <= NewInterval[<font color="darkred">1</font>]):<br>
            ShallBeRemoved.append(interval)<br>
        <font color="blue">elif</font> (interval[<font color="darkred">0</font>] == NewInterval[<font color="darkred">1</font>]):<br>
            NewInterval = [NewInterval[<font color="darkred">0</font>], interval[<font color="darkred">1</font>]]<br>
            ShallBeRemoved.append(interval)<br>
        <font color="blue">elif</font> (interval[<font color="darkred">1</font>] == NewInterval[<font color="darkred">0</font>]):<br>
            NewInterval = [NewInterval[<font color="darkred">1</font>], interval[<font color="darkred">0</font>]]<br>
            ShallBeRemoved.append(interval)<br>
        <font color="blue">elif</font> (interval[<font color="darkred">0</font>] > NewInterval[<font color="darkred">0</font>]) <font color="blue">and</font> (interval[<font color="darkred">0</font>] < NewInterval[<font color="darkred">1</font>]):<br>
            NewInterval = [NewInterval[<font color="darkred">0</font>], interval[<font color="darkred">1</font>]]<br>
            ShallBeRemoved.append(interval)<br>
        <font color="blue">elif</font> (interval[<font color="darkred">1</font>] > NewInterval[<font color="darkred">0</font>]) <font color="blue">and</font> (interval[<font color="darkred">1</font>] < NewInterval[<font color="darkred">1</font>]):<br>
            NewInterval = [interval[<font color="darkred">0</font>], NewInterval[<font color="darkred">1</font>]]<br>
            ShallBeRemoved.append(interval)<br>
    <font color="blue">for</font> interval <font color="blue">in</font> ShallBeRemoved:<br>
        Intervals.remove(interval)<br>   
    <font color="blue">if</font> len(Intervals) == <font color="darkred">0</font>:<br>
        <font color="blue">return</font>([NewInterval])<br>
    New_Intervals.append(NewInterval)<br>
    New_Intervals += Intervals<br>
    New_Intervals = sorted(New_Intervals)<br>
    <font color="blue">return</font>(New_Intervals)<br>
<font color="blue">print</font>(insert())
</pre>
