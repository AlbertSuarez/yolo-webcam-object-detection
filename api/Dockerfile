FROM python:3.6
WORKDIR /srv/yolo-object-detection
COPY api api
RUN pip install --upgrade pip
RUN pip3 install -r api/requirements.lock
RUN chmod +x api/install_darkflow.sh
RUN ./api/install_darkflow.sh
CMD uwsgi --ini api/api.ini