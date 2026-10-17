pipeline {
    agent any

    environment {
        STUDENT_NAME = 'Stanislav'
        STUDENT_SURNAME = 'Pak'
        STUDENT_GROUP = 'IT2-2314'
        STUDENT_ID = '37845'
        IMAGE_NAME = 'pak-stanislav-devops'
        CONTAINER_NAME = 'pak-stanislav-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git rev-parse --short HEAD'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 -m compileall -q app'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s tests -v'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t "$IMAGE_NAME" .'
            }
        }
        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f "$CONTAINER_NAME" >/dev/null 2>&1 || true
                    docker run -d --name "$CONTAINER_NAME" \
                      -e STUDENT_NAME="$STUDENT_NAME" \
                      -e STUDENT_SURNAME="$STUDENT_SURNAME" \
                      -e STUDENT_GROUP="$STUDENT_GROUP" \
                      -e STUDENT_ID="$STUDENT_ID" \
                      "$IMAGE_NAME"
                    docker inspect -f '{{.State.Running}}' "$CONTAINER_NAME" | grep -q true
                    docker logs "$CONTAINER_NAME"
                '''
            }
        }
    }

    post {
        success {
            echo "Student: ${env.STUDENT_NAME} ${env.STUDENT_SURNAME}"
            echo "Group: ${env.STUDENT_GROUP}"
            echo "Student ID: ${env.STUDENT_ID}"
            echo "Git commit: ${env.GIT_COMMIT}"
        }
    }
}
