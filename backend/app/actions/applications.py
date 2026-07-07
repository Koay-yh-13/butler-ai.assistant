import os
import subprocess
from pathlib import Path


COMMON_APPLICATIONS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "command prompt": "cmd.exe",
    "powershell": "powershell.exe",
    "task manager": "taskmgr.exe",
    "explorer": "explorer.exe",
}


class ApplicationManager:

    def open_application(self, application_name: str):
        app = application_name.lower().strip()

        if app in COMMON_APPLICATIONS:
            subprocess.Popen(COMMON_APPLICATIONS[app])
            return {
                "success": True,
                "message": f"Opened {application_name}."
            }

        return {
            "success": False,
            "message": f"Application '{application_name}' is not currently supported."
        }


application_manager = ApplicationManager()
