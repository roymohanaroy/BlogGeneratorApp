# graph.py
from langgraph.graph import StateGraph, END
from state.state import BlogState
from agents.agents import research_agent, outline_agent, section_agent, editor_agent

builder = StateGraph(BlogState)

builder.add_node("research", research_agent)
builder.add_node("outline", outline_agent)
builder.add_node("sections", section_agent)
builder.add_node("edit_blog", editor_agent)

builder.set_entry_point("research")

builder.add_edge("research", "outline")
builder.add_edge("outline", "sections")
builder.add_edge("sections", "edit_blog")
builder.add_edge("edit_blog", END)

graph = builder.compile()