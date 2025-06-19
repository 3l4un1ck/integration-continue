pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '=== Starting Checkout ==='
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/3l4un1ck/integration-continue.git',
                        credentialsId: 'github-creds'
                    ]]
                ])
                echo '=== Finished Checkout ==='
            }
        }
        stage('Build Docker image') {
            steps {
                echo '=== Building Docker image ==='
                sh 'docker-compose build'
                echo '=== Finished building Docker image ==='
            }
        }
        stage('Run tests in Docker') {
            steps {
                echo '=== Running tests in Docker ==='
                sh 'docker-compose up --abort-on-container-exit'
                echo '=== Finished running tests in Docker ==='
            }
        }
    }

    post {
        always {
            echo '=== Publishing JUnit test results ==='
            junit 'test-results.xml'
        }
    }
}
