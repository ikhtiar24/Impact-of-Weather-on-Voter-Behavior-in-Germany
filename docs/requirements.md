## Functional Requirements 

We want to analyze what influence weather conditions have on voter turnout in Germany. 

The following UML Activity Diagram shows an abstract description of the data analysis workflow: 
![Active Diagram](./ActiveDiagram.png)

For each node in the activity diagram, the following table lists the  input, output, and implementation (using packages or own implementation).
![Active Workflow Table](./ActiveWorkflowTable.pdf)

## Non-Functional Requirements 

- The system must be compatible with common operating systems (Windows, macOS, Linux) and require a Python version ≥ 3.10.
- the system must be clearly divided into an analysis part and a visualization part.
- All processed data must be automatically deleted after use.
- Analysis results must be presented clearly and understandably for end users.
- In the event of analysis errors, no results will be displayed.
- The system will be made publicly available.



