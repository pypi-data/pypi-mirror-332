"""
Welcome to Youtube Autonomous Voice Assistant
Module.
"""
from yta_general_utils.programming.validator.parameter import ParameterValidator
from yta_general_utils.programming.validator import PythonValidator
from yta_general_utils.text.transcriptor import WebRealTimeAudioTranscriptor
from pygame import mixer as PygameMixer
from typing import Union

import time
import pyttsx3


class VoiceAssistant:
    """
    Voice assistant class to improve the way you work.
    You will be able to work without using the 
    keyboard.
    """

    @property
    def audio_transcriptor(
        self
    ) -> WebRealTimeAudioTranscriptor:
        """
        The audio transcriptor capable of understanding
        what the user is saying through the microphone.
        """
        return self._audio_transcriptor

    def __init__(
        self
    ):
        self._audio_transcriptor = WebRealTimeAudioTranscriptor(do_use_local_web_page = False)
        PygameMixer.init()

    def _play_sound(
        self,
        sound: Union[PygameMixer.Sound, str],
        do_wait_until_finished: bool = True
    ) -> None:
        """
        Play the provided 'sound'. This method will wait
        until the whole sound is played if the 
        'do_wait_until_finished' flag is True.
        """
        ParameterValidator.validate_mandatory_instance_of('sound', sound, [PygameMixer.Sound, str])
        ParameterValidator.validate_mandatory_bool('do_wait_until_finished', do_wait_until_finished)

        if PythonValidator.is_string(sound):
            sound = PygameMixer.Sound(sound)

        sound.play()

        while (
            PygameMixer.get_busy() and
            do_wait_until_finished
        ):
            time.sleep(0.5)

    def _narrate(
        self,
        text: str
    ) -> None:
        """
        Play a voice sound narrating the provided 
        'text'.
        """
        ParameterValidator.validate_mandatory_string('text', text)

        pyttsx3.init().say(text)

    def _get_user_speech(
        self
    ) -> str:
        """
        Listen to the user voice speech and get the
        transcription of it.
        """
        return self.audio_transcriptor.transcribe()
    
    def execute(
        self
    ):
        for _ in range(2):
            text_speech = self._get_user_speech()
            print(text_speech)
            self._play_sound('C:/Users/dania/Downloads/wineglasssound.mp3')
        

    # for _ in range(2):
    #     print('Talk:')
    #     command = transcriptor.transcribe()
    #     print(command)
    #     play_sound('C:/Users/dania/Downloads/wineglasssound.mp3')
    #     play_sound(DefaultVoiceNarrator.narrate(command, Temp.get_filename('tempus.mp3')))