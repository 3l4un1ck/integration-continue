pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-u'
        }
    }// ou un label correspondant à ton agent avec Docker
    stages {
        stage('Run inside Docker') {
            steps {
                sh 'docker run --rm -v $PWD:/app -w /app python:3.10 sh -c "python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt && pytest --junitxml=report.xml"'
            }
        }
        stage('Publish report') {
            steps {
                junit 'report.xml'
            }
        }
    }
}
