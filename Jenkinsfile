pipeline {
    agent any

    environment {
        REGISTRY = 'localhost:5000'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Build Docker images
                    sh 'docker-compose build'
                }
            }
        }

        stage('Push') {
            steps {
                script {
                    // Push Docker images to local registry
                    sh 'docker push ${REGISTRY}/djangogirls-nginx'
                    sh 'docker push ${REGISTRY}/djangogirls-app'
                    sh 'docker push ${REGISTRY}/djangogirls-db'
                }
            }
        }

        stage('Show Branch') {
            steps {
                script {
                    sh 'git rev-parse --abbrev-ref HEAD'
                    sh 'echo "Current branch is ${BRANCH_NAME}"'
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                script {
                    echo 'Deploying application...'
                    // Deploy Docker containers using production compose file
                    sh 'docker-compose -f docker-compose.production.yml up -d'
                }
            }
        }
    }
}
