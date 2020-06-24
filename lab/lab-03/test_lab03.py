from lab03 import*
import pytest

def test_semanticAnalyze():
    data1 = ['-1']
    data2 = ['9876543210']
    data3 = ['1']
    assert semanticAnalyze(data1)==False
    assert semanticAnalyze(data2)==False
    assert semanticAnalyze(data3)==True

def test_syntaxAnalyze():
    data1 = ['a']
    data2 = ['1']
    assert syntaxAnalyze(data1) == True
    assert syntaxAnalyze(data2) == False

def test_analysisData():
    data1 = ['a']
    data2 = ['9876543210']
    data3 = ['1']
    assert analysisData(data1) == "'a' is not a number."
    assert analysisData(data2) == "9876543210 is not in range 0–2,147,483,647."
    assert analysisData(data3) == True