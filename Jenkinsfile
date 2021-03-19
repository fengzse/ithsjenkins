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
         stage('Robot Framework System tests with Selenium') {
            steps {
                 sh 'robot --variable BROWSER:headlesschrome -d TestLabAuto/Results  TestLabAuto/Tests'
                 }
            post {
                  always {
                        script {
                               step(
                                    [
                                     $class              : 'RobotPublisher',
                                      outputPath          : 'TestLabAuto/Results',
                                      outputFileName      : '**/output.xml',
                                      reportFileName      : '**/report.html',
                                      logFileName         : '**/log.html',
                                      disableArchiveOutput: false,
                                      passThreshold       : 50,
                                      unstableThreshold   : 40,
                                      otherFiles          : "**/*.png,**/*.jpg",
                                      ]
                               )
                        }
                  }
            }
         }
         stage ('Build'){
             	steps("SeleniumTest") {
         	        sh "mvn clean install"
                }
                dir("comtest/target") {
         	        sh "java -jar com.test-1.0-SNAPSHOT.jar"
                }
         }
    }
}