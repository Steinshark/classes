#comment
import flask
from BlockTools import *
from BlockchainUtilities import *
from os.path import isfile, isdir
from fcntl import flock, LOCK_SH,LOCK_EX, LOCK_UN
from json import dumps, loads
from os import listdir, mkdir
import argparse
import sys

# Package import to work on windows and linux
# Allows for nice text writing
try:
    sys.path.append("C:\classes")
    sys.path.append("D:\classes")
    sys.path.append("/home/m226252/classes")
    from Toolchain.terminal import *
except ModuleNotFoundError:
    print("Module import failed for Toolchain")



# This Class isnt even used....
def bad():
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7?JJYYY55555Y55YYYYYYJJ??7!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!7!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7JY555P555555555Y55YYYYYYYY555YJ?7!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!?JY555555P555555555555555YYYYY5555555J?!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!7JY55555P555P5YY555PPPP5555555555555555555Y?!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!!!!!!7J5P555P55P5PPPP5JY5PPPPPPPPP55P55555555555555J7~~~~~~~~~~~~~~~~~~~~~~!!!!!~~~~~~!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!!!!7YPPP5555PPPPPPPPPP5Y5PPPPPPPPPPPPP55P55555555555Y7~~~~~~~~~~~~~~77777?JJJ????J5PPP555YYYYYJJ?777!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!!7JPPP555PPPPPPPPPPPPGP55PPPPPPPPPPPPPPPP5PPP55555555Y7~~~~~~~~~!!7?J5555P5JJYPGB####BBBBBBBBBBBP5YJJ?7!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!75PPPPPPPPPPPGPPPGGPGGGP5PGGGPPPPPPPPPPPPPPP5555555555Y7!777???JJYYYY5PGGPYY5PGGBGBBBBBGGGGBBBBBBGGGGPYJ?7!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!?5PPPPPPPGGPGGGGGGGGGGGGP5PGGGGPPPPPPPPPPPPPP555P5555555YJJY555PPGGPPGGGPPPPPGBBBBB############BGGBBBBBG5YYJ77~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!JPGPPPPPGGGGGGGGGGGGGGGGGP5PPPPPGGPPPPPPPPPPPPP555555555555PGB#BBBBBGGPPP5PGBBB##&&&##&&&&##########BGG##G55J??77!~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!YGGGPGGGGGGGBBBBBGGGGGGGGP55PPGGGGGPPPPPPPPPPPP55555555555Y5PGBBBBBBB##GGBB#######&&&&##&&&#######BBBBPGB#G55JJ????7!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!JGGGGGGGBBBBBBBBBBBBBBGGGP5PPPGGGGGGGGGGPPPPPPPPPPP5555YYYYYY5GPYY5G#####&&&&####&&&&&&&#&&&&&##BGBB###GGGGPP5YJJJJ???77~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!?PBGGBBBBBB##BBBBBBBBBGGGGPPGGGGGGGGGGGGGGPPPPPPPPPP5555555YYY5PY??775B##BBGGBBBB##&&&&&&&&&&&&&&##&&BPPGGPGGP5YYYYJJ????77!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!JGGGBBBBBBB####BBBBBBBBBGPPPPPPPPGGGGGGGGPPPPPPPPPPPPPP5P55YJ?JYYYYYJ?YGPY?7??Y5PGB#&&&&&&&&&&&&&&&BP5555PGGP5555YYYYJ??????7!~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!75GBBBBBBBBBB#####BBBGGGPPPP555555PPPPGGGGPGPPPPPP55PPP5PP5YJ?JY55YYYYJJPP5YYJ??JY5PGB#&&&&&&&&&&&BP55PPPPGGPP555555YYYJJ???JJ?7!~~~~~~~~~~~~~~~~~~~^~^^^^~~~~~^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!7PBBBBBBBB#B###BBBBGGPPPPPP5555555PPPPGGGGGPGPPPPPPPPPPPGGPY777?J5YYYYJJ5GPP5YJ?JJY5PGB#&&&&&&&&#GPPGGPPPPPPPP55555555YYJJJJ??J?7!~^^~~~~~~^^^^^^^^^^^^^^^~~~~~^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!7PBBBBBBBBBBBBBGGGPPPPPPPPPPPPPPPPPPPPPPPGGGGPPPPPPPPPPGGGG5JYYJ??JYYYYJYGGP55J??JJ5PGBB#&&&&&BGPGG5YY5PPPPPPPPP5555555YYYJJJ??J?7!~^~^~~~~^~^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!75GGGBBGGBGGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP5555555PPPPGGGG5Y55Y??YYYJ?JGGPP5JJJYY5PGBBB####BGGGGP555PGPPPPPPPPPPP555YYYYJJJJJJ??7~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!J55555555Y5555PPPPPPPPPPPPPPPPPPPPPPPPPP555555555555555PPPP5YY5YJ?JYYJ?JPPP55JJJY555PGBBBGP5GBBBGGPPGPPPGGGGGPPP5555555YYYJJJJJJ??7~^^~~~~^^^^^^~~~~^^^^~^^^^~^^^~~~~~~~~~~~~~~~~~~~~^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!~!??JJJYYYY5555PPPPPGGPPGGGGGGGPPPPPPPP555555555555555PP55PPPYY5YJ?JYYYJJ55555YJJYYY55PGGGGGB#BBGGGGGGGGGGGPPPP555555555YYYYYJJJJJ?7!~^^^^~^^^^^^^^^^^^^^~^^^~^^~~~~~~~~~~~~~~~~~~~~~~^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!~!?JJYYYY55555PPPPPPPPPPPGGGGGPPPPP555555555555555555PP55PPPYJYYJ??Y5YJJY5P55YJJYYY5PPPGBBGPPPPGGGGGPPPPPPPPPPPPPPP5555YYYJJJJJJJ??!~^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!~!7?JJYYY55555555PPPPPPPGGGGGGGPPPPPPPPPP555555555555PPP55PPJJJYJJ?Y55Y??YP55YJ?JYY5PPPG#BG5PPPPGPPPPPGGGGGGGGPPPPPPPP55YYJJJJJJJ??7~^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~^^^~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!7JJJYY5555555555PPPGGGGGGGGGGGGGGGGGGGPPPPP555555555YYY5PY?JYJJ?J5YY???Y5YYJ??Y5PPGGBGGBGY?7?JYPGBBBBBGGGGGGGGGGGPP5YYJJJJJJJJ??7~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #~!!!!!!!!!!!!!!!~!7JJJYY5PP55555PPPGGGGGGGGBBB###BBBBBBBGGP55555555Y?7???YYJJYYYJJY5YJ??Y55YJJ?J5PGGPGBBGY??????Y5PGGBBBBBBBBBGGPPP555Y5YYYJJJ???!~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #~!!!!!!!!!!!!!!!!~!7JJYYYPPPPP555PPPPGGBB##&##BBBBB##BBGGPPP55555555YJYYJ???JYYYYJJY5YJ?J5P5YYJJPGBBBGBB5YYYYJ?J5P555PGB###BBBBGGPPGGGGGGG5YJJ?J?!~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!~!!7JJJYY5PPGP55PPPGB#&&&&&#BB##&&#BGGPPPPPPPPPPPPPP5YYYJ??JYYYYJ?J55YJ?Y5YYJJJ5BBB##BG55555YJYGGGP555PPGGBB#&&&#####BBBGPYJJYJ7~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!!~7?JYY55PGP5PGGB#&&&&&&&&&&###BGPPPPPPPPGGGPGGGGGGPYJYJ???YYYJ??JJJJ???77???YGB####P555555Y5GGPP555555PG#&&&&##BBGGGPPP5YJJ7!^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~^^^^~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!~~~!?5PGGGGGP5PGBB#########BBGGGPPPPPPGGGGGGGGGGGGGB#GJJJJ?7?YYYJJ????????????J5GBBBBP555P555GBBP?!7YPGGG####BBBGGGPPP55YJJ??7!!!~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!!~~!?YPB###B5Y5PGGGBBBBGGGGGGPPPPPPGGGGGGBBBBBBBBB#&&PJJJJ???JYYJ???????J????JY5B##GP55555PG###BP555PGBB#BBBGGGGPPP55YJJJ??77??7777!!~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #!!!!!!!!!!!!!!!!!!!!~~~~~~?5555YJY5PGGGGGGGGGGGPPPPPPPGGGGGGBBBBBBBB#&&@&5JJJJJ????77??????JJJJJYYYP##G555555PG#&###G555PBBBGGGGPPPP5555JJJJ??77????777777!~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #!!!!!!!!!!!!!!!!!!!!!~~~~~!7JJYJ?J5PPPGGGGGBBBBGPPPPPPPGGGGGBBBBBBB#&&&@@&5JJYJJ?777777????JJJJJYJJJ5GGP55555PB&&&&&BGGPBBBBGGGGPPPP5YYYYJ??????7?JJ??777??77!!~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #!!!!!!!!!!!!!!!!~!!!~!~~~~~!?JJJJJYPPPPPPPGGB##BBGPPPPPGGGGGBBBB##&&&&&@@@&5JJJJJJ??7777???JJJJJYJJ??JY5PP555PB&&&&###BB#BBBGGGPPP555YJJYJ?????????JJ????JJJ??77!!!~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #~!!!!!!!!!!!!~~~~~!!~~~~~~~!7?JJJJYPPPPPPPPPPGBBBBGGPPPGGGGGBBBB#&&@@@@@@@@&5JJJYYJ??777??????JJYJJJ???JY55555B&&##B###BBBBBBBBGP5YYY5YJJJJJJJ?????JJJ??JJJ???7777777!~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #~!!!!!!!!!!!!~~~!!!!~~~~~!?YPPJJYJJYPPPPPGGGGGBBBBBGGGBBBBBBBBB#&&&@@@@@@@@@#YJJYYYJ?777???????JJJJJJJJJJJYYY5G#&######BBBBBBBBBG5YYJY55JJJJJJJJJJJJJYJJJ????????????777!~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~
    #~!!!!!!!!!!!!!!~!!!!~~~~!JB###BPYJ?J5PPGB#######B####&&&&&&#BBB#&&@@@@@@@@@&#PJJJYYJJ??7???????JJJJJJJJJJJJJJYP#&######BBBGGBBGBGP555Y5PPYYYYYJJJJJJYYYJJ?JJJJJJ????????77!~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~
    #~!!!!!!!!!!!!!!~~!~~!~~!JG##&&&&BG5Y55PGGB#&&&&&&&&&&&&&&&&&&&#&&&@@@@@@@&#BBGY?JJYYYJJ?????????JYJJJJJJJJJJJYP#&######BBBGPPPPGGP55555PGPYYYYYYYYYYYYYJJJJJJJJJJJJJJ??????77!~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~!
    #~!!!!!!!!!!!!!!!!~~~~!?5B####&&&&&#BGGB###&&&&&&&&&&&&&&&&&&&&&@&@@@@@&#BGGGGG5JJJJYYJJ??77?????JYYYYYYJYJJYY5B##########BBGPPPGBPYYY555PGP55555Y5555YYYYJJJJJJJJJJJJJ????????77!~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~!
    #~!!!!!!!!!!!!!!!~~~!7YG#######&&&&&&&####&&&&###############&&@@@@@@@&BGBB##BBBY??JJYYJJ???77???JYYYYYYYYYYYYPB###########BGGGBGGGP5YYY55PGPP55555PP5YYYYYYYJJJJJJJJJJJJJ????????77!~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~!
    #~!!!!!!!!!!!!~!!~~!?5PGB######&&&&&&&&&&&##BPPPGBBB#BBB#####&&@@@@@@#B#########P??JJYYYJJ??7777??JYYYYYYYYY5PB####&&&####BBGGBBGGGGGPP5555PPPPPPPPP5555YYYYYYYYYYJJYYJJJJJJJ????????77!~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~!
    #~!!!!!!!!!!!!~!!~~!7J5555PB####&&&&&&&&&&&&&B555PGGB##&&&&&&&&@@@@@@&##########GJ?JJYYYJJJ????7??JYYYYYYYY5GB###&&&&&#####BBGGBBBGBBGGGPPPP55PPPPPGP555555YYYYYYYYYYYJJJJJJJJJJJJJJJJ???7!~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~!
    #~!!!!!!!!!!!!!!!~~~~!?YYYY5PGB##&&&&&&&&&&&&&#BB##&&&&&&&&&&@@@@@@@@&##&&&##&&&BY?JJYYYYJJJ???????JYYYY55PB#&&&&&&########BBBGBBBBGGGPGPPPGGPPPPPGGPPP5555555YYYYYYYYYYYYYYJYJJJJJJJJJ???J?!~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~!
    #~!!!!!!!!!!!!!!!~~~~~~7JY55PPGBBB#&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@&&##&&&&##BPJJJYYYYYJJJ?????JJYY55PG#&&&&&&&&#######BBBBGPGGPGPGGGGPPGGGGGGGGPPP55555555YY5YYYYYYYYYYYYYYJJJJJJJJJJJJJJ7~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~!
    #~!!!!!!!!!!!!~~~~~~~~~~!7YPGGPY?JPB##&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@&&&&&#BGGGPYYYYYYYYYJJ???JYY55PB#&&&&&############BBBBGPPGPPGGGBBGGGGGGGGGGGGP555555YYYYYYYYYY555555YYYYYYJJJJJJJJJJJ?7!~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~
    #~!!!!!!!!!!!!!~~~~~~~~~~!75PP5YY5PGB###&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@&&&&#BGGGGGBBGPPPP55YJJJJJJ55GB&&&&&&#############BBBBBGPPGGPPGGGGBGGBBGGGBBBGPP55555555YYYYYYYYYYY555555YYYYYYJJJJJJ????7~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~^~~~~~~~~~~~~~~
    #~!!!!!!!!~!!~~~~~~~~~~~~!7?JY5PPGBBGGGGB##&&&&&&&&#&&&&&&&@@@@@@@@&&##BBBGGGGGGGBBGBBBBGP55YYYYY5PB&&&&&&&&&############BBGGGGGPPGGPPPGGGBBBBBBBBBGGGPPPPPPP555555YYYYYJJJYYY555PP5YYJJJ?JJJ????7!~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~^~~~~~~~~~~~~~!
    #~!!!!!!!!~!!!~~~~~~~~~~~!7?JYYPGG5YY55PGGBBB#################&&##BGGGBBGGGGGGBBBGGGGBGBBGGPP5555G#&&&&&&&&&&&########BBBBBBGGGGGPPGGPPGGGGBBBBBBBBGGGGPPPPPPPPPP5555555YYYYYYY5PP555YJJJJJJJJJJJ???!~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~
    #~!!!!~!!!~!!!~~~~~~~~~~~!??JJY5PG5YJYY55PPPPPGGB####BB##BB###BGGPPPPGBBGPGGGGGGGGPGGBGGGGGGPPPPB&&&&&&&&&&###########BBBBBBGGGGGGPPPGPPGGGBBBBBB#BBGGGGGPPPPPPPPPPPPPPPP5P5555PP55YYJJJJYYYJJYJJJJJJ?7!~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~^~
    #~!!!!~!!!~~!~~~~~~~~~~~~7?JJY55PGGPYJJYY5555PPPGBBBBBBBBBBBGPPPPP55PGB#BBBGGGGGBBBBBBBBGGPGPPG#&&&&##&&&&&#B###BB##B#BBBBBBGGGGGGGGPPGGGGGBBBBB##BGGGGBGGGGGGGPPPGGGPPPPPPGPP555P5YJJJJJJYYYYYYYJJJJJJ?7~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~^^^~~~~~~~~~~~~^~
    #~!!!!~!!!~~~~~~~~!~~~~~!??JJYYY55PGG5YJYYY555PPGGBB#BBBBGP55YYYY555PPGB##BBBBBBBBBBGGGBBBBGGB#&&&&#####&##BBB#BBB###BBBBBBBGGGGGGGGGPPGBGBBB#BB##BGGGGGGBBGBGGGGGGGGGGGGGGGGP5YYY5YJJJJJJYYYYYYYYYYYJJ?7~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~^~~~~~~~~~~~~~!
    #~!!!!~!!!~~~!~~~~~~~~!7?JJJJJJYY5PGBBG5YYYY55PPGGGBBBGPP5YYYYYYY5555GGB##BGGGGGGGGGBBBBBBBBGB&&&&#########BGBBBBGB##BBBBBBBGGGGGGGGGPGGGBBGBB####BGGGGGBBBBBBBGGGGGGGGGGGGBGP5YYYYYYJJJJJYYY555555YYJJJ?7~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~^^^~~~~~~~~~~~~
    #~!!!!~!!!~~~!!!!~~~!!??JJJJJJYY5PGGBBBGP55Y55PGGBBBG55YYYYYY555555PPPGBBGBBBGGGBBB##BBBBBGBBBBB####BBB####BGBBGBGB###BBBBBGGGGGGGGGGGGGGGBBBB####BBGGGBBBBBBBBBBBGGGBGGGBGP555YYYYYYYYYYYJYYYYYY55YYYYJJJ?7~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^~^^^^^^^^^~^^^^^~
    #~!!!!!!!!~!!~!!!!!~!7?JJJYYYYYY55PGGBBBBGGP55PGGGP5YYYYY555555555PGPPPGGPPGBBBBBBBBBBBBBBBBBBBBBBBBBB#####BBBGGBGB##BBBBBBBBGBGGBBGGGGBBGGGBB####BBGGGBBBBBBBBBBBBBBBGGGP5YYYYYYYYYYYYYYYYYY5YJYYYYYYYYJJJJ?!~^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~^^^^^^^^^^^^^~
    #~!!!!!!!!~!!~!!~~~!7??JJYYYYYYY555PGGBBBBBBGPP55YYJYY5555555PPPPPPGGPPGPPGPB####BBBBBGGBBBBBBBBBBB########BBBGGBBBB##BBBBBGGGGGGGGBBGGGBBBGGB####BBBGGBBBBBBBBGBBBBBBBGP555555555YYYY5YYYYYY55555Y5555YYYJJJ?7~~^^^^^^^^^^^^^^^^^^^^^^^^^~~~~^~~~^^^^^^^^~
    #~!!!!!!!!~!!!!~~~~!??JJJJYYYYYY55PPPGGBB####B5YYYYY55555555PPPPGGGGGGBGGGBBBBB#####BBBBBBBBBBBBBB##&#######BBBGGBBB###BBBBGGGGGGGGBBBBBBBBBGGB####BBBGGGGGGGBBGBBBBBGGPPPPPPPP55555PPPPP5YYJJJYYY5555555YYYJJJ?7~^^^^^^^^^^^^^^^^^^^^^^^^~~~~~^^^^^^^^^^^~
    #~!!!!!!!!~~!!!~~~!7??JJYYYYYY555PPPPGGBBB#BG5YY5555P555555PPPGGGGBBBBBBBBBBBBBBBB######BBBBBBB###&&&#######BBBGGBBBB#BBBGGGGGBGGGGBBBBBBGBBBGBB####BBGGGGGGGBBBBBBBBBGGPPPPPPGGGGPPPPP555555PPPPPP55Y55555YYYYYJ?!~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~^^^^^~
    #~!!!!!!!!~~~!!~~~!?JJYY555555555555PPGBBG5YY5Y5P55PP55PP5PPGGGBBBBBBBBBBBBBBBBBBB#####&######&&&&#&########BBGGGBBBB#BBBGGGGGGBGGGBBBBBBGGBBBBB#####BGGGGGBBBBGBBBBB##BBGPPPPPP5PPP555PPGB##BGGPPY?777?JY555YYYYJJ7~^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~
    #~!!!!!!!!~~~~~~~!7?JJYYYYY555PPPPPGGPP5YJJJYPGGP55PP55PPPPGGBBBBBBBBBBGBBGBBBBBGGGGGBB######&&&&&&&#######BBBBBBBBBBB#BGGGGBBGBBGGGGBBBBGGGGBB###&&#BGGBBBBBGGBBBBBBBBBBBBBGP55555PGGGGB###BGGGP577?77777?JY5YYJJYJ7~^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~
    #~!!!!!!!!!~~~~!!7JJJYYY5555PPPPGPP5YYJJJY5Y5GBGP5PPPPPPPPGGBBBBBBBBBBGGGBBBBBBGGGGGGBBBB##&##&&&&&########BBBBBBBBBB###BBGGGGBBBBGPGGBBBGGGBBB###&&######BBBBBBBBBBBBBBBBBB##BGPGBBBBBB##BBBGGGGY7??J?77J?7Y55YYYJJ?!^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~
    #~!!!!!!!!!!~~~!7JJYYYYYYYYYYY555YJJJJJJ5P55PGGBPPP5PPPPPGGBBBBBBBBGGGGBBBBBBBGGGGGBBBBB#&&&###&&##########BBBBBBBBB####BBBBBGGGBBBGGGGGGGGBBBB#&&&&#######BBBBBBBBBBBBBBBBBBB######BBBBBBBBBBBGGPJ?77??JJ?7Y55YYYJJJ?~^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~
    #!!!!!!!!~!!~!!?JYYYYY555YYJJJJJJJJJJJY5PPPGGGGB#BPPPGPPGGBBBBBBBBGGGBBBBBBGGGGGGGBBBBB#&&&&&##&&#########B#BBBBBBBBBBBB#BBB#BBGGBBBBBBGGGGGBB##&&&&&&&####BBBBBBGBBBBBBBBBBBBBBB#BBBBGBBBBBBBBGGGY7?JYYJ?7Y55555YYJJJ7~^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~!
    #~!~!!!!!~~~!7JJYYY5PP5YJJJJJJJJJJYYYJYPPPGGGGBBBBBGGGPPGGBBBBBBGGBBBBBBBBBBBBBBBBBBB#&&&&&&&###&######BBBBB#BBBBB####BBBBBBB##BBBBBBBGGBBGGGBB###&&&&&&##BBGGGGGBBBBBBBBBBBBBBBBBBBGGGBBBBBBBBBGGP5JJ?J?Y5PPP555YYJJJ?7~^^^~^^^^^^^^^^^^~~~~~~~~~~~~~~~~^~
    #~!!!!~!!!!7JYYY5PGGPYJJJJJYYYYYYYYYJYPPPGGBBBBBBB#BGPPPGBBBBBBBBBBBBBBBBBBBBBBBBBBB#&&&&&&&&&##&######BBBBBB###BBB####BBBBBBBBBBBBGGGGGGGBBBGBB####&&&##BGGGGGGBBBBBBBBBBBBBBBBBGGGBBBBBBBBBBBBBGGGGPPPPPPPPPPP555YJJJJ7~^~~~^^^^^^^^^^~~~~~~~~~~~~~~~~~^~
    #!!!!!!7?JY555PGGGP5JJJJJYYYYYYY55YYJ5PPPBBBBBBBBBBBBPPGGBBBBBBBBBBBBBBBBBBBBBBBBB#&&&&&&&&&&###&&###BBBBBBBB#####B##BBBBBBBBGGGGGGGGPPPGPGGBBBBB###&&&&##BBBBGGGGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGGGGGPPPPPPPPPP55YYYYJJ?!~^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~
    #!!!!!?YY55PGBBG55YYYYJJJYYYYY55555YY5PGBBBBBBBBGGGGBGPGGGGBBBBBBBBGBBGGGGGGBBBB##&&&&&&&&&&&###&&##BBBBBBBBBBBBBBBBGGGGGBGGGGPPPPGBGGPGGBGGGGBBBB##&&&&&#B##BBGGGGGGBBBBBBBBBBBBBBBGGGGGGGBBBGGBBGGGGGGPGGPPPPPPP555YYJJJ?!~^^^^^^^^^^~~~~~~~~~~~~~~~~^~~~
    #~!!!!?JYPGBGP555YYYYJJJJY55555555555PPGBBBBBBBBGGGGBBBBGGGBB###BBBBGGGGBBBBBBB##&&&&&&&&&&&&######BBBBBBBBBBBGGGGGGGPGPPGGPPPPPPPPPGGGGGBBBGGGGBBB##&&&&#####BBBGGGGGBBBBBBBBBBBBGGBGGGBBBBBBGGBGGGGBGGGGGPPPPPPPPP5YYJYJJ?!~^^^^^^^^^~~~~~~~~~~~~~~~~~~~~
    #~!!!!?YPBGP5555YYYYYJJJJY5555555PP5PPGBBBBBBBBBBBBBBBB#BGGBBBBBBBBBBBGGBBBB###&&&&&&&&&&&&&&##B###BGBBBBBBBBGPPGGGPPPPPPPPPPGPPPPPPPGGGGPGBBBBBBGGB##&&&&######BBBGGGGGGBBBBBBBGGGBBGGGGBBBBBGBBGGGBBGGGGPPPPPPPP55Y555YYYJ?!^^^^^^^^^~~~~~~~~~~~~~~~~~~^~
    #~!!!!?PBGPPP555YYYYJJJJYY55555PPPPPPGGBBBBBBBBBBB#BBBBBBBBB#BBBBBBBBBBBBBB###&&&&&&&&&&&&&&&##B###BBBB###BBBGPGGGPPPPPPGPPPGGGGPPPPPPGBGGPGGBBGGGGGB#&&&&&######BBBGGGGGGGGGGBGBBBGBBBBGGGBBBBBBBGGGGGGGGGPPPPP55555555YYYYJ?~^^^~^^^~~~~~~~~~~~~~~~~~~~^~
    #!!!!!YBBBP5PP5YYYYYJJYYYY5555PPPPPPGGGBBBBBBBBBBBBBBBBBBBB#####BBBBB#######&&&&&&&&&&&&&&&&&##BB######BBBBBBGGGGGGGGGGGGGGGGPGGPPPPPPPGGBBBBBBBGGGGBB##&&&&&#####BBBBGGGGGGGGGGGBBBBBGBBBGGBBBBBBGGGGGGGGGPP55555PPPPP5555YYJ7~^^^^^~~~~~~~~~~~~~~~~~~~~~~
    #~!!!!JGBGP5P5Y5YYYYJJYP5Y555PPPPPPGGGGBBBBBBBBBBBBBBBBB##B###BBBBB#######&&&##&&&&&&&&&&#&&##BBB#####BBBBBBGGGGGGGGGGGGGGGGGPPPGGGGGPPPGGGBBBBBBGGGGBB##&&&&&####BBBBBBBBBBBBBBBBBBGBBBBBBBGBBBBBGGGGGGGGGPPP55PPPPPPPP55555Y?!~^^^^~~~~~~~~~~~~~~~~~~~~~~
    #!!!!!75GP5555YYYYYYJJ5GP5555PPPPGGGGGGBBBBBBBBBGGGBB###BBB#BBBBBBBBBBB#########&&&&&&&&&####BBBBB####BBBBBGGGBBBGGGGGGGGGGBBGGGGBBBBBGBGGGGGGGBBBGGGBB####&&&&######BB#BB###BBBGGBBGBBBBBBBBBBBBGGGGGGGPPPPPPPPGPPPPPPP555555J?7!~~^~~^~~~~~~~~~~~~~~~~~~~
    #~!!!!~755555Y5YYYYYYJ5BB555PPPPGGGGGGGBGGGGGGGGGBBB##BBBBBBBGBBBBBBBB###########&&&&&&&&###BBBBBB##BBBBBBGGGGBBBBGGGGGBGBBBBBBBBBBBBBBBBBGGGBGGGBBGGBBB####&&&&###########BBBBGGBBGBBBBBBBBBBBBBGGGGGGGGPPGGGGGGGGGPPPPPP55PP5YYJ7~~^~~~~~~~~~~~~~~~~~~~~~
    #~!!!!!!7Y555YYYYYYYYY5GBPY5PPPGGGGGGGGGGGGGGGGBBB##BBBBBBBBBBBBBBB###BBBBBBBBBB##&&&&&&&####BBBBGB##BBBBGGPGGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGBBGGGGGGBBBBB####&&&&########BBBBGGGBGBBBBBBBBBBBBBBGGGGGGGGGGGGGGGGGGGPPPPPPPPPP5JJJJ?!~~~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!?YYYYYYYYYYY5GBBP5PPPGGGGGGGGGGGGGGBBBBBBBGGGBGGBBBBBBB####BBGGBBBGGBGBB##&&&&&##BBBBBGGB##BBBGGPPGGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGBGGGGGGBB#BB####&&&&########BBBGGGGGGBBBBBBBBBBBGGGGGGGGBGBGBBBGGGBGGGPPPP55PGBPYJJJJJ7~~~~~~~~~~~~~~~~~~~~!
    #!!!!~!!!~~7?YYYYYYYYY5PBBBPPPPGGGGGGGGGGGGGBBBBBBBGGGBBBBBBBBB###&&####BBBBBBBGGGB##&&&##BBBBBBGGG##GGGGPPPGGBBBBBBBBBBBBBBB#BBBBBBBBBBBBBBBBGGGGGGGGBBB#BB######&&&&#######BBBGGGGGGBBBBBBBBGGGBBBBGBBBBGBBBGGBBGGGPPPPPGBBG5YYYJJJJ7~~~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!~!7JYYYYYY55PGBBGPPPGGGGGGGGGGGGGBBBBBGGGBBBBBBBBBB##&&&&&&&&&&&&####BBBB###&##BBBBBBBGGB#BBGGPPPGGBBBBBBBBBBBBBBB##BBBBBBBBBGGGBGGGBGGGGGBBBBBBBB##&&&&&&&&&######BBBBBBBGGGGBBBBBBBBBBBBBBBBGGBBBGGGGGBGPGGBBBP5P5YYYJYJJJ7~^~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!7JYYYY55PPGGBGPPGGGGGGGGGGGGBBBGGBBBBBBBBBBB####&&&&&&&&&&&&&&&&&&&&####&#BBBGBBBBGGGB#BGPPPPGGBBBBBBB##BBBBBBBB#BBBBBBBBGGGBBGGBBGGGGBBBBBB###&&&&&&&&&&&&#####BBBBBBBBGGGGGGGGGBBGGGBBBBGBBBGGGGGBBGGBBGGGP5555YYYYJJJ?7~~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!~!?JYY555PGGGBGPGGGGGGGGGGGGGGGGGBBBBBBBBBB###&&&&&&&&&&&&&&&##########&&#BBGGGBGGGGGB##GPPPGGGBBBBBBBBBBBBBBBBBBBBBGGGGBGGGGBBGGBBGGGGGBB########&&&&&&&&&&&&##BBBBBBBBBBBBGGGBBGGGGGBBGGGBBGGGGBB#BBBGGGGBGP5P5555YYYJJ?!~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!~~!?JY55PPPGGGGGGGGGGGGGGGGGGGGBBBBBBBBBB###&&&&&&&&&&&###############&&#BBBGGGGGGGGG##GPPPGGBBBBB###BBBBBBBBBBBBBBBGGGGGGGGBBBBBBGGGBBBB##########&&&&&&&&&&&&####BB##BBBBBGBBBGGGGGBBBBBBGGGGB###BBBBBGBBBGPP5PP555YJJJ7~~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!~~!7?Y55PPPGGGGGGGGGGGGGGGGGBBBBBBBBBB####&&#&&&&&&&&##############&#&##B#BGGGGGGGGGB#BP5PGGBBBBB##BBBBBBBBBBBBBBGGGGGGBBGBBB####BGGGBBBBB###BB#####&&&&&&&&&&&&&&#####B#BBBBBBGBBBBBGBBBGGGBBBBBBBBBGBBBBBGPPPPPP555YJJ?!~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!~!!7JY5PPPGGGGBBBBGGGGGGBBBBBBBBBBB#B55B###&&####################&&&#B###GGGGGGGGGG##GPPGBBBBBBBB##BB##BBBBGGGGGGGBGBB#BB#######BBGBBBBB############&&&&&&&&&&&&&######BBB#BGGBBBBBGBBBGBBBBB#BBGGBBBBBBGGPPPPPPP55YYJ?7~~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!!!!!7?Y5PPPGGBBBGGGBBBBBBBBBBBBB#BG?!?G###&###################&&#&##B###GPPGGGGGPGB#B5PGBBBBBBBB###BBBBBBBBBBBBBBBBBBBBBGGGB####BBBBBBBBB###########&&&&&&&&&&&&&#####BBBBBBBBGGGGGBBBBBGBB##BBBB#BBBBBGGGPPGGPPP55YJJ?!~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!~!!~~~!7?Y5PPGGGGGGGGBBBBB####BBPJ!~~?PBB################BB#######BBB###BPPPGGPPPPGBB55GBBBBBBBGBBBBBBBBBBBBBBGGGGGGGGGGGGGGBB###BGGBBBB#############&&&&&&&&&&&&######BBBBBBBBBBBBBBBBBBB##BBBBBBBBBBBGGGGGGGPPPP5YYJ?!~~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!!!~~!!~~!!7??JJJYY55PGGGBGGGP5Y7!~~~!?Y5PBBBBBBB#####BBBBBB#######BBB###BGPPPGPPPPPBBP5GBBBBBGBGGGBBBBBBBGGGGGPPPGGPPPGGGGGBBBB###BGGGBBBBB##########&&&&&&&&&&&&######BB#BBBBBBBBBGGBBBB##BBBBBBBBBBGGGGBGGGGGPPP55YJ?7~~~~~~~~~~~~~~!
    #~!!!!!!!!!!!!!!!!!!!!!!!!!!!!~~~~~!!!!77777?77!!!~~~~~~!7JYY5PGGGBBBBBBBBBBBB#####&#BBB####BGP55PGPPPPGBG5GBBBBBBBBBBBBGGPPPPPPPPGPPPPPPPPPGGBGGGGB###BGGBBBBBB#########&##&&&&&&&&&##B#######BBBGGGBBBBBBB##BBBBBBBGGBGGGBBBBGGGGGPP55YYJ?7~~~~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~~!7JJJY55PPPPGGGGGGGGBB#######BGB####BGP55PPGPPPPBBGPBB#BBBBBGGPPPPPPPPPPPPPGGPPPPPPGGGGBBGGGGB##BGGBBBBB#######################BGGB######BBBBBBB#BB#BBBBBBBGGBBBBBBBBBBGGGGGPPP5YJJJJ?!~~~~~~~~~~~!
    #~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~~~~7?JJY555555PPPPGGGGBB######BGGB####BBP555PPGPPPGBBBBBBGGGPPPPGGGPPPPPPPPPPPGGGPPGGGGGBBBGGGGGBBBBGGBBBBBBB####################BG55B#####B##BBB#BBBBBBBBBGGBB#BBBBBBBBBBGGGGPPP5YYY5YJJ7~~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!!!!!!!~!!!!!~~~~~~~~~~~~~~~~~~~~~~~~~!?JJYYY55555PPPPPGGB######&BGGBBBBBBBGP555PGGPPPG##BGGGPPPPPPGBGGPGPPPGGPPPPGGGGGGGBBBBBBGGGGGBBGGGBB##BBBBBBB##############BBGP5PG########BBB#BB##BBBGBBBBBBBBBBBBBBBBBGGGPPP55555YJJJ7~~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~~!!~~~~~~~~~~~~~~~~~~~~~!?JJYYYYY5555PPPPGBB#######BGGBBBBBBBGP5555PGGPPPB#BGGGGPPPPGGBBGGPPPGGGGPGGGGGGGGBBBBBBBBGGGGBBGGGBB##BBBBBBBB##########BBGGGGGGGB#######BB##BBBBBBBBBBBBBBB#BBBBBBBBBBBGGGPP5555YYYYJJ7~~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~~~~~~~!!~~~~~~~~~~~~~~~~~7?JYYY55555555PPGB########BGGBBBBBBBGP55555PGPPPGB#BGGPGGGGGGBBBGGPPPGGGGGGGGBBBBBBBBBBBGGGGGBBGGBB#B##BBBBBBBB#######BBGGGBBBBBBGBB#####BB##BBBGBBGGBBBBB####B###BBBBBBGGGGPPP5555YYYJJ!~~~~~~~!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~~~~~~~!~~~~~~~~~~~~~~~~~~!?JYY555YYY555PPPGB###&&###GGBBBBBGGGP555555PPGPPGB#BPPGGGGGGBBBBGGGGGBGGGGGGBBBBBBBBBBBBGGGGGGBBB#####BBBBBBBB####BBBGGB#####BBBGGBB###BB###BBBGBGBBBBBB########BBBBBBBBBBGPPPPPP55YYYJ?!~~~~~~!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~~~~!~~~~~~~~~~~~~~~~~!?Y55PPP5YYY55555PGB##&####BGGBBBBBGGGPP555555PGGGPGBBBGGGBBBBBBBBBBBBBBGGGBBBBBBBBBBBBBBBGGGGGGGBBB##B###BBBBBBBBBGGBBB#########BGGGGB##B####BBBBBBBBBBBBBBBBB###BBBBBBBBBGPPGGGPP555YYYJ?!~~~~~!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~!?J5PGGBBGP55PP5555PB#######GGBBGGGGGGGGP55YYY55PGGGPGB#BPGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBGGGGGGGBBB#####BBBBBBGGBBB############BGP555PB#####BBBBBBBBBBBBBBBBBBBBBBBBBBBGGPGGGGGGPPP55YYYJ?!~~~~!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~~~~~~~~~~~!7JY5PGGGBGGGGGGPPPPPGB#####BGGBBBGGGGGGGP55YYYY5PPGGPPG#BPGBBBBBBBBBBBBBBBBBB########B###BBBBBGGGGBBBB#########BBBB##########&&####BP5Y55PG########BBBBBBBBBBBBB#####BBBBBBGGGBGGGGGGPPP55YYJ7~~~~!
    #~!!!!!~~!!~!~~!!~~~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!7??JJJJYYJYY555YYYYYY55PPP5YY555YYYYYYYYYJJ?????JJJYYYY55YY5Y555555555555PPPPPPPPPPP55555555555Y5YY55555PPPPPPP55PPPPPPPPGPPPPPPPPP5YJJJJJJ5PPPPPPPP5555555555PPPPPPPPPPPP55555555555YYYYJJJJ?7!~~!
    pass
