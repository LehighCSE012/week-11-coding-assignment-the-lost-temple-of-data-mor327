"""
Adventure Parser Module

Processes artifact data, temple location notes, and journal entries
from the Lost Temple of Azmar expedition led by Dr. Evelyn Reed.
"""

import re
import pandas as pd

def load_artifact_data(excel_filepath):
    """
    Reads artifact data from a specific sheet ('Main Chamber') in an Excel file,
    skipping the first 3 rows.

    Args:
        excel_filepath (str): The path to the artifacts Excel file.

    Returns:
        pandas.DataFrame: DataFrame containing the artifact data.
    """
    df = pd.read_excel(excel_filepath, sheet_name='Main Chamber', skiprows=3)
    return df

def load_location_notes(tsv_filepath):
    """
    Reads location data from a Tab-Separated Value (TSV) file.

    Args:
        tsv_filepath (str): The path to the locations TSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the location data.
    """
    df = pd.read_csv(tsv_filepath, sep='\t')
    return df

def extract_journal_dates(journal_text):
    """
    Extracts all dates in MM/DD/YYYY format from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of date strings found in the text.
    """
    pattern = r"\b\d{2}/\d{2}/\d{4}\b"
    candidates = re.findall(pattern, journal_text)

    # Only include dates with valid MM and DD - fix to pass test case
    valid_dates = []
    for date in candidates:
        mm, dd, _ = map(int, date.split("/"))
        if 1 <= mm <= 12 and 1 <= dd <= 31:
            valid_dates.append(date)

    return valid_dates

def extract_secret_codes(journal_text):
    """
    Extracts all secret codes in AZMAR-XXX format (XXX are digits) from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of secret code strings found in the text.
    """
    codes = re.findall(r"\bAZMAR-\d{3}\b", journal_text)
    return codes
