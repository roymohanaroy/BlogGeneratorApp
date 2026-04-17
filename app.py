# main.py
from time import time
import time
from dotenv import load_dotenv
import os

load_dotenv()
from graphs.graph import graph
start = time.time()

topic = "The Future of Artificial Intelligence in Healthcare"

print("Before invoke")

result = graph.invoke({
    "topic": topic
})
print("TIME:", time.time() - start)
print("After invoke")

print(result["blog"])