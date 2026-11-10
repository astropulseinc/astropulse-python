"""Every cluster in the organization, and what it is running.

Run it with::

    export ASTROPULSE_API_KEY=...
    python examples/list_clusters.py
"""

from astropulse import Client

ap = Client()
for cluster in ap.clusters.list_clusters().data or []:
    print(f"{cluster.cluster_name:30} {cluster.state.value if cluster.state else ''}")
