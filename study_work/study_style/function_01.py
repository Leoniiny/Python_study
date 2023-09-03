
def show_stu_info(user_list):
    num = 0
    print("-"*14,"学生列表","-"*14)
    for dic in user_list:
        num += 1
        value_name = dic.get("name")
        value_age = dic.get("age")
        print(num ,value_name ,value_age)
    print("-"*40)


if __name__ == '__main__':
    user_list= [{"name":"张三","age":18},{"name":"李四","age":19},{"name":"王五","age":22}]
    # num = 0
    # print("-----学生列表-------")
    # for dic in user_list:
    #     num += 1
    #     value_name = dic.get("name")
    #     value_age = dic.get("age")
    #     print(num,value_name,value_age)
    show_stu_info(user_list)
