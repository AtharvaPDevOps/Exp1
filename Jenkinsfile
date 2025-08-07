pipeline {
    agent any

    environment {
        PATH = "${HOME}/.local/bin:${PATH}"
    }

    stages {
        stage('Install dependencies') {
            steps {
                dir('python-demo') {
                    sh 'python3 -m pip install --upgrade pip'
                    sh 'python3 -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run App') {
            steps {
                dir('python-demo') {
                    echo "Running the Python app..."
                    sh 'python3 main.py'
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('python-demo') {
                    echo 'Running unit tests...'
                    // This ensures pytest runs correctly
                    sh '${HOME}/.local/bin/pytest tests'
                }
            }
        }

        stage('Package') {
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
