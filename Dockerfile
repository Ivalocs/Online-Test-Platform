FROM ubuntu:latest
LABEL "Author"="Ishmeet"
LABEL "Project"="online_test_platform"
RUN apt update && apt install git -y
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip install pillow
RUN pip install whitenoise
RUN pip install django
WORKDIR /home
EXPOSE 8000
RUN git init
RUN git pull
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]