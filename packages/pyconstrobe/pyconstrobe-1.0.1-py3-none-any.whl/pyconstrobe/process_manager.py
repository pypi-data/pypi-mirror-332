import subprocess
import threading
import os
import sys

def debug(msg):
        build_mode = os.getenv('BUILD_MODE', 'Release')
        if build_mode=='Debug':
            sys.stderr.write(f"[DEBUG] {msg}\n")
            sys.stderr.flush()  

class ProcessManager:
    def __init__(self, callback=None):
        build_mode = os.getenv('BUILD_MODE', 'Release')  # Default to 'release' if not set
        print(build_mode)
        if build_mode=='Debug':
            path_to_exe = r"C:\source\constrobe\csApp\Debug\constrobe.exe"
        else:
            path_to_exe = r"C:\Program Files\constrobe\constrobe\constrobe.exe"



        self.process = subprocess.Popen(
            [path_to_exe, '--from-python'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        self.callback = callback  # Custom callback for processing messages
        self.keep_reading = True  # Flag to control the reading loop
        self.finishRunFlag = False
        self.gotTraceFlag = False
        self.gotResultsFlag = False
        self.reader_thread = threading.Thread(target=self.read_messages)
        self.reader_thread.daemon = True  # Allow thread to exit when main program exits
        self.reader_thread.start()

    def write_message(self, message):
        debug(f"Sending message: {message}")
        self.process.stdin.write(message + "\n")
        self.process.stdin.flush()

    def read_messages(self):
        """Read messages from the process's stdout."""
        while self.keep_reading:
            response = self.process.stdout.readline().strip()
            debug(f"Received message: {response}")

            if response:
                parts = response.split(" ",1)
                type = parts[0]
                message = parts[1] if len(parts)>1 else ""
                if type == "FINISHED_RUN":
                    self.finishRunFlag = True
                elif type == "CLOSED_CONSTROBE":
                    self.keep_reading = False  # Stop reading messages
                    break
                elif self.callback:
                    if type == "TRACE":
                        message=message.replace("|","\n")
                        self.gotTraceFlag = True
                    if type == "RESULTS":
                        self.gotResultsFlag = True

                    response_value = self.callback(type,message)
                    
                    if type == "GET":
                        response_message = f"RESPONSE_TO_GET {response_value}"
                        self.write_message(response_message)                    

    def cleanup(self):
        print("Cleaning up resources...")
        self.keep_reading = False  # Signal the thread to stop reading
        self.running = False  
        self.reader_thread.join()  # Wait for the thread to finish
        self.process.stdin.close()
        self.process.stdout.close()
        self.process.stderr.close()
        if self.process:
            self.process.terminate()  # Try to terminate the process gracefully
            try:
                return self.process.wait(timeout=5)  # Wait up to 5 seconds for it to finish
            except subprocess.TimeoutExpired:
                debug("Process did not terminate, force killing it...")
                self.process.kill()  # Force kill the process if it doesn't terminate in time
                return self.process.wait()  # Ensure it finishes
