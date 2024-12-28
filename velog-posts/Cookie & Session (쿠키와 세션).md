<h4 id="✔️-cookie와-session을-왜-사용하는-걸까">✔️ Cookie와 Session을 왜 사용하는 걸까?</h4>
<ul>
<li><p>http protocol의 특징</p>
<ul>
<li><p>client가 서버에 요청</p>
<ul>
<li><p>server는 요청에 대한 처리를 한 후 client에 응답</p>
</li>
<li><p>응답후 연결을 해제 &gt;&gt; <span style="color: red;"> stateless </span></p>
<ul>
<li>지속적인 연결로 인한 자원낭비를 줄이기 위해 연결을 해제한다.</li>
<li>그러나 client와 server가 연결 상태를 유지해야 하는 경우 문제가 발생(로그인 정보 등).</li>
<li>즉 client 단위로 상태 정보를 유지해야 하는 경우 Cookie와 Session이 사용된다.</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<ul>
<li>한마디로 얘기해서, HTTP protocol의 특징(약점)을 보완하기 위해 Cookie와 Session이 사용된다!!<br />
<hr />
<br />

</li>
</ul>
<h4 id="✔️-cookie">✔️ Cookie</h4>
<ul>
<li>jakarta.servlet.http.Cookie</li>
<li>서버에서 만들고 사용자의 컴퓨터에 저장하는 정보파일</li>
<li>사용자가 별도의 요청을 하지 않아도 브라우저는 request시 Request Header에 넣어 자동으로 서버에 전송</li>
<li>key와 value로 구성되고 String 형태로 이루어져 있음. =&gt; *.txt 형태로 저장됨</li>
<li>Browser마다 저장되는 쿠키는 다르다. (서버에서는 Browser가 다르면 다른 사용자로 인식)<br />

</li>
</ul>
<h4 id="✔️-cookie의-사용-목적">✔️ Cookie의 사용 목적</h4>
<ol>
<li>세션 관리 : 사용자 아이디, 접속시간, 장바구니 등의 서버가 알아야 할 정보 저장</li>
<li>개인화 : 사용자마다 다르게 그 사람에 적절한 페이지를 보여줄 수 있다.</li>
<li>트래킹 : 사용자의 행동과 패턴을 분석하고 기록<br />

</li>
</ol>
<h4 id="✔️-cookie의-종류">✔️ Cookie의 종류</h4>
<table>
<thead>
<tr>
<th align="center">쿠키 종류</th>
<th>특징</th>
</tr>
</thead>
<tbody><tr>
<td align="center">Session Cookie</td>
<td>사용자가 웹사이트를 방문할 때 생성되고, 해당 세션이 유지되는 동안에만 유효한 쿠키. 웹 브라우저 종료 시 세션 쿠키는 삭제됨. 일반적으로 로그인 상태유지, 장바구니(용도에 따라 다름)와 같이 임시 데이터 저장용으로 사용. (브라우저가 꺼지는 순간 다 날라감)</td>
</tr>
<tr>
<td align="center">Persistent Cookie</td>
<td>사용자의 컴퓨터에 저장되어 expire date(유효기간) 동안 유효한 쿠키. 웹 브라우저를 종료해도 유지. 사용자의 선호도 설정, 언어 선택, 로그인 정보 기억(아이디 저장, 자동로그인) 등에 사용. (하나의 컴퓨터에서는 계속 보임)</td>
</tr>
<tr>
<td align="center">Secure Cookie</td>
<td>HTTPS 프로토콜에서만 사용가능하며, 쿠키 정보가 암호화되어 전송됨.</td>
</tr>
<tr>
<td align="center">Third-Party Cookie</td>
<td>사용자가 방문하는 웹사이트 이외의 도메인에서 설정된 쿠키. 웹사이트의 통계, 광고 제공, 사용자 행동 분석 등의 목적으로 사용. Third-Party Cookie는 방문 웹사이트와 독립적으로 동작하며, 개인정보 보호 이슈로 인해 사용 제한이 있거나 사용자 동의를 받아야 함.</td>
</tr>
<tr>
<td align="center"><br /></td>
<td></td>
</tr>
</tbody></table>
<h4 id="✔️-cookie의-사용-예">✔️ Cookie의 사용 예</h4>
<ul>
<li><p>ID 저장(자동로그인)</p>
</li>
<li><p>일주일간 다시 보지 않기</p>
</li>
<li><p>최근 검색한 상품들을 광고에 추천</p>
</li>
<li><p>쇼핑몰 장바구니 기능</p>
<br />

