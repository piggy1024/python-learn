# exe EMS员工管理系统.py

# 创建一个列表保存员工信息,员工信息以字符串形式存到列表中
workers = ['孙悟空\t18\t\t男\t\t花果山','猪八戒\t22\t\t男\t\t高老庄']



print('=='*5,'欢迎使用EMS员工管理系统!','=='*5)
while True:
    print('请选择要执行的操作:')
    print('\t1.查询员工')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.退出系统')
    choose = input('请选择[1-4]:')
    print('============================================')

    # 根据用户选择做相关的操作
    if choose == '1':
        # 查询员工
        # 打印表头
        print('\t序号\t\t姓名\t\t年龄\t\t性别\t\t地址')
        # 创建一个变量,表示序号
        n = 1
        # 显示员工信息
        for worker in workers:
            print(f'\t{n}\t\t{worker}')
            n += 1
        print('============================================')
    elif choose == '2':
        # 添加员工
        a = input('->请输入员工的姓名:')
        b = input('->请输入员工的年龄:')
        c = input('->请输入员工的性别:')
        d = input('->请输入员工的地址:')
        print()
        new_worker = a +'\t'+ b+ '\t'+'\t' + c + '\t'+'\t' + d 

        # 将新的员工信息添加到列表workers
        workers.append(new_worker)
        print('该员工的信息已成功加入系统！')
        print('============================================')
    elif choose == '3':
        # 删除员工

        # 输入删除员工序号
        del_id = int(input('请输入要删除员工的序号：'))
        # 判断输入的序号是否存在
        if del_id < len(workers):
            # 根据序号将worker列表中索引为（序号-1）的对应员工信息删除
            workers.pop(del_id-1)
            print('该员工信息已从系统移除！')
            print('============================================')
        else :
            print('该员工不存在!')
            print('============================================')
            
    elif choose == '4':
        break
    else :
        print('无该操作,请重新选择!')
        print('============================================')