import json
import os
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html
from playwright.sync_api import sync_playwright

class BrowserTools():

    @tool("Scrape website content")
    def scrape_and_summarize_website(website):
        """Useful to scrape and summarize a website content"""
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(website)
            content = page.content()
            browser.close()
        
        elements = partition_html(text=content)
        content_text = "\n\n".join([str(el) for el in elements])
        content_chunks = [content_text[i:i + 8000] for i in range(0, len(content_text), 8000)]
        
        summaries = []
        for chunk in content_chunks:
            agent = Agent(
                role='Principal Researcher',
                goal='Do amazing researches and summaries based on the content you are working with',
                backstory="You're a Principal Researcher at a big company and you need to do a research about a given topic.",
                allow_delegation=False
            )
            task = Task(
                agent=agent,
                description=f'Analyze and summarize the content below, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
            )
            summary = task.execute()
            summaries.append(summary)
        
        return "\n\n".join(summaries)
