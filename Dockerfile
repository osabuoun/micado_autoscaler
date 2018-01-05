FROM python:3

ADD requirements.txt /autoscaler/requirements.txt
ADD autoscaler.py /autoscaler/autoscaler.py
WORKDIR /autoscaler/
RUN pip3 install -r requirements.txt
ENTRYPOINT python3 -m http.server