from api_secrets import API_KEY_ASSEMBLYAI
import sys
#upload
from api_communication import upload
from api_communication import save_transcript


filename = sys.argv[1]

audio_url = upload(filename)
save_transcript(audio_url, filename)