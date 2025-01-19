output "layers-arn" {
  value = { for key, mod in data.aws_lambda_layer_version.layers : mod.layer_name => mod.arn }
}