import json
import redis

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Read JSON file and load questions
with open('trivia_questions.json', 'r') as file:
    questions = json.load(file)

# Store each question in Redis
for idx, question in enumerate(questions, start=1):
    question_key = f"question:{idx}"
    redis_client.hset(question_key, 'question', question['question'])
    redis_client.hset(question_key, 'answer', question['answer'])
    for option_idx, option in enumerate(question['options'], start=1):
        redis_client.hset(question_key, f'option:{option_idx}', option)

print("Questions stored in Redis successfully.")