</li>
</ul>
<h4 id="✔️-cookie의-구성-요소">✔️ Cookie의 구성 요소</h4>
<ul>
<li>이름 : 여러 개의 쿠키가 client의 컴퓨터에 저장되므로 각 쿠키를 구별하는데 사용되는 이름</li>
<li>값 : 쿠키의 이름과 매핑되는 값</li>
<li>유효기간 : 쿠키의 유효기간</li>
<li>도메인 : 쿠키를 전송할 도메인</li>
<li>경로(path) : 쿠키를 전송할 요청 경로<br />

</li>
</ul>
<h4 id="✔️-cookie의-동작-순서">✔️ Cookie의 동작 순서</h4>
<ul>
<li>client가 페이지를 요청</li>
<li>WAS는 Cookie를 생성</li>
<li>HTTP Header에 Cookie를 넣어 응답</li>
<li>Browser는 넘겨받은 Cookie를 PC에 저장하고, 다시 WAS가 요청할 때 요청과 함께 Cookie를 전송</li>
<li>Browser가 종료되어도 Cookie의 만료 기간이 남아 있다면 Client는 계속 보관</li>
<li>동일 사이트 재방문 시 client의 PC에 해당 Cookie가 있는 경우, 요청 페이지와 함께 Cookie를 전송<br />

</li>
</ul>
<h4 id="✔️-cookie의-특징">✔️ Cookie의 특징</h4>
<ul>
<li>이름, 값, 만료일(저장 기간 설정), 경로 정보로 구성되어 있다.</li>
<li>클라이언트에 총 50~180개의 쿠키를 저장할 수 있다. (브라우저별 차이)</li>
<li>하나의 도메인 당 20개의 쿠키를 가질 수 있다.</li>
<li>하나의 쿠키는 4KB(=4096byte)까지 저장 가능하다.<br />

</li>
</ul>
<h4 id="✔️-cookie의-주요-기능">✔️ Cookie의 주요 기능</h4>
<table>
<thead>
<tr>
<th align="center">기능</th>
<th>method</th>
</tr>
</thead>
<tbody><tr>
<td align="center">생성</td>
<td>Cookie cookie = new Cookie(String name, String value);</td>
</tr>
<tr>
<td align="center">값 변경/얻기</td>
<td>cookie.setValue(String value); / String value = cookie.getValue();</td>
</tr>
<tr>
<td align="center">사용 도메인 지정/얻기</td>
<td>cookie.setDomain(String domain); / String domain = cookie.getDomain();</td>
</tr>
<tr>
<td align="center">값 범위지정/얻기</td>
<td>cookie.setPath(String path); / String path = cookie.path();</td>
</tr>
<tr>
<td align="center">cookie의 유효기간지정/얻기</td>
<td>cookie.setMaxAge(int expiry); / int expiry = cookie.getMaxAge(); cookie 삭제 : cookie.setMaxAge(0);</td>
</tr>
<tr>
<td align="center">생성된 cookie를 client에 전송</td>
<td>response.addCookie(cookie);</td>
</tr>
<tr>
<td align="center">client에 저장된 cookie 얻기</td>
<td>Cookie cookies[] = request.getCookies();</td>
</tr>
<tr>
<td align="center"><br /></td>
<td></td>
</tr>
<tr>
<td align="center"><hr /></td>
<td></td>
</tr>
<tr>
<td align="center"><br /></td>
<td></td>
</tr>
</tbody></table>
<h4 id="✔️-session">✔️ Session</h4>
<ul>
<li>jakarta.servlet.http.HttpSession</li>
<li>방문자가 웹 서버에 접속해 있는 상태를 하나의 단위로 보고 그것을 세션이라 한다.</li>
<li>WAS의 memory에 Object 형태로 저장</li>
<li>memory가 허용하는 용량까지 제한 없이 저장 가능<br />

