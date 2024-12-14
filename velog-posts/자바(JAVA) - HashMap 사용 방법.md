<p>자바의 HashMap은 <strong>키-값 쌍(Key-Value Pair)</strong>으로 데이터를 저장하고, 빠르게 키를 이용해 값을 검색해야 할 때 매우 유용한 자료구조이다. </p>
<ul>
<li>빈도 계산 (문자, 숫자 빈도 구하기)</li>
<li>빠른 검색 (특정 키를 기준으로 데이터 조회)</li>
<li>매핑 관계 (ID, 값 등 연결 저장)</li>
</ul>
<p>위와 같은 문제에서 HashMap을 사용하면 좋다.
<br /></p>
<h4 id="📌-선언-방법">📌 선언 방법</h4>
<pre><code class="language-java">Map&lt;String, String&gt; map1 = new HashMap&lt;String, String&gt;(); //HashMap 생성
Map&lt;String, String&gt; map2 = new HashMap&lt;&gt;(); //new에서 타입 파라미터 생략 가능
Map&lt;String, String&gt; map3 = new HashMap&lt;&gt;(map1); //map1의 모든 값을 가진 HashMap 생성
Map&lt;String, String&gt; map4 = new HashMap&lt;&gt;(10); //초기 용량 지정
Map&lt;String, String&gt; map5 = new HashMap&lt;&gt;(10, 0.7f); //초기 capacity, load factor 지정
Map&lt;String, String&gt; map6 = new HashMap&lt;String, String&gt;(){{ //초기값 지정
        put(&quot;a&quot;, &quot;b&quot;);
}};</code></pre>
<br />

<h4 id="📌-hashmap-메서드">📌 HashMap 메서드</h4>
<ol>
<li><p>put(K key, V value) : 키와 값을 맵에 저장. 키가 존재하면 새 값으로 대체</p>
<pre><code class="language-java">Map&lt;String, Integer&gt; map = new HashMap&lt;&gt;();
map.put(&quot;apple&quot;, 50);
map.put(&quot;banana&quot;, 30);</code></pre>
</li>
<li><p>get(Object key) : 지정된 키에 대응하는 값을 반환. 키가 없으면 null 반환</p>
<pre><code class="language-java">int price = map.get(&quot;apple&quot;); //50</code></pre>
</li>
<li><p>remove(Object key) : 키와 그에 대응하는 값을 제거</p>
<pre><code class="language-java">map.remove(&quot;banana&quot;);</code></pre>
</li>
<li><p>containsKey(Object key) : Map에 지정된 키가 존재하는지 여부를 반환</p>
<pre><code class="language-java">boolean hasApple = map.containsKey(&quot;apple&quot;); //true</code></pre>
</li>
<li><p>containsValue(Object value) : Map에 해당 값이 존재하는지 여부를 파악</p>
<pre><code class="language-java">boolean hasPrice50 = map.containsValue(50); //true</code></pre>
</li>
<li><p>keySet() : Map의 모든 키(key)를 set으로 반환</p>
<pre><code class="language-java">Map&lt;String, Integer&gt; map = new HashMap&lt;&gt;();
map.put(&quot;Alice&quot;, 25);
map.put(&quot;Bob&quot;, 30);
map.put(&quot;Charlie&quot;, 35);
</code></pre>
</li>
</ol>
<p>//모든 키 가져오기
Set keys = map.keySet();</p>
<p>//키 출력
for(String key : keys){
    System.out.println(&quot;Key: &quot; + key);
}</p>
<p>//결과
Key: Alice
Key: Bob
Key: Charlie</p>
<pre><code>
7. values() : 모든 값을 컬렉션 형태로 반환
```java
Map&lt;String, Integer&gt; map = new HashMap&lt;&gt;();
map.put(&quot;Alice&quot;, 25);
map.put(&quot;Bob&quot;, 30);
map.put(&quot;Charlie&quot;, 35);

// 모든 값 가져오기
Collection&lt;Integer&gt; values = map.values();

// 값 출력
for (Integer value : values) {
    System.out.println(&quot;Value: &quot; + value);
}

//결과
Value: 25
Value: 30
Value: 35</code></pre><ol start="8">
<li><p>entrySet() : Map의 모든 키-값을 꺼내야 할 때</p>
<pre><code class="language-java">for(Map.Entry&lt;String, Integer&gt; entry : map.entrySet()){
 System.out.println(entry.getKey() + &quot;: &quot; + entry.getValue());
}</code></pre>
</li>
<li><p>size() : Map에 저장된 키-값 쌍의 개수를 반환</p>
<pre><code class="language-java">int size = map.size();</code></pre>
</li>
<li><p>clear() : Map에 저장된 모든 것을 지울 때</p>
<pre><code class="language-java">map.clear();</code></pre>
</li>
<li><p>getOrDefault(Object key, V defaultValue) : 키에 대응하는 값을 반환하고, 키가 존재하지 않는다면 defaultValue 값을 반환</p>
<pre><code class="language-java">int price = map.getOrDefault(&quot;orange&quot;, 10); //없으면 10, 있으면 그 값을 반환</code></pre>
</li>
<li><p>replace(K key, V value) : Map에 지정된 key가 있으면 그에 대응하는 값으로 대체</p>
<pre><code class="language-java">map.replace(&quot;apple&quot;, 70);</code></pre>
</li>
</ol>