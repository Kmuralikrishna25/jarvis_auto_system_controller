from graph.builder import jarvis_graph


def run_jarvis():

    print("\nJarvis Activated")
    print("Type 'exit' to quit\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":

            print("\nJarvis: Goodbye\n")

            break

        initial_state = {
            "user_input": user_input,
            "next_agent": "",
            "response": ""
        }

        result = jarvis_graph.invoke(
            initial_state
        )

        print(f"\nJarvis: {result['response']}\n")


if __name__ == "__main__":

    run_jarvis()