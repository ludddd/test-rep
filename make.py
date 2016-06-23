import os
import sys 
try:
    import _winreg as winreg
except ImportError:
    import winreg as winreg
import shutil	
    
platform = 'win32'
if len(sys.argv) > 1:
	platform = sys.argv[1]
print('building for platform %s' % platform)	

def getUnityPath():
    regkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\\Unity Technologies\\Installer\\Unity')
    path = winreg.QueryValueEx(regkey, 'Location x64')[0]
    path = os.path.join(path, 'Editor', 'Unity.exe')
    return path.replace('\\', '/')

unityPath = '"%s"' % getUnityPath()
print(unityPath)

projectPath = os.path.abspath('./test')
buildMethod = {'win32' : 'BuildGame.BuildWindows', 'android' : 'BuildGame.BuildAndroid'}
cmd = '%s -batchmode -projectPath %s -executeMethod %s -quit' % (unityPath, projectPath, buildMethod[platform])
print(cmd)
os.system(cmd)

def packResult(platform):
	src_path = os.path.join('./test', 'build', platform)
	shutil.make_archive('build', 'zip', src_path)
	
packResult(platform)	