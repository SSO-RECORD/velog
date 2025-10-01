<h3 id="🔎-문제-링크">🔎 문제 링크</h3>
<p><a href="https://school.programmers.co.kr/learn/courses/30/lessons/178871">https://school.programmers.co.kr/learn/courses/30/lessons/178871</a>
<br /></p>
<h3 id="🔎-문제-설명">🔎 문제 설명</h3>
<blockquote>
</blockquote>
<p>얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 예를 들어 1등부터 3등까지 &quot;mumu&quot;, &quot;soe&quot;, &quot;poe&quot; 선수들이 순서대로 달리고 있을 때, 해설진이 &quot;soe&quot;선수를 불렀다면 2등인 &quot;soe&quot; 선수가 1등인 &quot;mumu&quot; 선수를 추월했다는 것입니다. 즉 &quot;soe&quot; 선수가 1등, &quot;mumu&quot; 선수가 2등으로 바뀝니다.
선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.</p>
<h4 id="제한사항">제한사항</h4>
<ul>
<li>5 ≤ players의 길이 ≤ 50,000<ul>
<li>players[i]는 i번째 선수의 이름을 의미합니다.</li>
<li>players의 원소들은 알파벳 소문자로만 이루어져 있습니다.</li>
<li>players에는 중복된 값이 들어가 있지 않습니다.</li>
<li>3 ≤ players[i]의 길이 ≤ 10</li>
</ul>
</li>
<li>2 ≤ callings의 길이 ≤ 1,000,000<ul>
<li>callings는 players의 원소들로만 이루어져 있습니다.</li>
<li>경주 진행중 1등인 선수의 이름은 불리지 않습니다.<h4 id="입출력-예">입출력 예</h4>
<table>
<thead>
<tr>
<th align="center">players</th>
<th align="center">callings</th>
<th align="center">result</th>
</tr>
</thead>
<tbody><tr>
<td align="center">[&quot;mumu&quot;, &quot;soe&quot;, &quot;poe&quot;, &quot;kai&quot;, &quot;mine&quot;]</td>
<td align="center">[&quot;kai&quot;, &quot;kai&quot;, &quot;mine&quot;, &quot;mine&quot;]</td>
<td align="center">[&quot;mumu&quot;, &quot;kai&quot;, &quot;mine&quot;, &quot;soe&quot;, &quot;poe&quot;]</td>
</tr>
</tbody></table>
</li>
</ul>
</li>
</ul>
<br />

<h3 id="🔎-나의-문제-풀이">🔎 나의 문제 풀이</h3>
<p>처음에는 for문을 사용해 callings 배열의 요소에 접근하면서, Java의 indexOf() 메서드(리스트에서만 사용 가능)를 통해 이름이 불린 선수의 인덱스를 찾아 바로 앞 사람과 자리를 바꾸는 방식으로 문제를 풀었다.</p>
<p>하지만 이렇게 풀면 시간초과가 발생했다.
for문은 O(n)이고, indexOf() 메서드 역시 내부적으로 순차 탐색을 수행하므로 O(m)의 시간이 걸려 전체 ** 시간 복잡도가 O(n × m) **이 됐기 때문이다.</p>
<p>그래서 키를 이용해 값을 빠르게 검색할 수 있는 자료구조인 ** Map **을 사용하는 방식으로 변경했다.
이렇게 하면 이름을 키로 사용해 인덱스를 빠르게 찾을 수 있어 성능 문제를 해결할 수 있었다.</p>
<br />

<h3 id="🔎-소스코드">🔎 소스코드</h3>
<pre><code class="language-java">import java.io.*;
import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {

        Map&lt;String, Integer&gt; playersMap = new HashMap&lt;&gt;();
        for(int i=0; i&lt;players.length; i++) {
            playersMap.put(players[i], i);
        }

        for(int i=0; i&lt;callings.length; i++){
            String name = callings[i];
            int index = playersMap.get(name);
            String temp = players[index-1];
            players[index-1] = name;
            players[index] = temp;
            playersMap.put(name, index-1);
            playersMap.put(temp, index);
        }

        return players;
    }
}</code></pre>
<br />

<h3 id="❕-느낀-점">❕ 느낀 점</h3>
<p>검색 시 시간복잡도를 줄이기 위해서 map을 사용하는 걸 잊지 말자!</p>