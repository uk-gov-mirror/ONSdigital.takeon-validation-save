#!/usr/bin/env bash

cd save-deploy-repository
echo Packaging serverless bundle...
serverless package --package pkg
echo Deploying to AWS...
serverless deploy --verbose;
