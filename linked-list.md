<h2> Linked list

---

<h5> Задача 1. <font size = "2"><a href="https://leetcode.com/problems/reverse-linked-list/">Ссылка на условие </a></font><br><br></h5> 
<pre>
<font color="blue">def</font> <b>reverseList</b>():<br>
    List = <font color="blue">input</font>().<font color="blue">split</font>(<font color="green">'->'</font>)<br>
    <font color="blue">del</font> List[<font color="darkred">-1</font>]<br>
    ReversedList = <font color="green">''</font><br>
    <font color="blue">for</font> index <font color="blue">in</font> range(len(List) <font color="darkred">-1</font>,<font color="darkred">-1</font>,<font color="darkred">-1</font>):<br>
        ReversedList += List[index] + <font color="green">'->'</font><br>
    <font color="blue">return</font>(ReversedList + <font color="green">'NULL'</font>)<br>
<font color="blue">print</font>(reverseList())
</pre>

---

<h5> Задача 2. <font size = "2"><a href="https://leetcode.com/problems/middle-of-the-linked-list/">Ссылка на условие </a></font><br><br></h5> 
<pre>
<font color="blue">def</font> <b>middleNode</b>():<br>
    List = input()<br>
    nodelist = []<br>
    List = List[<font color="darkred">1</font> : len(List) - <font color="darkred">1</font>].split(<font color="green">','</font>)<br>
    node = int(len(List)/<font color="darkred">2</font> + (len(List)%<font color="darkred">2</font>)*<font color="darkred">0.5</font>)<br>
    <font color="blue">if</font> len(List)%<font color="darkred">2</font> == <font color="darkred">0</font> :<br>
        <font color="blue">for</font> index <font color="blue">in</font> range(node, len(List)):<br>
            nodelist.append(int(List[index]))<br>
    <font color="blue">else</font>:<br>
        <font color="blue">for</font> index <font color="blue">in</font> range(node - <font color="darkred">1</font>, len(List)):<br>
            nodelist.append(int(List[index]))<br>
    string =<font color="green">'Node {} from this list (Serialization: {})'</font><br>
    <font color="blue">return</font>(string.format(node, nodelist))<br>
<font color="blue">print</font>(middleNode())<br>
</pre>

---

<h5> Задача 3. <font size = "2"><a href="https://leetcode.com/problems/merge-two-sorted-lists/">Ссылка на условие </a></font><br><br></h5>
<pre>
<font color="blue">def</font> <b>isPalindrome</b>():<br>
    string = input().split(<font color="green">'->'</font>)<br>
    Is = True<br>
    <font color="blue">for</font> i <font color="blue">in</font> range(len(string)):<br>
        <font color="blue">if</font> string[i] != string[len(string) - i - <font color="darkred">1</font>]:<br>
            Is = False<br>
    <font color="blue">return</font>(Is)<br>
<font color="blue">print</font>(isPalindrome())
</pre>

---

<h5> Задача 5. <font size = "2"><a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/">Ссылка на условие </a></font><br><br></h5>

<pre>
<font color="blue">def</font> <b>removeNthFromEnd</b>():<br>
    List = input().split(<font color="green">'->'</font>)<br>
    n = int(input())<br>
    <font color="blue">del</font> List[-n]<br>
    NewList = <font color="green">''</font><br>
    <font color="blue">for</font> i <font color="blue">in</font> range(len(List)):<br>
        <font color="blue">if</font> i != len(List) - <font color="darkred">1</font>:<br>
            NewList += List[i] + <font color="green">'->'</font><br>
        <font color="blue">else</font>:<br>
            NewList += List[i]<br>
    <font color="blue">return</font>(NewList)<br>
<font color="blue">print</font>(removeNthFromEnd())<br>
</pre>

---

<h5> Задача 8. <font size = "2"><a href="https://leetcode.com/problems/reorder-list/">Ссылка на условие </a></font><br><br></h5> 
<pre>
<font color="blue"> def </font> <b>reorderList</b>(): <br>
    List = input().split(<font color="green">'->'</font>)<br>
    NewList = <font color="green">''</font><br>
    <font color="blue">if</font> len(List)%<font color="darkred">2</font> == <font color="darkred">0</font>:<br>
        <font color="blue">for</font> <font color="blue">i</font> in range(len(List)//<font color="darkred">2</font>):<br>
            <font color="blue">if</font> i == len(List)//<font color="darkred">2</font> - <font color="darkred">1</font>:<br>
                NewList += List[i] + <font color="green">'->'</font> + List[len(List) - i - <font color="darkred">1</font>]<br>
            <font color="blue">else:</font><br>
                NewList += List[i] + <font color="green">'->'</font> + List[len(List) - i - <font color="darkred">1</font>] + <font color="green">'->'</font><br>
    <font color="blue">else:</font><br>
        <font color="blue">for</font> i <font color="blue">in</font> range(len(List)//<font color="darkred">2</font> + <font color="darkred">1</font>):<br>
            <font color="blue">if</font> i == len(List)//<font color="darkred">2</font>:<br>
                NewList += List[i]<br>
            <font color="blue">else</font>:<br>
                NewList += List[i] + <font color="green">'->'</font> + List[len(List) - i - <font color="darkred">1</font>] + <font color="green">'->'</font><br>
    <font color="blue">return</font>(NewList)<br>
<font color="blue">print</font>(reorderList())<br>
</pre>

---