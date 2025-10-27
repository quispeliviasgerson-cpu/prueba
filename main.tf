terraform {
  requiered_providers {
    local = {
      source = "hashicorp/local"
      version = "~>2.5.1"
      }
   }
}
provider "local" {}

#Variable opcional (para personalizar el nombre)
variable "nombre_servidor" {
  description = "Nombre del servidor simulado"
  type =string
  default ="Servidor_Prueba"
  }

  #Este recurso crea un archivo local que representa la 'infrestructura'

  resource "local_file" "infre" {
  filename= "${var.nombre_servidor}.txt"
  content = "Infraestructura simulada creada exitosamente. Timestamp: ${timestamp()}"
  }
