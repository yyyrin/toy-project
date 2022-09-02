# 

# PJT 04

### 프로젝트 목표

- 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
- Django web framework를 사용한 데이터 처리
- Django Model과 ORM에 대한 이해
- 관리자 페이지를 통한 데이터 관리
<br><br>

### 공통 요구사항
- 커뮤니티 웹 서비스의 데이터 구성 단계입니다.
- 영화 데이터의 생성, 조회, 수정, 삭제가 가능한 애플리케이션을 완성합니다.
- Django 프로젝트의 이름은 **mypjt**, 앱 이름은 **movies**로 지정합니다.
- 명시된 요구사항 이외에는 자유롭게 작성해도 무관합니다.
<br><br>

### Model
- 정의할 모델 클래스의 이름은 Movie이며, 다음과 같은 정보를 저장합니다.
  |필드명|데이터 유형|역할|
  |------|---|---|
  |title|varchar(20)|영화 제목|
  |audience|Integer|관객 수|
  |release_date|date|개봉일|
  |genre|varchar(30)|장르|
  |score|float|평점|
  |poster_url|text|포스터 경로|
  |description|text|줄거리|
<br><br>

### URL
- movies 앱은 다음 URL 요청에 맞는 역할을 가집니다.
  |URL 패턴|역할|
  |------|---|
  |/movies|전체 영화 목록 페이지 조회|
  |/movies/new/|새로운 영화 생성 페이지 조회|
  |/movies/create/|단일 영화 데이터 저장|
  |/movies/<pk\>/|단일 영화 상세 페이지 조회|
  |/movies/<pk\>/edit/|기존 영화 수정 페이지 조회|
  |/movies/<pk\>/update/|단일 영화 데이터 수정|
  |/movies/<pk\>/delete/|단일 영화 데이터 삭제|
<br><br>

### View
- movies 앱은 다음 역할을 가지는 view 함수를 가집니다.
  |View 함수명|역할|
  |------|---|
  |index|전체 영화 데이터 조회 및 index.html 렌더링|
  |new|장르 데이터 제공 및 new.html 렌더링|
  |create|새로운 영화 데이터 저장 및 detail 페이지로 리다이렉트|
  |detail|단일 영화 데이터 조회 및 detail.html 렌더링|
  |edit|수정 대상 영화 데이터 조회 및 edit.html 렌더링|
  |update|영화 데이터 수정 및 detail 페이지로 리다이렉트|
  |delete|단일 영화 데이터 삭제 및 index 페이지로 리다이렉트|  
<br><br>

### Admin
- 모델 Movie를 Admin site에 등록합니다.
- Admin site에서 데이터의 생성, 조회, 수정, 삭제가 가능해야 합니다.
<br><br><br>

### Template
- 사용 템플릿 목록
  1. `base.html`
  2. `index.html`
  3. `detail.html`
  4. `new.html`
  5. `edit.html`

# 

## A. `base.html`

* 요구 사항
  - 공통 부모 템플릿
    - 모든 템플릿 파일은 base.html을 상속받아 상용합니다.
<br><br>

