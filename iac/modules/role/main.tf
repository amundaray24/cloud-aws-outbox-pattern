resource "aws_iam_role" "this" {
  name                = var.name
  tags                = var.tags
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
}

resource "aws_iam_role_policy_attachment" "policy-attachment" {
  role        = aws_iam_role.this.name
  policy_arn  = var.policy-arn
}