class StaticServer:
    def __init__(self):
        self.app = flask.Flask(__name__)
        self.blocks = OrderedDict()


    # Maps a block hash to the block itself

        @self.app.route('/head')
        def head():
            return list(self.blocks.keys())[-1]

        @self.app.route('/fetch/<digest>')
        def fetch(digest):
            try:
                return self.blocks[digest]

            except KeyError:
                # HTTP code 400 indicates a bad request error
                return 'hash digest not found', 400

        @self.app.route('/<command>')
        def maintain(command):
            # Grab the commands
            arguments = [c.strip() for c in command.split(" ")]

            # Allow for block addition
            if arguments[0] == "add":
                if arguments[1] == "block":
                    block = arguments[2]
                    block_hash = hash('hex',block.encode()).hexdigest()
                    self.blocks[block_hash] = block

            # Allow for block removal
            elif arguments[0] == "remove":
                if arguments[1] == "head":
                    self.blocks.popitem()

            # Error case
            else:
                return f'command {command} not understood by server', 269

    def run(self,host='lion',port=5000,gen_block=None,override=True):
        if override:
            pass
        elif not self.blocks and gen_block is None:
            block = build_block('',{'chat' : 'my very own blockchain!'},0)
            block_hash = hash('hex',block.encode())
            self.blocks[block_hash] = block
            print(f"head is now {list(self.blocks.keys())[-1]}")
        else:
            block_hash = hash('hex',gen_block.encode())
            self.blocks[block_hash] = gen_block
            print(f"head is now {list(self.blocks.keys())[-1]}")



        self.app.run(host=host,port=port)



