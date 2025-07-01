
import os
import subprocess


def test_bin_scan_exists():
    
    assert os.path.exists("bin-scan")

def test_bin_scan():
    result = subprocess.run(["/workspace/bin-scan", "--target", "example.com", "--scan_type", "dig"], capture_output=True, text=True, check=True)
    assert "example.com" in result.stdout


def test_bin_scan_port():
    result = subprocess.run(["/workspace/bin-scan", "--target", "example.com", "--scan_type", "port"], capture_output=True, text=True, check=True)
    assert "open" in result.stdout



