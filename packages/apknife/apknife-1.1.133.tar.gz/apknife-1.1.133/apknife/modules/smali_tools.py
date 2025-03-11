import os
import subprocess

def get_baksmali_path():
    """Get the correct path to baksmali.jar."""
    return os.path.join(os.path.dirname(__file__), "tools", "baksmali.jar")

def decompile_apk(apk_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    baksmali_path = get_baksmali_path()
    cmd = f"java -jar {baksmali_path} d {apk_file} -o {output_dir}"
    
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"✅ Smali code extracted to {output_dir}")
    except subprocess.CalledProcessError:
        print("❌ Error during Smali decompilation")
