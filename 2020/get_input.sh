#!/usr/bin/env bash

# Enter your session cookie here: it's valid basically forever
cookie=<"53616c7465645f5f47436564ee3febb75fe0f20c2704d05ec296a9071b06edb43091ea0bef44cd6e86bff82e57ecaa2f">

[ -z $1 ] && echo "Provide the current day"    && exit 1

printf -v dirname "day_%02d" $1
mkdir "${dirname}"
curl "https://adventofcode.com/2020/day/$1/input" -s --cookie session="$cookie" > "${dirname}/input.txt"
