pipeline {
    agent { docker { image 'ranmarkovich/dockerjenkinspython:v1' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install flask'
                sh 'pip install pytest'
            }
        }
        stage('test') {
            steps {
                sh 'pytest test_app.py'
            }
        }
    }
}