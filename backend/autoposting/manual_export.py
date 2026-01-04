def export(content, filename="manual_post.txt"):
    with open(filename, "w") as f:
        f.write(content)
    return filename
