<h3 id="팀장-하지원-팀원-김소연">팀장: 하지원, 팀원: 김소연</h3>
<br />

<h4 id="⭐-구현-기능">⭐ <strong>구현 기능</strong></h4>
<h5 id="--f01--주택-실거래가-정보-수집">- F01 : 주택 실거래가 정보 수집</h5>
<h5 id="--f02--주택-실거래가-검색">- F02 : 주택 실거래가 검색</h5>
<h5 id="--f03--관심지역-정보-관리">- F03 : 관심지역 정보 관리</h5>
<h5 id="--f10--회원-관리">- F10 : 회원 관리</h5>
<h5 id="--f11--로그인-관리">- F11 : 로그인 관리</h5>
<br />

<h4 id="⭐-릴레이션-설계">⭐ <strong>릴레이션 설계</strong></h4>
<p><img alt="" src="https://velog.velcdn.com/images/ssossosso/post/17331289-6725-4a51-acb5-a8bebc710701/image.PNG" /></p>
<br />

<h4 id="⭐-테이블-생성">⭐ <strong>테이블 생성</strong></h4>
<h5 id="--user-table--사용자-정보를-저장">- User table : 사용자 정보를 저장.</h5>
<p><img alt="" src="https://velog.velcdn.com/images/ssossosso/post/b5f6debe-0301-42c4-b82c-e3c9c4d2c3ec/image.PNG" /></p>
<h5 id="--region-table--지역-정보를-저장-favoriteregion-houseinfos-테이블과-연관됨">- Region table : 지역 정보를 저장. FavoriteRegion, Houseinfos 테이블과 연관됨.</h5>
<p><img alt="" src="https://velog.velcdn.com/images/ssossosso/post/925435e3-6987-468c-b524-423ed76d7d44/image.PNG" /></p>
<h5 id="--favoriteregion-table--사용자의-관심-지역-정보를-저장-user-테이블과-1n-관계">- FavoriteRegion table : 사용자의 관심 지역 정보를 저장. User 테이블과 1:N 관계.</h5>
<p><img alt="" src="https://velog.velcdn.com/images/ssossosso/post/6bbc6d65-f42d-4cf5-b01b-ca8f3932c8a9/image.PNG" /></p>
<h5 id="--houseinfos-table--아파트-기본-정보를-저장">- Houseinfos table : 아파트 기본 정보를 저장.</h5>
<p><img alt="" src="https://velog.velcdn.com/images/ssossosso/post/5a8290eb-e298-4b89-8bb9-0ac6047ceaa3/image.PNG" /></p>
<h5 id="--housedeals-table--아파트-거래-정보를-저장">- Housedeals table : 아파트 거래 정보를 저장</h5>
<p><img alt="" src="https://velog.velcdn.com/images/ssossosso/post/09d9a628-5deb-4107-a732-fc8716c64020/image.PNG" /></p>
<h5 id="--eer-diagram">- EER Diagram</h5>
<p><img alt="" src="https://velog.velcdn.com/images/ssossosso/post/e640581d-9859-41ea-b2d3-ad8d77972fad/image.PNG" /></p>
<h5 id="--주요-관계">- 주요 관계</h5>
<ul>
<li>User -(1:N)-&gt; FavoriteRegion</li>
<li>Region -(1:N)-&gt; FavoriteRegion</li>
<li>Region -(1:N)-&gt; Houseinfos</li>
<li>Houseinfos -(1:N)-&gt; Housedeals</li>
</ul>
<br />


<h4 id="⭐-프로젝트-파일-구조">⭐ <strong>프로젝트 파일 구조</strong></h4>
<p><img alt="" src="https://velog.velcdn.com/images/ssossosso/post/f38f47a2-5554-4463-a268-ff1dce18bbad/image.PNG" /></p>
<p><strong>1. com.ssafy.board 패키지 : 프로젝트의 메인 패키지</strong></p>
<ul>
<li>Main.java : 프로그램 실행 파일</li>
</ul>
<p><strong>2. com.ssafy.board.model 패키지 : 데이터 모델(DTO)을 포함하는 패키지</strong></p>
<ul>
<li>AptDealDto.java : 아파트 거래 정보를 담는 데이터 객체</li>
<li>AptInfoDto.java : 아파트 정보를 담는 데이터 객체</li>
<li>FavoriteRegion.java : 관심 지역 정보를 담는 데이터 객체</li>
<li>UserDto.java : 사용자 정보를 담는 데이터 객체</li>
</ul>
<p><strong>3. com.ssafy.board.model.dao 패키지 : 데이터 접근 객체(DAO)를 포함하는 패키지</strong></p>
<ul>
<li>AptDao.java : 아파트 관련 데이터 접근 인터페이스</li>
<li>AptDaoImpl.java: AptDao 인터페이스의 구현체</li>
<li>FavoriteRegionDao.java: 관심 지역 데이터 접근 인터페이스</li>
<li>FavoriteRegionDaoImpl.java: FavoriteRegionDao 인터페이스의 구현체</li>
<li>UserDao.java: 사용자 데이터 접근 인터페이스</li>
<li>UserDaoImpl.java: UserDao 인터페이스의 구현체</li>
</ul>
<p><strong>4. com.ssafy.board.model.service 패키지 : 비즈니스 로직을 처리하는 서비스 클래스들을 포함</strong></p>
<ul>
<li>AptService.java: 아파트 관련 서비스 인터페이스</li>
<li>AptServiceImpl.java: AptService 인터페이스의 구현체</li>
<li>FavoriteRegionService.java: 관심 지역 관련 서비스 인터페이스</li>
<li>FavoriteRegionServiceImpl.java: FavoriteRegionService 인터페이스의 구현체</li>
<li>UserService.java: 사용자 관련 서비스 인터페이스</li>
<li>UserServiceImpl.java: UserService 인터페이스의 구현체</li>
</ul>
<br />

