import threading
import speech_recognition as sr
import win32com.client


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

        # Speak in small chunks
        if len(chunk.split()) >= 8:

            speaker.Speak(
                chunk,
                1
            )

            chunk = ""

    if chunk and not stop_event.is_set():

        speaker.Speak(
            chunk,
            1
        )


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

        speaker.Speak(
            "",
            3
        )

    except:

        pass


# ==========================================
# LISTEN FUNCTION
# ==========================================

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...\n")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=0.5
        )

        audio = recognizer.listen(
            source,
            phrase_time_limit=5
        )

    try:

        command = recognizer.recognize_google(
            audio
        )

        print(f"\nYou: {command}\n")

        return command.lower()

    except:

        return ""