# This Class is where its at
def good():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!~~!~~!!~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!777777
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!77!!7
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!77?JJJJJJJJ?77!~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!7?JY5555555555555555Y?7!~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!7?JJYJJ????????JJJJJYY55PP5YJ7!~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~7???77!!!!!!!!!!!!77777777??JY555Y?!~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!??7!!!!!777777777777777777?7777??JY55J!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!777!!!77777777777???????????????????7?JYY?!~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^~~^^~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~777!!777777777777777??????????????????????JYY?~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^~~~~~~~~~~~~~~~~~~^^~~^^~~~~~~~~~~~~~~~~~~~~~~~~^^^^^~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!??77!77!!!777777777????????7???7??7????JJ???JY5J!~~!~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^~~~~~~~~~~~~~~~~~~^^~^^^~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^~~~~~~~~~~~~~~~~~~~~~~^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!??777777?JY5PPP5YJJJJ????????JJJJ????????JJJ???Y5Y!~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^~~~~~~~~~~~~~~~~~~^^~^^^^^~~~~~~~~~~~~~~~~~~~~~~^^^^^~~~~~^~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~???777?5GBB######GPYYYYJJJYYYY55PGGPP5YJ???JJJJ?JYPY7!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^~^^~~~~~~~~~~~~~~^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^~~~~~~~~~~~~~~^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~7J??7?5GGGGGGGGGGPP55YYYJYY555PPB##&&&&#BP5J?JJJJJY55Y!~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^~~~~~~~~~~~~~~^^^^^^~~^~^^~~~~~~~~~^^~~~~~~~~~~~~~~~~~~^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~???7J555YYYYYY5PPPP5YJ??7??YY5PGGBBBBB#####BPJ?JJYY55PJ!~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^~~~^^^^^~~~^^^^^^^^^^~~~^~^^^^^~~~~~~^^^^~~~~~~~^~~~~~~~~^^^^^^~^~~~~~~~~~~^^~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!??77JYJJJ??JY5PGBBG5J77!777?J5GBBBGPP55PPPGGBGY?JJYYY5Y7~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^~^~^^^^^^^^^^^^^^^^^^~~^^~^^^^~~~~~^~~^~^^^^^^^^^^~~~~~^^^^^^^^^^~~~~~~~~~~^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!??7?JJJJJY5GBB#BG5Y?7!!!77??JYPGBBGP5YYY555PPGPJ?JYYY557~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~^^^^^^^^^^~~~~~~~~~~~~~^^^^^^^^~~~~^^^~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~7?77?JJY55PPPP5YJ?777!!7777????JYPB##BGGP555PPPPJ?JYYYY5?~!~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~^~^^^^~^^^^^~^~^^^~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~7?7!77777777777???77!!77??????JJ??JYPGB##BBP55P5Y??JYYYY?~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~^~~~~^^^^^^^^^^^^^~~~~~~~~^~~^^^~~~~^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!777!!!!!777??JJJ????77?JJJJJ???JYJJ????JJYYY555YJ??JYYYY7~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^~^^^^^^^^^^^^^^^~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!777!!!77???JJYYJYGB#G5YY55GBBGYJY55JJ?????????JJJJ?JYYYJ!~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~^^^^^^^^^^^^^^^~~~~~^^^~~~~~~^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!777777777?JJY55YJ?J5GB###GGB#&&&&BP555YYJJJ???????J???JYYY?~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~JYY?7777??Y5PP5YJJ5PGB##&&&#&&&###BPYJJY55YYYJJJJJJJ???JYYY7~~~!!~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~!Y5J?777??YPGPPGGGBBB#BBBBBBBB###&##BGP555PPP55YYJJJJJ??JY5J7!!~!!~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~^~~~~~~~~~~~~~~~~~~^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~!JJ?77?7?YPGBBBBBBGP555555555PPPGGGB####BGGGGG55YJJJJJJJYYY5PPJ!~~!~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~??J?7???5PGBBBGP5555YY55PPPPPGGGGPPPGB#&&##BBGP5YJJJJJJYY55PG57~!~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~7?JY???JY55GBGPPPPYJJJJJYYY5555PPGBBBGG##&##BGP5YYJJJJYJYYY5G5!~!~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~^^^^^~~~~~~~~~~~~~~~~~~~~~~^^^^~~!!77?PP5YY55PBG5YJ?????JYYYY55555Y555PGGGB###BGGP5YYYJY55J55YYPY!~~~~!~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~^^^^^^^~~~~~~~~~~~~~~~~~~^^~!?JYPGGP?!7GBBGGGGB#BPYJJYPGBB####BBBGP55YYYY5PG###GGGP5YYYYPG5Y5PYYJ!~~~~~!~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~^^^^^^^~~~~~~~~~~~~~~~~~~!JPGBBBGGBBG5YG###BB###BGPPGB##&&&&&&&&&&#BGP555PGB#&#BBBBGGGGB#G5YJJYJ?7777!!~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~^~JGBBBPPPPPGBBGB####B####BBBBB######&#&&&&&###BGGGGB#&&#########&#GYJ?JJ5BBBBBBP5J?!!~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~^^^^^^^^~~^^^^^~~^^^^^~~~~~~^~^~^~75BGP5P5PB#####################################BBBB###&&&&&&&&###&BBGP5PB#&&&#&####BG5J?!!~~~~!!!~!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~^^^^^^^^^~~^^^^^~~^^^^^^~~~~~~^^~75GPP5YPPP###BG55PGGGB#&&&&&&#######&&&&&&&&&&&&#####&&&&&&&&&&&&&&##&&&&#&&&&&####BB#####BG5J7!~~!!!!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~^^^^^^^^^^^^^^~^~~~~7YGGP5YYPGGGGPYY555PGGGYP#&&&&&&&&#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&GG#&&&&&&&&&&&&&&##BBBB#####BG5?!~~!!!!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~^^^^^^^^^^^^^~~^^^^~?PPP5YYY5GP5J?JJY5PGGBB5?JP#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#P5BBGBB#&&&&&&&&&&&&###BBBB##BB#BGY?!~~!!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~^~^~~~~~~~~^~^^~75PP5YY5PP5YJJ?JJY5PPGGBGY?JYP#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@&#G55P####GPBBB#&&&&&&&&&&&#####GGGB###BG57~!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~^~~~^~~^^^^^~~~^^^~JP5YJYPGG5J??JJJJ5PGGGGBBGYJJYY5B&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@&&#GP555G&&&&#P5G55G#&&#####&#&&&&&##BBBB##B#GJ!!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~^^^^^~~^^^^^^~!YPYJJY5P5JJJJJJJY5GGGBBB##GYYYYYY5PB#&&&&&&&&&&&&&&&&&&&&&&&&&&&&#BPPPP55B&&&&##GPP5YP#&&&##########&&&##GG##B#BJ!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~^~^^~?5YJJY55YJ??JJJJYY5PGBBBB###GYYY555555PB#&&&&&&&&&&&&&&&&&&&&&&&##BGGPPPPPG#&&&#BBGPP5YYG&&&&&&&&&##&&&&&&&BGB##BBP7!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~7Y5YJYY5YJ???JY555PPGGBBBB##&&G55555555555PGB####&&&&&&&&&&&&&##BBGGGGGGPPPPB&&##BBGPP5YJY5#&&&&&&&&&&&&&#####GGGGGGG7!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~^^!J55YYY5YJJJJJJJ5PPPGGBBBB####&&GP555555555555PPGGGGBB########BBBBGGGGGGGGGGGGB##BBGGP55YYYY5B&&&&&&&&&&&&####BBGBGPGG57~!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~^^^~^~?Y5YJJJJY5PPPPPPPPGGGGBBBBB###&&&BPPPP555555555PPPPPPGGGGGGGBBBGGGGGGGGGBGGGGB###BBBBGP55YYYYPG#&&&&&&&&&&&###BP55GGPPG5?!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~^^^^~7JY5YYYYJJ5GBGGGGGGPGGBBBBB#####&&&BGPPPPPPPPPPPP5PPPPPPPPPGGGGGGGGBBGBBBBBBBGB#####BBGGPPYYYYYPPBB##&&&&&&&###BBP5PGGPGG5J!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~7JJYYY55P5YPGGGGGGGGP5PBBBBB#####&&&&BGGPPPPPPPPPPPPPPPPPPPPPGGGGGGGBBBBBBBBBBBB###BBBGGGGGP5YYY5PPGGGBB##&&&&##BBBGGGPPGGPYJ7~!!!!!!!!!!!!!!7
    #^^^^~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~!7?JYJJY555555GGGBBGGGGGGGBBBBBBB###&&&&#BBGPPPPPPPPPPPPPPPPPPPPPGGGGGGBBBBBBBBBBB####BBBGGP555555YY5PGP55PPGBB#######BPGP5PPGPYJ?!!!!!!!!!!!!!!!7
    #^^^^~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~!77?JJJJJJJJJJY5PPPGGGBGGGGGGGBBBBB######&&&##BBGGPPPPPPPPPPPPPPPPPPPGGGGGGGBBBBBBBBBB###BBGPPPP5YYYYYY55PPGPYYY5PGGBBB####GPGP5PGGPYJJ7!!!!!!!!!!!!!!7
    #^^~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~!7?JJYYYJJJJJJJJJJJYYY5PPGGGBGGGGGGGBBBBBB#####&&&##BBGGGPPPPPPPPPPPPPPPPPPPGGGGGGGGBBBBBBB##BBGGPP555P55YY5555PGGPYYYPPPGBBBBGGGGBGPPPGG5YYJ?!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~7JYYYYY5YYJJJJJJJJJJJYJYYY5PGGGGGGGGGGGBBBBBB####&&&#BBBBGGGPPPPPPPPPPPPPPPPPPGGGGGGGGGBBBBBB##BGGGGPPP55PP555555PGGG5Y5PP5PGGGBGGPPBBGGPPGP5Y5Y?!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!JYYYY55555YYYJJJJJJJYYYYYY55PGGGGBGGGGGGGGBBBBBB##&&##BBBBGGGGGPPPPPPPPPPPPPPPPPGGGGGGGGBBBBB##BBGGGGPGGGGPG55555PPGGGG5PGPYY55PPGGGGGBGGBPGG5Y5YJ7!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~?YYY5Y??JYYYJJJJJYYYYYYY5PP5PGGGBBGGGGGGGGGBBBBB#&&##BBBBGGGGGGPPPPPPPPPPPPPPPPPGGGGGGGBBBBB###BGGGGPPGBGGGGPPPPGGGGGGGGGP5Y55555PPPGGP55PPPG5YYYJ7!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!?YYJ?77?JYYYYYYYYYYYY55PPPPGGGGBBBBBGGGGGGBBBB##&#BBBBGGGGGGGGGPPPPPPPPGGGGGGGPGGGGGGGBBBBB##BGGGGPGBBBGGGGGGGGGGGBGBBBGPPPPP55PP5GGGPP555PG5YY?7!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~!77?JYYJJJJJYYY555555555555PPPGGGGBBBGGGGBBBBBBB##GPPGGGGGGPPGGGGPPPPPPPPGGGGGGGPPPPPGGGBBBBB###GGGGGGBBBBBBBBGGGGBBBBB#BBGGGGGP55GP55PP55555PPY?!!~!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~77??J?JJYYJJYY5555555PPP5555PPPGGGGGBBBBBBGGBBBB#&&BPYJJY5PPPPPPPPPPPPPPPPPGGGGGGGGPPPPPGGBBBBB##BGGGGBBBBBBBBBBBBBBBGB##BBGGGGGGP55GGP5PPY5PPPG5?~~!!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~!7??JJJJJJJYYYYYY5PPPPGGP555PPPGPPGGGGGBBBGGGGGGBB#&&#PYJJJ????JY55PPPPPPPPPPPGGGGGGGPPPPPPGBBBBBGGPPGGGBBBBBBBBBBBBBBBBB###BBBGGGGGGGPP5PPPGPPPPGPY7!~~!!!!!!!!!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~!7?JJJJJJYYYYYY55PPP5JJ5P55PGGGGGGPGGGGGGBBBBBBBB#&&&&&B5J????77777777?JYY5555PPGGGGGGGPPPPPPPP5YYJJJJPGBBBBBBBBBBBBBBBBB####BBBGBGGGGGP5555GPP555PGPP5J?!!!!!!!!!!!!!!!!!!
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~7??JJJJJJYYYYYYYY555Y?77JYYY5GBBBBGGGGGGBBBBBBBBB###&&##GYJJ??77777777!!!!77777???JJJJJJJJ????????JJJYPBBBBBBBBBBBBBBB########BBBBGGPGGP555PPGGG555PPPP5YYJJ?7!~!!!!!!!!!!!!
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~7?JJJJJJJYYYYYYYYYY55YYYYYY555GBBBBBGGGGGGGGGBBBBBBB#####B5JJJ???77777!!!!!!7!!777!7!!7777777??????????5GBB#BBBBBBBBB#######&##BBBGGGPGPPPPGGGGGGGGGPPPP555YYYYYJ77!!!!!!!!!!7
    #^~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~!?JJJJJJJJYYYYYYYYYY5P5YY55PPPGGGGGB###GGGGGGGGGB###BB#####GJ???????777777!!!!!!!!!!!!!!777777777777777?JPBB#BGBBBBB######&&&###BPPGBGGGGGGGGPPPPP55P55PPP5555555YYYJJ?!!!!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~7?JJJJJJJJYY5555YYP55P5JJY5PPGGGGGBB##BBGPGGGGGGGBB##BBBB###GJ7777777777777777777777!!7777777777777777???5BB#BGBBBBB######&&&##BGBBBBBBGPPPP5555Y5555PP55PPP55555555YYYYJ?7!!!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!7?JJJJJJJYYYY55P55P555YJJJJYY5PGGGBBBBBGGPPPPGGGGGGGB#BBBBB#GYY?7777777777777777777777777777777777777777?YGBBBBBBBB#####BBB##&##BBB###BGP555555555PPPPPPP5PGPP5Y55PP55YYYYYJ?7!!!7
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~!??JJJJJJYYYY555555PP55YJJJJJYYY5PGBBGGGPP5555PPPPPPPPGB#BBBBBYJJJ?7777777777!!!!!!!!!!!!!!777777777777777?5BBBGGBBBBBBBBBGG######BBBBBGGPPPPPPPP55PPGGGGGGPPPPP55Y55PPP5555YYYJ7!!7
    #^~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~7?JJJJJYYYYY55555YYPG5YYJJJJYYYYY5PGGPPP5555YYYY55PPPPPPGBBGBBGYJJJ?77777777777!!!!!!!!!!!!!!!!777777777777YGBBBGBBBBBBBBGGGB#BBB####BGPPPGGGPP555PPPP5PGBGBGPPPPPP5555PPP55555Y5YJ?7
    #^~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~!??JJJJJJYYYY55555YY5G5YYYYYYYYYYYYY5555YYYYYYYYYYYY55PPPPPPBBBBB5JJ???777777777!!!!!!!!!!!!!!!!!!!!!!77!!77JPBBBGGBBBB##BGGGBBBBBB####BGPGGG5YJ????JPGGPPPGBBBBGGPPPP5PPPPP5555555555Y
    #^~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~7JJJJJJJJYYYYY555PP55P5YJYYYYYYYYYYYYYYYYYYYYYYYYYYY5555PPPPPPBBBBGJ????777777777!!!!!!!!!!!!!!!!!!!!!!!!!!7?5GBBBGGBBBBBBGGGBBBBBBB####BGPPY?777?JJJJ5GGBGGGGGGGP5PPPPPPPPGBP55PPPPPP5P
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!??JJJJJJJJYYYYY55PPP55PYJJJYYYYYYYYYYYYYYYYYYYYYYYYY5555P5PPPPPPBBBGY????777777777!!!!!!!!!!!!!!!!!!!!!!!!!!7JPBBBGGGGGGGGGGGGBBBGGGGBB##BPY?77?JJYYY555555555PPPPPPPPPGP555GGPPGGGGPPP55
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~7?J?JJJJJJJJYYYYY5PPPP5P5JJJJYY5Y55YYYYYYYYYYYYYYYYYY55555GGP5PPPPPBBB5????777777777777!!!!!!!!!!!!!!!!!!!!!!!7?J5PGGBGPPPPPPPPGBGGPPPGGBBGY?7??JJYYY55PPPPPPPPPGGGGGGGPPPP55PGPPGGPPPPP555
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~7?JJJJJYJJJJJYYYYY5PGGG55YJJJJYYY55YYYYYY55555555Y555555555PBBP5PPPPPBBGJ??777777777777777!!!!!!!!!!!!!!!!!!!!7????JJ5P5Y555555PGGPP55555Y?77??JJJJJJPGGGGBBB#######BBGPPPPPPPPPGGP55Y55555P
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~7?JJJJJJYYYJJJJY5555PGGGP5YJJJYYYY55YYYY55555555555555555555PBBP5PPPPPPGGY??777777!!77!!!777!!!!!!!!!!!!!!!!!!7JYYYYYJJJYY55555GGP5555YJ?777??JYYYYJJP#&&############BBGPPPPPPGGGGP555555555P
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~7?JJYJJJJYYYYJJJYYPPP5PPGGPYJJJYYY55YJYY55PP5PP555555555P5555PBG55PPPPPPGG5??777777!!!!!!!!777!7!!!!!!!!!!!!!!!!?JYY555YJJY5555PG5555YJ77777?JJYYYYY5B#############BBBBGGPPPPPGGGP555555555555
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~7?JJJYYYYYYYY5YYJJY5PGPPPGGGYJJYYYY5YJJJ55PPPPPP55555P55PP5555GB555PPPPPPPG5??777777!!!7!!!77775BG?!!!!!!!!!!!!!!?JJJJJYYJ?JYYY55YYYJ?77777??JYYYYY5G#####BBBBBBGBGGPPPPPPPPPPGBGPP55PPP5555555
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~^^^^^^^^^^^^^^^^^!??JJJJYYYY55YYY55YY555PGGPPGPYJYYJY5PYJJJ5PPPGG5555PPPP5PPP5555GG555PPP5PPPGPJ?7777777!7!!!!77!75GY7!!!!!!!!!!!!!7YY?77777???????7777777?????JY55YY5GBBGGGGPPPPPPPPPPPPPPPPPPPGBBBGPPPPPPPPPPP5P
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~!???JJJJYYY5P55YYY5P55PPPPGGGPPYYYYYY5PYJJYPPPGGP55PP5PP55PPP5555GG55PPPGPPPPPPJ?77777777!!7!!!!!?P?!!!!!!!!!!!!!!!?5PJ?JJJJJYYYYYYJJ????JJYYJJJJYYJJJ5PPPPPPPPPPP55555PPPPPPPPGB#BGPPPPPPGPPPPPPP
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!??JJJJJJYY555P555YY5PPPPPPPPGGG5Y5YYY55YJJ5GPPGGP5PPP5GP5PPPG5555GP55PPPGGPPPP5J?77777777!!!!?J77PY!7!!!!!!!!!!!!!!JGGPYJJYYY5Y555YYYYJJYYYYYYJJJJJJJJ?JY5PPPPPPPPPP5P5PPPPPPPGBBGGPPPGGGGGGPPPPPP
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^!???JJJJJYYYY555555555P5PPGGGGGGGP5555555YJY5GPPGG55GP55GP5PPPG55PPGP5PPPPPGPPPPPJ?77777777!!!7G&#BP!!7777!!!!!!!77!75GGPPYJJYY55555555555555555YJJJJJJJJJJYPPPPPPPPPPPPPPPPPPPGBBGPPGGGGGGPPPGPPPPP
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~7???JJJJJYYYYY55555555PGPPPPGBBBGP5P555YYYYYPP5PPP5PPP5PG55PPPP55GPPP55P5PPGBGPPPY?7777777777YB&&&#?!7777777!!!!!777JPBGPY??JYYYYYYYYYYJJJYYYYYYYYYYYYYYYJJJPPPPPPGGPPPPPPPPPPGB#GGGGGGGGGGGGGGGGGGG
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~!?JJ?JJJJJJYYYYYY555555PPPGGGGGGGBBG5Y5PYYYYY55YYYYY555555P5PPPPP55GGPPP5P555GBBP5P5J?7777777JPP5#&&#J!7777777!!!!!7775GBG5??JYJYYYYJYYYJJJJJJJJYYYYYJJJJJJJJJPPPPPGGPPPPPPPPPPG#BBBBBBGGGBGGBBBBBGGPG
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~7JJJJJJJJJJYYYY5555555PPPPP5PGBBBBBBGP5PPYYYYYYYYYYYYYYJYYYYYY555PPPPGPPPPP555GB#BG5PJ?77777?5P?!J#&&#7!!77777777!!!77JPBBGP5YYYYYYYYYYYYYYYYYYYY5555YJJJ?JJJJJYPPGGGPPPPPPPPPPG##BBBGG555PPPPPPGB#GPY5
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~7JJJJJJJJYYYYYY555555PPPPGGPPPPGGBGBBBGPPYYYYYYYYYYYYYYYYYJJJJYYYYYY55PPPP5P555PB###GPY??7777?JJYG&&&&#Y!!777777!!!!77?YGBBGPPGGG5JJJJJYYYYYYYYYYYYYYYYYJJJJJJJJJYPGBGPGGGPPPPPGB#BBGPP55YY5Y55555PGBBGP
    #^~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~!?JJJY5YYYYYYYYYY555PP55PPPPPGGGGGGGGGPBBG5YYJJYYY55555YYYYYYYYYYYJJJJYYYYYYYYYY5PG###BG5J?7!7?YP###G5PB&&BY7!77777777!7JPBBBGGGBGBBPJ?JJJYYYY5Y5YJJJJJYYYYYYYYYJJJY55PGGGGGGGGPGB##BGPP5555555555555PGG##
    #^~~~~~~~~~~~~~^^~^^^^^^^^^^^^^^^^^^^^^^^~^^^^~~7?JJJJY5YYY55555YY5PPPPPP5PGPPPPGGPGGGGPGGGYYJJJJYY5555555YYYYYYYYYYYYYYYJYYYYYYYYPB#BBBGY?JY5B#BGY?7!!!7?5GBBY7!77777777YGBBGGGBGGBGGPYJ?JYY5Y55YYJ????JY5555YYYJJJY5555PGGBBGBGB##BGGGPPPP55555555555PGG#
    #^~~~~~~~~~~~~~~~~~^^~~~~^^~^~~~^^^^^^^~^^^^^^~7?JJJJJYYYY55P55PP55PGGPPPPPPGGPPPGGPPPGGGGPYJJJJJYY555555YYYYYYYYYYYYYYYYYYYYYYY5PG#BBBBP5GBBPY?7777777777!!?P#BJ77777777YGBBBBBBGGBGGGG5YJJYYYYYJ???????????????J?JY555555PPGGGB##BGPPPPPPPPPP55555555PPGB
    #^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^~~^~^~7JJJJJJJYYYYY55555PPP55GGGPPPPPGGGPPPGGGPGBG5YJJJJYYY55555555555YYYYYYYYYYYYYYY5555GB#BBBG5JYJ?777777??7777777!!?PBG5J?7777YGGBBGGGPPPPP5PB#G5YYYYJJJJJYYJJJJ???J????JP555PP5P555PG#BBGPPPPPPPPP5555555PPPPGG
    #^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~?YYYYYYYYYYY5555PPPPGP55PGGGGPPPGBGGPPGBGGGG5YJJJJYYY55555555555555555555555555555PB#BB#GPY77JJ?77777??7777777777!JG5J7777?5GBBGGPPP55555P#&&&#BGPJ?JJJJYYYYJJJJJJJ??YP555PPPGG5YYPBBGPPPPPPPPPP55555PPPPPPGG
    #^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~!JYYYYY5YYYYY5PPPPPGPPPP5PPGBBGPPPGBBBGGGBBBPYYJJJYYYYYY555YYY55555555555555555PPPPGB#BBBGPY??55J7777777?J77777777777777777?YGBBBGPPPPPP55PB&&&&&&&BY7777???JJJJJJJJJJ5P555PPPGG55YYY5PPPPPPPPPPPPPPPPPPPPPPPG
    #^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~7JYYYYYYYY5YYYPGGGPPPPPGGPPPGGBBGPPGBBBBBBBGPYYJJJJYYYYY555YYYYY55555555P55PPPPPPPGBBBGBBPP5YJ7777?77777JY7777777?55?777777?YGBBBGPPPPPPPPPB#&&&&&&&G?7777??JJJJJJJJJ5BGP5PPGGBBP5YYYYY5PPPPPPPPPGGGGGGPPPPPPG
    #^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~?J5555YYYYY55Y5GGGGPPPPPPGGGPGGGBGPGBBBBBBBB5YJJJJY5YYYYYYYYYY5YY55555PPPPPPPPPPGGBB#BBBBP555Y?777777777?77777777?JJ?7?7????YGBBGGPGPPPPPPPPB#&&&&&@&PJ77??JJJJJJJJJ5BBGPPPPGB#BGP5YYYYYY5PGGGGBBBBBBBBBBBGGPP
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!?JYPPPP55YY5555PGBBGPPPPPPGGPPGGGBGGBBBBBBBB5YJJJJY5YYY5YYYYYY5Y55555PPPPPPPGGGGBBBBBBBBGPY55YYJ?777777777??777777777???????YG#BGPGGPPPPGGGGPGB##&&&@&BY???JJJJJJYYG##GGGPPPGB##BGGP5YJJYYY5GBGGGGGGGGGGGGGBGG
    #^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!?JJY55GBBGGPPPPPPGGBBBGGGPPPGPPPPGGBBBBBB##BYYYJJY55YYY5YYYYY55Y555555PPPPGGGGGGBB##BBBBP5JJYYYYJ?77777777777777777?????????JG#BGGGPPPGGGGGGGGPGGB#&&&@&BGP5555PGB&&#BGBGPPGGB##BBGP5YYYYJYY55555555555555PPPG
    #^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!JYYJYY5GGBBBGGGGGGGGBBBBGBBGGPPPPPGBBBBBB##G5YYYJY5YYYY5YYYYYPYY555555PPPPPGGGGBBBB#BBBBPY??JJYYJJ?777777777777??77?????????JPBBGGPPPGGGGGGGBGGGPPGGB#&@@@@@&&&&@@&#BGGBBBBB######BPYYYYYJYYYYY555555555555PPG
    #^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~!YP5JJY5PPPGGBBGGPGGGGGBBBBBBBGPPPPGBBBBGGBBG5YYYYY5YYYY5YYYY55YYY5555PPPPPPGGGGBBB##BBBGP5J???JJJJJ?77777777777777??????????JP#BBPPPPGGGGBBBBBBBGGPGBGB#&@@@@@&&##BBBGGGGGB##&####BG5YYYYYYYYYYY55555PPPPPPPPP
    #^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~7YP5YJJ5PPPPGGBBBBBBGGGGGGBBB##BGGGBBBB##BGGGPYYYYY5YYY5YYYYYPYJYY55555PP5PPGGGBBBB#BBB#GPPY?7??JJJJJ??7777777777?????????JJJJG##BGPPGGGGBBBBBBBBBGGGGGGGB##&&#BBBBBBBBBGGGG#BB###BGP5YYYYYYYYYYYYY55PPPPPGGGGG
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!?Y5PP5Y5PGPPPPGGB#####BGGGGBBBB#BBBBBBBBBBBB5JY55YYYYYY55YYY5PYJYY55555555PPGGGBBB##BBBBPPP5J?7??JJJJJ?777777777?????????JJJJYG##BGPPGGGBBBBBBBBBBBBBGGGGGGGGGGBBBBBBBBBBBB##BBBBBBP555YYYYYYYYYYYYYYYY5PPPPPPG
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!JYYYPPPPPGBBBGGGGBBB#####BBBBB#B###BBBBBBBGY!~?5P555YY555YYY5PYJYY555555555PGGBBBB##BB#GPPPP5J?77?JJJJJ?7777777??????????JJJJ5B##BGPPGGBBBBBBBBBBBBGGPGBGGGGBBGGGGBB######BBBBBBBBG5555555YYJYYYYYYYYYYYY5PPPPP
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!?JYY5PGPPPGGGBBBB###########BBB######BGGGPY!^~?55555555P5555PPYYY555P5555555PGBBB##BBBBPPPPP5Y?777??JJJ??777777?????????JJJJJ5B##BGPGGBBBBBBBBBBBBBGPPPGB#GG########B#####BBBGBBBGPPPPPPPP55YJJYYYYYYY5YY5PPGGG
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!?JJYY5PGGGPPGGGGBBB##########BBB########GJ!~~!YYYYYYY55PPPPPPP555555PP5P5YY55PBBB#BBBBP5PPP555J?77?????J??777777????????JJJJJP###BGPGBBBBBBBBBBBBBBBGP55G#BPGB######BBBBBBBBGGBBGPPPPPPPPPPPP5YY5PP5YY55YY555PG
    #^~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~^~?JJJYYYY55555GBBBGGGGGGB#############BGGPY!~~7YYYYYYYY55Y555P5555PPPPP5P555555GB#BGBBP55P55555YJ?777???????777777777????JJJJJP###BPPGBBBGGGBBBBBBBBBBPPPPBBGGBB#BGB#BBBGGBBGGGGGPPPPPPPPPP5P55YPBBG55555YYYY55P
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7JJYY5555555PPPGGGGGGGGGBB######&&&&##BBGPY7!!Y55Y555555555PGP55555PPPPGPPPPPPPGB#BB#G55PPPPPPP55YJ??JJJJJJJJJ?????JJJJJJYYYY5G###BGGBBBBBBBBBBBBBBBB#BGGGGBGBBBBBGGBBBBBBGGGGGGGGGGGGGPPPPPPP5PB##G5555P555555P
    pass
