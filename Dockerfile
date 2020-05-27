FROM python:2.7

MAINTAINER david@davidlcassidy.com

ADD rando.py /

RUN pip install flask slackclient

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["rando.py"]