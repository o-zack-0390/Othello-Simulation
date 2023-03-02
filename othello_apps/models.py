from django.db import models

class Koma(models.Model):
    
#   id   : 番号
    id = models.IntegerField(primary_key=True)

#   name : 駒名
    name = models.CharField(max_length=100)

#   hp   : 駒のHP
    hp = models.IntegerField(blank=False, null=False)

#   atk  : 駒の攻撃力
    atk = models.IntegerField(blank=False, null=False)

#   start_f_normal_s1  : (通常ダメージ, 固定, 最小値)
    start_f_normal_s1  = models.IntegerField(blank=False, null=False)

#   end_f_normal_s1    : (通常ダメージ, 固定, 最大値)
    end_f_normal_s1    = models.IntegerField(blank=False, null=False)

#   start_m_normal_s1  : (通常ダメージ, 倍率, 最小値)
    start_m_normal_s1  = models.DecimalField(blank=False, null=False)

#   upper_m_normal_s1  : (通常ダメージ, 倍率, 上昇値)
    upper_m_normal_s1  = models.DecimalField(blank=False, null=False)

#   end_m_normal_s1    : (通常ダメージ, 倍率, 最大値)
    end_m_normal_s1    = models.DecimalField(blank=False, null=False)

#   start_f_special_s1 : (特殊ダメージ, 固定, 最小値)
    start_f_special_s1 = models.IntegerField(blank=False, null=False)

#   end_f_special_s1   : (特殊ダメージ, 固定, 最大値)
    end_f_special_s1   = models.IntegerField(blank=False, null=False)

#   start_m_special_s1 : (特殊ダメージ, 倍率, 最小値)
    start_m_special_s1 = models.DecimalField(blank=False, null=False)

#   upper_m_special_s1 : (特殊ダメージ, 倍率, 上昇値)
    upper_m_special_s1 = models.DecimalField(blank=False, null=False)

#   end_m_special_s1   : (特殊ダメージ, 倍率, 最大値)
    end_m_special_s1   = models.DecimalField(blank=False, null=False)

#   active_turn_s1     : (スキル継続ターン数)
    active_turn_s1     = models.PositiveSmallIntegerField(blank=False, null=False)