pipeline {
    agent any
    triggers {
        // Execute pipeline every 7 days
         cron('H H */7 * *')
         
    }
    stages {
        stage('Build') {
            steps {
               echo '🔐 Cloning private GitHub repository...'
               git branch: 'main',
               url:  'https://github.com/dhruvaK524/SDETTestDhruva.git',
               credentialsId: 'student-api'
                echo '✅ Repository successfully cloned and workspace is ready for the next stage!'
                echo 'Building the project...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
    post {
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
