print("Welcome to Fantasy Quest!")

#============
#LESSON 1 LOG
#============

# 1. WHAT COMMAND DOES
# The print() tool sends a line of text string data to your console screen.
# It requires parenthesis, and text must be wrapped inside quoatation marks.

# 2. UNDER THE HOOD
# - Phyton turns this line into low-level instructions called bytecode.
# - The interpreter allocates a block of temporary memory (Ram) to hold text.
# - It uses sys.stdout to stream the raw data bytes down to the OS kernel.
#
# 3. OS AND POWERSHELL INTERACTION
# - PowerShell starts up python.exe as an isolated sub-process in Windows.
# - Phyton makes a Win32 system call to WriteConsoleW inside Kernel32.dll.
# - Windows terminal read those bytes and prints them onto monitor.
#
# ERROR MATRIX (Testing as i go)
# ERROR 1:print("Welcome to Fantasy Quest!) ->
# #SyntaxError: unterminated string literal.
# Note: forgot to close text string with matching quote mark.
#
# ERROR 2:Print("Welcome to Fantasy Quest!") ->
# NameError: name 'Print' is not defined.
# Note: Python is case-sensitive and does not recognize capital functions.
#
# ERROE 3:print "Welcome to Fantasy Quest!" ->
# SyntaxError: Missing parentheses in call.
# Note: Python 3 requires parntheses around function inputs.
#
# THE GHOST ERROR (AI used to create it)
# print("Welcome to Fantasy Quest! ⚔️") ->
# Triggers character drop.
# On my Windows PowerShell screen, this displays as:
# Welcome to Fantasy Quest! ??
# 
# Note: Windows consoles use old code pages that miss complex emojis.

