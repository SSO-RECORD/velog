<h3 id="mysql-datetime-형식-변경하는-방법">MYSQL DATETIME 형식 변경하는 방법</h3>
<hr />

<h4 id="💡-date_format-함수-사용">💡 DATE_FORMAT() 함수 사용</h4>
<pre><code class="language-SQL">DATE_FORMAT(컬럼명, &quot;원하는 형식&quot;)</code></pre>
<h5 id="--원하는-형식에-따라-출력-값이-달라진다">- &quot;원하는 형식&quot;에 따라 출력 값이 달라진다</h5>
<pre><code class="language-SQL">DATE_FORMAT(컬럼명, &quot;%Y-%M-%D)  # 2018-January-22nd

DATE_FORMAT(컬럼명, &quot;%y-%M-%D)  # 18-January-22nd

DATE_FORMAT(컬럼명, &quot;%Y-%m-%D)  # 2018-01-22nd

DATE_FORMAT(컬럼명, &quot;%Y-%m-%d)  # 2018-01-22</code></pre>