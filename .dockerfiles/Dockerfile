FROM        eb_ubuntu
MAINTAINER  archysp11@gmail.com

# 현재경로의 모든 파일들을 컨테이너의 /srv/deploy_eb_docker폴더에 복사
COPY        . /srv/deploy_eb_docker
# cd /srv/deploy_eb_docker와 같은 효과
WORKDIR     /srv/deploy_eb_docker
# requirements설치
RUN         /root/.pyenv/versions/deploy_eb_docker/bin/pip install -r .requirements/debug.txt

#supervisor 파일복사
COPY        .config/supervisor/uwsgi.conf /etc/supervisor/conf.d/

CMD         supervisord -n

# 외부 노출할 포트
EXPOSE      80 8000

# uwsgi실행경로
#   /root/.pyenv/versions/deploy_eb_docker/bin/uwsgi
# 1.실행중인 컨테이너의 내부에서 uwsgi를 사용해서 8000번 포트로 외부와 연결해서 Django를 실행해보기
    # uwsgi를
    #   http 8000포트,
    #   chdir 프로젝트 django 코드
    #   home 가상환경 경로 적용 후 실행
    #/root/.pyenv/versions/deploy_eb_docker/bin/uwsgi --http :8000 --chdir /srv/deploy_eb_docker/django_app --home /root/.pyenv/versions/deploy_eb_docker -w config.wsgi.debug


# 2.docker run실행시 곧바로 uWSGI에 의해서 서버가 작동되도록 Dockerfile을 수정 후 build, run 해보기

# 3.uwsgi설정을 ini파일로 작성(.config/uwsgi/uwsgi-app.ini)하고
#   작성한 파일로 실행되도록 supervisor/uwsgi.conf파일을 수정
    #   /root/.pyenv/versions/deploy_eb_docker/bin/uwsgi --ini /srv/deploy_eb_docker/.config/uwsgi/uwsgi-app.ini



