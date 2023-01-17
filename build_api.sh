#!/usr/bin/env bash
swagger-codegen generate \
    -i https://api.elevenlabs.io/openapi.json \
    -l python \
    -o . \
    --api-package=tts \
    --model-package=models \
    --additional-properties=packageName=eleven_tts
