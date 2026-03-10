from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini")

def research_agent(state):
    topic = state["topic"]

    prompt = f"""
    Research the topic: {topic}

    Provide important facts, trends, and date and retun only first 3-5 points instead of the full research content
    """

    result = llm.invoke(prompt)

    return {"research": result.content}


def outline_agent(state):
    topic = state["topic"]
    research = state["research"]

    prompt = f"""
    Create a detailed blog outline for the topic: {topic}

    Use this research:
    {research}

    Return 5-7 section headings.
    """

    result = llm.invoke(prompt)

    outline = result.content.split("\n")

    return {"outline": outline}


def section_agent(state):
    topic = state["topic"]
    outline = state["outline"]

    sections = []

    for section in outline:
        prompt = f"""
        Write a blog section for:

        Blog topic: {topic}
        Section: {section}

        Write 2-3 paragraphs.
        """

        result = llm.invoke(prompt)

        sections.append(result.content)

    return {"sections": sections}


def editor_agent(state):
    sections = state["sections"]

    draft = "\n\n".join(sections)

    prompt = f"""
    Edit and polish this blog article.
    Improve clarity, SEO, and flow.

    {draft}
    """

    result = llm.invoke(prompt)

    return {"blog": result.content}