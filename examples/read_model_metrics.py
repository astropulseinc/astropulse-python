"""Read one model's inference metrics: latency percentiles, time to first
token, token rates, queue depth and KV cache, the same numbers the console
shows.

Run it with::

    export ASTROPULSE_API_KEY=...
    python examples/read_model_metrics.py qwen-chat          # optionally: 15m
"""

import sys

from astropulse import Client

if len(sys.argv) < 2:
    raise SystemExit(f"usage: {sys.argv[0]} <application> [window, default 15m]")
APP = sys.argv[1]
WINDOW = sys.argv[2] if len(sys.argv) > 2 else "15m"

FIELDS = [
    ("request_count", "requests measured", "{:.0f}"),
    ("requests_per_second", "requests/s", "{:.3f}"),
    ("request_latency_p50_seconds", "latency p50", "{:.3f} s"),
    ("request_latency_p95_seconds", "latency p95", "{:.3f} s"),
    ("request_latency_p99_seconds", "latency p99", "{:.3f} s"),
    ("time_to_first_token_p50_seconds", "TTFT p50", "{:.3f} s"),
    ("time_to_first_token_p95_seconds", "TTFT p95", "{:.3f} s"),
    ("time_per_output_token_p50_seconds", "per-output-token p50", "{:.4f} s"),
    ("prompt_tokens_per_second", "prompt tokens/s", "{:.1f}"),
    ("generation_tokens_per_second", "generated tokens/s", "{:.1f}"),
    ("requests_running", "running", "{:.2f}"),
    ("requests_waiting", "queued", "{:.2f}"),
    ("kv_cache_utilization", "KV cache used", "{:.1%}"),
    ("measured_seconds", "seconds of coverage", "{:.0f}"),
]


def main() -> int:
    client = Client()
    series = client.applications.get_application_metrics_series(app_name=APP, window=WINDOW).data
    summary = getattr(series, "inference_summary", None)

    if not summary:
        # Said plainly rather than printed as zeros: a model that has served
        # nothing and a model whose metrics are not arriving look identical in
        # a table of zeroes, and they need different fixes.
        print(f"{APP}: no inference summary for the last {WINDOW}.")
        print("Either nothing has called the model, or the agent is not reading")
        print("the predictor's metrics port.")
        return 1

    print(f"{APP} — inference over {WINDOW} ({summary.runtime_name or summary.runtime})")
    for attr, label, fmt in FIELDS:
        value = getattr(summary, attr, None)
        if value is not None:
            print(f"  {label:<22} {fmt.format(value)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
