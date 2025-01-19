data "aws_dynamodb_table" "dynamo-table" {
  name  = var.name
}