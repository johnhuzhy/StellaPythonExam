from random import random
"""
Level 1 Elements Stone
"""
l1_value = 0.75  # 0.75 Gold
l1_value_diamond = 8  # 8 Diamond

"""
Level 1 -> Level 3 Elements Stone
"""
l1_to_l3 = 12  # 12 level 1 ES + level1 ES
l1_to_l3_value = 0.39  # 0.39 Gold
l1_to_l3_strength = 10  # 10 Strength

"""
Level 3 -> Level 4 Elements Stone
"""
l3_to_l4 = 16  # 16 level1 ES + level3 ES
l3_to_l4_value = 0.897  # 0.897 Gold
l3_to_l4_strength = 10  # 10 Strength
# Probability of success. If failed, lost all except strength.
l3_to_l4_rate = 0.4878

"""
Level 4 -> Level 6 Elements Stone
"""
l4_to_l6 = 12  # 12 level4 ES + level4 ES
l4_to_l6_value = 19.75  # 0.897 Gold
l4_to_l6_strength = 10  # 10 Strength

sum_stone = 0
sum_diamond = 0
sum_gold = 0
sum_strength = 0

# 1级1个石头购买的所需的金和钻石


def l1():
    global sum_gold, sum_diamond
    sum_gold = l1_value
    sum_diamond = l1_value_diamond
    return sum_gold, sum_diamond

# 1级到3级需要的石头，金，体力


def l1tol3():
    global sum_stone, sum_gold, sum_diamond, sum_strength
    l1_gold, l1_value_diamond = l1()
    sum_stone = l1_to_l3      # 12 level 1 ES + level1 ES
    sum_gold += l1_to_l3*l1_gold
    sum_diamond += l1_to_l3*l1_value_diamond
    sum_gold += l1_to_l3_value     # 0.39 Gold
    sum_strength += l1_to_l3_strength  # 10 Strength

    return sum_gold, sum_diamond, sum_strength


# 3级到4级需要的石头，金，体力，概率
def l3tol4():
    global sum_gold, sum_diamond, sum_strength
    # 1级所需要的金，钻石
    l1_gold, l1_diamond = l1()
    # 3级所需要的金，钻石，体力
    l3_gold, l3_diamond, l3_strength = l1tol3()

    sum_gold += l3_to_l4*l1_gold  # l3_to_l4 = 16  16 level1 ES + level3 ES
    sum_gold += l3_to_l4_value  # l3_to_l4_value = 0.897  # 0.897 Gold
    sum_diamond += l3_to_l4*l1_diamond
    sum_strength += l3_strength  # l3_to_l4_strength = 10  # 10 Strength
    sum_strength += l3_to_l4_strength

    # Probability of success. If failed, lost all except strength.
    #l3_to_l4_rate = 0.4878
    while random() < l3_to_l4_rate:
        return sum_gold, sum_diamond, sum_strength
    else:
        sum_gold = 0
        sum_diamond = 0
        l3tol4()

# 4级到6级需要的石头，金，体力


def l4tol6():
    global sum_gold, sum_diamond, sum_strength
    l4_gold, l4_diamond, l4_strength = l3tol4()
    # l4_to_l6 = 12  # 12 level4 ES + level4 ES
    sum_gold += (l4_to_l6+1)*l4_gold
    sum_gold += l4_to_l6_value  # l4_to_l6_value = 19.75  # 0.897 Gold
    sum_diamond = (l4_to_l6+1)*l4_diamond
    sum_strength += l4_strength
    sum_strength += l4_to_l6_strength  # l4_to_l6_strength = 10  # 10 Strength

    return sum_gold, sum_diamond, sum_strength


# if __name__ == "__main__":
l6_gold, l6_diamond, l6_strength = l4tol6()
# 1 diamond = 0.78 gold
# 1 tili = 1 gold
total_gold = l6_diamond*0.78+l6_strength*1+l6_gold
print(total_gold)

