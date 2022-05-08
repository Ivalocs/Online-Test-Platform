pipeline {
  environment {
    Image_name = "psychik/online_test_platform"
    DockerHubCredential = 'psychik-dockerhub'
    Docker_image = ''
  }
  agent any
  stages {
    stage('Git Clone') {
      steps {
        git([url: 'https://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@github.com/Psychik-N/online_test_platform.git', branch: 'master', credentialsId: 'psychik-github'])

      }
    }
    stage('Build') {
	steps{
         sh "python3 manage.py migrate"
      }
    }
    stage('Build Docker Image') {
      steps{
        script {
          Docker_image = docker.build Image_name
        }
      }
    }
    stage('Deploy Image to Docker') {
      steps{
        script {
          docker.withRegistry( '', DockerHubCredential ) {
             Docker_image.push('latest')
          }
        }
      }
    }
    stage('Delete Docker Image') {
      steps{
         sh "docker rmi $Image_name:latest"
      }
    }

    stage("Run Ansible Playbook") {
      steps{
      ansiblePlaybook(
      	credentialsId: "container_access_key",
        inventory: "Inventory",
        installation: "ansible",
        limit: "",
        playbook: "docker_playbook.yaml",
        extras: ""
      )
    }
    }

  }
}
