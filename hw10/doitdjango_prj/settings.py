import os
from pathlib import Path

# 1. 기본 경로 설정
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. 보안 키 (실제 배포할 때는 비밀로 해야 해!)
SECRET_KEY = 'django-insecure-key-for-wonjae-homework'

# 3. 디버그 모드 (개발 중에는 True)
DEBUG = True

ALLOWED_HOSTS = []

# 💡 4단계 핵심: 우리가 만든 앱 등록
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 💡 현재 폴더에 실제로 존재하는 앱만 등록해야 에러가 안 나!
    'single_pages',
    # 'blog', # 👈 아직 blog 폴더를 안 만들어서 에러가 나니까 잠시 꺼둘게!
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 메인 URL 설정 파일 위치
ROOT_URLCONF = 'doitdjango_prj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'doitdjango_prj.wsgi.application'

# 데이터베이스 설정 (기본 SQLite 사용)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 비밀번호 검증 설정
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# 한국어 및 서울 시간 설정
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = True

# 정적 파일 (CSS, JS) 설정
STATIC_URL = 'static/'

# 💡 부트스트랩 파일을 찾기 위해 필요한 경로 설정
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'