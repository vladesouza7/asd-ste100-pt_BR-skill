"""Testes do linter. Rode com: python3 -m pytest tests/ ou python3 tests/test_ste_lint_ptbr.py"""
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "ste_lint_ptbr", HERE.parent / "scripts" / "ste-lint-ptbr.py")
lint_mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lint_mod)
lint = lint_mod.lint


def rules(text):
    return {f["rule"] for f in lint(text)[0]}


def test_selftest_cases():
    for rule, bad, good in lint_mod.SELFTEST_CASES:
        assert rule in rules(bad), (rule, bad)
        assert rule not in rules(good), (rule, good)


def test_hedges_pass_clean():
    assert lint(lint_mod.HEDGES)[0] == []


def test_skips_code_front_matter_and_off_regions():
    text = "---\ntitle: x; y\n---\n```\nrealize a verificação;\n```\n<!-- ste-lint: off -->\nvc tb;\n<!-- ste-lint: on -->\nVerifique o filtro.\n"
    assert lint(text)[0] == []


def test_table_cells_are_linted_separately():
    text = "| A | B |\n|---|---|\n| Verifique o log. | Cheque a saída. |\n"
    assert "rotacao-de-sinonimos" in rules(text)
    assert "tamanho-da-frase" not in rules("| " + " ".join(["x"] * 20) + " | " + " ".join(["y"] * 20) + " |\n|---|---|\n| a | b |\n")


def test_edge_case_fixture_reports_two_dangling_items():
    text = (HERE.parent / "examples" / "linter-edge-cases.md").read_text(encoding="utf-8")
    found = [f for f in lint(text)[0] if f["rule"] == "conjuncao-solta"]
    assert len(found) == 2
    assert all(f["level"] == "hard" for f in found)


def test_exit_code_and_baseline(capsys):
    assert lint_mod.main(["--selftest"]) == 0
    fixture = str(HERE.parent / "examples" / "linter-edge-cases.md")
    assert lint_mod.main([fixture]) == 1
    assert lint_mod.main(["--baseline", "2", fixture]) == 0
    assert lint_mod.main(["--disable", "conjuncao-solta", fixture]) == 0
    assert lint_mod.main(["--baseline", "x", fixture]) == 2
    capsys.readouterr()


if __name__ == "__main__":
    test_selftest_cases()
    test_hedges_pass_clean()
    test_skips_code_front_matter_and_off_regions()
    test_table_cells_are_linted_separately()
    test_edge_case_fixture_reports_two_dangling_items()
    print("OK")
