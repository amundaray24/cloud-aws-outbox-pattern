#!/bin/bash

echo "copping the lambda code to the output folder"
cp ../../src/lambdas/lambda_outbox_pattern_action_splitter/function.py .

echo "compressing splitter"
zip -r lambdas/action-splitter.zip function.py

echo "delete the lambda code"
rm -rf function.py

echo "!Success! The lambda code has been generated and compressed"