resource "aws_iam_role" "this" {
  name                = var.name
  assume_role_policy  = jsonencode({
   Version =  "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = var.service
        }
      }
    ]
  })
  tags = {
    owner       = "amundaray24"
    project     = "monkey-architecture"
    environment = "dev"
    contact     = "https://github.com/amundaray24"
  }
}

resource "aws_iam_role_policy_attachment" "policy-attachment" {
  role        = aws_iam_role.this.name
  policy_arn  = var.policy-arn
}