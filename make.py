import os
import _winreg
    

def getUnityPath():
    regkey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, 'SOFTWARE\\Unity Technologies\\Installer\\Unity')
    path = _winreg.QueryValueEx(regkey, 'Location x64')[0]
    path = os.path.join(path, 'Editor', 'Unity.exe')
    return path.replace('\\', '/')

#unityPath = '"D:/Program Files/Unity/Editor/Unity.exe"'
unityPath = '"%s"' % getUnityPath()
print(unityPath)

projectPath = os.path.abspath('./test')
targetPath = os.path.abspath('./test_auto.exe')
cmd = '%s -batchmode -projectPath %s -buildWindowsPlayer %s -quit' % (unityPath, projectPath, targetPath)
print(cmd)
os.system(cmd)