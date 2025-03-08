import subprocess

command = ["./src/mcpandroidbuild/build.sh", "/Users/dx73fc/projects/P19448-feature-au-money-transfer"]
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False).stdout

lines = result.decode("utf-8").splitlines()
error_lines = [line for line in lines if "failure: " in line.lower() or "e: file:" in line.lower() or " failed" in line.lower()]
error_message = "\n".join(error_lines)
if not error_message:
    error_message = "Successful"
