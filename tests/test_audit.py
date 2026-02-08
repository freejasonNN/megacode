from __future__ import annotations

from pathlib import Path

import audit


def test_normalize_relative_path() -> None:
    assert audit._normalize_relative_path("./src\\foo.cs") == "src/foo.cs"


def test_resolve_repo_path_blocks_escape(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    path = audit._resolve_repo_path(repo, "src/file.cs")
    assert path == repo / "src" / "file.cs"

    try:
        audit._resolve_repo_path(repo, "../etc/passwd")
        assert False, "expected ValueError for escaping repo root"
    except ValueError:
        pass


def test_collect_source_manifest_indexes_expected_files(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    src = repo / "src"
    src.mkdir(parents=True)
    (src / "Controller.cs").write_text("public class Controller {}", encoding="utf-8")
    (src / "ignored.txt").write_text("ignore me", encoding="utf-8")
    (src / "web.config").write_text("<configuration/>", encoding="utf-8")

    manifest, stats = audit.collect_source_manifest(
        repo,
        max_files=100,
        max_file_bytes=200000,
        skip_hidden_dirs=True,
    )
    paths = {item["path"] for item in manifest}

    assert "src/Controller.cs" in paths
    assert "src/web.config" in paths
    assert "src/ignored.txt" not in paths
    assert stats["files"] == 2


def test_rlm_tools_list_read_search(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir(parents=True)
    file_path = repo / "Program.cs"
    file_path.write_text(
        "var s = \"secret\";\n"
        "var sql = \"SELECT * FROM t\";\n",
        encoding="utf-8",
    )

    manifest = [
        {
            "path": "Program.cs",
            "bytes": file_path.stat().st_size,
            "ext": ".cs",
            "signal_score": 2,
            "path_score": 0,
        }
    ]

    list_manifest, read_file, search_pattern = audit.build_rlm_tools(
        repo,
        manifest,
        default_tool_max_lines=50,
        default_tool_max_chars=5000,
        default_search_max_files=100,
        default_search_max_matches=100,
    )

    listed = list_manifest(limit=10)
    assert listed and listed[0]["path"] == "Program.cs"

    snippet = read_file("Program.cs", start_line=1)
    assert snippet["path"] == "Program.cs"
    assert "1: var s = \"secret\";" in snippet["content"]

    matches = search_pattern("secret", ignore_case=True)
    assert matches
    assert matches[0]["path"] == "Program.cs"
