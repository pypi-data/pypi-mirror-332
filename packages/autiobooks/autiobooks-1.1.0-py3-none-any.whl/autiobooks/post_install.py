import os
import sys
from pathlib import Path

def install():
    # Get the applications directory
    if sys.platform.startswith('linux'):
        apps_dir = Path(sys.prefix) / 'share' / 'applications'
        desktop_file = Path(__file__).parent / 'autiobooks.desktop'
        
        # Create directory if it doesn't exist
        apps_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy .desktop file
        if desktop_file.exists():
            target = apps_dir / 'autiobooks.desktop'
            target.write_text(desktop_file.read_text())
            os.chmod(target, 0o755)

if __name__ == '__main__':
    install()