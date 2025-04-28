from function.check_in import get_listening_classes_and_sign, check_exam

if __name__ == "__main__":
    # check_exam()
    get_listening_classes_and_sign(filtered_courses=[
        # 默认为空 所有课题监听课程测试
        # 若填写课程名称 则只监听列表里的课，其余课仅签到,建议按自己需求添加
        "计算机组成原理","数据结构"
    ])