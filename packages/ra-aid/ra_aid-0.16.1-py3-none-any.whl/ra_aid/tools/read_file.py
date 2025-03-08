import logging
import os.path
import time
from typing import Dict

from langchain_core.tools import tool
from rich.console import Console
from rich.panel import Panel

from ra_aid.text.processing import truncate_output
from ra_aid.tools.memory import is_binary_file

console = Console()

# Standard buffer size for file reading
CHUNK_SIZE = 8192


@tool
def read_file_tool(filepath: str, encoding: str = "utf-8") -> Dict[str, str]:
    """Read and return the contents of a text file.

    Args:
        filepath: Path to the file to read
        encoding: File encoding to use (default: utf-8)
    
    DO NOT ATTEMPT TO READ BINARY FILES
    """
    start_time = time.time()
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        # Check if the file is binary
        if is_binary_file(filepath):
            console.print(
                Panel(
                    f"Cannot read binary file: {filepath}",
                    title="⚠ Binary File Detected",
                    border_style="bright_red",
                )
            )
            return {"error": "read_file failed because we cannot read binary files"}

        logging.debug(f"Starting to read file: {filepath}")
        content = []
        line_count = 0
        total_bytes = 0

        with open(filepath, "r", encoding=encoding) as f:
            while True:
                chunk = f.read(CHUNK_SIZE)
                if not chunk:
                    break

                content.append(chunk)
                total_bytes += len(chunk)
                line_count += chunk.count("\n")

                logging.debug(
                    f"Read chunk: {len(chunk)} bytes, running total: {total_bytes} bytes"
                )

        full_content = "".join(content)
        elapsed = time.time() - start_time

        logging.debug(f"File read complete: {total_bytes} bytes in {elapsed:.2f}s")
        logging.debug(f"Pre-truncation stats: {total_bytes} bytes, {line_count} lines")

        console.print(
            Panel(
                f"Read {line_count} lines ({total_bytes} bytes) from {filepath} in {elapsed:.2f}s",
                title="📄 File Read",
                border_style="bright_blue",
            )
        )

        # Truncate if needed
        truncated = truncate_output(full_content) if full_content else ""

        return {"content": truncated}

    except Exception:
        elapsed = time.time() - start_time
        raise
