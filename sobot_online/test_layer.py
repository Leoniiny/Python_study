# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
import pytest
from sobot_online.common.file_dealing import *


class Test_GetSessionStatisticsPage:
    test_data = load_yaml_file(filepath=r"/data/test_data/statistic_case.yml")["data"]

    @pytest.mark.parametrize("case_num,expect,searchWay, startDate, endDate,source,page, size, channelFlag, "
                             "robotIdsParam, departIdsParam,allViewFlag, groupIdsParam, staffIdsParam,summaryWay", test_data)
    def test_get_session_statistics_page(self, case_num,expect,searchWay=3, startDate="2024-06-17 00:00:00", endDate="2024-06-17 23:59:00",
                                    source="",page=1, size=15, channelFlag="", robotIdsParam="", departIdsParam="",
                                    allViewFlag="", groupIdsParam="", staffIdsParam="",summaryWay=""):
        self.test_get_session_statistics_page(searchWay, startDate, endDate,source,page, size, channelFlag,
                             robotIdsParam, departIdsParam,allViewFlag, groupIdsParam, staffIdsParam,summaryWay)
        pytest.assume(expect == "成功")

if __name__ == '__main__':
    pytest.main(["-vs", __file__])
