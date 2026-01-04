class MediaAgent:
    def run(self, lesson_text):
        return {
            "image_prompt": f"Create an educational image for: {lesson_text[:200]}",
            "video_script": f"Video narration: {lesson_text}"
        }
