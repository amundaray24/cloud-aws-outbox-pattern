output "tables-arn" {
  value = try(data.aws_dynamodb_table.dynamo-table.arn,null)
}

output "streams-arn" {
  value = try(data.aws_dynamodb_table.dynamo-table.stream_arn,null)
}