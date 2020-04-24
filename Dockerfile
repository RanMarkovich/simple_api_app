FROM python:3.7-slim
COPY . /simple_api_app
WORKDIR /simple_api_app
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytes", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null