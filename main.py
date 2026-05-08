from graph.builder import jarvis_graph

from agents.voice_agent import (
    listen,
    listen_for_interrupt,
    speak,
    speak_and_check_interrupt,
    stop_speaking
)

from tools.memory_tools import (
    load_memory,
    save_memory
)

from tools.scheduler_tools import (
    check_reminders,
    list_reminders
)

import threading
import time


# ==========================================
# REMINDER CHECKER
# ==========================================

def reminder_checker(memory: list, running: list):

    while running[0]:

        reminders = check_reminders()

        for task in reminders:

            speak(f"Reminder: {task}")

        time.sleep(30)


# ==========================================
# PROCESS USER REQUEST
# ==========================================
# PROCESS USER REQUEST
# ==========================================

def process_command(user_input: str, memory: list):

    initial_state = {
        "user_input": user_input,
        "next_agent": "",
        "response": "",
        "conversation_history": memory,
        "context": {},
        "pending_agents": []
    }

    result = jarvis_graph.invoke(
        initial_state
    )

    response = result.get("response", "")

    memory = result.get(
        "conversation_history",
        memory
    )

    # Speak and check for interruption
    interrupt = speak_and_check_interrupt(response)

    if interrupt:

        return process_command(
            interrupt,
            memory
        )

    # Process pending agents from supervisor
    pending = result.get("pending_agents", [])

    for agent_name in pending:

        print(f"\n[Processing next agent: {agent_name}]\n")

        state2 = {
            "user_input": user_input,
            "next_agent": agent_name,
            "response": "",
            "conversation_history": memory,
            "context": {},
            "pending_agents": []
        }

        result2 = jarvis_graph.invoke(state2)

        response2 = result2.get("response", "")

        memory = result2.get(
            "conversation_history",
            memory
        )

        interrupt = speak_and_check_interrupt(response2)

        if interrupt:

            return process_command(
                interrupt,
                memory
            )

    return memory

    # ==========================================
    # SINGLE COMMAND PROCESSING
    # ==========================================

    initial_state = {
        "user_input": user_input,
        "next_agent": "",
        "response": "",
        "conversation_history": memory,
        "context": {}
    }

    result = jarvis_graph.invoke(
        initial_state
    )

    response = result.get("response", "")

    memory = result.get(
        "conversation_history",
        memory
    )

    # Speak and check for interruption
    interrupt = speak_and_check_interrupt(
        response
    )

    # If interrupted, process the new command (loop)
    while interrupt:

        print(f"\n[Processing interrupt: {interrupt}]\n")

        interrupt = process_command(
            interrupt,
            memory
        )

    return memory


# ==========================================
# MAIN JARVIS LOOP
# ==========================================

def run_jarvis():

    speak("Jarvis activated.")

    memory = load_memory()

    running = [True]

    reminder_thread = threading.Thread(
        target=reminder_checker,
        args=(memory, running),
        daemon=True
    )

    reminder_thread.start()

    while True:

        user_input = listen()

        # Ignore empty audio
        if not user_input:
            continue

        # ======================================
        # STOP SPEAKING COMMANDS
        # ======================================

        if any(word in user_input for word in [
            "stop",
            "stop speaking",
            "be quiet",
            "silence"
        ]):

            stop_speaking()

            continue

        # ======================================
        # EXIT COMMANDS
        # ======================================

        if any(word in user_input for word in [
            "exit",
            "quit",
            "shutdown jarvis"
        ]):

            stop_speaking()

            save_memory(memory)

            running[0] = False

            speak("Goodbye.")

            break

        # ======================================
        # LIST REMINDERS
        # ======================================

        if "list reminders" in user_input or "show reminders" in user_input:

            interrupt = speak_and_check_interrupt(
                list_reminders()
            )

            if interrupt:
                process_command(interrupt, memory)

            continue

        # ======================================
        # SET REMINDER
        # ======================================

        if "remind me" in user_input or "set reminder" in user_input:

            from tools.scheduler_tools import add_reminder

            if "in" in user_input:

                parts = user_input.split("in")

                if len(parts) > 1:

                    time_part = parts[1].strip()

                    task = parts[0].replace(
                        "remind me",
                        ""
                    ).replace(
                        "set reminder",
                        ""
                    ).strip()

                    minutes = 0

                    if "minute" in time_part:
                        try:
                            minutes = int(
                                time_part.split()[0]
                            )
                        except:
                            minutes = 5

                    interrupt = speak_and_check_interrupt(
                        add_reminder(
                            task,
                            delay_minutes=minutes
                        )
                    )

                    if interrupt:
                        process_command(interrupt, memory)

            continue

        # ======================================
        # PROCESS REQUEST
        # ======================================

        memory = process_command(
            user_input,
            memory
        )


# ==========================================
# ENTRY POINT
# ==========================================

if __name__ == "__main__":

    run_jarvis()