import requests
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

def get_html(url):
    return urlopen(url).read()

def get_remote_soup(url):
    return BeautifulSoup(get_html(url))

def get_local_soup(file_name):
    with open(file_name, 'r') as f:
        return BeautifulSoup(f.read())

post_dict = {
    #"Value1_1" : "",
    #"Value5_1" : "",
    #"Value2_1" : "",
    "Value6_1" : "03%2F26%2F2016",
    #"Value3_1" : "",
    "Value6_2" : "04%2F09%2F2016",
    "searchID.x" : 120,
    "searchID.y" : 15,
    "FieldName1" : "police_call_agency",
    "Operator1" : "OR",
    "NumCriteriaDetails1" : 1,
    "ComparisonType1_1" : "MULTI_OR_%3D",
    "MatchNull1_1" : "N",
    "FieldName2" : "police_call_address",
    "Operator2" : "OR",
    "NumCriteriaDetails2" : 1,
    "ComparisonType2_1" : "LIKE",
    "MatchNull2_1" : "N",
    "FieldName3" : "police_call_city",
    "Operator3" : "OR",
    "NumCriteriaDetails3" : 1,
    "ComparisonType3_1" : "%3D",
    "MatchNull3_1" : "N",
    "NumCriteriaDetails4" : 1,
    "MatchNull4_1" : "N",
    "FieldName5" : "police_call_crime",
    "Operator5" : "OR",
    "NumCriteriaDetails5" : 1,
    "ComparisonType5_1" : "MULTI_OR_%3D",
    "MatchNull5_1" : "N",
    "FieldName6" : "police_call_date",
    "Operator6" : "AND",
    "NumCriteriaDetails6" : 2,
    "ComparisonType6_1" : "%3E%3D",
    "MatchNull6_1" : "N",
    "ComparisonType6_2" : "%3C%3D",
    "MatchNull6_2" : "N",
    "NumCriteriaDetails7" : 1,
    "MatchNull7_1" : "N",
    "AppKey" : "183210004bc157ae61784b8da07a"

}

request =
