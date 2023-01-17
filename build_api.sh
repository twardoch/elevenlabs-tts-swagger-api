#!/usr/bin/env bash

# Install https://github.com/swagger-api/swagger-codegen 
# e.g. on macOS `brew install swagger-codegen` and then:

swagger-codegen generate \
    -i https://api.elevenlabs.io/openapi.json \
    -l python \
    -o . \
    --api-package=tts \
    --model-package=models \
    --additional-properties=packageName=eleven_tts