class DynamicServer:


################################################################################
#                                   Run Init
################################################################################

    def __init__(self):

        # Info
        printc(f"\tInitialize",TAN)
        self.app = flask.Flask(__name__)
        self.empty = True
        self.head_hash = ''                     # Keep track of whats in current
        self.longest_chain = 0                  # This will be used as a dynamic
                                                #                 'current.json'
        self.scan_chains()                      # Builds the initial chains list
        printc(f"\tInitialized, Starting server\n\n\n",GREEN)




################################################################################
#                    HANDLE HEAD REQUESTS
################################################################################

        @self.app.route('/head')
        def head():

            # Some simple debug code
            printc(f"\thead requested, sending {self.head_hash[:10]}",TAN)
            printc(f"\thead accounting for actual length {iter_local_chain(self.head_hash)}",TAN)

            # Open, lock, read the head file, and send the info back
            with open('cache/current.json') as file :
                flock(file,LOCK_SH)
                info = loads(file.read())
                flock(file,LOCK_UN)

            # Can't imagine how this would not return 200
            return info['head'], 200


################################################################################
#                    HANDLE HASH-FETCH REQUESTS
################################################################################

        @self.app.route('/fetch/<digest>')
        def fetch(digest):

            # Some simple debug code
            printc(f"request made: {digest}",TAN)

            # Make the (hopefully existing) filename
            filename = f'cache/{digest}.json'

            # Handle an error - 404 == not found here
            if not isfile(filename):
                return f'{RED}{filename} not found in cache{RED}', 404

            # Open up that file up (with locks!) and shoot it back to them
            else:
                with open(filename) as file:
                    flock(file,LOCK_SH)
                    block = file.read()
                    flock(file,LOCK_UN)
                    return block, 200


