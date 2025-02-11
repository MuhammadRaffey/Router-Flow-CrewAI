from crewai.flow.flow import Flow,start,listen,router
from pydantic import BaseModel

class RouterSchema(BaseModel):
    name: str = ""
    age: int = 0

class RouterFlow(Flow[RouterSchema]):
    @start()
    def input_data(self):
        self.state.name=input("Enter your name: ")
        self.state.age=int(input("Enter your age: "))

    @router(input_data)
    def condition(self):
        if self.state.age<18:
            return "minor"
        else:
            return "adult"
    @listen("minor")
    def minorFunc(self):
        print(f"Hello {self.state.name}, you are a minor")

    @listen("adult")
    def adultFunc(self):
        print(f"Hello {self.state.name}, you are an adult")
        
        

def kickoff():
    flow=RouterFlow()
    flow.kickoff()

def plot():
    flow=RouterFlow()
    flow.plot()

