from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
import sqlite3

def list_tables() -> list[str]:
    """Retrieve the names of all tables in the database."""
    # Include print logging statements so you can see when functions are being called.
    # print(' - DB CALL: list_tables()')
    db_conn = sqlite3.connect("sample.db")
    cursor = db_conn.cursor()
    # Fetch the table names.
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return [t[0] for t in tables]

def describe_table(table_name: str) -> list[tuple[str, str]]:
    """Look up the table schema.
    Returns:
      List of columns, where each entry is a tuple of (column, type).
    """
    # print(f' - DB CALL: describe_table({table_name})')
    db_conn = sqlite3.connect("sample.db")
    cursor = db_conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    schema = cursor.fetchall()
    # [column index, column name, column type, ...]
    return [(col[1], col[2]) for col in schema]

def execute_query(sql: str) -> list[list[str]]:
    """Execute an SQL statement, returning the results."""
    # print(f' - DB CALL: execute_query({sql})')
    db_conn = sqlite3.connect("sample.db")
    cursor = db_conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

def chat(question):

    system_prompt = """You are a helpful chatbot that can interact with an SQL database
    for a computer store. You will take the users questions and turn them into SQL
    queries using the tools available. Once you have the information you need, you will
    answer the user's question using the data returned.

    Use list_tables to see what tables are present, describe_table to understand the
    schema, and execute_query to issue an SQL SELECT query."""

    tools = [list_tables, describe_table, execute_query]
    model = ChatOllama(model="qwen2.5:7b")
    graph = create_react_agent(model, tools, prompt=system_prompt)

    inputs = {"messages": [("user", question)]}
    for s in graph.stream(inputs, stream_mode="values"):
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
            response = message
        else:
            message.pretty_print()
            response = message.pretty_repr()
        yield response