pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID     = credentials('aws-access-key')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-key')
        AWS_DEFAULT_REGION    = 'ap-south-1'
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/VBharathirajA/Python_AWS_Automation.git'
            }
        }

        stage('Install boto3') {
            steps {
                bat 'pip install boto3'
            }
        }

        stage('Run Python Script') {
            steps {
                bat 'python ec2_create.py'
            }
        }
    }
}
