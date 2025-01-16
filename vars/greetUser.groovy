stage('Greet User') {
    steps {
        script {
            // Calling greetUser function from the vars directory in the shared library
            greetUser('Gowtham')
        }
    }
}

