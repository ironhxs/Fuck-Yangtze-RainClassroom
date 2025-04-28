from function.check_in import get_listening_classes_and_sign, check_exam

if __name__ == "__main__":
    # check_exam()
    get_listening_classes_and_sign()


# 测试题空时进行OCR搜题
# request_ai(type="单选题",problem="",options=[
#         {
#           "key": "A",
#           "value": ""
#         },
#         {
#           "key": "B",
#           "value": ""
#         },
#         {
#           "key": "C",
#           "value": ""
#         },
#         {
#           "key": "D",
#           "value": ""
#         }
#       ],img_url="https://qn-st0.yuketang.cn/Fn8KemG7VHD1cjIlYIjMJHMTSFEO?imageView2/2/w/1280/format/webp")
