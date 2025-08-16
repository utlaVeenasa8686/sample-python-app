pipeline {
    agent any

    environment {
        PROJECT_ID = "your-gcp-project-id" # replace with your PROJECT_ID 
        REGION = "us-central1" # replace with your REGION
        REPO = "python-app-repo" # Replace with your repo
        IMAGE = "python-app"
        GAR_IMAGE = "${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO}/${IMAGE}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/yourname/sample-python-app.git'
            }
        }

        stage('Auth with GCP') {
            steps {
                withCredentials([file(credentialsId: 'gcp-artifact-key', variable: 'GCP_KEY')]) {
                    sh '''
                        gcloud auth activate-service-account --key-file=$GCP_KEY
                        gcloud config set project $PROJECT_ID
                    '''
                }
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

