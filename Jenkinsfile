pipeline {
    agent any

    environment {
        IMAGE_NAME = "selenium-test-image"
        CONTAINER_NAME = "selenium-test-container-${BUILD_NUMBER}"

    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    try {
                        echo "Cloning the Repository"
                        checkout scm
                        echo "Repository cloned Successfully"
                    } catch (err) {
                        echo "Repository clone failed"
                        echo "Error message: ${err}"
                        currentBuild.result = 'FAILURE'
                        error("Stopping pipeline due to checkout failure")
                    }
                }
            }
        }

        stage('Docker Image Creation'){
            steps{
                script{
                    echo "Creating the Docker Image for Test !"

                    try{
                        sh '''
                        set -e

                        echo "Building Docker Image"
                        docker build --no-cache -t $IMAGE_NAME .

                        echo "Image created successfully"
                        '''
                    } catch(err){
                        echo "Docker Image creation FAILED"
                        echo "Error details : ${err}"
                        currentBuild.result = 'FAILURE'
                        error("Stopping pipeline due to Docker Image creation failure")
                    }
                }
            }
        }

        stage('Docker Container Creation'){
            steps{
                script{
                    echo "Docker Container creation & running Tests"

                    catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                        sh '''
                        echo "Running Docker container"
                        docker run --name $CONTAINER_NAME $IMAGE_NAME
                        '''
                    }

                    echo "Tests execution stage completed (pass or fail)"
                }
            }
        }
    }

    post {
        always {
            sh '''
            docker rm -f $CONTAINER_NAME || true
            docker rmi -f $IMAGE_NAME || true
            '''
        }
    }
}