FROM python:3.8

ADD . /code

WORKDIR /code

RUN pip install -r  requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["python","./QT.py"]

