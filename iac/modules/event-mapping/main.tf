resource "aws_lambda_event_source_mapping" "this" {
  event_source_arn  = var.source-arn
  function_name     = "${var.lambda-arn}:${var.lambda-alias-name}"
  starting_position = var.starting-position
  batch_size        = var.batch-size
}