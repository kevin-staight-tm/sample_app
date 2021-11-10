node {
   def commit_id
   stage('Preparation') {
     checkout scm
     sh "git rev-parse --short HEAD > .git/commit-id"                        
     commit_id = readFile('.git/commit-id').trim()
   }
   try {
      stage('clean docker') {
         sh "/bin/bash -c \"docker ps -q --filter name=python_app | grep -q . && docker stop python_app && docker rm -fv python_app\""
//          sh "/bin/bas -c \"docker ps -q --filter name=python_app | grep -q . && docker stop python_app && docker rm -fv python_app\""

      }
      stage('run docker') {
         sh "docker build -t kstaight/python-app-example:${commit_id} ."
         sh "docker run -d -p 9000:9000 --name python_app kstaight/python-app-example:${commit_id}"
      }
   } catch(e) {
      sh "echo 'BUILD FAILED - STARTING FAILURE SCRIPT'"
      currentBuild.result = "FAILURE";
      def subject = "${env.JOB_NAME} - Build #${env.BUILD_NUMBER} ${currentBuild.result}"
      def content = '${JELLY_SCRIPT,template="html"}' //from plugin
      emailext(body: content, mimeType: 'text/html',
               replyTo: 'kstaight@hotmail.com', subject: subject,
               to: 'kstaight@hotmail.com', attachLog: true )
      throw e

//       def to = emailextrecipients([
//          [$class: 'CulpritsRecipientProvider'],
//          [$class: 'DevelopersRecipientProvider'],
//          [$class: 'RequesterRecipientProvider'],])
//       if(to != null && !to.isEmpty()) {
//          emailext(body: content, mimeType: 'text/html',
//                   replyTo: 'kstaight@hotmail.com', subject: subject,
//                   to: 'kstaight@hotmail.com', attachLog: true )
//       }
   }
   
//    stage('docker build/push') {
//      docker.withRegistry('https://index.docker.io/v1/', 'dockerhub') {
//        def app = docker.build("kstaight/python-app-example:${commit_id}", '.')
//         app.run("-p9000:9000")
//      }
//    }
}