################################################################################
#                    HANDLE PUSH REQUESTS TO THE SERVER
################################################################################

        @self.app.route('/push', methods=['POST'])
        def push_block():

            # Get data from form
            received_data = flask.request.form
            printc(f"\twhile head is {self.head_hash[:5]}",TAN,endl='')
            printc(f"\trecieved '{str(received_data)[:35]} ... {str(received_data)[-20:]}'",TAN)

            # Check if the data is JSON decodable
            try:
                block = JSON_to_block(received_data['block'])
                printc(f"\tdecoded to '{str(block)[:35]} ... {str(block)[-20:]}'",TAN)

            except JSONDecodeError as j:
                printc(f"\terror decoding data",RED)
                return f"JSON error when decoding '{block}'", 418

            # Check if the block fields are valid
            if not check_fields(block,allowed_versions = [0],allowed_hashes=['']+grab_cached_hashes()):
                printc(f"\trejected block - invalid",RED)
                return "bad block", 418

            # Check if the block checks out as valid
            # Write block if its valid, and update chains

            # Add the block if it is good
            else:

                # Back to JSON
                block_string = dumps(block)
                block_hash   = hash(block_string.encode())
                # Save file in cache folder
                with open(f'cache/{block_hash}.json','w') as file:
                    file.write(block_string)

                printc(f"\taccepted block",GREEN)
                self.update_chains(block)
                return "Accepted!", 200


