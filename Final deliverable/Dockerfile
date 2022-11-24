FROM python:3.10.6
WORKDIR /app
ADD ./app
COPY requirements.txt /app
RUN pip install -r requirements.txt
RUN pip install ibm_db
RUN pip install pandas
RUN pip install linkedin_api
RUN pip install Flask-Mail
RUN pip install sendgrid
EXPOSE 5000
CMD ["python","./app.py"]
