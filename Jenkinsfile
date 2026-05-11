pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID     = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
        AWS_DEFAULT_REGION    = 'ap-south-1'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo 'Code cloned successfully'
            }
        }

        stage('Install dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run script') {
            steps {
                bat 'python main.py'
            }
        }

    }

    post {
        success { echo 'Build passed!' }
        failure { echo 'Build failed — check logs above' }
    }
}
