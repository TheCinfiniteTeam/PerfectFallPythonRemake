# -*-coding:UTF-8 -*-

# 导入基础库

# Util&Log
import Util

logger = Util.Logger()
logger.info('Start for import library')
# End

import pygame

logger.info('End for import library')
# &&&&********-----********&&&& #

# Log
logger.info('Start for init pygame')
# end
pygame.init()
pygame.mixer.init()
# log
logger.info("End for init pygame")
# end


# Program End For Debug
logger.debug('Log List:' + str(logger.logs))
