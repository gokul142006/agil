pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Parallel Checks') {
            parallel {
                stage('Frontend Check') {
                    steps {
                        sh 'python3 frontend_check.py'
                    }
                }

                stage('Backend Check') {
                    steps {
                        sh 'python3 backend_check.py'
                    }
                }
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'frontend_report.txt,backend_report.txt',
                                 fingerprint: true
            }
        }
    }
}