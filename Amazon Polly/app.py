import boto3

polly = boto3.client('polly',region_name='us-east-1',aws_access_key_id='YOUR_AWS_KEY_ID',aws_secret_access_key='YOUR_AWS_SECRET_ACCESS_KEY')

text="""Once upon a time, in a big green forest, there lived a little squirrel named Sam. Sam was very friendly and loved to share his food with other animals. One day, he found a big acorn and decided to share it with his friends.
"""

response = polly.synthesize_speech(Text=text, OutputFormat="mp3",
                                    VoiceId="Aditi")

if "AudioStream" in response:
   with response["AudioStream"] as stream:
      output_file = "speech.mp3"
      with open(output_file, "wb") as file:
         file.write(stream.read())
    
else:
   print("Could not stream audio")