################################################################################
#                Before server starts, check which chain to use
################################################################################

    def scan_chains(self):

        # Info
        printc(f"\tFetching local chains",TAN)

        # Make sure 'cache' folder exists
        if not isdir('cache'):
            mkdir('cache')

        # Make sure 'current.json' exists
        if not isfile('cache/current.json'):
            with open("cache/current.json", 'w') as file:
                file.write('{"head" : "", "length" : 0}')

        # Setup dictionaries
        possible_hashes         = grab_cached_hashes()  # list of all hashes found in 'cache'
        hashes_to_prev_hash     = {}                    # holds prev_hash of block
        hash_len                = {}                    # maps chains to their length

        # Get all hashes found in 'cache' and map them to their prev_hash
        for hash in grab_cached_hashes():
                with open(f"cache/{hash}.json",'r') as f:
                    prev_hash = loads(f.read().strip())['prev_hash']
                    hashes_to_prev_hash[hash] = prev_hash

        # From possible_hashes, remove all hashes that appeared as a prev_hash
        # This means that they are not the head of a chain
        for not_possible_end_hash in hashes_to_prev_hash.values():
            try:
                possible_hashes.remove(not_possible_end_hash)
            except ValueError:
                printc(f"\t\ttried to remove {not_possible_end_hash[:10]} from list\n\t\tbut it did not exists",RED)

        self.longest_chain = 0
        self.head_hash = ''

        # Find the longest chain
        for hash in possible_hashes:
            hash_len[hash] = iter_local_chain(hash)     # Runs through and grabs length of chain starting from 'hash'

            # Update as necessary
            if hash_len[hash] > longest:
                self.longest_chain  = hash_len[hash]
                self.head_hash      = hash

        # Info
        printc(f"\t\tFound {len(possible_hashes)} chains",TAN)
        printc(f"\t\tLongest chain: {longest} block",TAN)

        self.empty = not possible_hashes

        # If there were no chains
        if self.empty:
            self.hash_len[''] = 0

        # Write the longset chain
        self.write_current()

        # Info
        printc(f"\t\thead is now at {self.head_hash} of len {self.longest_chain}", GREEN)

        # Keep track of all chains
        self.all_chains = hash_len

