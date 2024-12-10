import csv
import pandas as pd
import os
import openpyxl

def take_transactions_from_csv(filename):
    '''Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями'''
    with open(filename, encoding='utf-8') as f:
        data = csv.DictReader(f, delimiter=';')
        data_list = [row for row in data]
    return data_list