pipeline {
  agent { docker { image 'python:3.7' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'python app.py'
      }
    }
    stage('test') {
      steps {
        sh 'pytest test_app.py'
      }
    }
  }
}