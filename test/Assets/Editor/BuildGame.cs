using UnityEngine;
using UnityEditor;
using System.Linq;
using System.IO;

public class BuildGame {

	[MenuItem("Tools/BuildWindows")]
	public static void BuildWindows()
	{
		Build(BuildTarget.StandaloneWindows);
	}

	[MenuItem("Tools/BuildAndroid")]
	public static void BuildAndroid()
	{
		Build (BuildTarget.Android);
	}

	public static void Build(BuildTarget target) {
		var targetPath = GetTargetPath (target);
		var baseTargetDir = Path.GetDirectoryName (targetPath);
		if (!Directory.Exists(baseTargetDir)) {
			Directory.CreateDirectory (baseTargetDir);
		}
		BuildPipeline.BuildPlayer (GetScenes (), targetPath, target, BuildOptions.None);
	}

	public static string[] GetScenes()
	{
		var rez = from scene in EditorBuildSettings.scenes
		          select scene.path;
		return rez.ToArray ();
	}

	private static string GetTargetPath(BuildTarget target)
	{
		return Path.Combine (Path.Combine (Application.dataPath, ".."), GetTargetName (target));
	}

	private static string GetTargetName(BuildTarget target)
	{
		switch (target) {
		case BuildTarget.Android:
			return "build/android/game.apk";
		case BuildTarget.StandaloneWindows:
		case BuildTarget.StandaloneWindows64:
			return "build/win32/game.exe";
		default:
			throw new System.ArgumentOutOfRangeException ();
		}
	}
}
