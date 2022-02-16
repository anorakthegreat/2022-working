#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


^!#+a::
sleep 100
send {PrintScreen}
sleep 100
Run, mspaint.exe,,, Paint
sleep 1000
send #{Up}
sleep 1000
run chrome.exe "https://app.slack.com/client/T1DRRAYBZ/D02T62D872R"				;replace this one link to the slack url of who you want to summon
sleep 6000
send ^v
sleep 1000
send Pls sanad halp
sleep 1000
send {Enter}
sleep 100
WinClose "ahk_pid %Paint%"