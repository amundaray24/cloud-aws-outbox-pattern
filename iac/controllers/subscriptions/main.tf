module "resources" {
  for_each  = { for resource in var.resources: resource.name => resource }
  source                  = "../../modules/sqs"
  topic-arn               = var.topics-arn[each.value.topic]
  name                    = each.value.name
  retention-time          = each.value.retention-time
  filter-policy           = each.value.filter-policy
  visibility-timeout      = each.value.visibility-timeout
  visibility-timeout-dlq  = 30
  tags                    = var.tags
}