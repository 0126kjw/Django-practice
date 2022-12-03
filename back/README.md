# `django-auth`

Django, DRF(Django REST Framework), dj-rest-auth, django-allauth를 활용하여 로그인과 회원가입을 구현하였습니다. 
User Model의 username 대신 email을 사용하도록 변경하였습니다.

## 실행 방법

```bash
cd django-auth
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

위와 같이 입력하고 http://localhost:8000/ 으로 접속하면 됩니다.

아직 장고 공부가 부족해서 코드랑 구조에 대한 이해도가 높아지면 차후에 폴더 정리할 예정입니다.

우선 겹치지 않도록 작업하던 폴더 그대로 옮겨놨습니다.

## API Document
https://documenter.getpostman.com/view/22491165/2s83zgsPrg