# -*- codeing = utf-8 -*-
# @Time :2025/2/20 00:27
# @Author :luzebin
import pandas as pd

from smartpush.export.basic.ExcelExportChecker import check_excel_all, read_excel_and_write_to_list, \
    read_excel_from_oss, read_excel_csv_data, check_excel
from smartpush.export.basic.ReadExcel import read_excel_from_oss
from smartpush.export.basic.ReadExcel import read_excel_and_write_to_dict
from smartpush.export.basic.GetOssUrl import get_oss_address_with_retry, export_requestParam, import_requestParam

if __name__ == '__main__':
    oss1 = "https://cdn.smartpushedm.com/material_ec2/2025-02-25/58c4a3a885884741b22380c360ac2894/【自动化导出】营销活动URL点击与热图.xlsx"
    oss2 = "https://cdn.smartpushedm.com/material_ec2/2025-02-27/a5e18e3b3a83432daca871953cb8471b/【自动化导出】营销活动URL点击与热图.xlsx"
    # # print(check_excel_all(oss1, oss1))
    oss3 = "https://cdn.smartpushedm.com/material_ec2/2025-02-25/58c4a3a885884741b22380c360ac2894/【自动化导出】营销活动URL点击与热图.xlsx"
    oss4 = "https://cdn.smartpushedm.com/material_ec2/2025-02-26/58cee630b4c84eec9572b867af4ce692/%E3%80%90%E8%87%AA%E5%8A%A8%E5%8C%96%E5%AF%BC%E5%87%BA%E3%80%91%E8%90%A5%E9%94%80%E6%B4%BB%E5%8A%A8URL%E7%82%B9%E5%87%BB%E4%B8%8E%E7%83%AD%E5%9B%BE.xlsx"
    expected_oss = "https://cdn.smartpushedm.com/material_ec2/2025-02-26/757df7e77ce544e193257c0da35a4983/%E3%80%90%E8%87%AA%E5%8A%A8%E5%8C%96%E5%AF%BC%E5%87%BA%E3%80%91%E8%90%A5%E9%94%80%E6%B4%BB%E5%8A%A8%E6%95%B0%E6%8D%AE%E6%A6%82%E8%A7%88.xlsx"
    actual_oss = "https://cdn.smartpushedm.com/material_ec2/2025-02-26/757df7e77ce544e193257c0da35a4983/%E3%80%90%E8%87%AA%E5%8A%A8%E5%8C%96%E5%AF%BC%E5%87%BA%E3%80%91%E8%90%A5%E9%94%80%E6%B4%BB%E5%8A%A8%E6%95%B0%E6%8D%AE%E6%A6%82%E8%A7%88.xlsx"

    e_person_oss1 = "https://cdn.smartpushedm.com/material_ec2/2025-02-27/b48f34b3e88045d189631ec1f0f23d51/%E5%AF%BC%E5%87%BA%E5%85%A8%E9%83%A8%E5%AE%A2%E6%88%B7.csv"
    a_person_oss2 = "https://cdn.smartpushedm.com/material_ec2/2025-02-27/c50519d803c04e3b9b52d9f625fed413/%E5%AF%BC%E5%87%BA%E5%85%A8%E9%83%A8%E5%AE%A2%E6%88%B7.csv"
    host = "https://test.smartpushedm.com/api-em-ec2"
    reqHeaders = {
        'cookie': 'osudb_appid=SMARTPUSH;osudb_oar=#01#SID0000123BL6ciRHRKpvOm/vWT9OS9brpfhSErcOdgeXJc0RJFopg83z0N3RzDE4w2DE5cQj6ALkLP8vG6Rhs0sR7NfToZvCLWXdQtYk6DJoKe4tqdo4kNcIc9F5obzLuyRmwGy9CZKcg/bMlmNyDZwBI1SIO;osudb_subappid=1;osudb_uid=4213785247;ecom_http_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDM4NDI1NTIsImp0aSI6IjEwNGQwOTVjLTA3MDItNDI5MC1iZjQzLWQ4YTVhNjdmNDM2NSIsInVzZXJJbmZvIjp7ImlkIjowLCJ1c2VySWQiOiI0MjEzNzg1MjQ3IiwidXNlcm5hbWUiOiIiLCJlbWFpbCI6ImZlbGl4LnNoYW9Ac2hvcGxpbmVhcHAuY29tIiwidXNlclJvbGUiOiJvd25lciIsInBsYXRmb3JtVHlwZSI6Nywic3ViUGxhdGZvcm0iOjEsInBob25lIjoiIiwibGFuZ3VhZ2UiOiJ6aC1oYW5zLWNuIiwiYXV0aFR5cGUiOiIiLCJhdHRyaWJ1dGVzIjp7ImNvdW50cnlDb2RlIjoiQ04iLCJjdXJyZW5jeSI6IkpQWSIsImN1cnJlbmN5U3ltYm9sIjoiSlDCpSIsImRvbWFpbiI6InNtYXJ0cHVzaDQubXlzaG9wbGluZXN0Zy5jb20iLCJsYW5ndWFnZSI6ImVuIiwibWVyY2hhbnRFbWFpbCI6ImZlbGl4LnNoYW9Ac2hvcGxpbmUuY29tIiwibWVyY2hhbnROYW1lIjoiU21hcnRQdXNoNF9lYzJf6Ieq5Yqo5YyW5bqX6ZO6IiwicGhvbmUiOiIiLCJzY29wZUNoYW5nZWQiOmZhbHNlLCJzdGFmZkxhbmd1YWdlIjoiemgtaGFucy1jbiIsInN0YXR1cyI6MCwidGltZXpvbmUiOiJBc2lhL01hY2FvIn0sInN0b3JlSWQiOiIxNjQ0Mzk1OTIwNDQ0IiwiaGFuZGxlIjoic21hcnRwdXNoNCIsImVudiI6IkNOIiwic3RlIjoiIiwidmVyaWZ5IjoiIn0sImxvZ2luVGltZSI6MTc0MTI1MDU1MjI4Miwic2NvcGUiOlsiZW1haWwtbWFya2V0IiwiY29va2llIiwic2wtZWNvbS1lbWFpbC1tYXJrZXQtbmV3LXRlc3QiLCJlbWFpbC1tYXJrZXQtbmV3LWRldi1mcyIsImFwaS11Yy1lYzIiLCJhcGktc3UtZWMyIiwiYXBpLWVtLWVjMiIsImZsb3ctcGx1Z2luIl0sImNsaWVudF9pZCI6ImVtYWlsLW1hcmtldCJ9.SjeTCLaZqbEFEFNeKe_EjrwmR0LdEYO9697ymVNzf5Q;',
        'Content-Type': 'application/json'}
    actual_oss = get_oss_address_with_retry(11911, host, reqHeaders, import_requestParam, is_import=True)
    actual_oss = get_oss_address_with_retry(11896, host, reqHeaders, export_requestParam)
    # # res=read_excel_and_write_to_dict(read_excel_from_oss(actual_oss))
    # # print(res)
    # # print(read_excel_and_write_to_dict(read_excel_from_oss(oss1), type=".xlsx"))
    # print(check_excel(check_type="all", actual_oss=actual_oss, expected_oss=expected_oss))
    # print(check_excel_all(actual_oss=oss1, expected_oss=oss2,skiprows =1))
    # print(check_excel_all(actual_oss=oss1, expected_oss=oss2, ignore_sort=0))
    # print(check_excel_all(actual_oss=a_person_oss2, expected_oss=e_person_oss1, check_type="including"))
    # print(check_excel_all(actual_oss=e_person_oss1, expected_oss=a_person_oss2, check_type="person"))
    # read_excel_csv_data(type=)

    # flow_ex="https://cdn.smartpushedm.com/material_ec2/2025-02-20/ad9e1534b8134dd098e96813f17d4b4d/%E6%B5%8B%E8%AF%95flow%E6%95%B0%E6%8D%AE%E6%8A%A5%E5%91%8A%E5%AF%BC%E5%87%BA%E5%8B%BF%E5%8A%A8%E6%95%B0%E6%8D%AE%E6%A6%82%E8%A7%88.xlsx"
    # flow_ac="https://cdn.smartpushedm.com/material_ec2/2025-03-04/0c8f919f28d4455f9908f905aada7efb/测试flow数据报告导出勿动数据概览.xlsx"
    # print(check_excel_all(actual_oss=flow_ac, expected_oss=flow_ex, check_type="including",export_type="flow",skiprows=1))
