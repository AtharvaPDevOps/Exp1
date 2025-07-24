pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                // Put your actual build commands here, for example:
                // sh 'npm install' or sh './gradlew build'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Put your test commands here, like:
                // sh 'npm test'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the app...'
                // Optional: Add deployment logic
            }
        }
    }
}
