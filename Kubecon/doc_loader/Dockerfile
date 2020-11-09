FROM tensorflow/tensorflow
RUN python3 -m pip install keras
RUN pip install --upgrade pip
RUN python3 -m pip install pandas
RUN python3 -m pip install google-cloud-storage
RUN python3 -m pip install pyyaml
COPY ./src /pipelines/component/src
