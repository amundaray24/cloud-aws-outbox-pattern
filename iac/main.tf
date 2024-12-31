terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.82.2"
    }
  }
}

provider "aws" {
  region  = "eu-central-1"
  profile = "personal"
}

# module "secret" {
#   source                  = "./modules/secret-manager"
#   name                    = "monkey-euc1-secret-outbox-pattern"
#   description             = "Secret Manager for the outbox pattern"
#   recovery-window-in-days = 0
# }

module "bucket" {
  source  = "./modules/s3"
  name    = "monkey-euc1-s3-outbox-pattern"
}

module "topic" {
  source      = "./modules/sns"
  name        = "monkey-euc1-sns-outbox-pattern.fifo"
}

module "insert-sub" {
  source              = "./modules/sqs"
  name                = "monkey-euc1-sqs-outbox-pattern-insert-sub"
  topic-arn           = module.topic.arn
  retention-time      = 604800
  depends_on          = [module.topic]
  visibility-timeout  = 30
  filter-policy   = {
    "operation": ["INSERT"]
  }
}

module "modify-sub" {
  source              = "./modules/sqs"
  name                = "monkey-euc1-sqs-outbox-pattern-modify-sub"
  topic-arn           = module.topic.arn
  retention-time      = 604800
  depends_on          = [module.topic]
  visibility-timeout  = 30
  filter-policy   = {
    "operation": ["MODIFY"]
  }
}

module "remove-sub" {
  source              = "./modules/sqs"
  name                = "monkey-euc1-sqs-outbox-pattern-remove-sub"
  topic-arn           = module.topic.arn
  retention-time      = 604800
  depends_on          = [module.topic]
  visibility-timeout  = 30
  filter-policy   = {
    "operation": ["REMOVE"]
  }
}

module "table" {
  source          = "./modules/dynamo"
  name            = "monkey-euc1-dynamo-outbox-pattern"
  hash-key-name   = "id"
  hash-key-type   = "S"
  range-key-name  = "created_at"
  range-key-type  = "S"
  billing-mode    = "PAY_PER_REQUEST"
}

module "layer-code" {
  source      = "./modules/s3-resource"
  bucket-name = "monkey-euc1-s3-outbox-pattern"
  key         = "layers/python3.13-layer.zip"
  path        = "${path.module}/binaries/layers/python3.13-layer.zip"
  depends_on  = [module.bucket]
}

module "layer" {
  source              = "./modules/layer"
  name                = "monkey-euc1-layer-outbox-pattern"
  description         = "Lambda Layer for the outbox pattern"
  s3-bucket           = "monkey-euc1-s3-outbox-pattern"
  s3-key              = "layers/python3.13-layer.zip"
  compatible-runtimes = ["python3.13"]
  depends_on          = [module.layer-code]
}

module "lambda-policy" {
  source        = "./modules/iam-policy"
  name          = "monkey-euc1-policy-outbox-pattern-lambda-policy"
  description   = "Policy to access the secret, dynamodb and topic/subscriptions"
  policy        = {
    Version = "2012-10-17"
    Statement = [
      # {
      #   Effect   = "Allow",
      #   Action   = ["secretsmanager:GetSecretValue"],
      #   Resource = module.secret.arn
      # },
      {
        Effect   = "Allow",
        Action   = [
          "dynamodb:DescribeStream",
          "dynamodb:GetRecords",
          "dynamodb:GetShardIterator",
          "dynamodb:ListStreams"
        ],
        Resource = module.table.stream-arn
      },
      {
        Effect   = "Allow",
        Action   = [
          "sns:Publish"
        ],
        Resource =module.topic.arn
      },
      {
        Effect   = "Allow"
        Action   = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "arn:aws:logs:*:*:*"
      },
      {
        Action = [
          "xray:PutTraceSegments",
          "xray:PutTelemetryRecords"
        ],
        Effect = "Allow",
        Resource = "*"
      }
    ]
  }
  # depends_on    = [module.secret, module.table, module.topic]
  depends_on    = [module.table, module.topic]
}

module "lambda-role" {
  source      = "./modules/role"
  name        = "monkey-euc1-role-outbox-pattern-lambda-role"
  service     = "lambda.amazonaws.com"
  policy-arn  = module.lambda-policy.arn
  depends_on  = [module.lambda-policy]
}

module "action-splitter-code" {
  source      = "./modules/s3-resource"
  bucket-name = "monkey-euc1-s3-outbox-pattern"
  key         = "lambdas/action-splitter.zip"
  path        = "${path.module}/binaries/lambdas/action-splitter.zip"
  depends_on  = [module.bucket]
}

module "action-splitter-function" {
  source                = "./modules/lambda"
  name                  = "monkey-euc1-lambda-outbox-pattern-action-splitter"
  runtime               = "python3.13"
  handler               = "function.handler"
  role-arn              = module.lambda-role.arn
  s3-bucket             = "monkey-euc1-s3-outbox-pattern"
  s3-key                = "lambdas/action-splitter.zip"
  time-out              = 30
  layers-arn            = [module.layer.arn]
  alias-name            = "active"
  environment-variables = {
    AWS_ACCOUNT_ID                     = "123456789012"
    LOG_LEVEL                          = "INFO"
    APP_ACTION_SPLITTER_SNS_TOPIC_NAME = "monkey-euc1-sns-outbox-pattern.fifo"

  }
  depends_on = [module.action-splitter-code, module.lambda-role, module.layer]
}

module "action-splitter-event-mapping" {
  source              = "./modules/event-mapping"
  source-arn          = module.table.stream-arn
  lambda-arn          = module.action-splitter-function.arn
  starting-position   = "LATEST"
  batch-size          = 5
  depends_on          = [module.table, module.action-splitter-function]
  lambda-alias-name   = "active"
}