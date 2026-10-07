from agent.model import call_model


def main():

    messages = [...]
    tools = [...]
    while True:
        response = call_model(messages,tools)