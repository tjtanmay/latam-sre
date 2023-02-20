resource "kubernetes_namespace" "flight-app" {
  metadata {
    name = "flight-app"
  }
}