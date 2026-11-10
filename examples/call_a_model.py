"""Call a model the platform is serving, using the endpoint it reports.

The SDK's job here is the first half: ask the platform where the model answers
and which access policy guards it. The call itself is ordinary HTTP against an
OpenAI-compatible endpoint, so it needs the `openai` package or `requests` --
nothing AstroPulse-specific.

Run it with::

    pip install "astropulse[examples] @ git+https://github.com/astropulseinc/astropulse-python"

    export ASTROPULSE_API_KEY=...     # your platform key
    export MODEL_KEY=...              # a key the endpoint's access policy accepts
    python examples/call_a_model.py qwen-chat
"""

import os
import sys

import requests

from astropulse import Client


def main() -> int:
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} <application>")
        return 2
    application = sys.argv[1]

    model_key = os.environ.get("MODEL_KEY")
    if not model_key:
        print("MODEL_KEY is required: a key from the Secret the access policy names")
        return 2

    # 1. Ask the platform where this model answers and who may call it.
    client = Client()
    endpoint = client.applications.get_application_endpoint(app_name=application).data
    if endpoint is None or not endpoint.url:
        print(f"{application} has no open endpoint; nothing to call")
        return 1

    print(f"endpoint : {endpoint.url}")
    print(f"policy   : {endpoint.policy} (revision {endpoint.policy_revision})")
    print(f"phase    : {endpoint.phase.value if endpoint.phase else ''}")

    # 2. The runtime answers to one model id, and the platform reports it:
    #    neither the name the application was deployed under nor the model's
    #    repository id is that value.
    deployed = client.applications.get_application(app_name=application).data
    served = deployed.model.served_model_name if deployed and deployed.model else None
    if not served:
        print(f"{application} reports no served model name; nothing to call")
        return 1
    authorization = {"Authorization": f"Bearer {model_key}"}
    print(f"model    : {served}")

    # The endpoint says the same thing, for anyone who would rather ask.
    listing = requests.get(f"{endpoint.url}/models", headers=authorization, timeout=60)
    listing.raise_for_status()
    print(f"serves   : {[m['id'] for m in listing.json()['data']]}")

    # 3. Call it.
    answer = requests.post(
        f"{endpoint.url}/chat/completions",
        headers=authorization,
        json={
            "model": served,
            "messages": [{"role": "user", "content": "Say hi"}],
            "max_tokens": 16,
        },
        timeout=120,
    )
    answer.raise_for_status()
    body = answer.json()
    print("reply    :", body["choices"][0]["message"]["content"].strip())
    print("usage    :", body.get("usage"))

    # 4. And show that the policy is enforced: the same call without a key.
    refused = requests.post(
        f"{endpoint.url}/chat/completions",
        json={"model": served, "messages": [{"role": "user", "content": "hi"}]},
        timeout=60,
    )
    print(f"no key   : {refused.status_code} (401 means the endpoint refused it)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
