from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from github_weekly_feishu import build_doc


SOURCE = ROOT / "examples" / "weekly.md"
OUT = ROOT / "dist" / "weekly-feishu.docx"


if __name__ == "__main__":
    print(build_doc(SOURCE, OUT, assets_root=ROOT))
