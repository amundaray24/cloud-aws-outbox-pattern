module "resources" {
  for_each  = { for resource in var.resources: resource.name => resource }
  source                    = "../../modules/dynamo"
  name                      = each.value.name
  hash-key-name             = each.value.hash-key-name
  range-key-name            = each.value.range-key-name
  billing-mode              = each.value.billing-mode
  stream-enabled            = each.value.stream-enabled
  stream-view-type          = each.value.stream-view-type
  attributes                = each.value.attributes
  global-secondary-indexes  = each.value.global-secondary-indexes
  tags                      = var.tags
}