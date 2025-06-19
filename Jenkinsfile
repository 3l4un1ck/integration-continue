pipeline {
    agent any
    tools {
        python 'Python 3.10'
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/<ton-username>/todo_manager.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh '. venv/bin/activate && pytest --cov=todo tests/'
            }
        }
    }
    post {
        always {
            junit '**/test-results.xml'
        }
    }
}
