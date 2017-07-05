from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'

# Static URLs
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')

# 배포모드이기 때문에 DEBUG는 False
DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = config_secret_deploy['django']['databases']

print('@@@ DEBUG:', DEBUG)
print('@@@ ALLOWED_HOSTS:', ALLOWED_HOSTS)

# 1. RDS연동 후 데이터 들어가는지 확인
#    DJANGO_SETTINGS_MODULE=config.settings.deploy 설정
#    createsuperuser 커맨드 실행 후 pgAdmin으로 auth_user 테이블에 데이터가 들어갔는지 확인

# - Custom User Model
# member app 생성, AbstractUser를 상속받은 User 클래스 정의, img_profile필드(ImageField)추가
# AUTH_USER_MODEL에 등록
# RDS에서 데이터베이서 초기화 후 migrate실행
# User를 Django admin에 등록

# - 파일 업로드 관련 설정
# MEDIA_URL, MEDIA_ROOT설정 -> debug.py, deploy.py 에 각각 다로 설정(같은 값)
#   MEDIA_ROOT는 프로젝트폴더 /.media 폴더 사용
# 이 후 img_profile필드 채웠을 때 정상적으로 파일 업로드 되는지 확인