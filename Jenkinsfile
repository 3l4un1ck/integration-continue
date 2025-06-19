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
        stage('Install dependencies') {
            steps {
                echo '=== Starting Install dependencies ==='
                sh '''
                    echo "Creating virtual environment..."
                    python3 -m venv venv
                    echo "Activating virtual environment..."
                    . venv/bin/activate
                    echo "Upgrading pip..."
                    pip install --upgrade pip
                    echo "Installing requirements..."
                    pip install -r requirements.txt
                '''
                echo '=== Finished Install dependencies ==='
            }
        }
        stage('Run tests') {
            steps {
                echo '=== Starting Run tests ==='
                sh '''
                    echo "Activating virtual environment..."
                    . venv/bin/activate
                    echo "Running pytest..."
                    pytest --cov=todo tests/ --junitxml=test-results.xml
                '''
                echo '=== Finished Run tests ==='
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