</li>
</ul>
<h4 id="✔️-session의-사용-예">✔️ session의 사용 예</h4>
<ol>
<li>site 내에서 화면을 이동해도 로그인(사용자 정보)이 풀리지 않고 유지</li>
<li>장바구니<br />

</li>
</ol>
<h4 id="✔️-session의-동작-순서">✔️ session의 동작 순서</h4>
<ul>
<li>클라이언트가 페이지를 요청</li>
<li>서버는 접근한 클라이언트의 Request-Header 필드인 Cookie를 확인하여, 클라이언트가 해당 session-id를 보냈는지 확인</li>
<li>session-id가 존재하지 않는다면, 서버는 session-id를 생성해 클라이언트에게 돌려준다.</li>
<li>서버에서 클라이언트로 돌려준 session-id를 쿠키를 사용해 서버에 저장. 쿠키 이름 : JSESSIONID</li>
<li>클라이언트는 재접속 시, 이 쿠키(JSESSIONID)를 이용하여 session-id 값을 서버에 전달<br />

</li>
</ul>
<h4 id="✔️-session의-특징">✔️ session의 특징</h4>
<ul>
<li><p>웹 서버에 웹 컨테이너의 상태를 유지하기 위한 정보를 저장</p>
</li>
<li><p>웹 서버에 저장되는 쿠기(=세션 쿠키)</p>
</li>
<li><p>브라우저를 닫거나, 서버에서 세션을 삭제 했을 때만 삭제가 되므로, 쿠키보다 비교적 보안이 좋다.</p>
</li>
<li><p>저장 데이터에 제한이 없다.</p>
</li>
<li><p>각 클라이언트 고유 Session ID를 부여한다.</p>
</li>
<li><p>Session ID로 클라이언트를 구분하여 각 클라이언트 요구에 맞는 서비스 제공</p>
<br />

</li>
</ul>
<h4 id="✔️-httpsession의-주요-기능">✔️ HttpSession의 주요 기능</h4>
<table>
<thead>
<tr>
<th align="center">기능</th>
<th>method</th>
</tr>
</thead>
<tbody><tr>
<td align="center">생성</td>
<td>HttpSession session = request.getSession(); HttpSession session = request.getSession(false);</td>
</tr>
<tr>
<td align="center">값 저장</td>
<td>session.setAttribute(String name, Object value);</td>
</tr>
<tr>
<td align="center">값 얻기</td>
<td>Object obj = session.getAttribute(String name);</td>
</tr>
<tr>
<td align="center">값 제거</td>
<td>session.removeAttribute(String name); //특정 이름의 속성 제거 session.invalidate(); //binding되어 있는 모든 속성 제거</td>
</tr>
<tr>
<td align="center">생성시간</td>
<td>long ct = session.getCreationTime();</td>
</tr>
<tr>
<td align="center">마지막 접근 시간</td>
<td>long lat = session.getLastAccessedTime();</td>
</tr>
<tr>
<td align="center"><br /></td>
<td></td>
</tr>
<tr>
<td align="center"><hr /></td>
<td></td>
</tr>
<tr>
<td align="center"><br /></td>
<td></td>
</tr>
</tbody></table>
<h4 id="✔️-cookie--session의-공통점">✔️ Cookie &amp; Session의 공통점</h4>
<ol>
<li>목적: 둘 다 사용자 정보를 저장하거나 사용자를 식별하는 데 사용된다. 예를 들어, 로그인 상태를 유지하거나 사용자가 설정한 정보를 기억하는 데 쓰인다.</li>
<li>웹 애플리케이션에서 사용: 세션과 쿠키 모두 웹 애플리케이션에서 상태를 유지하기 위한 방법으로 자주 사용된다. HTTP는 기본적으로 무상태(stateless) 프로토콜이기 때문에, 세션과 쿠키를 이용해 상태를 관리할 수 있다.</li>
<li>키-값 쌍: 세션과 쿠키는 모두 키-값 쌍의 형태로 데이터를 저장한다.
ex) 세션: session.setAttribute(&quot;username&quot;, &quot;john&quot;), 쿠키: cookie.setValue(&quot;username=John&quot;)<br />

