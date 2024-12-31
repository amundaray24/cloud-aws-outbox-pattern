resource "aws_iam_policy" "this" {
  name        = var.name
  description = var.description
  policy = jsonencode(var.policy)
  tags = {
    owner       = "amundaray24"
    project     = "monkey-architecture"
    environment = "dev"
    contact     = "https://github.com/amundaray24"
  }
}