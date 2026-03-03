# from core.channel_service import scan_channels_by_keyword
# from core.video_service import scan_videos_by_keyword
# from core.comment_service import scan_video_comments
# from utils.file_saver import save_json, save_csv


# def run():
#     keyword = input("🔎 Enter keyword: ")

#     print("\n=== CHANNELS ===")
#     channels = scan_channels_by_keyword(keyword)
#     for c in channels:
#         print(c)

#     save_json(channels, "channels", keyword)
#     save_csv(channels, "channels", keyword)

#     print("\n=== VIDEOS ===")
#     videos = scan_videos_by_keyword(keyword)
#     for v in videos:
#         print(v)

#     save_json(videos, "videos", keyword)
#     save_csv(videos, "videos", keyword)

#     if videos:
#         print("\n=== COMMENTS (First Video) ===")
#         comments = scan_video_comments(videos[0]["video_id"])
#         for c in comments:
#             print(c)

#         save_json(comments, "comments", keyword)
#         save_csv(comments, "comments", keyword)


# if __name__ == "__main__":
#     run()


from core.channel_service import scan_channels_by_keyword
from core.video_service import scan_videos_by_keyword
from core.comment_service import scan_video_comments
from utils.file_saver import save_json, save_csv


def extract_video_id(url: str):
    import re
    match = re.search(r"v=([^&]+)", url)
    return match.group(1) if match else None


def run():
    print("====== YOUTUBE TOOL ======")

    keyword = input("🔎 Keyword / Video URL: ")
    data_type = input("📂 Type (channel / video / comment): ").lower()
    limit_input = input("📊 Limit (default 20): ")

    limit = int(limit_input) if limit_input.isdigit() else 20

    # =============================
    # CHANNEL
    # =============================
    if data_type == "channel":
        data = scan_channels_by_keyword(keyword, max_results=limit)

        print("\n=== CHANNELS ===")
        for item in data:
            print(item)

        save_json(data, "channels", keyword)
        save_csv(data, "channels", keyword)

    # =============================
    # VIDEO
    # =============================
    elif data_type == "video":
        data = scan_videos_by_keyword(keyword, max_results=limit)

        print("\n=== VIDEOS ===")
        for item in data:
            print(item)

        save_json(data, "videos", keyword)
        save_csv(data, "videos", keyword)

    # =============================
    # COMMENT
    # =============================
    elif data_type == "comment":
        video_id = extract_video_id(keyword)

        if not video_id:
            print("❌ Invalid YouTube video URL")
            return

        data = scan_video_comments(video_id, max_results=limit)

        print("\n=== COMMENTS ===")
        for item in data:
            print(item)

        save_json(data, "comments", video_id)
        save_csv(data, "comments", video_id)

    else:
        print("❌ Invalid type. Choose channel / video / comment")


if __name__ == "__main__":
    run()