resource "aws_sqs_queue" "this" {
  name                        = "${var.name}.fifo"
  message_retention_seconds   = var.retention-time
  fifo_queue                  = true
  visibility_timeout_seconds  = var.visibility-timeout
  tags                        = var.tags
  depends_on                  = [aws_sqs_queue.dlq]
  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.dlq.arn
    maxReceiveCount     = 5
  })
}

resource "aws_sqs_queue" "dlq" {
  name                        = "${var.name}-dql.fifo"
  message_retention_seconds   = var.retention-time
  fifo_queue                  = true
  visibility_timeout_seconds  = var.visibility-timeout-dlq
  tags                        = var.tags
}

resource "aws_sns_topic_subscription" "subscription" {
  topic_arn             = var.topic-arn
  protocol              = "sqs"
  endpoint              = aws_sqs_queue.this.arn
  raw_message_delivery  = true
  filter_policy         = jsonencode(var.filter-policy)
}

resource "aws_sqs_queue_policy" "policy" {
  queue_url = aws_sqs_queue.this.id
  policy    = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect    = "Allow",
        Principal = "*",
        Action    = "sqs:SendMessage",
        Resource  = aws_sqs_queue.this.arn
        Condition = {
          ArnEquals = {
            "aws:SourceArn": var.topic-arn
          }
        }
      }
    ]
  })
}