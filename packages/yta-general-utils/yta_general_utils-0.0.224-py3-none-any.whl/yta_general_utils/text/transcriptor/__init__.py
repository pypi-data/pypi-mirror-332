from yta_general_utils.web.scraper.chrome_scraper import ChromeScraper
from yta_general_utils.programming.validator.parameter import ParameterValidator
from typing import Union

import time


class WebRealTimeAudioTranscriptor:
    """
    Class to wrap a functionality related to real
    time audio transcription by using a web scraper.

    This class uses local files to create a simple
    web page that uses the chrome speech recognition
    to get the transcription.
    """

    _URL: str = 'file:///C:/Users/dania/Downloads/JS-TRANSCRIBE/transcribe.html'
    """
    The url to our local web page file.
    """
    max_waiting_time: Union[float, None]
    """
    The maximum time the software will be waiting
    to detect an audio transcription before exiting
    with an empty result.
    """

    def __init__(
        self,
        max_waiting_time: Union[float, None] = 15.0
    ):
        ParameterValidator.validate_positive_float('max_waiting_time', max_waiting_time, do_include_zero = True)

        self.scraper = ChromeScraper()
        self.max_waiting_time = (
            9999 # TODO: This is risky if no microphone or something
            if (
                max_waiting_time == 0 or
                max_waiting_time is None
            ) else
            max_waiting_time
        )

    def _load(
        self
    ):
        """
        Navigates to the web page when not yet on it.
        """
        if self.scraper.current_url != self._URL:
            self.scraper.go_to_web_and_wait_until_loaded(self._URL)

    def _get_transcription(
        self
    ):
        """
        Get the text that has been transcripted from the
        audio.
        """
        self._load()

        return self.scraper.find_element_by_id('result').get_attribute('value')
    
    def _click_transcription_button(
        self
    ):
        """
        Performa click on the button that enables (or
        disables) the microphone so it starts (or ends)
        transcribing the text.
        """
        self._load()

        self.scraper.find_element_by_id('toggle').click()
    
    def transcribe(
        self
    ) -> str:
        """
        A web scraper instance loads the internal web
        that uses the Chrome speech recognition to get
        the audio transcription, by pressing the
        button, waiting for audio input through the
        microphone, and pressing the button again.

        If the page was previously loaded it won't be
        loaded again.
        """
        self._load()

        WAITING_TIME = 0.25

        self._click_transcription_button()

        time_elapsed = 0
        while time_elapsed < self.max_waiting_time:
            transcription = self._get_transcription()
            if transcription != '':
                # We have it, force exit the loop
                time_elapsed = self.max_waiting_time
            else:
                time.sleep(WAITING_TIME)
                time_elapsed += WAITING_TIME

        self._click_transcription_button()

        return transcription



