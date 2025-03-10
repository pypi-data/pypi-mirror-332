from otaro import Task

task = Task.from_config("./examples/sample.yml")

for message in task.get_prompt(topic="life")["messages"]:
    print(message["content"])
