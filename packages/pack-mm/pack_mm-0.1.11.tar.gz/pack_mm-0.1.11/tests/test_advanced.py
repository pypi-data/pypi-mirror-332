"""Advanced tests for packmm."""

# Author; alin m elena, alin@elena.re
# Contribs;
# Date: 23-02-2025
# ©alin m elena,
from __future__ import annotations

from ase.build import bulk
from ase.io import read, write
import pytest
from typer.testing import CliRunner

from pack_mm.cli.packmm import app

runner = CliRunner()

err = 1.0e-8


def test_packmm_hmc(tmp_path):
    """Check values."""
    result = runner.invoke(
        app,
        [
            "--nmols",
            "2",
            "--model",
            "small-0b2",
            "--insert-strategy",
            "hmc",
            "--seed",
            "2042",
            "--cell-a",
            "10",
            "--cell-b",
            "10",
            "--cell-c",
            "10",
            "--out-path",
            tmp_path,
        ],
    )
    assert result.exit_code == 0
    assert (tmp_path / "1H2O.cif").exists()
    assert (tmp_path / "2H2O.cif").exists()
    f = read(tmp_path / "2H2O.cif")
    assert f[0].position == pytest.approx([7.83420049, 6.21661184, 5.21814887], abs=err)
    assert (tmp_path / "2H2O-opt.cif").exists()
    f = read(tmp_path / "2H2O-opt.cif")
    assert f[0].position == pytest.approx([7.83120709, 6.21742874, 5.22597213], abs=err)


def test_packmm_every(tmp_path):
    """Check values."""
    na = bulk("NaCl", "rocksalt", a=5.61, cubic=True)
    write(tmp_path / "system.cif", na)
    write("system.cif", na)

    result = runner.invoke(
        app,
        [
            "--system",
            tmp_path / "system.cif",
            "--molecule",
            "H2",
            "--every",
            "1",
            "--nmols",
            "2",
            "--model",
            "small-0b2",
            "--seed",
            "2042",
            "--out-path",
            tmp_path,
            "--threshold",
            "0.5",
            "--no-geometry",
        ],
    )
    assert result.exit_code == 0
    assert (tmp_path / "system.cif").exists()
    assert (tmp_path / "system+1H2.cif").exists()
    assert (tmp_path / "system+2H2.cif").exists()
    f = read(tmp_path / "system+2H2.cif")
    assert f[0].position == pytest.approx([1.24701529, 0.024216, 0.11632905], abs=err)
