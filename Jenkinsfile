pipeline {
    agent any

    environment {
        PYTHON = 'python3'
    }

    stages {
        stage('Install dependencies') {
            steps {
                dir('python-demo') {
                    sh '${PYTHON} -m pip install --upgrade pip'
                    sh '${PYTHON} -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run App') {
            steps {
                dir('python-demo') {
                    echo 'Running the Python app...'
                    sh '${PYTHON} main.py < /dev/null' // avoid interactive prompt blocking
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('python-demo') {
                    echo 'Running unit tests...'
                    sh 'PYTHONPATH=. pytest tests'
                }
            }
        }

        stage('Package') {
            steps {
                dir('python-demo') {
                    echo 'Packaging the app...'
                    sh 'tar -czf app.tar.gz *.py requirements.txt tests/'
                    archiveArtifacts artifacts: 'python-demo/app.tar.gz', fingerprint: true
                }
            }
        }
    }
}
