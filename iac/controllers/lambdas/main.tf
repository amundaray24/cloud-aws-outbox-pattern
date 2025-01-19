module "layers" {
  for_each  = { for resource in var.resources: resource.name => resource }
  source    = "../../data/layers"
  resources = [for layer in each.value.layers : layer]
}

module "streams" {
  for_each = {
    for resource in var.resources :
    resource.name => resource
    if lookup(resource, "dynamo-trigger", null) != null
  }
  source = "../../data/dynamo"
  name   = each.value.dynamo-trigger.table
}

module "dynamo-event-mapping" {
  for_each = {
    for resource in var.resources :
    resource.name => resource
    if lookup(resource, "dynamo-trigger", null) != null
  }
  source              = "../../modules/event-mapping"
  source-arn          = module.streams[each.value.name].streams-arn
  lambda-arn          = module.resources[each.value.name].arn
  starting-position   = each.value.dynamo-trigger.starting-position
  batch-size          = each.value.dynamo-trigger.batch-size
  lambda-alias-name   = "active"
  depends_on          = [module.resources, module.streams]
}

module "resources" {
  for_each              = { for resource in var.resources: resource.name => resource }
  source                = "../../modules/lambda"
  name                  = each.value.name
  runtime               = each.value.runtime
  handler               = each.value.handler
  filename              = var.filename
  role-arn              = var.role-arn
  time-out              = each.value.timeout
  layers-arn            = [for layer in each.value.layers : module.layers[each.value.name].layers-arn[layer.name]]
  environment-variables = each.value.environment-variables
  alias-name            = "active"
  tags                  = var.tags
  depends_on            = [module.layers]
}
