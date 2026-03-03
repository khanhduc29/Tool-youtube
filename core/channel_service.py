from core.youtube_api import search_channels, get_channel_details


def scan_channels_by_keyword(keyword: str, max_results=20):
    data = search_channels(keyword, max_results)

    if not data or "items" not in data:
        return []

    results = []

    for item in data["items"]:
        channel_id = item["snippet"]["channelId"]
        detail = get_channel_details(channel_id)

        if not detail or not detail.get("items"):
            continue

        info = detail["items"][0]
        snippet = info["snippet"]
        stats = info["statistics"]

        results.append({
            "name": snippet["title"],
            "channel_id": channel_id,
            "channel_url": f"https://youtube.com/channel/{channel_id}",
            "avatar": snippet["thumbnails"]["default"]["url"],
            "subscribers": int(stats.get("subscriberCount", 0)),
            "total_videos": int(stats.get("videoCount", 0)),
            "total_views": int(stats.get("viewCount", 0)),
            "created_at": snippet["publishedAt"],
            "description": snippet["description"]
        })

    return results