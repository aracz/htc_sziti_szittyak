FROM python:3.6

EXPOSE 8501

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT streamlit run dashboard.py
