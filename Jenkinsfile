pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/<ton-username>/todo_manager.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --cov=todo tests/ --junitxml=test-results.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'
        }
    }
}
