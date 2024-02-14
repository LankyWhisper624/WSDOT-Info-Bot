# WSDOT-Info-Bot
A bot that uses the WSDOT Live Traffic API to generate mastadon posts.  
Currently all it does is get the pass conditions and writes them to a file.

## TODO:
- Check the output file for updates
- Use the output file to generate formatted posts on Mastodon
- Add support for highway alerts
- Add cameras to major highways and passes
- Directly save the json response instead of re-formatting the string

## passinfo.txt format
The passinfo.txt file contains a custom formatted set of strings representing the status of all the passes in Washington State. The format is as follows:  
1. Pass Name and Highway
2. Direction 1 and restriction
3. Direction 2 and restriction
4. Road Condition
5. Weather Report
6. Temperature (F)

Each category is separated by the vertical bar character (```|```).
