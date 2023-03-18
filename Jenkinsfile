pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/koradia/helloworld.git'
            }
        }
        stage('Build Code') {
            steps {
//                 sh "chmod u+x prog1.py"
//                 sh "./prog1.py"
                echo "tyui"
            }
        }
     stage('Test Code') {
            steps {
//                 sh "chmod u+x test.py"
//                 sh "./test.py"
            }
        }
    } 
}
