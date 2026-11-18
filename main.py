"""news-image-20261118 entry: copy the bundled news-summary image to the output.

The program runs with no network. It copies entry.png (the image this
repository holds, a front-page summary of the world news of Wednesday
18 November 2026) to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png).
Both runs write the same bytes because the source file is fixed.
"""
import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out_dir / "entry.png")
