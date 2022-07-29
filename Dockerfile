FROM python:3.9.13-bullseye

WORKDIR trista-nudes
COPY . .

# RUN apk --no-cache add musl-dev linux-headers g++
RUN pip3 install -U pip
RUN pip3 install -e .

ENTRYPOINT ["python3", "-m", "nudenet.web_application"]