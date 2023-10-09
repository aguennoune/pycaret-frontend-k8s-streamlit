FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/aguennoune/pycaret-frontend-k8s-streamlit.git /app

RUN pip install -r https://raw.githubusercontent.com/aguennoune/pycaret-frontend-k8s-streamlit/main/src/frontend/k8s_streamlit/requirements.txt

RUN chmod 644 src/frontend/k8s_streamlit/insurance_gbr_model_23122020.pkl

COPY insurance_gbr_model_23122020.pkl /app/

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]