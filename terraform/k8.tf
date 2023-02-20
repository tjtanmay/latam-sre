locals {
 flightapp_labels = {
   App = "flight-app"
   Tier = "frontend"
 }
}

resource "kubernetes_deployment" "flight-app" {
 metadata {
   name = "flight-app"
   labels = local.flightapp_labels
 }
 spec {
   replicas = 1
   selector {
     match_labels = local.flightapp_labels
   }
   template {
     metadata {
       labels = local.flightapp_labels
     }
     spec {
       container {
         image = "tjtanmay25/app"
         name  = "flight-app"
         port {
           container_port = 5000
         }
       }
     }
   }
 }
}

resource "kubernetes_service" "flight-app-service" {
 metadata {
   name = "flight-app-service"
 }
 spec {
   selector = local.flightapp_labels
   port {
     port        = 5000
     target_port = 5000
     node_port = 32001
   }
   type = "LoadBalancer"
 }
}