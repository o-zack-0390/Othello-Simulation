from django.db import models

# 駒のステータス
class Status(models.Model):
    
#   id     : 番号
    id     = models.IntegerField(blank=False, null=False)

#   rarity : 「S」 or 「A」 or [B]
    rarity = models.CharField(blank=False, null=False, max_length=5)

#   name   : 駒名
    name   = models.CharField(blank=False, null=False, max_length=50, primary_key=True)

#   hp     : 駒のHP
    hp     = models.IntegerField(blank=False, null=False)

#   atk    : 駒の攻撃力
    atk    = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name


# 駒のスキル
class Skill(models.Model):

#   外部キー             : Statusを参照
    status             = models.ForeignKey(Status, on_delete=models.CASCADE)

#   name               : 駒名
    name               = models.CharField(blank=False, null=False, max_length=50, primary_key=True)

#   start_f_normal_s1  : (通常ダメージ, 固定, 最小値)
    start_f_normal_s1  = models.IntegerField(blank=True, null=True)

#   upper_f_normal_s1  : (通常ダメージ, 固定, 上昇値)
    upper_f_normal_s1  = models.IntegerField(blank=True, null=True)

#   end_f_normal_s1    : (通常ダメージ, 固定, 最大値)
    end_f_normal_s1    = models.IntegerField(blank=True, null=True)

#   start_m_normal_s1  : (通常ダメージ, 倍率, 最小値)
    start_m_normal_s1  = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   upper_m_normal_s1  : (通常ダメージ, 倍率, 上昇値)
    upper_m_normal_s1  = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   end_m_normal_s1    : (通常ダメージ, 倍率, 最大値)
    end_m_normal_s1    = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   is_shield_pass_s1  : 貫通スキルか判定
    is_shield_pass_s1  = models.BooleanField()

#   is_debuff_pass_s1  : デバフ無効スキルか判定
    is_debuff_pass_s1  = models.BooleanField()

#   start_f_special_s1 : (特殊ダメージ, 固定, 最小値)
    start_f_special_s1 = models.IntegerField(blank=True, null=True)

#   upper_f_special_s1 : (特殊ダメージ, 固定, 上昇値)
    upper_f_special_s1 = models.IntegerField(blank=True, null=True)

#   end_f_special_s1   : (特殊ダメージ, 固定, 最大値)
    end_f_special_s1   = models.IntegerField(blank=True, null=True)

#   start_m_special_s1 : (特殊ダメージ, 倍率, 最小値)
    start_m_special_s1 = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   upper_m_special_s1 : (特殊ダメージ, 倍率, 上昇値)
    upper_m_special_s1 = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   end_m_special_s1   : (特殊ダメージ, 倍率, 最大値)
    end_m_special_s1   = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   barrier_s1         : バリア値
    barrier_s1         = models.IntegerField(blank=True, null=True)

#   barrier_return_s1  : バリアの残ダメージ
    barrier_return_s1  = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   barrier_type_s1    : バリアのタイプ → 「通常」 or 「特殊」
    barrier_type_s1    = models.CharField(blank=False, null=False, max_length=10)

#   upper_m_type_s1    : 倍率上昇の形式 → 「演算方式」or「加算方式」 (固定ダメージの場合はnull)
    upper_m_type_s1    = models.CharField(blank=True, null=True, max_length=10)

#   target_type_s1     : 倍率上昇が「自分の駒数依存」 or 「相手の駒数依存」
    target_type_s1     = models.CharField(blank=True, null=True, max_length=10)

#   summons_s1         : 召喚駒
    summons_s1         = models.CharField(blank=True, null=True, max_length=50)

#   active_turn_s1     : スキル継続ターン数
    active_turn_s1     = models.PositiveSmallIntegerField(blank=False, null=False)

    def __str__(self):
        return self.name


# 駒のコンボスキル
class Combo_Skill(models.Model):

#   外部キー             : Statusを参照
    status             = models.ForeignKey(Status, on_delete=models.CASCADE)

