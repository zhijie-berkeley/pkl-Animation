#!/bin/sh
#how to run this shell: ./saveMultAnimation.sh

echo start saving animation ...

echo start saving H2AZ-PolII-movie
python /Users/ZHIJIE/Documents/2018\ Paper/Data\ figures/Movies/H2AZ-PolII-movie/*.py /Users/ZHIJIE/Documents/2018\ Paper/Data\ figures/Movies/H2AZ-PolII-movie/*.pkl --save

echo start saving uH2B-PolII-movie
python /Users/ZHIJIE/Documents/2018\ Paper/Data\ figures/Movies/uH2B-PolII-movie/*.py /Users/ZHIJIE/Documents/2018\ Paper/Data\ figures/Movies/uH2B-PolII-movie/*.pkl --save

echo start saving WT-PolII-movie
python /Users/ZHIJIE/Documents/2018\ Paper/Data\ figures/Movies/WT-PolII-movie/*.py /Users/ZHIJIE/Documents/2018\ Paper/Data\ figures/Movies/WT-PolII-movie/*.pkl --save

echo done

