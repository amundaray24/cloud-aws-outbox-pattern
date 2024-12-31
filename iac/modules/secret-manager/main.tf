resource "aws_secretsmanager_secret" "this" {
  name                    = var.name
  description             = var.description
  recovery_window_in_days = var.recovery-window-in-days
  tags = {
    owner       = "amundaray24"
    project     = "monkey-architecture"
    environment = "dev"
    contact     = "https://github.com/amundaray24"
  }
}