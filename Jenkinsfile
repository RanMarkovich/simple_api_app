pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('run') {
      steps {
        sh 'python3 app/app.py'
      }
    }
    stage('test') {
      steps {
        sh 'python tests/test_app.py'
      }
      post {
        always {
          junit 'test-reports/app.xml'
        }
      }
    }
  }
}