from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def match_questions_to_topics(questions, topics, model):
    topic_embeddings = model.encode(topics)
    question_embeddings = model.encode(questions)

    matches = {topic: [] for topic in topics}

    for idx, q_emb in enumerate(question_embeddings):
        sims = cosine_similarity([q_emb], topic_embeddings)[0]
        best_match_idx = np.argmax(sims)
        best_topic = topics[best_match_idx]
        matches[best_topic].append(questions[idx])

    return matches
