#!/bin/bash
# sends a request to that URL,and display the size of the body of the response
curl -s "$1" | wc -c
