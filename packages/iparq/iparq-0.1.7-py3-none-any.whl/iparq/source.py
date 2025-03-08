import pyarrow.parquet as pq
import typer
from pydantic import BaseModel
from rich import print
from rich.console import Console

app = typer.Typer()
console = Console()


class ParquetMetaModel(BaseModel):
    """
    ParquetMetaModel is a data model representing metadata for a Parquet file.

    Attributes:
        created_by (str): The creator of the Parquet file.
        num_columns (int): The number of columns in the Parquet file.
        num_rows (int): The number of rows in the Parquet file.
        num_row_groups (int): The number of row groups in the Parquet file.
        format_version (str): The version of the Parquet format used.
        serialized_size (int): The size of the serialized Parquet file in bytes.
    """

    created_by: str
    num_columns: int
    num_rows: int
    num_row_groups: int
    format_version: str
    serialized_size: int


def read_parquet_metadata(filename: str):
    """
    Reads the metadata of a Parquet file and extracts the compression codecs used.

    Args:
        filename (str): The path to the Parquet file.

    Returns:
        tuple: A tuple containing:
            - parquet_metadata (pyarrow.parquet.FileMetaData): The metadata of the Parquet file.
            - compression_codecs (set): A set of compression codecs used in the Parquet file.
    """
    try:
        compression_codecs = set([])
        parquet_metadata = pq.ParquetFile(filename).metadata

        for i in range(parquet_metadata.num_row_groups):
            for j in range(parquet_metadata.num_columns):
                compression_codecs.add(
                    parquet_metadata.row_group(i).column(j).compression
                )

    except FileNotFoundError:
        console.print(
            f"Cannot open: {filename}.", style="blink bold red underline on white"
        )
        exit(1)

    return parquet_metadata, compression_codecs


def print_parquet_metadata(parquet_metadata):
    """
    Prints the metadata of a Parquet file.

    Args:
        parquet_metadata: An object containing metadata of a Parquet file.
                          Expected attributes are:
                          - created_by: The creator of the Parquet file.
                          - num_columns: The number of columns in the Parquet file.
                          - num_rows: The number of rows in the Parquet file.
                          - num_row_groups: The number of row groups in the Parquet file.
                          - format_version: The format version of the Parquet file.
                          - serialized_size: The serialized size of the Parquet file.

    Raises:
        AttributeError: If the provided parquet_metadata object does not have the expected attributes.
    """
    try:
        meta = ParquetMetaModel(
            created_by=parquet_metadata.created_by,
            num_columns=parquet_metadata.num_columns,
            num_rows=parquet_metadata.num_rows,
            num_row_groups=parquet_metadata.num_row_groups,
            format_version=str(parquet_metadata.format_version),
            serialized_size=parquet_metadata.serialized_size,
        )
        console.print(meta)

    except AttributeError as e:
        console.print(f"Error: {e}", style="blink bold red underline on white")
    finally:
        pass


def print_compression_types(parquet_metadata) -> None:
    """
    Prints the compression type for each column in each row group of the Parquet file.
    """
    try:
        num_row_groups = parquet_metadata.num_row_groups
        num_columns = parquet_metadata.num_columns
        console.print("[bold underline]Column Compression Info:[/bold underline]")
        for i in range(num_row_groups):
            console.print(f"[bold]Row Group {i}:[/bold]")
            for j in range(num_columns):
                column_chunk = parquet_metadata.row_group(i).column(j)
                compression = column_chunk.compression
                column_name = parquet_metadata.schema.column(j).name
                console.print(
                    f"  Column '{column_name}' (Index {j}): [italic]{compression}[/italic]"
                )
    except Exception as e:
        console.print(
            f"Error while printing compression types: {e}",
            style="blink bold red underline on white",
        )
    finally:
        pass


def print_bloom_filter_info(parquet_metadata) -> None:
    """
    Prints information about bloom filters for each column in each row group of the Parquet file.
    """
    try:
        num_row_groups = parquet_metadata.num_row_groups
        num_columns = parquet_metadata.num_columns
        has_bloom_filters = False

        console.print("[bold underline]Bloom Filter Info:[/bold underline]")

        for i in range(num_row_groups):
            row_group = parquet_metadata.row_group(i)
            bloom_filters_in_group = False

            for j in range(num_columns):
                column_chunk = row_group.column(j)
                column_name = parquet_metadata.schema.column(j).name

                # Check if this column has bloom filters using is_stats_set
                if hasattr(column_chunk, "is_stats_set") and column_chunk.is_stats_set:
                    if not bloom_filters_in_group:
                        console.print(f"[bold]Row Group {i}:[/bold]")
                        bloom_filters_in_group = True
                    has_bloom_filters = True
                    console.print(
                        f"  Column '{column_name}' (Index {j}): [green]Has bloom filter[/green]"
                    )

        if not has_bloom_filters:
            console.print("  [italic]No bloom filters found in any column[/italic]")

    except Exception as e:
        console.print(
            f"Error while printing bloom filter information: {e}",
            style="blink bold red underline on white",
        )


@app.command()
def main(filename: str):
    """
    Main function to read and print Parquet file metadata.

    Args:
        filename (str): The path to the Parquet file.

    Returns:
        Metadata of the Parquet file and the compression codecs used.
    """
    (parquet_metadata, compression) = read_parquet_metadata(filename)

    print_parquet_metadata(parquet_metadata)
    print_compression_types(parquet_metadata)
    print_bloom_filter_info(parquet_metadata)
    print(f"Compression codecs: {compression}")


if __name__ == "__main__":
    app()
