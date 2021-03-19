pipeline{
    agent any
    stages{
        stage('Checkout'){
            steps{
                git 'https://github.com/fengzse/ithsjenkins.git'
            }
        }
        stage('Build'){
            steps{
                sh "mvn compile"  // "bat" for Windows, "sh" for MacOs and Linux
            }
        }
        stage('newman') {
            steps {
            sh 'newman run RestfulBooker_Feng/Restful_Booker_Feng_LabPostman.postman_collection.json --environment RestfulBooker_Feng/Restful_Booker_Feng.postman_environment.json --reporters junit'
            }
            post {
                always {
                        junit '**/*xml'
                }
            }
        }
        stage('Test'){
            steps{
                sh "mvn test"
            }
            post{
                always{
                    junit '**/TEST*.xml'
                    emailext attachLog: true, attachmentsPattern: '**/TEST*.xml', body:'',
                    recipientProviders:[culprits()],
                    subject:'$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS!'
                }
            }
        }
    }
}