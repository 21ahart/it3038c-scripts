#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
DEATHS=$(echo $DATA | jq '.[0].death')
HOSPITAL=$(echo $DATA | jq '.[0].hospitalizedCurrently')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases, $DEATHS Deaths, $HOSPITAL Currently Hospitalized, and $NEGATIVE negatives "
