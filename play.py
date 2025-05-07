import subprocess

# Path to the executable
exe_path = "play.exe"

try:
    # Run the executable and capture output
    result = subprocess.run(
        [exe_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,  # Automatically decode output as string
        shell=True  # Required for running .exe directly on Windows
    )

    # Print or log the output
    print("Standard Output:")
    print(result.stdout)

    print("Standard Error:")
    print(result.stderr)

except Exception as e:
    print(f"An error occurred: {e}")
