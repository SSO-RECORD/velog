<h4 id="💡-주요-mysql-수학-함수">💡 주요 MySQL 수학 함수</h4>
<br />

<h5 id="1-abs숫자">1. ABS(숫자)</h5>
<h5 id="-숫자의-절댓값을-반환">: 숫자의 절댓값을 반환</h5>
<pre><code class="language-SQL">ABS(-10) --- 10 반환</code></pre>
<br />

<h5 id="2-ceiling숫자--ceil숫자">2. CEILING(숫자) / CEIL(숫자)</h5>
<h5 id="-주어진-숫자를-올림하여-가장-큰-정수를-반환">: 주어진 숫자를 올림하여 가장 큰 정수를 반환</h5>
<pre><code class="language-SQL">CEILING(3.14) --- 4 반환</code></pre>
<br />

<h5 id="3-floor숫자">3. FLOOR(숫자)</h5>
<h5 id="-주어진-숫자를-내림하여-가장-작은-정수를-반환">: 주어진 숫자를 내림하여 가장 작은 정수를 반환</h5>
<pre><code class="language-SQL">FLOOR(3.14) --- 3 반환</code></pre>
<br />

<h5 id="4-round숫자-자리수">4. ROUND(숫자, [자리수])</h5>
<h5 id="-주어진-숫자를-지정된-자리수만큼-반올림">: 주어진 숫자를 지정된 자리수만큼 반올림</h5>
<pre><code class="language-SQL">ROUND(3.14159, 2) --- 3.14 반환</code></pre>
<br />

<h5 id="5-sqrt숫자">5. SQRT(숫자)</h5>
<h5 id="-숫자의-제곱근을-반환">: 숫자의 제곱근을 반환</h5>
<pre><code class="language-SQL">SQRT(16) --- 4 반환</code></pre>
<br />

<h5 id="6-mod숫자1-숫자2">6. MOD(숫자1, 숫자2)</h5>
<h5 id="-숫자1을-숫자2로-나눈-나머지를-반환">: 숫자1을 숫자2로 나눈 나머지를 반환</h5>
<pre><code class="language-SQL">MOD(10, 3) --- 1 반환</code></pre>
<br />

<h5 id="7-sign숫자">7. SIGN(숫자)</h5>
<h5 id="-숫자의-부호를-반환-양수면-1-음수면--1-0이면-0을-반환">: 숫자의 부호를 반환. 양수면 1, 음수면 -1, 0이면 0을 반환</h5>