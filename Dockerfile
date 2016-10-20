FROM django:1.9.5-python2
MAINTAINER Kevin
ENV DIR /src/
RUN mkdir ${DIR}
COPY requirements.txt .
RUN ["pip","install","-r","requirements.txt"]
WORKDIR ${DIR}
LABEL version="1.0" \
      description="This image is used to set up django sevier."

