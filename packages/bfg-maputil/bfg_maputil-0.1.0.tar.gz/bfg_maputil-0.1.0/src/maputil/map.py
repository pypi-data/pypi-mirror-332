import json
import os
import sqlite3
import threading
from concurrent.futures import ThreadPoolExecutor

import pandas as pd

from .progress import tqdm

DBFILE = "/tmp/maputil.db"


def conn():
    return sqlite3.connect(DBFILE, check_same_thread=False)


def clear():
    os.remove(DBFILE)


def prepdb(db):
    assert isinstance(db, sqlite3.Connection)

    db.execute("create table if not exists cache(key text primary key,val text)")
    db.commit()


def additem(db, key, jsonval):
    assert isinstance(db, sqlite3.Connection)
    assert isinstance(key, str)

    db.execute("insert into cache(key,val) values(?,?)", (key, jsonval))
    db.commit()


def getitem(db, key):
    assert isinstance(db, sqlite3.Connection)
    assert isinstance(key, str)

    cur = db.execute("select val from cache where key=?", (key,))
    ret = cur.fetchone()
    if ret is None:
        return None
    return ret[0]


def select(fn, inputs, run, progress=False, concurrency=1):
    """
    Apply a function to a collection of inputs with caching and optional concurrency.

    Parameters:
    -----------
    fn : callable
        The function to apply to each input element.
    inputs : list or pandas.Series
        The collection of input values to process.
    run : str
        A unique identifier for this run, used for caching results.
    progress : bool, default=False
        Whether to display a progress bar during execution.
    concurrency : int, default=1
        Number of concurrent workers. If greater than 1, processing is done in parallel.

    Returns:
    --------
    list or pandas.Series
        If inputs was a list, returns a list of results.
        If inputs was a pandas.Series, returns a pandas.Series with the same index.

    Notes:
    ------
    Results are cached based on the run identifier and input position.
    Subsequent calls with the same run identifier will use cached results.
    """
    assert callable(fn)
    assert isinstance(inputs, list) or isinstance(inputs, pd.Series)
    assert isinstance(run, str)
    assert isinstance(progress, bool)
    assert isinstance(concurrency, int) and concurrency > 0

    if isinstance(inputs, pd.Series):
        index = inputs.index
        inputs = inputs.tolist()
    else:
        index = None

    with conn() as db:
        prepdb(db)
        dblock = threading.Lock()

        def memfn(item):
            idx, input = item
            key = f"{run}:{idx}"
            with dblock:
                jsonval = getitem(db, key)
            if jsonval is None:
                val = fn(input)
                with dblock:
                    jsonval = json.dumps(val)
                    additem(db, key, jsonval)
            else:
                val = json.loads(jsonval)
            return val

        if concurrency == 1:
            if progress:
                inputs = tqdm(inputs)
            outputs = []
            for item in enumerate(inputs):
                outputs.append(memfn(item))
        else:
            with ThreadPoolExecutor(max_workers=concurrency) as executor:
                outputs = executor.map(memfn, enumerate(inputs))
                if progress:
                    outputs = tqdm(outputs, total=len(inputs))
                outputs = list(outputs)

    if index is None:
        return outputs
    else:
        return pd.Series(outputs, index=index)
