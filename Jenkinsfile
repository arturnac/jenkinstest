pipeline {
  agent any
  stages {
    stage('stage1') {
      agent any
      environment {
        foo = 'bar'
      }
      steps {
        echo 'hello'
      }
    }

  }
  environment {
    foo = 'bar'
  }
}