FROM python
RUN pip install dash
RUN pip install plotly
RUN pip install pandas
COPY . /home/jovyan
CMD ["python", "fun.py"]
