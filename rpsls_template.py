#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�21.12.1
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        number = 0
        return name
    if name=="ʷ����":
        number = 1
        return name
    if name=="ֽ":
        number = 2
        return name
    if name== "����":
        number = 3
        return name
    if name == "����":
        number = 4
        return name
    else:
        print("Error: No Correct Name")
        return name


    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        number="ʯͷ"
        return number
    if number== 1:
        number="ʷ����"
        return number
    if number==2:
        number="ֽ"
        return number
    if number==3:
        number="����"
        return number
    if number==4:
        number="����"
        return number

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    pass #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    player_choice=name_to_number(player_choice)# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    comp_number=random.randrange(0,5) # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    comp_number=number_to_name(comp_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    print("���Ե�ѡ���ǣ�"+str(comp_number))# ����Ļ����ʾ�����ѡ����������
    comp_number=name_to_number(comp_number)
    if player_choice==comp_number:
        print("ƽ��")
    elif (player_choice==4 and comp_number==3) or (player_choice==4 and comp_number==2) or (player_choice==3 and comp_number==1) or (player_choice==3 and comp_number==2) or (player_choice==2 and comp_number==1) or (player_choice==2 and comp_number==0) or(player_choice==1 and comp_number==4) or (player_choice==1 and comp_number==0) or (player_choice==0 and comp_number==3) or (player_choice==0 and comp_number==4):
        print("��Ӯ��")
    else:
        print("������")


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice









    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

     #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


