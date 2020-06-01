# 函数返回多个结果

# R Skill1 Skill2

def damage(skill1, skill2):
    damage1 = skill1*3
    damage2 = skill2*2+10
    return damage1, damage2 #函数返回多个结果

# damages=damage(3,6)
# print(damages[0],damages[1])
# print(type(damages))   # tuple

#用名字接收比上面那种用元组0，1取更直观，这个更推荐
skill_damage,skill2_damage=damage(3,6)
print(skill_damage,skill2_damage)
