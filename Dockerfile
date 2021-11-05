FROM jupyter/scipy-notebook
RUN pip install dash
RUN pip install plotly
RUN pip install pandas
RUN pip install jupytext
COPY . /home/jovyan
CMD ["python", "fun.py"]
