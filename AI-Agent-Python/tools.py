from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime



#Make Custom Tool Calling

#we make our own custom tool so we can save this to a file.
# In order to save this to a file we can actually write our own Python function. Any function for that matter(which we create) can we wrapped as a tool.

#So If you want a tool that calls an API, you can do that. Just write a Python function, wrap it as a tool, and you can pass as many of these to your agent and really get some advanced functionality here.

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
        
    return f"Data successfully saved to {filename}"
 
save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Save structured research data to a text file.",
)


#will get rate limit if we use them too much and then we'll be able to create our own custom tool.
# Creating tool that can access DuckDuckGo kind of google search

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search", #key thing: you need to have some 'name'. In between name, should not have any space for long names use '_' or Camel case.
    func=search.run,
    description="Search the web for information", #agent knows when it should be using this tool.
)

#Wikipedia Tool

#can give top_k_results=5 if want 5 different results from wikipedia
#doc_content_chars_max=100 for quick demo. To get a lot more content from the wikipedia page, then would put 1000 or 10000(characters), It will take longer to run. And you may get rate limited faster because you don't even need an API key for this.
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)  
#converting api_wrapper to a tool
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper) #no need to wrap in a custom tool, just pass this as a tool directly to link chain.
