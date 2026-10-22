"""Profile 05-langchain. No model or network required."""
from typing import TypedDict
from langgraph.graph import StateGraph,START,END
class State(TypedDict):
    question:str
    answer:str
def answer(state:State):
    return {'answer':'Local graph executed: '+state['question']}
graph=StateGraph(State);graph.add_node('answer',answer);graph.add_edge(START,'answer');graph.add_edge('answer',END)
print(graph.compile().invoke({'question':'hello','answer':''}))
