pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask-app'
        CONTAINER_NAME = 'flask-container'
        DOCKER_PORT = '5000'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout code from GitHub
                git branch: 'main', url: 'https://github.com/your-repo/your-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                // Stop and remove any existing container with the same name
                script {
                    sh """
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    """
                }

                // Run the Docker container
                script {
                    sh "docker run -d -p ${DOCKER_PORT}:${DOCKER_PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}"
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace after the pipeline
            cleanWs()
        }
    }
}