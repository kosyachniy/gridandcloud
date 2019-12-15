FROM python:3.6.9-slim

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
#COPY ./opencv-python-16 /app/opencv-python-16
#COPY ./opencv-3.4.2 /app/opencv-3.4.2
RUN pip3 install -U pip && \
    pip3 install -U pip setuptools && \
    pip3 install -U numpy && \
    pip3 install -U scikit-image && \
    pip3 install -U scikit-learn && \
    pip3 install opencv-python==3.4.2.16 && \
    pip3 install opencv-contrib-python==3.4.2.16

RUN apt-get install libglib2.0-0

RUN pip install -r requirements.txt
#RUN python opencv-python-16/setup.py
#RUN mv opencv-3.4.2 OpenCV && \
#    cd OpenCV && \
#    mkdir build && \
#    cd build && \
#    cmake && \
#    make -j4 && \
#    make install

ENTRYPOINT ["python", "main.py"]
