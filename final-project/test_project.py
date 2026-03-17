import pytest
from project import function_1, function_2, function_3, function_4
import csv

def test_function_1(tmp_path):
    #I WILL CREATE FIRSTLY A TEMPORALY CSV
    path = tmp_path / "function_1.csv"
    swimmers = [
        {"name": "Phelps", "time": "48:35", "country": "USA"},
        {"name": "Lochte", "time": "49:00", "country": "USA"},
    ]

    with open(path, "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["name", "time", "country"])
        writer.writeheader()
        writer.writerows(swimmers)

    result = function_1(path)

    #fILAS Y COLUMNAS ANTES DE ENTRAR A LA TABLA
    #i PUT THE POSITION IN FIRST PLACE

    assert result[0][1] == "Phelps"
    assert result[1][1] == "Lochte"
    assert result[0][0] == 1
    assert result[1][0] == 2

def test_function_2(tmp_path):
    #I WILL CREATE FIRSTLY A TEMPORALY CSV
    path = tmp_path / "function_2.csv"
    swimmers = [
        {"name": "Phelps", "time": "48:35", "country": "USA"},
        {"name": "Lochte", "time": "49:00", "country": "USA"},
        {"name": "Iga", "time": "50:00", "country": "Poland"},
        {"name": "Esparta", "time": "52:64", "country": "Greece"},
    ]

    with open(path, "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["name", "time", "country"])
        writer.writeheader()
        writer.writerows(swimmers)

    result = function_2(path)

    assert "Best Time: Phelps" in result
    assert "Worst Time: Esparta" in result
    assert "Average:" in result
    assert "Median:" in result



def test_function_3(tmp_path):
    #I WILL CREATE FIRSTLY A TEMPORALY CSV
    path = tmp_path / "function_3.csv"
    swimmers = [
        {"name": "Phelps", "time": "48:35", "country": "USA"},
    ]

    with open(path, "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["name", "time", "country"])
        writer.writeheader()
        writer.writerows(swimmers)

    result = function_3(path, "Phelps")

    assert "Phelps" in result
    assert "48:35" in result
    assert "USA" in result


def test_function_4():
    assert function_4(1) == "swimmers_50_free.csv"
    assert function_4(2) == "swimmers_100_free.csv"
    assert function_4(3) == "swimmers_200_free.csv"
    assert function_4(4) == "swimmers_400_free.csv"
    assert function_4(99) == None
