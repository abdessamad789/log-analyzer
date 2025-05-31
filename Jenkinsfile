pipeline {
    agent any
    stages {
        stage('Start') {
            steps {
                echo 'Début de l\'analyse des logs'
            }
        }
        stage('Analyze') {
            steps {
                // Si tu es sous Linux ou macOS
                sh 'python log_analyzer.py'

                // Si tu es sous Windows, utilise :
                // bat 'python log_analyzer.py'
            }
        }
        stage('End') {
            steps {
                echo 'Fin du pipeline'
            }
        }
    }
}
