"""A request through the whole client, against a local server: the path, the method, the key header,
the query and the typed response. Unit tests reach into pieces; this fails when a regeneration
breaks the wire."""

from __future__ import annotations

import json
import threading
from collections.abc import Iterator
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any

import pytest

from astropulse import Client
from astropulse.models import ClusterStatus, K8sClusterListResponse, Provider

LISTING = {
    "status": "success",
    "data": [{"clusterName": "demo", "provider": "aws", "state": "Ready"}],
}


class _Recorder(BaseHTTPRequestHandler):
    seen: list[dict[str, Any]] = []

    def do_GET(self) -> None:
        _Recorder.seen.append(
            {"method": "GET", "path": self.path, "key": self.headers.get("X-Astro-API-Key")}
        )
        body = json.dumps(LISTING).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: Any) -> None:
        pass


@pytest.fixture
def server() -> Iterator[str]:
    _Recorder.seen = []
    httpd = HTTPServer(("127.0.0.1", 0), _Recorder)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{httpd.server_address[1]}"
    httpd.shutdown()
    httpd.server_close()


def test_listing_clusters_round_trips(server: str) -> None:
    ap = Client("test-key", base_url=server, retries=None)
    listing = ap.clusters.list_clusters(provider_id="aws")
    ap.close()

    assert _Recorder.seen == [
        {"method": "GET", "path": "/api/v1/clusters?providerId=aws", "key": "test-key"}
    ]
    assert isinstance(listing, K8sClusterListResponse)
    assert listing.data is not None
    assert [(c.cluster_name, c.provider, c.state) for c in listing.data] == [
        ("demo", Provider.Aws, ClusterStatus.Ready)
    ]