</li>
</ol>
<h4 id="✔️-cookie--session의-차이점">✔️ Cookie &amp; Session의 차이점</h4>
<table>
<thead>
<tr>
<th align="center">특징</th>
<th>Session</th>
<th>Cookie</th>
</tr>
</thead>
<tbody><tr>
<td align="center">저장 위치</td>
<td>서버에 저장</td>
<td>클라이언트(브라우저)에 저장</td>
</tr>
<tr>
<td align="center">데이터 보안</td>
<td>서버에 저장되므로 비교적 안전(클라이언트는 세션 ID만 알 수 있음)</td>
<td>클라이언트에 저장되므로 보안에 취약(사용자가 변조 가능)</td>
</tr>
<tr>
<td align="center">유효 기간</td>
<td>기본적으로 브라우저 종료 시 삭제</td>
<td>만료 기간 설정 가능(설정하지 않으면 브라우저 종료 시 삭제)</td>
</tr>
<tr>
<td align="center">용량 제한</td>
<td>서버 용량에 의존(제한 없음)</td>
<td>보통 4KB 이하로 제한</td>
</tr>
<tr>
<td align="center">용도</td>
<td>사용자의 세션 정보, 인증상태 유지, 일시적 데이터 저장</td>
<td>사용자 식별, 자동 로그인, 언어 설정 등 간단한 데이터 저장</td>
</tr>
<tr>
<td align="center">보존 기간</td>
<td>세션 종료 시 삭제(브라우저를 닫으면 종료)</td>
<td>설정된 만료 기간까지 유지</td>
</tr>
<tr>
<td align="center"><br /></td>
<td></td>
<td></td>
</tr>
</tbody></table>
<h4 id="✔️-session으로도-id-저장-체크-여부를-관리할-수-있을까">✔️ session으로도 ID 저장 체크 여부를 관리할 수 있을까?</h4>
<ul>
<li>가능은 하다. 
하지만,  세션은 브라우저 종료 시 자동으로 삭제되기 때문에, 아이디 저장 상태가 브라우저 종료 후에도 유지되지 않기 때문에 쿠키를 사용하는 것이 더 적합하다. 
아이디 저장 체크 여부 같은 사용자 설정을 오래 유지하려면 쿠키를 사용하는 것이 더 나은 선택이다.
따라서, 아이디 저장 기능과 같은 장기적인 사용자 정보를 다루려면 쿠키가 더 적합하고, 세션은 일시적인 데이터나 로그인 상태 유지에 더 적합하다.<br />


</li>
</ul>
<h4 id="👉-span-stylebackground-colorfff5b1-cookie와-session의-특징을-잘-생각하면서-무엇을-사용하는-것이-적절할-지-판단하고-사용하면-좋을-것-같다span">👉 <span style="background-color: #fff5b1;"> cookie와 session의 특징을 잘 생각하면서, 무엇을 사용하는 것이 적절할 지 판단하고 사용하면 좋을 것 같다.</span></h4>