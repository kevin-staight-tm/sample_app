FROM jupyter/scipy-notebook
RUN pip install dash
RUN pip install plotly
RUN pip install pandas
RUN pip install jupytext
CMD ["python", "fun.py"]
