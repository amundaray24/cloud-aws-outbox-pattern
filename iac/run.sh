#!/bin/bash

# This script is used to run the terraform commands

resources_files=()
resources_files+=("buckets")
resources_files+=("dynamo")
resources_files+=("topics")
resources_files+=("subscriptions")
resources_files+=("lambdas")

command=$1
resources_params=

if [ -z "$command" ]; then
  echo "No command provided"
  exit 1
fi

for resource in "${resources_files[@]}"; do
  resources_params+="--var-file=resources/$resource.json "
done

echo "Running command: $command with params: $resources_params"

if [ "$command" == "init" ]; then
  terraform init
elif [ "$command" == "plan" ]; then
  terraform plan $resources_params
elif [ "$command" == "apply" ]; then
  terraform apply --auto-approve $resources_params
elif [ "$command" == "destroy" ]; then
  terraform destroy $resources_params
else
  echo "Command not supported"
  exit 1
fi