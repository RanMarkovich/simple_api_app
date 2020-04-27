pipeline {
  agent { docker { image 'python:3.7' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
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