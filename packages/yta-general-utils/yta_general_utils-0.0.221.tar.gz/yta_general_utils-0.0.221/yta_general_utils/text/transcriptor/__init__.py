from yta_general_utils.web.scraper.chrome_scraper import ChromeScraper

import time


class WebRealTimeAudioTranscriptor:
    """
    Class to wrap a functionality related to real
    time audio transcription by using a web scrapper.
    """

    _URL: str = 'file:///C:/Users/dania/Downloads/JS-TRANSCRIBE/transcribe.html'
    _MAX_WAITING_TIME: float = 20

    def __init__(
        self
    ):
        self.scrapper = ChromeScraper()

    def _load(
        self
    ):
        # TODO: Do this only if not in the webpage (?)
        self.scrapper.go_to_web_and_wait_until_loaded(self._URL)
    
    def transcribe(
        self
    ) -> str:
        self._load()

        text_element = self.scrapper.find_element_by_id('result')
        button = self.scrapper.find_element_by_id('toggle')

        button.click()

        WAITING_TIME = 0.25

        time_elapsed = 0
        while time_elapsed < self._MAX_WAITING_TIME:
            text = text_element.get_attribute('value')
            if text != '':
                # We have it, force exit the loop
                time_elapsed = self._MAX_WAITING_TIME
            else:
                time.sleep(WAITING_TIME)
                time_elapsed += WAITING_TIME

        button.click()

        return text



