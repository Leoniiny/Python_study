# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
from sobot_online.Bs_layer.bs_OnlineAgent import ConsoleSetting


class Do_Scheme(ConsoleSetting):
    def __init__(self):
        super().__init__()

    def up_down_scheme(self,list_status=1, scheme_name="", page=1, pageSize=999999, status=0, editType="1"):
        sche_rest = super().get_scheme_list(status=list_status,scheme_name=scheme_name,page=page,pageSize=pageSize)
        temp_sche_list = sche_rest.get('items')
        if temp_sche_list:
            for sche_info in temp_sche_list:
                schemeid = sche_info.get('id')
                print(f"schemeid  >>>：{schemeid}")
                super().update_scheme(schemeid,status=status,editType=editType)


if __name__ == '__main__':
    obj = Do_Scheme()
    obj.up_down_scheme()
