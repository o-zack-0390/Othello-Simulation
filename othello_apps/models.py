from django.db import models

class Koma_Status(models.Model):
    
#   id   : 番号
    id   = models.IntegerField(primary_key=True)

#   name : 駒名
    name = models.CharField(max_length=100)

#   hp   : 駒のHP
    hp   = models.IntegerField(blank=False, null=False)

#   atk  : 駒の攻撃力
    atk  = models.IntegerField(blank=False, null=False)

#   start_f_normal_s1  : (通常ダメージ, 固定, 最小値)
    start_f_normal_s1  = models.IntegerField(blank=False, null=False)

#   upper_f_normal_s1  : (通常ダメージ, 固定, 上昇値)
    upper_f_normal_s1  = models.IntegerField(blank=False, null=False)

#   end_f_normal_s1    : (通常ダメージ, 固定, 最大値)
    end_f_normal_s1    = models.IntegerField(blank=False, null=False)

#   start_m_normal_s1  : (通常ダメージ, 倍率, 最小値)
    start_m_normal_s1  = models.DecimalField(blank=False, null=False)

#   upper_m_normal_s1  : (通常ダメージ, 倍率, 上昇値)
    upper_m_normal_s1  = models.DecimalField(blank=False, null=False)

#   end_m_normal_s1    : (通常ダメージ, 倍率, 最大値)
    end_m_normal_s1    = models.DecimalField(blank=False, null=False)

#   is_shield_pass_s1  : 貫通スキルか判定
    is_shield_pass_s1  = models.BooleanField(blank=False, null=False)

#   start_f_special_s1 : (特殊ダメージ, 固定, 最小値)
    start_f_special_s1 = models.IntegerField(blank=False, null=False)

#   upper_f_special_s1 : (特殊ダメージ, 固定, 上昇値)
    upper_f_special_s1 = models.IntegerField(blank=False, null=False)

#   end_f_special_s1   : (特殊ダメージ, 固定, 最大値)
    end_f_special_s1   = models.IntegerField(blank=False, null=False)

#   start_m_special_s1 : (特殊ダメージ, 倍率, 最小値)
    start_m_special_s1 = models.DecimalField(blank=False, null=False)

#   upper_m_special_s1 : (特殊ダメージ, 倍率, 上昇値)
    upper_m_special_s1 = models.DecimalField(blank=False, null=False)

#   end_m_special_s1   : (特殊ダメージ, 倍率, 最大値)
    end_m_special_s1   = models.DecimalField(blank=False, null=False)

#   upper_m_type_s1    : 倍率上昇の形式 → 「演算方式」or「加算方式」 (固定ダメージの場合はnull)
    upper_m_type_s1    = models.CharField(blank=True, null=True)

#   target_type_s1     : 倍率上昇が「自分の駒数依存」 or 「相手の駒数依存」
    target_type_s1     = models.CharField(blank=True, null=True)

#   active_turn_s1     : (スキル継続ターン数)
    active_turn_s1     = models.PositiveSmallIntegerField(blank=False, null=False)