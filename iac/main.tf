terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.82.2"
    }
  }
  backend "s3" {
    bucket  = "monkey-euc1-s3-terraform-state"
    key     = "outbox-pattern/terraform.tfstate"
    region  = "eu-central-1"
    profile = "personal"
    encrypt = true
  }
}

provider "aws" {
  region  = "eu-central-1"
  profile = "personal"
}

#FIXED MODULES
module "lambda-policy" {
  source        = "./modules/iam-policy"
  name          = "monkey-euc1-policy-outbox-pattern-lambda-policy"
  description   = "Policy to access the secret, dynamodb and topic/subscriptions"
  policy        = {
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "*"
      },
      {
        Action = [
          "xray:PutTraceSegments",
          "xray:PutTelemetryRecords"
        ],
        Effect = "Allow",
        Resource = "*"
      },
      {
        Effect   = "Allow",
        Action   = [
          "dynamodb:DescribeStream",
          "dynamodb:GetRecords",
          "dynamodb:GetShardIterator",
          "dynamodb:ListStreams"
        ],
        Resource = "*"
      },
      {
        Effect   = "Allow",
        Action   = [
          "sns:Publish"
        ],
        Resource = "*"
      }
    ]
  }
  tags          = {
    owner   = "amundaray24"
    project = "monkey-architecture"
    contact = "https://github.com/amundaray24"
  }
}

module "lambda-role" {
  source      = "./modules/role"
  name        = "monkey-euc1-role-outbox-pattern-lambda-role"
  service     = "lambda.amazonaws.com"
  policy-arn  = module.lambda-policy.arn
  depends_on  = [module.lambda-policy]
  tags        = {
    owner   = "amundaray24"
    project = "monkey-architecture"
    contact = "https://github.com/amundaray24"
  }
}

module "bucket-code" {
  source      = "./modules/s3"
  name        = "monkey-euc1-s3-outbox-pattern-code"
  tags          = {
    owner   = "amundaray24"
    project = "monkey-architecture"
    contact = "https://github.com/amundaray24"
  }
}

#DYNAMICS MODULES
module "buckets" {
  source    = "./controllers/buckets"
  resources = var.buckets
  tags      = var.tags
}

module "topics" {
  source    = "./controllers/topics"
  resources = var.topics
  tags      = var.tags
}

module "subscriptions" {
  source      = "./controllers/subscriptions"
  resources   = var.subscriptions
  topics-arn  = module.topics.arn-list
  tags        = var.tags
  depends_on = [module.topics]
}

module "dynamo" {
  source          = "./controllers/dynamo"
  resources       = var.dynamo
  tags            = var.tags
}

module "lambdas" {
  source      = "./controllers/lambdas"
  resources   = var.lambdas
  role-arn    = module.lambda-role.arn
  filename    = "./binaries/function.zip"
  tags        = var.tags
}