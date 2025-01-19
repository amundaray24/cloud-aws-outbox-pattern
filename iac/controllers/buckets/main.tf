module "resources" {
  for_each  = { for resource in var.resources: resource.name => resource }
  source    = "../../modules/s3"
  name      = each.value.name
  tags      = var.tags
}