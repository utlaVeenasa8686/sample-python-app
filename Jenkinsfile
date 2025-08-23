pipeline {
    agent any

    environment {
        PROJECT_ID = "second-project-gar" 
        REGION = "us-central1" 
        REPO = "my-docker-repo" 
        IMAGE = "hanu-python-app"
        GAR_IMAGE = "${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO}/${IMAGE}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/hanumantharao19/sample-python-app.git'
            }
        }

        stage('Auth with GCP') {
            steps {
                
                    sh '''
                        gcloud config set project $PROJECT_ID
                    '''
                }
            
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                        docker build -t ${GAR_IMAGE}:${BUILD_NUMBER} .
                    """
                }
            }
        }

        stage('Push to Artifact Registry') {
            steps {
                script {
                    sh """
                        gcloud auth configure-docker ${REGION}-docker.pkg.dev --quiet
                        docker push ${GAR_IMAGE}:${BUILD_NUMBER}
                        docker tag ${GAR_IMAGE}:${BUILD_NUMBER} ${GAR_IMAGE}:latest
                        docker push ${GAR_IMAGE}:latest
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Successfully built and pushed: ${GAR_IMAGE}:${BUILD_NUMBER}"
        }
        failure {
            echo "❌ Build failed!"
        }
    }
}
