data "aws_lambda_layer_version" "layers" {
  for_each = { for resource in var.resources: resource.name => resource }
  layer_name  = each.value.name
  version     = each.value.version
}