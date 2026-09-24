"""Apply the intended AMS colors to the native Bambu Studio project."""

import json
import os
import sys
import tempfile
import zipfile


COLORS = ["#17191C", "#73777B", "#A71930"]
SETTINGS_PATH = "Metadata/project_settings.config"


def main(source: str, destination: str) -> None:
    destination_dir = os.path.dirname(os.path.abspath(destination))
    fd, temporary = tempfile.mkstemp(suffix=".3mf", dir=destination_dir)
    os.close(fd)
    try:
        with zipfile.ZipFile(source, "r") as incoming, zipfile.ZipFile(
            temporary, "w", zipfile.ZIP_DEFLATED
        ) as outgoing:
            for item in incoming.infolist():
                data = incoming.read(item.filename)
                if item.filename == SETTINGS_PATH:
                    settings = json.loads(data.decode("utf-8"))
                    settings["filament_colour"] = COLORS
                    settings["extruder_colour"] = COLORS
                    settings["default_filament_colour"] = COLORS
                    data = json.dumps(settings, indent=4).encode("utf-8")
                outgoing.writestr(item, data)
        os.replace(temporary, destination)
    finally:
        if os.path.exists(temporary):
            os.remove(temporary)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: patch_bambu_colors.py SOURCE.3mf DESTINATION.3mf")
    main(sys.argv[1], sys.argv[2])
