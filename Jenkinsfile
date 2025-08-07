pipeline {
    agent any

    environment {
        PYTHONPATH = '.'
        PATH = "${HOME}/.local/bin:${PATH}"
    }

    stages {

        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                dir('python-demo') {
                    sh 'python3 -m pip install --upgrade pip'
                    sh 'python3 -m pip install -r requirements.txt'
                }
            }
        }

        stage('Deploy') {
            steps {
                dir('python-demo') {
                    echo 'Running the Python app...'
                    sh 'python3 main.py'
                }
            }
        }

        stage('Test') {
            steps {
                dir('python-demo') {
                    echo 'Running unit tests...'
                    sh 'pytest tests'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
