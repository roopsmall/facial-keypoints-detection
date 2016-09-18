FROM phusion/baseimage:0.9.18
MAINTAINER roop small

CMD ["/sbin/my_init"]

RUN apt-get update
RUN apt-get install -y python python-pip blah blah
RUN pip install blah
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


ENV ENV_VAR1="blah"
ENV ENV_VAR2="blahblah"

ADD . /home

VOLUME blahblahblah

WORKDIR /home
