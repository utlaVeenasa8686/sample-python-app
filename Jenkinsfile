pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1"                    // change to your AWS region
        AWS_ACCOUNT_ID = "813168483484"    // e.g., 123456789012
        REPO = "python_repo"                     // must exist in ECR
        IMAGE = "python"
        ECR_IMAGE = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${REPO}/${IMAGE}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/hanumantharao19/sample-python-app.git'
            }
        }

        stage('Auth with AWS ECR') {
            steps {
                script {
                    // Authenticate Docker with ECR using IAM role (no access keys required)
                    sh """
                        aws ecr get-login-password --region ${AWS_REGION} \
                          | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
                    """
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                        docker build -t ${ECR_IMAGE}:${BUILD_NUMBER} .
                    """
                }
            }
        }

        stage('Push to AWS ECR') {
            steps {
                script {
                    sh """
                        docker push ${ECR_IMAGE}:${BUILD_NUMBER}
                        docker tag ${ECR_IMAGE}:${BUILD_NUMBER} ${ECR_IMAGE}:latest
                        docker push ${ECR_IMAGE}:latest
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Successfully built and pushed: ${ECR_IMAGE}:${BUILD_NUMBER}"
        }
        failure {
            echo "❌ Build failed!"
        }
    }
}

