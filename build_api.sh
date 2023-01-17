#!/usr/bin/env bash
swagger-codegen generate \
    -i https://api.elevenlabs.io/openapi.json \
    -l python \
    -o . \
    --model-name-prefix=eleven \
    --api-package=tts \
    --model-package=models \
    --additional-properties=packageName=eleven_tts
