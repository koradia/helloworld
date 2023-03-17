pipeline {
   agent any
     stages {
        stage('clone git') {
              steps {
                    sh "chmod u+x helloworld.py"
                    git 'https://github.com/BThangaraju/Jenkins.git'
                    }
        }
        stage('Build Code') {
               steps {
                     sh "chmod u+x prog1.py"
                     sh "./prog1.py"
                     }
        }
         stage('Test Code') {
               steps {
                      sh "chmod u+x test.py"
                      sh "./test.py"
                     }
         }
       }
}
