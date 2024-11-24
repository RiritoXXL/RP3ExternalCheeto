from uniref import WinUniRef

def InitRP3():
    winrp3 = WinUniRef("RP3.exe")
    return winrp3

def GetMinValue_Addr():
    rp3_res = InitRP3().find_class_in_image("Assembly-CSharp.dll", "RP3.Resource+Resource")
    resource = rp3_res.find_method("get_ResourceValue")
    print(resource.address)

def Main():
    # Only For Testing :D
    GetMinValue_Addr()