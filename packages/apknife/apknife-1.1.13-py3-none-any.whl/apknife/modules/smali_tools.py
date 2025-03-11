import os
import subprocess
import importlib.resources as pkg_resources  # Python 3.9+

def get_baksmali_path():
    """Gets the correct path to baksmali.jar inside the installed package."""
    try:
        with pkg_resources.path("apknife.modules.tools", "baksmali.jar") as jar_path:
            return str(jar_path)
    except ModuleNotFoundError:
        print("❌ Error: baksmali.jar not found!")
        return None

def decompile_apk(apk_dir, output_dir):
    """Decompiles the given APK using baksmali."""
    baksmali_jar = get_baksmali_path()
    if not baksmali_jar:
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cmd = f"java -jar {baksmali_jar} d {apk_dir} -o {output_dir}"
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"✅ Smali code extracted to {output_dir}")
    except subprocess.CalledProcessError:
        print("❌ Error during Smali decompilation")

def find_oncreate(smali_dir):
    """Searches for 'onCreate' method in Smali files."""
    for root, _, files in os.walk(smali_dir):
        for file in files:
            if file.endswith(".smali"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    content = f.read()
                    if "onCreate" in content:
                        print(f"✅ Found onCreate in {file}")
