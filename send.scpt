#runs a script that sends sms message out loud through apple terminal
#use cd to find SMS folder in terminal
#run send.scpt to send the sms msg
#to run type: MacBook-Pro:sms adrianmendozaperez$ osascript send.scpt +00000000000 (your number) 'msg'
#^specifications for my computer

on run {targetPhoneNumber, targetMessageToSend}
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy targetPhoneNumber of targetService
        set targetMessage to targetMessageToSend
        send targetMessage to targetBuddy
        say targetMessage
    end tell
end run
