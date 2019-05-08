#coding = utf-8


from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod
class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil('/Users/pmy/Downloads/selenium code/config/keyword.xls')

        #步骤：拿到行数 -> 循环行数，去执行每一条case -> 是否执行 -> 拿到执行方法、操作值、输入数据
        #     -> 是否有输入数据 ->（有）执行方法（输入数据，操作元素）、（无）执行方法（操作元素）

        case_lines = handle_excel.get_lines()
        if case_lines:   #case_lines不为空
            for i in range(1,case_lines):         #从第1行开始
                is_run = handle_excel.get_col_value(i,3)   #传入行号和列号
                if is_run == 'yes':
                    methond = handle_excel.get_col_value(i, 4)
                    send_value = handle_excel.get_col_value(i, 5)
                    handle_value = handle_excel.get_col_value(i, 6)
                    #获取预期结果方法
                    except_result_method = handle_excel.get_col_value(i,7)
                    except_result = handle_excel.get_col_value(i, 8)

                    #''而不是None
                    self.run_method(methond,send_value,handle_value)

                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        else:
                            print("没有else")
                    else:
                        print("kong")

    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split('=')


    # 执行方法
    def run_method(self,method,send_value='',handle_value=''):
        # 字符串变成执行方法
        method_value = getattr(self.action_method, method)

        if send_value == '' and handle_value != '':
            #（无）执行方法（操作元素）
            result = method_value(handle_value)
        elif send_value == '' and handle_value == '':
            result = method_value()
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        else:
            #（有）执行方法（输入数据，操作元素）
            result = method_value(send_value, handle_value)
        return result



if __name__ == '__main__':
    test = KeywordCase()
    test.run_main()

