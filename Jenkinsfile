pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhubcredentials') 
        PATH = "/bin:/usr/bin:/usr/local/bin:$PATH"
    }
    
    stages {
        stage("Git Checkout") {
            steps {
                git credentialsId: 'githubpassword', url: 'https://github.com/nishant-cloudoric/mapi.git'
                echo 'Git Checkout Completed'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh "docker build -t thecyberbaby/mapi:$BUILD_NUMBER ."
                echo 'Build Image Completed'
            }
        }
        
        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhubcredentials', usernameVariable: 'DOCKERHUB_CREDENTIALS_USR', passwordVariable: 'DOCKERHUB_CREDENTIALS_PSW')]) {
                    sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                    echo 'Login Completed'
                }
            }
        }
        
        stage('Push Image to Docker Hub') {
            steps {
                sh "docker push thecyberbaby/mapi:$BUILD_NUMBER"
                echo 'Push Image Completed'
            }
        }
    }
    
    post {
        always {
            sh 'docker logout'
        }
    }
}
