from django.urls import path, include, re_path
from .views import KakaoLogin, GoogleLogin

urlpatterns = [
    # 로그인, 정보 조회 등
    path('', include('dj_rest_auth.urls')),

    # 회원가입
    path('registration/', include('dj_rest_auth.registration.urls')),

    # 소셜(임시)
    re_path(r'^kakao/login/$', KakaoLogin.as_view(), name='kakao_login'),
    re_path(r'^google/login/$', GoogleLogin.as_view(), name='google_login'),
]
