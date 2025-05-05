def categorize_topics(topic_question_map):
    freq_map = {topic: len(questions) for topic, questions in topic_question_map.items()}
    sorted_topics = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

    total = len(sorted_topics)
    top_cut = int(total * 0.3)
    mid_cut = int(total * 0.7)

    categories = {
        "Most Important": sorted_topics[:top_cut],
        "Moderate Importance": sorted_topics[top_cut:mid_cut],
        "Less Likely": sorted_topics[mid_cut:]
    }

    return categories
