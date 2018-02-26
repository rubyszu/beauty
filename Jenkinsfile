pipeline {
	agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
            }
        }
        stage('Test') {
            steps {
                sh './a.sh'
            }
        }
        stage('Lint & xxx') {
            steps {
                sh 'cd pmd-example && ./run.sh'
                sh 'cd ..'
            }
        }
        

    }
    post {
        always {
            echo 'This will always run'
            junit 'results.xml'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}