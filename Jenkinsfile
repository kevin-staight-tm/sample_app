node {
   def commit_id
   stage('Preparation') {
     checkout scm
     sh "git rev-parse --short HEAD > .git/commit-id"                        
     commit_id = readFile('.git/commit-id').trim()
   }
   stage('run docker') {
      sh "docker build -t kstaight/python-app-example:${commit_id} ."
      sh "docker run -p 9000:9000 kstaight/python-app-example:${commit_id}"
   }
//    stage('docker build/push') {
//      docker.withRegistry('https://index.docker.io/v1/', 'dockerhub') {
//        def app = docker.build("kstaight/python-app-example:${commit_id}", '.')
//         app.run("-p9000:9000")
//      }
//    }
}
