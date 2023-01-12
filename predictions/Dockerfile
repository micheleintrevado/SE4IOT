FROM python:3.11
WORKDIR /app
COPY . .
RUN pip3 install flask
RUN pip3 install pandas
RUN pip install scikit-learn
CMD ["python3", "app.py"]
