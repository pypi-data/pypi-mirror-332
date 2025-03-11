from yta_general_utils.web.scraper.chrome_scraper import ChromeScraper
from yta_general_utils.programming.validator.parameter import ParameterValidator
from yta_general_utils.text.transcriptor.web import TRANSCRIBER_HTML_FILENAME
from yta_general_utils.programming.path import get_project_abspath
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

    _LOCAL_URL: str = f'file:///{get_project_abspath()}{TRANSCRIBER_HTML_FILENAME}'
    _REMOTE_URL: str = 'https://iridescent-pie-f24ff0.netlify.app/'
    """
    The url to our local web page file.
    """
    max_waiting_time: Union[float, None]
    """
    The maximum time the software will be waiting
    to detect an audio transcription before exiting
    with an empty result.
    """
    do_use_local_web_page: bool
    """
    Flag that indicates if the resource must be a
    local web page (that will be loaded from a file
    in our system) or from a remote url.
    """

    def __init__(
        self,
        max_waiting_time: Union[float, None] = 15.0,
        do_use_local_web_page: bool = True
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
        self.do_use_local_web_page = do_use_local_web_page

    @property
    def url(
        self
    ) -> str:
        """
        The url that must be used to interact with the
        web page that is able to catch the audio and
        transcribe it.
        """
        return (
            self._LOCAL_URL
            if self.do_use_local_web_page else
            self._REMOTE_URL
        )

    def _load(
        self
    ):
        """
        Navigates to the web page when not yet on it.

        For internal use only.
        """
        if self.scraper.current_url != self.url:
            self.scraper.go_to_web_and_wait_until_loaded(self.url)

    def _get_transcription(
        self
    ):
        """
        Get the text that has been transcripted from the
        audio.

        For internal use only.
        """
        self._load()

        return self.scraper.find_element_by_id('final_transcription').text
    
    def _click_transcription_button(
        self
    ):
        """
        Performa click on the button that enables (or
        disables) the microphone so it starts (or ends)
        transcribing the text.

        For internal use only.
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
        TIME_TO_STOP = 1.5
        """
        The time that has to be spent once a final
        transcription has been found to consider it
        as a definitive one. There can be more final
        transcriptions after that one due to some 
        logic that I still don't understand properly.
        """

        self._click_transcription_button()

        time_elapsed = 0
        final_transcription_time_elapsed = 0
        transcription = ''
        while (
            time_elapsed < self.max_waiting_time and
            (
                (
                    final_transcription_time_elapsed != 0 and
                    (final_transcription_time_elapsed + TIME_TO_STOP) > time_elapsed
                ) or
                final_transcription_time_elapsed == 0
            )
        ):
            tmp_transcription = self._get_transcription()
            if tmp_transcription != transcription:
                transcription = tmp_transcription
                #time_elapsed = self.max_waiting_time
                final_transcription_time_elapsed = time_elapsed
            else:
                time.sleep(WAITING_TIME)

            time_elapsed += WAITING_TIME

        self._click_transcription_button()

        return transcription