#   name               : 駒名
    name               = models.CharField(blank=False, null=False, max_length=50, primary_key=True)

#   start_f_normal_s2  : (通常ダメージ, 固定, 最小値)
    start_f_normal_s2  = models.IntegerField(blank=True, null=True)

#   upper_f_normal_s2  : (通常ダメージ, 固定, 上昇値)
    upper_f_normal_s2  = models.IntegerField(blank=True, null=True)

#   end_f_normal_s2    : (通常ダメージ, 固定, 最大値)
    end_f_normal_s2    = models.IntegerField(blank=True, null=True)

#   start_m_normal_s2  : (通常ダメージ, 倍率, 最小値)
    start_m_normal_s2  = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   upper_m_normal_s2  : (通常ダメージ, 倍率, 上昇値)
    upper_m_normal_s2  = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   end_m_normal_s2    : (通常ダメージ, 倍率, 最大値)
    end_m_normal_s2    = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   is_shield_pass_s2  : 貫通スキルか判定
    is_shield_pass_s2  = models.BooleanField()

#   is_debuff_pass_s2  : デバフ無効スキルか判定
    is_debuff_pass_s2  = models.BooleanField()

#   start_f_special_s2 : (特殊ダメージ, 固定, 最小値)
    start_f_special_s2 = models.IntegerField(blank=True, null=True)

#   upper_f_special_s2 : (特殊ダメージ, 固定, 上昇値)
    upper_f_special_s2 = models.IntegerField(blank=True, null=True)

#   end_f_special_s2   : (特殊ダメージ, 固定, 最大値)
    end_f_special_s2   = models.IntegerField(blank=True, null=True)

#   start_m_special_s2 : (特殊ダメージ, 倍率, 最小値)
    start_m_special_s2 = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   upper_m_special_s2 : (特殊ダメージ, 倍率, 上昇値)
    upper_m_special_s2 = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   end_m_special_s2   : (特殊ダメージ, 倍率, 最大値)
    end_m_special_s2   = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   barrier_s2         : バリア値
    barrier_s2         = models.IntegerField(blank=True, null=True)

#   barrier_return_s2  : バリアの残ダメージ
    barrier_return_s2  = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   barrier_type_s2    : バリアのタイプ → 「通常」 or 「特殊」
    barrier_type_s2    = models.CharField(blank=False, null=False, max_length=10)

#   upper_m_type_s2    : 倍率上昇の形式 → 「演算方式」or「加算方式」 (固定ダメージの場合はnull)
    upper_m_type_s2    = models.CharField(blank=True, null=True, max_length=10)

#   target_type_s2     : 倍率上昇が「自分の駒数依存」 or 「相手の駒数依存」
    target_type_s2     = models.CharField(blank=True, null=True, max_length=10)

#   summons_s2         : 召喚駒
    summons_s2         = models.CharField(blank=True, null=True, max_length=50)

#   active_turn_s2     : スキル継続ターン数
    active_turn_s2     = models.PositiveSmallIntegerField(blank=False, null=False)

    def __str__(self):
        return self.name


# 防御駒の定義
class Shield(models.Model):
    
#   id          : 番号
    id          = models.IntegerField(blank=False, null=False)

#   name        : 駒名
    name        = models.CharField(blank=False, null=False, max_length=50, primary_key=True)

#   debuff      : 通常デバフ率
    debuff      = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   coercion    : 威圧
    coercion    = models.IntegerField(blank=True, null=True)

#   normal_cut  : 通常カット率
    normal_cut  = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   special_cut : 特殊カット率
    special_cut = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

#   cut_type    : 「表になっている間」 or 「ひっくり返されたとき」
    cut_type    = models.CharField(blank=False, null=False, max_length=10)

#   active_turn : スキル継続ターン数
    active_turn = models.PositiveSmallIntegerField(blank=False, null=False)

    def __str__(self):
        return self.name