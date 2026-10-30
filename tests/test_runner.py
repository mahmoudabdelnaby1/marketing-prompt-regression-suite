import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from prompt_eval_runner import run_eval

class TestPromptEval(unittest.TestCase):
    def test_eval(self):
        s = Path(__file__).resolve().parent.parent / "eval_suites" / "ad_copy_json_suite.json"
        out = Path(__file__).resolve().parent.parent / "reports" / "sample_eval_report.html"
        res = run_eval(str(s), str(out))
        self.assertGreaterEqual(res["passed"], 1)

if __name__ == "__main__":
    unittest.main()
