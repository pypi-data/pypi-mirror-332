import qbittorrentapi
from plexflow.core.downloads.candidates.download_candidate import DownloadCandidate
from typing import List


def schedule_download(magnet: str, category: str = None, tags: List[str] = ()):
    # instantiate a Client using the appropriate WebUI configuration
    conn_info = dict(
        host="192.168.1.50",
        port=8081,
        username="admin",
        password="adminadmin",
    )
    qbt_client = qbittorrentapi.Client(**conn_info)

    # or use a context manager:
    with qbittorrentapi.Client(**conn_info) as qbt_client:
        if qbt_client.torrents_add(
            urls=magnet, 
            save_path='/media/cloud2/mediacloud/tmp/torrents',
            content_layout='Subfolder',
            tags=tags,
            category=category) != "Ok.":
            raise Exception("Failed to add torrent.")
