resource "aws_dynamodb_table" "this" {
  name              = var.name
  billing_mode      = var.billing-mode
  hash_key          = var.hash-key-name
  range_key         = var.range-key-name
  stream_enabled    = var.stream-enabled
  stream_view_type  = var.stream-view-type
  tags              = var.tags

  dynamic "attribute" {
    for_each = var.attributes
    content {
      name = attribute.value.name
      type = attribute.value.type
    }
  }

  dynamic "global_secondary_index" {
    for_each = var.global-secondary-indexes
    content {
      name            = global_secondary_index.value.name
      hash_key        = global_secondary_index.value.hash-key
      projection_type = global_secondary_index.value.projection-type
    }
  }
}