<h4 id="⭐-프로그램-주요-기능">⭐ <strong>프로그램 주요 기능</strong></h4>
<ol>
<li>아파트 거래 목록 : 아파트 거래 정보를 제공</li>
</ol>
<ul>
<li>아파트 기본 정보 : 아파트명, 지역 코드, 주소(도로명, 지번), 건축년도, 위치(위도/경도)</li>
<li>거래 상세 정보 : 거래 연원일, 층 수, 전용 면적, 거래 금액
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/1ed9b7ba-16d0-447e-98d3-c21555f4d685/image.PNG" /></li>
</ul>
<ol start="2">
<li>유저 + 관심 목록 : 관심 목록을 가진 사용자의 정보를 제공</li>
</ol>
<ul>
<li>사용자 항목 : 사용자ID, 이름, 이메일 주소, 계정 생성일, 생년월일</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/ssossosso/post/1c874503-d3a1-417a-b8e7-3a18d67ebca2/image.PNG" /></p>
<ol start="3">
<li><p>유저 생성 : 사용자의 이름, 이메일, 비밀번호를 입력받아 새로운 사용자를 데이터베이스에 추가하는 기능
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/3e96b014-47c1-46dc-9611-806289eb992e/image.PNG" />
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/a8dd6e89-0563-4df2-b686-de35de32e1b6/image.PNG" /></p>
</li>
<li><p>유저 조회 : 입력받은 아이디를 기반으로 해당 사용자의 정보를 데이터베이스에서 조회하여 출력하는 기능
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/32e0f6e0-c570-4262-be98-cdbf198ff5fa/image.PNG" />
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/d814ad25-f7b1-4ea8-871b-1951f17f860a/image.PNG" /></p>
</li>
<li><p>유저 수정 : 입력받은 새로운 이름, 이메일, 비밀번호로 기존 사용자 정보를 업데이트 하는 기능
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/74172682-af5d-41b4-af70-d84fdaef1669/image.PNG" />
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/ab4289e8-7413-4cf1-ad02-022902fd49f8/image.PNG" /></p>
</li>
<li><p>유저 삭제 : 입력받은 아이디에 해당하는 유저 정보를 데이터베이스에서 삭제하는 기능
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/c72c7918-a0d1-47ae-81d6-67a2baf5eb6d/image.PNG" />
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/63831cc0-5a33-4571-8b36-c4725f00bcbd/image.PNG" /></p>
</li>
<li><p>관심 지역 추가 : 유저 id와 법정동 시구군 코드를 관심 지역을 데이터베이스에 추가하는 기능
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/2353e4ba-2b2a-44cb-bdca-ba845ad29467/image.PNG" />
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/20b34111-10f8-4f09-bc38-a6b3508bbe8c/image.PNG" /></p>
</li>
<li><p>관심 지역 조회 : 유저 id를 입력받아 해당 유저의 관심 지역을 조회하여 출력하는 기능
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/a01e4215-6413-4cd6-86b8-cdf5d62922e0/image.PNG" />
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/f6b8e052-36e9-4ebc-b443-d15d15e26855/image.PNG" /></p>
</li>
<li><p>관심 지역 삭제 : 유저 id를 입력받아 해당 유저의 관심 지역 정보를 데이터베이스에서 삭제하는 기능
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/50b1af51-54c1-4a1d-8b52-7abe34879cd8/image.PNG" />
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/383cd0e5-6586-495d-88d5-772f28b4dbf0/image.PNG" /></p>
</li>
</ol>
<br />

<h4 id="⭐-화면-캡쳐">⭐ <strong>화면 캡쳐</strong></h4>
<p><img alt="" src="https://velog.velcdn.com/images/ssossosso/post/3ff86f02-f784-4a64-be67-71b989ec1f5f/image.gif" />
<img alt="" src="https://velog.velcdn.com/images/ssossosso/post/9d7060f5-1c14-4651-a912-547407148514/image.gif" /></p>