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
    return l1_value, l1_value_diamond


# 1级到3级需要的石头，金，体力
def l1tol3():
    l3_gold = l3_diamond = l3_strength = 0
    l1_gold, l1_value_diamond = l1()
    l3_stone = l1_to_l3+1      # 12 level 1 ES + level1 ES
    l3_gold += l3_stone*l1_gold
    l3_diamond += l3_stone*l1_value_diamond
    l3_gold += l1_to_l3_value     # 0.39 Gold
    l3_strength += l1_to_l3_strength  # 10 Strength

    return l3_gold, l3_diamond, l3_strength


# 3级到4级需要的石头，金，体力，概率
def l3tol4():
    l4_gold = l4_diamond = l4_strength = 0
    while True:
        # 1级所需要的金，钻石
        _l1_gold, _l1_diamond = l1()
        # 3级所需要的金，钻石，体力
        _l3_gold, _l3_diamond, _l3_strength = l1tol3()
        l4_gold += l3_to_l4 * _l1_gold  # l3_to_l4 = 16  16 level1 ES + level3 ES
        l4_gold += _l3_gold
        l4_gold += l3_to_l4_value  # l3_to_l4_value = 0.897  # 0.897 Gold
        l4_diamond += l3_to_l4 * _l1_diamond
        l4_diamond += _l3_diamond
        l4_strength += _l3_strength
        rate = random()
        print(f"ランダム:{rate:.4f}")
        #l3_to_l4_rate = 0.4878
        # Probability of success. If failed, lost all except strength.
        if rate < l3_to_l4_rate:
            l4_strength += l3_to_l4_strength  # l3_to_l4_strength = 10  # 10 Strength
            print(f"★ 成功 ★")
            break
    return l4_gold, l4_diamond, l4_strength


# 4级到6级需要的石头，金，体力
def l4tol6():
    l6_gold = l6_diamond = l6_strength = 0
    # l4_to_l6 = 12  # 12 level4 ES + level4 ES
    for idx in range(l4_to_l6+1):
        _l4_gold, _l4_diamond, _l4_strength = l3tol4()
        l6_gold += _l4_gold
        l6_diamond += _l4_diamond
        l6_strength += _l4_strength
    l6_gold += l4_to_l6_value  # l4_to_l6_value = 19.75  # 0.897 Gold
    l6_strength += l4_to_l6_strength  # l4_to_l6_strength = 10  # 10 Strength

    return l6_gold, l6_diamond, l6_strength


# if __name__ == "__main__":
l6_gold, l6_diamond, l6_strength = l4tol6()
# 1 diamond = 0.78 gold
# 1 tili = 1 gold
total_gold = l6_diamond*0.78 + l6_strength*1 + l6_gold
print(f"生成費用：{total_gold:.2f}")
