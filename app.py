# main.py
from graphs.graph import graph

topic = "The Future of Artificial Intelligence in Healthcare"

result = graph.invoke({
    "topic": topic
})

print(result["blog"])