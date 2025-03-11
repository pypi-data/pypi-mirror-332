"""
This code connects to a running QuestDB instance and displays information
about the tables and partitions in the database. It uses two SQL statements
to retrieve this information: "tables()" and "table_partitions()". The output
is formatted and printed to the console.
"""
import json

from questdb_connect import connect

from examples import CONNECTION_ATTRS


def print_partition(row):
    p_index, p_by, _, min_ts, max_ts, num_rows, _, p_size, *_ = row
    print(
        f" - Partition {p_index} by {p_by} [{min_ts}, {max_ts}] {num_rows} rows {p_size}"
    )


def print_table(row):
    table_id, table_name, ts_column, p_by, _, _, is_wal, dir_name, is_dedup = row
    msg = ", ".join(
        (
            f"Table id:{table_id}",
            f"name:{table_name}",
            f"ts-col:{ts_column}",
            f"partition-by:{p_by}",
            f"is-wal:{is_wal}",
            f"dir-name:{dir_name}",
            f"is-dedup:{is_dedup}",
        )
    )
    print(msg)


def print_server_info(dsn_parameters):
    print(f"QuestDB server information: {json.dumps(dsn_parameters, indent=4)}")


def main():
    with connect(**CONNECTION_ATTRS) as conn:
        print_server_info(conn.get_dsn_parameters())
        with conn.cursor() as tables_cur, conn.cursor() as partitions_cur:
            tables_cur.execute("tables()")
            for table_row in tables_cur.fetchall():
                print_table(table_row)
                partitions_cur.execute(f"table_partitions('{table_row[1]}')")
                for partition_row in partitions_cur.fetchall():
                    print_partition(partition_row)


if __name__ == "__main__":
    main()
