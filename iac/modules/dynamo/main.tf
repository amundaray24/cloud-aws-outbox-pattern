resource "aws_dynamodb_table" "this" {
  name         = var.name
  billing_mode = var.billing-mode
  hash_key     = var.hash-key-name
  range_key    = var.range-key-name

  attribute {
    name = var.hash-key-name
    type = var.hash-key-type
  }

  attribute {
    name = var.range-key-name
    type = var.range-key-type
  }

  attribute {
    name = "subject"
    type = "S"
  }

  global_secondary_index {
    hash_key        = "subject"
    name            = "${var.name}-subject-index"
    projection_type = "ALL"
  }

  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"
  tags = {
    owner       = "amundaray24"
    project     = "monkey-architecture"
    environment = "dev"
    contact     = "https://github.com/amundaray24"
  }
}