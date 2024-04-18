import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
os.environ["OPENAI_MODEL_NAME"] = 'yabi/breeze-7b-instruct-v1_0_q6_k'
os.environ["OPENAI_API_KEY"] = 'sk-111111111111111111111111111111111111111111111111'

search_tool = SerperDevTool(
    name="Search the internet", search_url="https://buzzorange.com/techorange/latest",    description="A tool that can be used to seman",
)

researcher = Agent(
    role='Senior Research Analyst',
    goal='發現人工智慧和數據科學的前沿發展',
    backstory="""您在一家領先的科技智庫工作。
   您的專長在於識別新興趨勢。
   您擁有剖析複雜數據並提出可行見解的技巧。""",
    verbose=True,
    allow_delegation=True,
)
writer = Agent(
    role='Tech Content Strategist',
    goal='製作有關技術進步的引人注目的內容',
    backstory="""您是一位著名的內容策略師，以富有洞察力和引人入勝的文章而聞名。
   您將複雜的概念轉化為引人入勝的敘述。""",
    verbose=True,
    allow_delegation=True
)

# 建立任務給Agent
task1 = Task(
    description="""對2024年人工智慧最新進展進行全面分析。
   確定關鍵趨勢、突破性技術和潛在的行業影響。""",
    expected_output="完整的分析報告要點",
    agent=researcher
)

task2 = Task(
    description="""利用提供的見解，開發一個引人入勝的博客
   這篇文章強調了最重要的人工智慧進步。
   您的貼文應該內容豐富且易於理解，適合精通科技的受眾。
   讓它聽起來很酷，避免使用複雜的單詞，這樣聽起來就不像人工智慧""",
    expected_output="完整的部落格文章至少有 4 段",
    agent=writer
)

# 參與協作的Agent和任務
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2,
)

result = crew.kickoff()

print("######################")
print(result)
