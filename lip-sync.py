import azure.cognitiveservices.speech as speechsdk
# from azure.cognitiveservices.speech.audio import AudioOutputConfig
# from azure.cognitiveservices.speech.speech import AudioDataStream

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "", "westus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
# audio_config = AudioOutputConfig(filename="/Users/altumcaelum/Desktop/School/Microsoft/file.wav")
# Creates a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
# speech_synthesizer.speak_text_async("A simple test to write to a file.")
# audio_config = AudioOutputConfig(use_default_speaker=True)
speech_synthesizer.viseme_received.connect(lambda evt: print("Viseme event received: audio offset: {}ms, viseme id: {}.".format(evt.audio_offset / 10000, evt.viseme_id)))

ssml_string = open("ssml.xml","r").read()

result = speech_synthesizer.speak_ssml_async(ssml_string).get()
# stream = AudioDataStream(result)

