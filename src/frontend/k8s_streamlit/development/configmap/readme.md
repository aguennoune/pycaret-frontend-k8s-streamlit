##### Test the `aguennoune/pycaret-k8s-streamlit:1.10.0` Docker image locally:


```bash
cd ./src/frontend/k8s_streamlit

docker run --rm -it \
-v ${PWD}:/app \
-w /app \
-d -p 8501:8501 \
aguennoune/pycaret-k8s-streamlit:1.10.0 /bin/sh
```

The Streamlit `app.py` should be up and running in a container :)
