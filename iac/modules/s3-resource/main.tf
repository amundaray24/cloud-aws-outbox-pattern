resource "aws_s3_object" "this" {
  bucket = var.bucket-name
  key    = var.key
  source = var.path
  tags = {
    owner       = "amundaray24"
    project     = "monkey-architecture"
    environment = "dev"
    contact     = "https://github.com/amundaray24"
  }
}