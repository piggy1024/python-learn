# 《《唐僧大战白骨精》》.py

# 角色的攻击力
fight = 5
# 角色的生命值
hp = 5

# boss的攻击力
boss_fight = 6
# boss的生命值
boss_hp = 6


print('-'*10,'欢迎来到游戏《《唐僧大战白骨精》》！','-'*10)


while  True:


    id = int(input(""">请选择你的游戏角色：
                            1. 唐僧
                            2. 白骨精
    请选择："""))


    if id == 1:
        print('''恭喜你成功选择唐僧角色，请开始你的游戏之旅！

                你的角色为->唐僧<-, 生命值为5,攻击力为5.

                 ''')
        step = int(input('''请选择你的游戏之路：

                            1.练级
                            2.打boss
                            3.逃跑\n'''))
        if step == 1:
            fight += 5
            hp += 5
            print(f'''恭喜练级成功！攻击力增加5，生命值增加5快去挑战boss吧。

                    当前生命值为{hp},攻击力为{fight}

                    1.使用技能雷霆半月斩。
                    2.使用技能一口盐汽水喷死你。\n''')
            choose = int(input('''选择技能：'''))
            if choose == 1:
                print('boss白骨精已被干掉！恭喜通关！')
            else:
                boss_hp -= 5
                print(f'''boss的攻击力为6，生命值为6.
                        boss剩余生命值为{boss_hp},你已经死亡！挑战失败！游戏OVER！''')

        elif step == 2:
            print(f'''当前生命值为{hp},攻击力为{fight}

                    1.使用技能雷霆半月斩。
                    2.使用技能一口盐汽水喷死你。\n''')
            choose = int(input('''选择技能：'''))
            if choose == 1:
                print('未练级，弱爆了！直接被白骨精KO！游戏OVER！')
            else:
                print('''boss白骨精将你吊起来打！回去好好练级吧。挑战失败！游戏OVER！''')
        else:
            print('年轻人，这么怂。逃是逃不了的，你被按在地上摩擦了！游戏OVER！')

    elif id == 2:
        print('该角色过强，官方目前正在紧急调整！')
    else:
        print('无此角色！')