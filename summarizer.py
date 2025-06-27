from transformers import pipeline

def summarize_article(text, max_length=130, min_length=30):
    # Load the summarization pipeline
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Generate the summary
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)

    return summary[0]['summary_text']

# Example input: A long article
article_text = """
OpenAI has recently launched a new version of ChatGPT that allows users to interact through voice and image prompts. This marks a major milestone in the field of AI as it enables multimodal interactions, making the model more flexible and human-like. The voice capability uses a new text-to-speech model, while image understanding is powered by GPT-4 with vision. This update makes ChatGPT not only a powerful chatbot for text, but also an assistant that can see and speak.
Users can now take pictures of a broken appliance and ask for repair advice or snap a photo of a meal and ask for the recipe. These features are being rolled out gradually and will be available for Plus users in the coming weeks.
"""

# Call the summarizer
summary = summarize_article(article_text)

# Output the result
print("Original Article:\n", article_text)
print("\nSummary:\n", summary)

