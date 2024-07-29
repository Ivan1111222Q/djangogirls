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
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                script {
                    // Deploy Docker containers using production compose file
                    sh 'docker-compose -f docker-compose.production.yml up -d'
                }
            }
        }
    }
}
