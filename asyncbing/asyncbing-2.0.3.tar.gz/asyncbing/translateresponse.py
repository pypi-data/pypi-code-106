

class TranslateResponse:
    """The class for the Bing Translate Response.
    .. warning::
        You must not manually initialize this!"""
    def __init__(self, data: dict):
        self.data = data[0] # there's always one item in the list
    
    @property
    def detected_language(self) -> str:
        """Returns the translated output of the query."""
        return self.data['detectedLanguage']['language']
    
    @property
    def detected_language_confidence(self) -> float:
        """Returns the confidence of the detected language."""
        return self.data['detectedLanguage']['score']

    @property
    def translated_output(self) -> str:
        """Returns the translated output."""
        return self.data['translations'][0]['text']

    @property
    def translated_language(self) -> str:
        """Returns the language of the translated output."""
        return self.data['translations'][0]['to']

