#!/usr/bin/env python3

from eleven_tts import tts, ApiClient
import os
from attrdict import AttrDict as ad

api_key = os.environ.get("ELEVENLABS_API_TOKEN", None) or input(
    "On the ElevenLabs website, click Profile, copy your the API key and paste it here, " + 
    "or set it as the ELEVENLABS_API_TOKEN environment variable:"
)

api_client = ApiClient()
api_client.configuration.host = "https://api.elevenlabs.io"
samples = tts.samples_api.SamplesApi(api_client=api_client)
history = tts.history_api.HistoryApi(api_client=api_client)
o = history.get_generated_items_v1_history_get(xi_api_key=api_key)
print(o.history[-1])
