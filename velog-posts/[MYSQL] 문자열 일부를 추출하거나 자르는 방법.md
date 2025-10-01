<h3 id="💡-문자열-일부를-추출하거나-자르는-방법">💡 문자열 일부를 추출하거나 자르는 방법</h3>
<br />

<h4 id="1-substring-사용---원하는-길이만큼-추출">1. SUBSTRING() 사용 - 원하는 길이만큼 추출</h4>
<pre><code class="language-SQL">SUBSTRING(STR, START, LENGTH)</code></pre>
<ul>
<li>STR : '컬럼명' 혹은 '자르고 싶은 문자열'</li>
<li>START : 추출할 문자열의 시작 위치(1부터 시작)</li>
<li>LENGTH : 추출할 문자열의 길이<br />

</li>
</ul>
<h4 id="2-substr-사용---원하는-부분--부분-추출">2. SUBSTR() 사용 - 원하는 부분 ~ 부분 추출</h4>
<pre><code class="language-SQL">SUBSTR(STR, START, END)</code></pre>
<ul>
<li>STR : '컬럼명' 혹은 '자르고 싶은 문자열'</li>
<li>START : 추출할 문자열의 시작 위치(1부터 시작)</li>
<li>END : 추출할 문자열의 마지막 위치<br />

</li>
</ul>
<h4 id="3-left-사용---왼쪽부터-원하는-길이만큼-추출">3. LEFT() 사용 - 왼쪽부터 원하는 길이만큼 추출</h4>
<pre><code class="language-SQL">LEFT(STR, LENGTH)</code></pre>
<ul>
<li>STR : '컬럼명' 혹은 '자르고 싶은 문자열'</li>
<li>LENGTH : 추출할 문자열의 길이<br />

</li>
</ul>
<h4 id="4-right-사용---오른쪽부터-원하는-길이만큼-추출">4. RIGHT() 사용 - 오른쪽부터 원하는 길이만큼 추출</h4>
<pre><code class="language-SQL">RIGHT(STR, LENGTH)</code></pre>
<ul>
<li>STR : '컬럼명' 혹은 '자르고 싶은 문자열'</li>
<li>LENGTH : 추출할 문자열의 길이</li>
</ul>