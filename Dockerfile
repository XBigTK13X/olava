# DOCKER VERSION 1.8.2

FROM python

MAINTAINER Tim "XBigTK13X" Kretschmer (tim@simplepathstudios.com)

ADD ./ /root/olava

WORKDIR /root/olava

RUN chmod +x script/app/launch.sh

WORKDIR /root/olava

RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/bash","-c"]

CMD ["script/app/launch.sh"]