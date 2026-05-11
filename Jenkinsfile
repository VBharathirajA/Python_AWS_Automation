pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID     = credentials('boto3

')
        AWS_SECRET_ACCESS_KEY = credentials('0xF3AZ6%
')
        AWS_DEFAULT_REGION    = 'ap-south-1'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo "Cloned successfully"
            }
        }

        stage('Verify Python') {
            steps {
                bat 'python --version'
                bat 'pip --version'
            }
        }

        stage('Install dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Verify AWS credentials') {
            steps {
                bat 'python -c "import boto3; c=boto3.client(\'sts\'); print(\'Account:\', c.get_caller_identity()[\'Account\'])"'
            }
        }

        stage('Run script') {
            steps {
                bat 'python main.py'
            }
        }

    }

    post {
        success { echo 'Build PASSED!' }
        failure { echo 'Build FAILED — check logs above' }
        always  { cleanWs() }
    }
}
