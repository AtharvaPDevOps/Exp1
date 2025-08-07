pipeline {
    agent any

    environment {
        PATH = "${HOME}/.local/bin:${PATH}"
    }

    stages {
        stage('Clone') {
            steps {
                dir('python-demo') {
                    sh 'python3 -m pip install --upgrade pip'
                    sh 'python3 -m pip install -r requirements.txt'
                }
            }
        }

        stage('Build') {
            steps {
                dir('python-demo') {
                    echo "Running the Python app..."
                    sh 'python3 main.py'
                }
            }
        }

        stage('Deploy') {
            steps {
                dir('python-demo') {
                    echo 'Running unit tests...'
                    // This ensures pytest runs correctly
                    sh '${HOME}/.local/bin/pytest tests'
                }
            }
        }

        stage('Test') {
            steps {
                dir('python-demo') {
                    echo 'Simulating packaging step...'
                    sh 'tar -czf temperature_converter.tar.gz *.py'
                    echo 'Packaging complete.'
                }
            }
        }
    }
}
