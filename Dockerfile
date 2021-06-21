FROM python:3
RUN mkdir /dashapp

COPY . /dashapp

WORKDIR /dashapp
VOLUME /dashapp   
RUN pip install -r requirements.txt
EXPOSE 8050       
ENTRYPOINT ["python"]
CMD ["app.py"]