# ------------- example 01 -------------
global_varialble = "I'm Global"

def modify_global():
    global global_varialble
    global_varialble = "I'm modified"

modify_global()
print(global_varialble)

# ------------- example 02 -------------
def modify_without_global():
    local_var = "I'm local"
    print(local_var)

modify_without_global()