* 문제 접근 방법 및 코드 설명
  
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  </head>
  <body>
      {% block content %}
      {% endblock content %}
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
  </body>
  </html>    
  ```
  <br>

  * 이 문제에서 어려웠던점
    - 이 문제는 딱히 어렵지 않았다. 기존에 사용했던 `base.html`을 복사해서 사용했다. 
  <br><br>

  * 내가 생각하는 이 문제의 포인트
    - 공통 부모 템플릿인 `base.html`을 작성할 수 있는가
<br><br>

-----
## B. `index.html`

* 요구 사항
  - "전체 영화 목록 조회 페이지"
    - 데이터베이스에 존재하는 모든 영화의 목록을 표시합니다.
    - 적절한 HTML 요소를 사용하여 영화 제목 및 평점을 표시하며, 제목을 클릭 시 해당 영화의 상세 조회 페이지(detail.html)로 이동한다.
<br><br>

* 문제 접근 방법 및 코드 설명
  
  ```html
  {% extends 'base.html' %}
  {% block content %}
  <h1>INDEX</h1>
  <br>
  <a href="{% url 'movies:new' %}">[NEW]</a>
  <hr>
  {% for movie in movies %}
  <p>
      <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>
      {{ movie.score }}
      <hr>
  </p>
  {% endfor %}
  {% endblock content %}   
  ```
  <br>

  * 이 문제에서 어려웠던점
    - 어제 학습했던 코드를 보면서 거의 클론코딩을 했기 때문에 어렵진 않았다.
    - 하지만 이 코드를 왜 사용하는지 아직 정확하게 이해하지 못했다.
  <br><br>

  * 내가 생각하는 이 문제의 포인트
    - 조회 페이지를 작성할 수 있는가
<br><br>

-----
## `C. detail.html`

* 요구 사항
  - "영화 상세 정보 페이지"
    - 특정 영화의 상세 정보를 표시합니다.
    - 해당 영화의 수정 및 삭제 버튼을 표시합니다.
    - 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크를 표시합니다.
<br><br>

* 문제 접근 방법 및 코드 설명
  
  ```html
  {% extends 'base.html' %}
  {% block content %}
  <h1>DETAIL</h1>
  <hr>
  <img src="{{ movie.poster_url }}" alt="영화 포스터" width="500">
  <br><br>
  <p>{{ movie.title }}</p>
  <p>Audience : {{ movie.audience }}</p>
  <p>Release Dates : {{ movie.release_date }}</p>
  <p>Genre : {{ movie.genre }}</p>
  <p>Score : {{ movie.score }}</p>
  <p>{{ movie.description }}</p>
  <a href="{% url 'movies:edit' movie.pk %}">EDIT</a>
  <form action="{% url 'movies:delete' movie.pk %}" method="POST">
      {% csrf_token %}
      <button>DELETE</button>
  </form>
  <a href="{% url 'movies:index' %}">BACK</a>
  {% endblock content %}
  ```
  <br>

  * 이 문제에서 어려웠던점
    - Django Template Language가 익숙하지 않았다. 개념 공부가 더 필요하다.
    - 코드는 마찬가지로 어제 작성했던 코드와 거의 유사하게 작성했다.
  <br><br>

  * 내가 생각하는 이 문제의 포인트
    - 상세 정보 페이지를 작성할 수 있는가
    - DTL을 사용할 수 있는가
<br><br>

-----
## `D. new.html`

* 요구 사항
  - "영화 생성 페이지"
    - 특정 영화를 생성하기 위한 HTML form 요소를 표시합니다.
    - 작성한 정보는 제출(submit)시 단일 영화 데이터를 저장하는 URL로 요청과 함께 전송됩니다.
    - 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크를 표시합니다.
<br><br>

* 문제 접근 방법 및 코드 설명
  
  ```html
  {% extends 'base.html' %}
  {% block content %}
  <h1>NEW</h1>
  <hr>
  <form action="{% url 'movies:create' %}" method="POST">
      {% csrf_token %}
      <label for="title">TITLE</label>
      <input type="text" id="title" name="title">
      <br>
      <label for="audience">AUDIENCE</label>
      <input type="number" id="audience" name="audience">
      <br>
      <label for="release_date">RELEASE_DATE</label>
      <input type="date" id="release_date" name="release_date">
      <br>
      <label for="genre">GENRE</label>
      <select name="genre" id="genre">
          <option value="comedy" selected>코미디</option>
          <option value="romance">로맨스</option>
          <option value="action">액션</option>
          <option value="drama">드라마</option>
          <option value="horror">공포</option>
      </select>
      <br>
      <label for="score">SCORE</label>
      <input type="number" id="score" name="score" min="0" max="5">
      <br>
      <label for="poster_url">POSTER_URL</label>
      <input type="url" id="poster_url" name="poster_url">
      <br>
      <label for="description">DESCRIPTION</label>
      <textarea name="description" id="description" cols="30" rows="10"></textarea>
      <br>
      <button>Submit</button>
  </form>
  <hr>
  <a href="{% url 'movies:index' %}">BACK</a>

  {% endblock content %}
  ```
  <br>

  * 이 문제에서 어려웠던점
    - html을 오랜만에 사용하다보니 input의 type을 거의 잊어버렸다.. 이번 기회에 다시 복습할 수 있었다.
  <br><br>

  * 내가 생각하는 이 문제의 포인트
    - Django 프로젝트의 흐름을 이해했는가
    - html을 작성할 수 있는가
<br><br>

-----
## `E. edit.html`

* 요구 사항
  - "영화 수정 페이지"
    - 특정 영화를 수정하기 위한 HTML form 요소를 표시합니다.
    - HTML input 요소에는 기존 데이터를 출력합니다.
    - Reset 버튼은 사용자의 모든 입력을 초기 값으로 재설정 합니다.
    - 작성한 정보는 제출(submit)시 단일 영화 데이터를 수정하는 URL로 요청과 함께 전송됩니다.
    - 영화 상세 정보 페이지(detail.html)로 이동하는 링크를 표시합니다.
<br><br>

* 문제 접근 방법 및 코드 설명
  
  ```html
  {% extends 'base.html' %}
  {% block content %}
  <br>
  <h1>EDIT</h1>
  <hr>
  <form action="{% url 'movies:update' movie.pk %}" method="POST">
      {% csrf_token %}
      <label for="title">TITLE</label>
      <input type="text" id="title" name="title" value="{{ movie.title }}">
      <br>
      <label for="audience">AUDIENCE</label>
      <input type="number" id="audience" name="audience" value="{{ movie.audience }}">
      <br>
      <label for="release_date">RELEASE_DATE</label>
      <input type="date" id="release_date" name="release_date" value="{{ movie.release_date | date:'Y-m-d' }}">
      <br>
      <label for="genre">GENRE</label>
      <select name="genre" id="genre" value="{{ movie.genre }}">
          <option value="comedy">코미디</option>
          <option value="romance">로맨스</option>
          <option value="action">액션</option>
          <option value="drama">드라마</option>
          <option value="horror">공포</option>
      </select>
      <br>
      <label for="score">SCORE</label>
      <input type="number" id="score" name="score" min="0" max="5" value="{{ movie.score }}">
      <br>
      <label for="poster_url">POSTER_URL</label>
      <input type="url" id="poster_url" name="poster_url" value="{{ movie.poster_url }}">
      <br>
      <label for="description">DESCRIPTION</label>
      <textarea name="description" id="description" cols="30" rows="10">{{ movie.description }}</textarea>
      <br>
      <input type="reset" value="Reset">
      <button>Submit</button>
  </form>
  <hr>
  <a href="{% url 'movies:index' %}">BACK</a>
  {% endblock content %}
  ```
  <br>

  * 이 문제에서 어려웠던점
    - 가장 많은 시간이 소요되었던 부분이다.
    - 기존 데이터를 출력해야 했기에 value 값을 모두 지정해줘야 했다.
    - `release_date`에서 오류가 발생했다. 알고보니 date의 형식을 지정해줘야 했던 것이다. 이를 수정하였더니 url과 관련된 오류도 해결되었다. 신기한 경험이었다.
  <br><br>

  * 내가 생각하는 이 문제의 포인트
    - Django 프로젝트의 흐름을 이해했는가
    - html을 작성할 수 있는가
<br><br><br>


#
# 후기

* 코드를 작성하며 Django의 흐름을 따라간 덕분에 어제보다 훨씬 이해가 잘 되었다.
* 하지만 아직 개념적인 부분에서 부족한 게 많다는 것을 느꼈다.
* 이번 주말에 Django 복습 안 하면 진짜 큰일이다.
* 이번 프로젝트를 하면서 내가 어떤 개념을 확실하게 이해하지 못했는지 알게 되었다. 예를 들면 DTL과 Model, pk와 관련된 개념들!!
* 프로젝트를 하다보면 어려움을 만나서 머리가 아플 때가 많다. 하지만 프로젝트를 통해 내가 어려워하는 부분을 명확히 알게 되고, 복습도 할 수 있어서 정말 좋은 시간이라고 생각한다. 프로젝트 만세..!
#
