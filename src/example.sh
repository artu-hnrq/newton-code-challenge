#!/bin/bash

newton request-calculation add 10 36 -p 4444
newton request-calculation sub 20 12 -p 4444
newton request-calculation mul 4 15 -p 4444
newton request-calculation div 5 3 -p 4444

newton request-calculation add 1 1 -p 4444
newton request-calculation sub 4 10 -p 4444
newton request-calculation mul 0 999 -p 4444
newton request-calculation div 4 0 -p 4444

newton connect-client -n artu -p 4444
newton connect-client -n carol -p 4444
newton connect-client -n louis -p 4444
newton connect-client -n jim -p 4444

newton present-db 4444

newton connect-client -n gerald -p 4444
newton connect-client -n paul -p 4444
newton connect-client -n zion -p 4444
newton connect-client -n ruan -p 4444
newton connect-client -n john -p 4444

newton present-db 4444
