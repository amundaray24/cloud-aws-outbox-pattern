# 🌩️ AWS Outbox Pattern

## 🏗️ Infrastructure (`/iac`)

The `/iac` directory contains the Terraform configuration for the project's infrastructure. Here, providers, modules, and resources necessary to deploy the infrastructure on AWS are defined.

### 📄 Main Files

- `main.tf`: Main Terraform configuration file that includes the definition of providers and modules.

### 📦 Modules

- `modules/s3`: S3 module configuration.
- `modules/sns`: SNS module configuration.
- `modules/sqs`: SQS module configuration.
- `modules/dynamo`: DynamoDB module configuration.
- `modules/layer`: Lambda Layer module configuration.
- `modules/iam-policy`: IAM policies module configuration.
- `modules/role`: IAM roles module configuration.
- `modules/s3-resource`: S3 resources module configuration.
- `modules/lambda`: Lambda module configuration.
- `modules/event-mapping`: Event mapping module configuration.
- `modules/secrets-manager`: Secrets Manager module configuration.

## 💻 Code (`/src`)

The `/src` directory contains the project's source code, including Lambda functions and utilities.

### 🐍 Lambdas

- `action-splitter`: Lambda function responsible for splitting actions.
  - **Code Path**: `src/lambdas/lambda_outbox_pattern_action_splitter`
  - **Handler**: `function.handler`
  - **Runtime**: `python3.13`
  - **Dependencies**: `requirements.txt`

### 🛠️ Utilities

- `logger`: Contains logging setup and utility functions for consistent logging across the project.
  - **Code Path**: `src/utils/lambda_utils_logger`
  - **Description**: Provides a standardized logging configuration to be used by all Lambda functions.

- `secret manager`: Contains helper functions that are used across multiple Lambda functions to interact with AWS Secrets Manager.
  - **Code Path**: `src/utils/lambda_utils_secret_manager`
  - **Description**: Provides common utility functions for interacting with AWS Secrets Manager.

- `xray`: Contains helper functions for interacting with AWS Xray services.
  - **Code Path**: `src/utils/lambda_utils_xray`
  - **Description**: Provides utility functions for common AWS Xray operations such as starting and ending traces.


## 🗂️ Project Structure

```plaintext
.
├── iac
│   ├── main.tf
│   └── modules
│       ├── s3
│       ├── sns
│       └── ...
└── src
    ├── lambdas
    │   ├── lambda_outbox_pattern_action_splitter
    │   └── ...
    └── utils
        ├── lambda_utils_logger
        └── ...