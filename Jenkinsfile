pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'docker run -p 8080:8080 --user root \
     -v /var/run/docker.sock:/var/run/docker.sock jenkinsci/blueocean'
        sh 'docker build -t simple-api-app:latest .'
        sh 'docker run -d -p 5000:5000 simple-api-app'
      }
    }
    stage('test') {
      steps {
        sh 'pytest test_app.py'
      }
    }
  }
}