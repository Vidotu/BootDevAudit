
start_health = 100


#===========================
# LESSON 2 MANIFESR: ARCHITECTUAL LOG
#=============================
# 1. WHAT COMMAND DOES
# Variables are not permanent storage boxes. They are simple Lables.
# The '=' symbol links the name on left to the data on right. 
#
# 2. UNDER THE HOOD 
# - Phyton creates a number object '100' insidr a free spot in RAM.
# - It adds the name 'player_health' to its internal name dictionary.
# - It sets that name to point directly to the memory address of '100'. 
# - It keeps track of how many names point to this object (Ref Count =1).
#
# 3. OS AND POWESHELL INTERACTION
# PowerShell spawns python.exe inside a free spot  in your RAM.
# All variable pointers live and die inside that specific process RAM.
# The moment the scrip ends, Windows reclaims the memory block entirely
#
# 4. ERROR MATRIX (TESTING AS I GO)
# - ERROR 1: print(player_health) ->
# NameError: name 'player_health' is not defined
# Note: Tried to read a variable name that does not exist in Phyton
#
# - ERROR 2: player health = 100 ->
# UnboundLocalError: cannot access local variable 'gold' where it is not associated with a value
# Note: You cannot use spaces in variable names. Use underscores (player_health) instead.
#
# - ERROR 3: 100 = player_health ->
# SyntaxError: cannot assign to literal here.
# Note: Alitteral number is a costant. You cannot use it as a variable name target.
# 
# GHOST ERROR (AI used to Create it)
# print = 100                       # Overwriting the print tool name
# player_health = print + 50        # Math works fine!
# print("Checking player health")   # CRASHES HERE!->
# TypeError: 'int' object is not callable
# Note: if you use a build-in Python tool name (like print) as a variable
# name, you will overwrite the tool abd completely break it for later lines