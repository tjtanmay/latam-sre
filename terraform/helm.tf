

locals {
 flightapp_labels = {
   App = "flight-app"
   Tier = "frontend"
 }
}

resource "helm_release" "flightapp" {
 name  = "flight-app"
 chart = "${abspath(path.root)}/charts/flightapp-chart"
}
