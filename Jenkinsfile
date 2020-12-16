pipeline
{
    environment {
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
 options
 {
  timestamps()
 }
 agent none
 stages
 {
  stage('Check scm')
  {
   agent any
   steps
   {
    checkout scm
   }
  } // stage Build
  stage('Build')
  {
      agent any
      steps{
          junit test.py
      }
   steps
   {
    echo "Building ...${BUILD_NUMBER}"
    echo "Build completed"
   }
  } // stage Build
  stage('Test')
  {
   agent
   {
    docker
    {
     image 'python:3.8.5'
     args '-u=\"root\"'
    }
   }
   steps
   {
    sh 'pip install --no-cache-dir -r ./Requirements.txt'
    sh 'python3 test.py'
   }
   post
   {
    always
    {
     junit 'test-reports/*.xml'
    }
    success
    {
     echo "Application testing successfully completed "
    }
    failure
    {
     echo "Oooppss!!! Tests failed!"
    }
   } // post
  }} // stage Test
}
