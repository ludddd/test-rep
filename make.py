import os
try:
    import _winreg as winreg
except ImportError:
    import winreg as winreg
import zipfile	
    

def getUnityPath():
    regkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\\Unity Technologies\\Installer\\Unity')
    path = winreg.QueryValueEx(regkey, 'Location x64')[0]
    path = os.path.join(path, 'Editor', 'Unity.exe')
    return path.replace('\\', '/')

#unityPath = '"D:/Program Files/Unity/Editor/Unity.exe"'
unityPath = '"%s"' % getUnityPath()
print(unityPath)

targetName = './test_auto'

def getExeName(name):
	return name + '.exe'
	
def getDataFolderName(name):
	return name + '_Data'

projectPath = os.path.abspath('./test')
cmd = '%s -batchmode -projectPath %s -buildWindowsPlayer %s -quit' % (unityPath, projectPath, getExeName(targetName))
print(cmd)
os.system(cmd)

def packResult(name):
	z = zipfile.ZipFile('build_win32.zip', 'w')
	z.write(getExeName(name))
	for root, _, filenames in os.walk(getDataFolderName(name)):
		for name in filenames:
			name = os.path.join(root, name)
			name = os.path.normpath(name)
			z.write(name, name)
	z.close()
	
packResult(targetName)	