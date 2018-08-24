# import ESL
import settings
import esl


if __name__ == '__main__':
    try:
        esl_cli = esl.ESLcon(settings.ESL_SERVER, settings.ESL_PASSWD)
        esl_cli.start()
        esl_cli.join()
    except KeyboardInterrupt as e:
        pass
