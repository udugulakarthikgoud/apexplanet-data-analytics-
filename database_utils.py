{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f8cf5fe5-1a9b-4b9d-9855-87fc8d9d0c41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Database utility ready!\n"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "import pandas as pd\n",
    "\n",
    "def get_connection(db_path=\"superstore.db\"):\n",
    "    \"\"\"Create and return a database connection.\"\"\"\n",
    "    return sqlite3.connect(db_path)\n",
    "\n",
    "def run_query(query, db_path=\"superstore.db\"):\n",
    "    \"\"\"Run a SQL query and return the result as a DataFrame.\"\"\"\n",
    "    conn = get_connection(db_path)\n",
    "    result = pd.read_sql_query(query, conn)\n",
    "    conn.close()\n",
    "    return result\n",
    "\n",
    "print(\"Database utility ready!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "739c3a82-7715-42f5-91c4-a60b6f853331",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
