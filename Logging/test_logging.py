import logging
import sys


# create logger 
logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)


# add formatter : shape of output
myformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# handeler : show information in console
cmd_handeler = logging.StreamHandler(stream=sys.stdout)
cmd_handeler.setFormatter(myformatter)


# add handeler to  logger
logger.addHandler(cmd_handeler)



def mylogic(x,y):
    try:
        logger.info(f"Start mylogic divided {x} / {y}")
        result = x/y
        return result
    
    except Exception as e :
        logger.error("Error in mylogic : %s", str(e))



if __name__ == "__main__":
    print(mylogic(50,10))