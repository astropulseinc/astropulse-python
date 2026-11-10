"""Register the organization's Hugging Face token, once.

Every gated model then deploys without a per-application secret.

Run it with::

    export ASTROPULSE_API_KEY=...
    python examples/connect_huggingface.py hf_xxx
"""

import sys

from astropulse import Client
from astropulse.models import HuggingFaceIntegrationRequest

if len(sys.argv) < 2:
    raise SystemExit(f"usage: {sys.argv[0]} <hugging-face-token>")

ap = Client()
ap.integrations.connect_huggingface(HuggingFaceIntegrationRequest(token=sys.argv[1]))
# Print the fields the API wrote; a model's repr shows its enums raw.
status = ap.integrations.get_huggingface_integration().data
if status:
    print(status.state.value if status.state else "")
    if status.message:
        print(status.message)
