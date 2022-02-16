#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


^!#+a::
sleep, 100
send {PrintScreen}
sleep, 500
run MSPaint
sleep, 1000
send, #{Up}
sleep 1000
run chrome.exe "https://app.slack.com/client/T1DRRAYBZ/D02T62D872R"
sleep 7000
send ^v
sleep 1000
send Pls sanad halp
sleep 1000
send {Enter}
send {Enter}