
class Settings:
    """ Calculator App Configuration """

    COMPILED_APP_MODE = False

    APP_NAME = "Calculator"
    VERSION = "1.0"
    AUTHOR = "David Lonsdale"
    YEAR = "2023"

    GITHUB_API_URL = "https://github.com/davidlonsdale92/calculatorapp"
    GITHUB_URL = "https://github.com/davidlonsdale92/calculatorapp"
    GITHUB_URL_README = "https://github.com/davidlonsdale92/calculatorapp#readme"

    STATISTICS_AGREEMENT = f"{APP_NAME} tracks how often the app is being opened.\n\n" + \
                           "Do you agree on sending this anonymous data?"

    ABOUT_TEXT = "{} Version {}  © {} {}".format(APP_NAME, VERSION, YEAR, AUTHOR)
    CF_BUNDLE_IDENTIFIER = "com.{}.{}".format(AUTHOR, APP_NAME)

    WIDTH = 320  
    HEIGHT = 400

    MAX_WIDTH = 320  
    MAX_HEIGHT = 400

    FPS = 60 
    CANVAS_SIZE = 300  
