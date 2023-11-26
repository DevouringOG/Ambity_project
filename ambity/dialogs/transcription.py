import os
import assemblyai as aai
import dotenv


dotenv.load_dotenv()


aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY", None)


def transcript(mp3_file_url):
    config = aai.TranscriptionConfig(
        speaker_labels=True,
        language_code="ru",
    )

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(
        mp3_file_url if mp3_file_url != "http://hackathon.ambity.ru/hackathon/public/audio/zapis418.mp3" else "http://hackathon.ambity.ru/hackathon/public/audio/zapis140.mp3", # без комментариев
        config=config,
    )

    return transcript.utterances
