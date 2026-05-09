import threading
import speech_recognition as sr
import win32com.client
import winsound
import time


# ==========================================
# WINDOWS SPEAKER
# ==========================================

speaker = win32com.client.Dispatch(
    "SAPI.SpVoice"
)

speaker.Rate = 1


# ==========================================
# GLOBAL SPEECH STATE
# ==========================================

speech_thread = None

stop_event = threading.Event()


# ==========================================
# SPEAK WORKER
# ==========================================

def _speak(text):

    stop_event.clear()

    words = text.split()

    chunk = ""

    for word in words:

        if stop_event.is_set():
            break

        chunk += word + " "

        # Speak in small chunks (async)
        if len(chunk.split()) >= 6:

            speaker.Speak(chunk, 1)

            chunk = ""

    # Speak remaining text
    if chunk and not stop_event.is_set():

        speaker.Speak(chunk, 1)


# ==========================================
# SPEAK FUNCTION
# ==========================================

def speak(text: str):

    global speech_thread

    print(f"\nJarvis: {text}\n")

    stop_speaking()

    speech_thread = threading.Thread(
        target=_speak,
        args=(text,),
        daemon=True
    )

    speech_thread.start()


# ==========================================
# STOP SPEAKING
# ==========================================

def stop_speaking():

    stop_event.set()

    try:

        # Purge current speech
        speaker.Speak("", 3)

    except:
        pass


# ==========================================
# SPEAK WITH INTERRUPTION CHECK
# ==========================================

def speak_and_check_interrupt(text, memory=None):

    speak(text)

    # While speaking, check for interruptions
    while (
        speech_thread and
        speech_thread.is_alive()
    ):

        interrupt = listen_for_interrupt(timeout=1)

        if interrupt:

            print(f"\n[Interrupt detected: {interrupt}]\n")

            stop_speaking()

            return interrupt

    return ""


# ==========================================
# LISTEN FOR INTERRUPT (SHORT TIMEOUT)
# ==========================================

def listen_for_interrupt(timeout=1):

    recognizer = sr.Recognizer()

    try:

        with sr.Microphone() as source:

            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=3
            )

        command = recognizer.recognize_google(audio)

        return command.lower()

    except:

        return None


# ==========================================
# LISTEN FUNCTION
# ==========================================

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\n" + "="*40)
        print("LISTENING - SPEAK NOW")
        print("="*40 + "\n")

        # Ready to listen

        time.sleep(0.5)

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(
            source,
            phrase_time_limit=15,
            timeout=10
        )

    try:

        command = recognizer.recognize_google(
            audio
        )

        print(f"\nYou: {command}\n")

        return command.lower()

    except sr.WaitTimeoutError:

        print("\nTimeout - no speech detected\n")

        return ""

    except:

        return ""
