def create_media(media_agent, shorts_agent, content):
    media = media_agent.run(content)
    shorts = shorts_agent.run(content)
    return {
        "media": media,
        "shorts": shorts
    }
