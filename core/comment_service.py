from core.youtube_api import get_video_comments
from core.classifier import classify_intent
from utils.language import detect_language


def scan_video_comments(video_id: str, max_results=20):
    data = get_video_comments(video_id, max_results)

    if not data or "items" not in data:
        return []

    results = []

    for item in data["items"]:
        comment_data = item["snippet"]["topLevelComment"]["snippet"]

        text = comment_data["textDisplay"]

        results.append({
            "author": comment_data["authorDisplayName"],
            "content": text,
            "language": detect_language(text),
            "intent": classify_intent(text),
            "likes": comment_data.get("likeCount", 0),
            "published_at": comment_data.get("publishedAt")
        })

    return results