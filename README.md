# RouterFlow Example with CrewAI

This repository contains an example of a router flow implemented using the `crewai.flow.flow` library. The flow guides users based on their age, categorizing them as either minors or adults.

## Prerequisites

Before running this code, ensure that you have the following installed:

- Python 3.11+
- `uv` package manager

You can install `uv` using one of the following methods:

```bash
# Using curl
curl -LsSf https://astral.sh/uv/install.sh | sh

# Using pip
pip install uv
```

For more installation options and details, refer to the [uv installation guide](https://docs.astral.sh/uv/installation/).

## Overview

This flow uses `crewai.flow.flow` to create an interactive experience where users provide their name and age. Based on the age input, the flow routes the user to a specific function that prints a message indicating whether they are a minor or an adult.

### Components

- **RouterSchema**: Defines the state schema with fields for `name` and `age`.
- **RouterFlow**: Inherits from `Flow` and contains the flow logic.
- **kickoff()**: Starts the flow.
- **plot()**: Generates a plot of the flow and saves it as `crewai_flow.html`.

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### Step 2: Sync Dependencies with `uv`

Run the following command to create a virtual environment and install all the necessary dependencies automatically:

```bash
uv sync
```

This will set up a virtual environment (`.venv`) and install all dependencies listed in `pyproject.toml`.

### Step 3: Running the Flow

To run the flow using `uv`:

```bash
uv run router
```

### Step 4: Generating the Flow Plot

To generate a visual representation of the flow:

```bash
uv run plot
```

The plot will be saved as `crewai_flow.html` in the current directory.

## Code Structure

### Schema Definition

```python
from pydantic import BaseModel

class RouterSchema(BaseModel):
    name: str = ""
    age: int = 0
```

This schema ensures that the state has two fields: `name` (a string) and `age` (an integer).

### Flow Definition

```python
from crewai.flow.flow import Flow, start, listen, router

class RouterFlow(Flow[RouterSchema]):
    @start()
    def input_data(self):
        self.state.name = input("Enter your name: ")
        self.state.age = int(input("Enter your age: "))

    @router("input_data")
    def condition(self):
        if self.state.age < 18:
            return "minor"
        else:
            return "adult"

    @listen("minor")
    def minorFunc(self):
        print(f"Hello {self.state.name}, you are a minor")

    @listen("adult")
    def adultFunc(self):
        print(f"Hello {self.state.name}, you are an adult")
```

### Functions

- **`input_data`**: Collects user input for `name` and `age`.
- **`condition`**: Routes the user based on their age.
- **`minorFunc`**: Prints a message for users under 18.
- **`adultFunc`**: Prints a message for users 18 and older.

### Execution

```python
def kickoff():
    flow = RouterFlow()
    flow.kickoff()

def plot():
    flow = RouterFlow()
    flow.plot()
```

- `kickoff()`: Starts the flow and interacts with the user.
- `plot()`: Generates a visual representation of the flow and saves it as `crewai_flow.html`.

## Example Interaction

```
Enter your name: John
Enter your age: 16
Hello John, you are a minor
```

```
Enter your name: Jane
Enter your age: 25
Hello Jane, you are an adult
```

## License

This code is provided under the MIT License.