################################################################################
#                  As server runs, update the current chains
################################################################################

    def update_chains(self,block):
        block_hash = hash(dumps(block).encode())
        prev_hash = block['prev_hash']

        # This case we are adding to an existing chain
        if block['prev_hash'] in self.all_chains:

            # Info
            printc(f"pushed block into chain len {self.all_chains[prev_hash]}",TAN)

        # Get old chain length
            prev_len = self.all_chains[prev_hash]

        # Update the chain to have new head
            del(self.all_chains[prev_hash])
            self.all_chains[block_hash] = prev_len + 1
            printc(f"updated {prev_hash[:10]} chain, now len {self.all_chains[block_hash]}",RED)

            # If this makes a new longest chain, update file
            if self.all_chains[block_hash] > self.longest_chain:
                self.head_hash = block_hash
                self.longest_chain = self.all_chains[block_hash]
                self.empty = False
                self.write_current()

        # This case we are creating a chain

        # This case, this is a new block
        else:

            # Info
            printc(f"pushed block not part of existing chain",TAN)

        # Make new chain
            self.all_chains[block_hash] = 1

        # Check if its the longest (Aka first block)
            if self.all_chains[block_hash] > self.longest_chain:
                self.head_hash = block_hash
                self.longest_chain = self.all_chains[block_hash]
                self.empty = False
                self.write_current()

################################################################################
#                Write the current.json with most recent chain data
################################################################################

    def write_current(self):
        with open('cache/current.json','w') as file:
            flock(file,LOCK_SH)
            info = {'length' : self.longest_chain, 'head' : self.head_hash}
            file.write(dumps(info))
            flock(file,LOCK_UN)

################################################################################
#                      Execute an instance of the server
################################################################################

    def run(self,host='lion',port=5002):

        # Info
        printc(f"SERVER STARTED ON PORT {port}",GREEN)

        # Start
        self.app.run(host=host,port=port)



################################################################################
#                    Default Behavior: asks for user input to run
################################################################################

if __name__ == '__main__':

    # Ask for user input
    host = input('run on host: ').strip()
    port = input('run on port: ')

    # Build server
    s = DynamicServer()

    if not host and not port:
        s.run()
    else:
        s.run(host=host,port=int(port))
