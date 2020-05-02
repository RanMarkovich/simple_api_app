node('flask_slave'){
    stage('SCM'){
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false,
         extensions: [], submoduleCfg: [],
         userRemoteConfigs: [[url: 'https://github.com/RanMarkovich/simple_api_app.git']]])
    }
    stage('Build'){
        sh 'docker build -t app:lts .'
        sh 'pip3 --no-cache-dir install -r requirements.txt'
    }
    stage('Run'){
        sh 'docker run -d -p 5000:5000 app'
    }
    stage('Test'){
        sh 'pytest test_app.py'
    }
}