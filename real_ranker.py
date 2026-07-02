import json
import csv
import re
from datetime import datetime
from turtle import title

def load_candidates(file_path):
    candidates = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            candidates.append(json.loads(line))

    return candidates

def calculate_score(candidate):
    score = 0

    profile = candidate["profile"]
    summary = profile["summary"].lower()
    headline = profile["headline"].lower()
    if "retrieval" in summary or "retrieval" in headline:
        score += 20

    if "ranking" in summary or "ranking" in headline:
        score += 20

    if "embeddings" in summary or "embeddings" in headline:
        score += 20

    if "recommendation" in summary or "recommendation" in headline:
        score += 20
    skills = candidate["skills"]
    education = candidate["education"]
    for edu in education:
        if edu["tier"] == "tier_1":
            score += 15
        elif edu["tier"] == "tier_2":
            score += 10
        elif edu["tier"] == "tier_3":
            score += 5
    career = candidate["career_history"]
    for job in career:
        company = job["company"].lower()

        if "google" in company:
            score += 20
        elif "microsoft" in company:
            score += 20
        elif "amazon" in company:
            score += 15
        elif "meta" in company:
            score += 15
        elif "openai" in company:
            score += 25
    signals = candidate["redrob_signals"]


    # Experience
    experience = profile["years_of_experience"]
    if experience >= 8:
        score += 30
    elif experience >= 5:
        score += 20
    elif experience >= 3:
        score += 10

    # Career history
    for job in career:
        description = job["description"].lower()
        title = job["title"].lower()

    if "ai engineer" in title:
        score += 25
    elif "machine learning" in title:
        score += 25
    elif "data scientist" in title:
        score += 20
    elif "ml engineer" in title:
        score += 25
    elif "backend engineer" in title:
        score += 8
        text = (
    profile["headline"].lower() + " " +
    profile["summary"].lower() + " " +
    description
)

        if "recommendation" in text:
            score += 15

        if "ranking" in text:
            score += 15

        if "retrieval" in text:
            score += 15

        if "embedding" in text:
            score += 15

        if "llm" in text:
            score += 15
        if "pinecone" in text:
            score += 20

        if "milvus" in text:
            score += 20

        if "qdrant" in text:
            score += 20

        if "weaviate" in text:
            score += 20

        # Open to work
        if signals["open_to_work_flag"]:
            score += 15

        # Recruiter response rate
        if signals["recruiter_response_rate"] >= 0.8:
            score += 20
        elif signals["recruiter_response_rate"] >= 0.5:
            score += 10

        # Relocation
        if signals["willing_to_relocate"]:
            score += 10

        # Notice period
        if signals["notice_period_days"] <= 15:
            score += 10
        elif signals["notice_period_days"] <= 30:
            score += 5

    # Python skill
    for skill in skills:
        if "Python" in skill["name"]:
            score += 15

    # AI Skills
    ai_keywords = [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "LLM",
        "Fine-tuning LLMs",
        "LoRA",
        "PEFT",
        "NLP",
        "Embeddings",
        "Sentence Transformers",
        "Vector Database",
        "Pinecone",
        "Milvus",
        "Qdrant",
        "Weaviate",
        "FAISS",
        "OpenSearch",
        "Elasticsearch",
        "Retrieval",
        "RAG",
        "Ranking",
        "Recommendation Systems",
        "TensorFlow",
        "PyTorch",
        "Hugging Face",
        "BGE",
        "E5",
        "XGBoost"
        "LangChain",
        "LlamaIndex",
        "OpenAI",
        "Gemini",
        "Transformers",
        "BERT",
        "Prompt Engineering",
        "Generative AI",
        "Agentic AI",
        "Vector Search",
        "Semantic Search",
        "Knowledge Graph",
        "MLOps",
        "Docker",
        "Kubernetes",
        "AWS",
        "Azure",
        "GCP",
        "Recommendation System",
        "Search Engine",
        "Hybrid Search",
        "BM25",
        "Re-ranking",
        "Sentence Transformers",
        "PEFT",
        "QLoRA",
        "NDCG",
        "MRR",
    ]

    for skill in skills:
        name = skill["name"].lower()

    if name in [k.lower() for k in ai_keywords]:
        score += 10

    if "python" in name:
        score += 5

    if "langchain" in name:
        score += 20

    if "llamaindex" in name:
        score += 20
    if "huggingface" in name:
        score += 15

    if "transformers" in name:
        score += 15

    if "pytorch" in name:
        score += 10

    if "tensorflow" in name:
        score += 10

    if "openai" in name:
        score += 15

    if "gemini" in name:
        score += 15

    if "transformers" in name:
        score += 15

    if "bert" in name:
        score += 15

    if "prompt engineering" in name:
        score += 20

    score += signals["recruiter_response_rate"] * 20
    if signals["github_activity_score"] >= 80:
        score += 15
    elif signals["github_activity_score"] >= 50:
        score += 8

    return round(score, 3)

ranked = []
candidates = load_candidates("C:/Users/poojitha/Downloads/[PUB] India_runs_data_and_ai_challenge/[PUB] India_runs_data_and_ai_challenge/India_runs_data_and_ai_challenge/candidates.jsonl")


for candidate in candidates:
    score = calculate_score(candidate)

    reason = []

    if candidate["profile"]["years_of_experience"] >= 5:
        reason.append("Strong experience")

    if candidate["redrob_signals"]["open_to_work_flag"]:
        reason.append("Open to work")

    if candidate["redrob_signals"]["notice_period_days"] <= 30:
        reason.append("Short notice period")

    ranked.append({
        "candidate_id": candidate["candidate_id"],
        "score": score,
        "reasoning": ", ".join(reason)
    })

ranked.sort(key=lambda x: x["score"], reverse=True)

for i, candidate in enumerate(ranked, start=1):
    candidate["rank"] = i



import csv

with open("submission.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["candidate_id", "rank", "score", "reasoning"])
    
    for candidate in ranked[:100]:
        writer.writerow([
            candidate["candidate_id"],
            candidate["rank"],
            candidate["score"],
            candidate["reasoning"]
        ])

print("submission.csv created successfully!")