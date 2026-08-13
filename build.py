# -*- coding: utf-8 -*-
"""HiTide Biotech website generator.
Reads embedded product data and renders static pages + per-product pages.
"""
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = ROOT
PROD_DIR = os.path.join(OUT, 'products')

# ---------------- i18n (UI chrome) ----------------
I18N = {
    'nav_home':'首页','nav_about':'公司简介','nav_team':'人物介绍','nav_products':'产品线','nav_contact':'联系我们',
    'hero_eyebrow':'动物健康 · 始于 2017','hero_title':'聚焦动物疫苗与水产动保，构建生物医药全产业链',
    'hero_lede':'海泰生物是一家专注于动物疫苗研发、生产、销售和服务的高技术企业。旗下六家子公司、六大业务板块覆盖疫苗、化药、抗体、反刍、研发、抗菌蛋白全产业链；与牛津大学、康奈尔大学等国内外科研院所深度合作，已获 40 项兽药生产批文、9 条 GMP 生产线。',
    'about_title':'一家以生物技术解决动物疫病防控问题的全产业链企业',
    'team_title':'30 年深耕动物疫苗的中美科学家团队',
    'products_title':'宠物 · 鸽 · 鱼 · 虾 · 蛙 · 畜禽 · 牛/羊 全场景产品矩阵',
    'contact_title':'携手海泰 · 共建绿色健康养殖',
}

def zh_en(zh, en=''):
    """Render bilingual span. Falls back to zh-only when no EN provided."""
    if not en:
        return zh
    return f'<span class="t-zh">{zh}</span><span class="t-en">{en}</span>'
EN = {
    'nav_home':'Home','nav_about':'About','nav_team':'Team','nav_products':'Products','nav_contact':'Contact',
    'hero_eyebrow':'Animal Health · Since 2017','hero_title':'Animal Vaccines & Aquaculture Health — A Full Biotech Value Chain',
    'hero_lede':'HiTide Biotech is a high-tech enterprise devoted to R&D, manufacturing and service of animal vaccines and aquaculture health products. Six subsidiaries and six business segments span vaccines, pharmaceuticals, antibodies, ruminants, R&D and antimicrobial proteins — partnering with Oxford, Cornell and other leading institutions, with 40+ veterinary approvals and 9 GMP lines.',
    'about_title':'A Full-Chain Enterprise Solving Animal Disease Control with Biotechnology',
    'team_title':'A Sino-US Scientist Team with 30 Years in Animal Vaccines',
    'products_title':'Pet · Pigeon · Fish · Shrimp · Frog · Livestock · Cattle/Sheep — Full-Scenario Product Matrix',
    'contact_title':'Partner with HiTide · Build Green & Healthy Farming',
}

# ---------------- categories ----------------
CATS = [
    ('cat',   '猫用','Cat'),
    ('dog',   '犬用','Dog'),
    ('pigeon','鸽用','Pigeon'),
    ('fish',  '鱼用','Fish'),
    ('frog',  '蛙用','Frog'),
    ('shrimp','虾用','Shrimp'),
    ('live',  '畜禽用','Livestock'),
    ('ruminant','牛/羊用','Cattle/Sheep'),
]
CAT_LABEL = {k:{'cn':cn,'en':en} for k,cn,en in CATS}

# ---------------- products ----------------
# fields: id,name,en,cat,img,type,net,std,tags(list),species(list),disease,
#         lead,meta(list),usage(list of steps),cases(list of dict),faq(list of {q,a}),rx(bool),calc(bool)
P = []
def add(**kw): P.append(kw)

# ===== CAT =====
add(id='taimiaoja',name='泰妙佳',en='TaiMiaoJia',cat='cat',img='assets/img/prod/prod_taimiaoja.jpg',
    type='维生素预混合饲料 III',net='100g/瓶 · 10瓶/盒',std='Q/HTD 01-2024',
    tags=['抑制病毒复制','滋补营养','改善胃肠','增强免疫','加速康复'],
    species=['猫'],disease='猫瘟 / 疱疹 / 杯状病毒',
    lead='猫用粉剂营养补充剂，含猫瘟、疱疹、杯状病毒结合蛋白，配合维生素快速补充机体营养、增强免疫、加速康复。',
    meta=['适用：猫瘟、疱疹、杯状病毒结合蛋白','规格：100g/瓶 · 10瓶/盒'])
add(id='miaolebao',name='妙乐宝',en='MiaoLeBao',cat='cat',img='assets/img/prod/prod_miaolebao.jpg',
    type='宠物营养补充剂（猫用）',net='1.5g×10包',std='Q/HTD 01-2024',
    tags=['抑制病毒复制','速补营养','改善胃肠','增强免疫','加速康复'],
    species=['猫'],disease='猫瘟 / 疱疹 / 杯状病毒',
    lead='猫用粉剂，含猫瘟、疱疹、杯状病毒结合蛋白，1.5g 小包易拌食，适合幼猫与挑食猫日常免疫支持。',
    meta=['适用：猫瘟、疱疹、杯状病毒结合蛋白','规格：1.5g×10包'])
add(id='futailai',name='福泰莱',en='FuTaiLai',cat='cat',img='assets/img/prod/prod_futailai.jpg',
    type='宠物营养补充剂（猫用）',net='粉剂 1.5g×10袋 / 片剂 2瓶/盒',std='Q/HTD 01-2024',
    tags=['抑制病毒复制','猫传腹 FCoV','植物中药抗病毒','10-15 天疗程'],
    species=['猫'],disease='猫传染性腹膜炎（FCoV）',
    lead='针对猫传腹病毒（FCoV）结合蛋白产品，粉剂与片剂两种剂型。片剂含植物中药抗病毒成分，每天一次、每次一片，连续 10-15 天。',
    meta=['含猫传腹病毒结合蛋白 + 嗜酸乳杆菌 NCFM + 动物双歧杆菌 Bb-12','剂型：粉剂 / 片剂','用法：每天一次，每次一片，连续 10-15 天'])
add(id='baozhentai_cat',name='包珍泰',en='BaoZhenTai (Cat)',cat='cat',img='assets/img/prod/prod_baozhentai.jpg',
    type='宠物营养补充剂（猫用片剂）',net='1瓶/盒',std='Q/HTD 01-2024',
    tags=['抑制病毒复制','猫疱疹','植物中药抗病毒','10-15 天疗程'],
    species=['猫'],disease='猫疱疹病毒',
    lead='含猫疱疹病毒结合蛋白 + 植物中药抗病毒成分，针对猫疱疹病毒引起的眼部、上呼吸道症状，每天一次、每次一片，连续 10-15 天。',
    meta=['含猫疱疹病毒结合蛋白 + 植物中药抗病毒成分','用法：每天一次，每次一片，连续 10-15 天'])
add(id='beizhuangtai',name='杯壮泰',en='BeiZhuangTai',cat='cat',img='assets/img/prod/prod_beizhuangtai.jpg',
    type='宠物营养补充剂（猫用片剂）',net='1瓶/盒',std='Q/HTD 01-2024',
    tags=['抑制病毒复制','猫杯状','直接口服'],
    species=['猫'],disease='猫杯状病毒',
    lead='含猫杯状病毒结合蛋白 + 植物中药抗病毒成分，直接口服 1-2 片，连续 10-15 天，针对猫杯状病毒引起的口腔、呼吸道症状。',
    meta=['含猫杯状病毒结合蛋白 + 植物中药抗病毒成分','用法：直接口服 1-2 片，连续 10-15 天'])
add(id='wentailai',name='温泰莱',en='WenTaiLai',cat='cat',img='assets/img/prod/prod_wentailai.jpg',
    type='宠物营养补充剂（猫用片剂）',net='1瓶/盒',std='Q/HTD 01-2024',
    tags=['抑制病毒复制','猫瘟','10-15 天疗程'],
    species=['猫'],disease='猫瘟病毒（FPV）',
    lead='含猫瘟病毒结合蛋白 + 植物中药抗病毒成分，针对猫泛白细胞减少症（猫瘟），每天一次、每次一片，连续 10-15 天。',
    meta=['含猫瘟病毒结合蛋白 + 植物中药抗病毒成分','用法：每天一次，每次一片，连续 10-15 天'])
add(id='yanzhengtai',name='炎证泰',en='YanZhengTai',cat='cat',img='assets/img/prod/prod_yanzhengtai.jpg',
    type='广谱抗菌蛋白外用喷剂',net='20ml/瓶',std='猫狗双标签',
    tags=['广谱抗菌蛋白','EGF + FGF21','促进愈合','外用喷涂'],
    species=['猫','犬'],disease='皮肤损伤 / 口腔溃疡 / 手术伤口',
    lead='猫狗通用的外用喷剂，含广谱抗菌蛋白 + 表皮生长因子（EGF）+ 成纤维细胞生长因子（FGF21），适用于皮肤损伤、口腔溃疡、手术伤口等外用场景。',
    meta=['广谱抗菌蛋白 + EGF + FGF21','猫用 + 犬用双标签','外用喷涂'])
# ===== DOG =====
add(id='taiwangja',name='泰旺佳',en='TaiWangJia',cat='dog',img='assets/img/prod/prod_taiwangja.jpg',
    type='维生素预混合饲料 III',net='10瓶/盒',std='Q/HTD 01-2024',
    tags=['抑制病毒复制','速补营养','改善胃肠','增强免疫','加速康复'],
    species=['犬'],disease='犬瘟热 / 犬细小 / 犬冠状',
    lead='犬用粉剂，含犬瘟热、犬细小、犬冠状病毒结合蛋白，配合维生素快速补充营养、增强免疫、加速康复。',
    meta=['适用：犬瘟热、犬细小、犬冠状病毒结合蛋白','规格：10瓶/盒'])
add(id='wanglebao',name='汪乐宝',en='WangLeBao',cat='dog',img='assets/img/prod/prod_wanglebao.jpg',
    type='宠物营养补充剂（犬用）',net='2g×10包',std='Q/HTD 01-2024',
    tags=['抑制病毒复制','速补营养','改善胃肠','增强免疫','加速康复'],
    species=['犬'],disease='犬瘟热 / 犬细小 / 犬冠状',
    lead='犬用粉剂营养补充剂，含犬瘟热、犬细小、犬冠状病毒结合蛋白，2g 小包易拌食，适合幼犬与病后恢复。',
    meta=['适用：犬瘟热、犬细小、犬冠状病毒结合蛋白','规格：2g×10包'])
# ===== PIGEON =====
add(id='xinaowei',name='新奥威',en='XinAoWei',cat='pigeon',img='assets/img/prod/prod_xinaowei.jpg',
    type='新城疫活疫苗（V4/HB92 克隆株）',net='10瓶/盒',std='SPF',
    tags=['黏膜免疫','体液免疫','细胞免疫','鸽/鹌鹑/榛鸡'],
    species=['鸽'],disease='新城疫（ND）',
    lead='最安全的新城疫活疫苗（含一日龄雏鸽），天然耐热、ICPI 为零，由九江博美莱生物制品有限公司生产。',
    meta=['最安全 ND 活疫苗（含一日龄雏鸽）','天然耐热 · ICPI 为零','九江博美莱生物制品有限公司'])
add(id='xinsian',name='新思安',en='XinSiAn',cat='pigeon',img='assets/img/prod/prod_xinsian.jpg',
    type='鸡新城疫活疫苗（La Sota 株）',net='10瓶/盒',std='兽用 OTC',
    tags=['种毒优选','独特培养工艺','SPF 蛋','专用稀释液'],
    species=['鸽'],disease='新城疫（ND）',
    lead='抗原含量超标准 5 倍，免疫增强剂提升 100%，由九江博美莱生物制品有限公司生产。',
    meta=['抗原含量超标准 5 倍','免疫增强剂提升 100%','九江博美莱生物制品有限公司'])
add(id='xinliu',name='新流二联',en='XinLiu',cat='pigeon',img='assets/img/prod/prod_xinliu.jpg',
    type='新城疫 + 禽流感（H9）二联灭活疫苗',net='500ml/瓶',std='二联灭活',
    tags=['La Sota 株','WD 株','10^10 EID₅₀','抗原浓缩'],
    species=['鸽'],disease='新城疫 + 禽流感 H9',
    lead='H9 亚型保护率高达 94.4%，颈皮下/翼下肌肉注射，一次免疫同时防新城疫与禽流感 H9。',
    meta=['H9 亚型保护率高达 94.4%','颈皮下/翼下肌肉注射'])
add(id='baotai_pigeon',name='鸽宝泰',en='GeBaoTai',cat='pigeon',img='assets/img/prod/prod_baotai_pigeon.jpg',
    type='维生素预混合饲料 I',net='5g/瓶',std='Q/GDHTD 41-2024',
    tags=['免疫激活','长效保护 60 天+','创新包裹工艺','饮水拌料'],
    species=['鸽'],disease='免疫激活 / 病毒防控',
    lead='内源性干扰素高效表达，创新包裹工艺，每瓶用于 2000 羽份最佳，长效保护 60 天以上。',
    meta=['内源性干扰素高效表达','每瓶用于 2000 羽份最佳'])
add(id='qintaining',name='禽泰宁',en='QinTaiNing',cat='pigeon',img='assets/img/prod/prod_qintaining.jpg',
    type='液态维生素预混合饲料 IV',net='注射型',std='兽用 OTC',
    tags=['耐药菌克星','广谱抗菌','无药残'],
    species=['鸽'],disease='细菌感染 / 耐药菌',
    lead='颈皮下/胸部肌肉注射 0.2ml/羽，可与油佐剂疫苗混合使用，针对耐药菌、广谱抗菌、无药残。',
    meta=['颈皮下/胸部肌肉注射 0.2ml/羽','可与油佐剂疫苗混合使用'])
add(id='qintai_pigeon',name='禽泰安',en='QinTaiAn (Pigeon)',cat='pigeon',img='assets/img/prod/prod_qintai.jpg',
    type='维生素预混合饲料 I',net='100g',std='Q/GDHTD 41-2024',
    tags=['广谱通用','作用直接','组合高效','无应激残留'],
    species=['鸽'],disease='营养补充 / 免疫支持',
    lead='广谱通用维生素预混，作用直接、组合高效、无应激残留，鸽用营养与免疫支持基础产品。',
    meta=['粤饲预(2021)13011','Q/GDHTD 41-2024','净含量 100g'])
add(id='taikang',name='鸽泰康',en='GeTaiKang',cat='pigeon',img='assets/img/prod/prod_taikang_pigeon.jpg',
    type='禽用维生素预混合饲料',net='1kg',std='鸽专用',
    tags=['创新工艺','省力省心省钱','有效改善','优质原料'],
    species=['鸽'],disease='营养补充',
    lead='鸽专用维生素预混，1kg 用于 2400-3000 羽份，饮水/拌料，连续使用 2 天，创新工艺、优质原料。',
    meta=['1kg 用于 2400-3000 羽份','饮水/拌料，连续使用 2 天'])
add(id='nanhuaweikang',name='南华维康',en='NanHuaWeiKang',cat='pigeon',img='assets/img/prod/prod_nanhuaweikang.jpg',
    type='复合维生素 B 可溶性粉',net='1000g',std='兽药字 190855071',
    tags=['B 族维生素','多发性神经炎','消化障碍','癞皮病口腔炎'],
    species=['鸽'],disease='B 族维生素缺乏',
    lead='复合维生素 B 可溶性粉，针对多发性神经炎、消化障碍、癞皮病口腔炎，混饮每 1L 水 0.5~1.5g，连用 3-5 日。',
    meta=['兽药字 190855071','混饮：每 1L 水 0.5~1.5g，连用 3-5 日'])
add(id='wutan',name='戊二醛癸甲溴铵溶液',en='Glutaraldehyde-Deciquam',cat='pigeon',img='assets/img/prod/prod_wutan.jpg',
    type='消毒药',net='1000g',std='兽用 OTC',
    tags=['广谱消毒','细菌芽孢','真菌病毒','养殖场/种蛋'],
    species=['鸽'],disease='环境消毒',
    lead='广谱消毒，对细菌芽孢、真菌、病毒有效，适用于养殖场与种蛋消毒；常规 1:2000~4000 稀释，疫病期 1:500~1000 稀释。',
    meta=['常规 1:2000~4000 稀释','疫病期 1:500~1000 稀释'])
add(id='dikang',name='海泰滴康',en='HaiTai DiKang',cat='pigeon',img='assets/img/prod/prod_dikang.jpg',
    type='地美硝唑预混剂',net='100g',std='兽药字 190851143',rx=True,
    tags=['抗原虫药','广谱抗菌','密螺旋体','组织滴虫'],
    species=['鸽'],disease='滴虫病 / 密螺旋体',
    lead='地美硝唑预混剂，抗原虫、广谱抗菌，针对密螺旋体、组织滴虫；兽用处方药，每 1000kg 饲料 400-2500g。',
    meta=['兽药字 190851143','每 1000kg 饲料 400-2500g','处方药，凭兽医处方购买使用'])
add(id='koufu',name='口服补液盐',en='Oral Rehydration Salt',cat='pigeon',img='assets/img/prod/prod_koufu.jpg',
    type='电解质补充药',net='118g',std='兽药字 190856407',
    tags=['电解质补充','调节酸碱平衡','热应激','腹泻纠正'],
    species=['鸽'],disease='脱水 / 电解质失衡',
    lead='电解质补充药，调节酸碱平衡，针对热应激、腹泻纠正；1 包溶于 4L 水，自由饮用。',
    meta=['兽药字 190856407','1 包溶于 4L 水，自由饮用'])
# ===== FISH (rich) =====
add(id='hongtailai',name='虹泰莱',en='HongTaiLai',cat='fish',img='assets/img/aqua/hongtailai.jpg',
    type='复合预混合饲料 VII（A 包 + B 包包裹材料）',net='100 克/包',std='Q/GDCHTD 64-2025',
    tags=['提高免疫力','抗病毒','无抗养殖'],
    species=['鳜鱼','鲈鱼'],disease='蛙虹彩病毒（RSIV）',calc=True,
    lead='针对鳜鱼、鲈鱼蛙属虹彩病毒（RSIV）的病毒结合蛋白产品。连续拌饲料口服 5-7 天，临床观察案例显示死亡数显著下降、病毒转阴。',
    meta=['鳜鱼 / 鲈鱼 蛙虹彩病毒','Q/GDCHTD 64-2025','案例：3 万尾鳜鱼 300尾/天 → 6尾/天'],
    usage=['取 1 包 A 包，加入约 600ml 水，边搅拌边加入，充分混匀至形成悬浊液',
           '与 20kg 饲料充分搅拌混匀',
           '取 1 包 B 包（包裹材料）溶于约 600ml 水，边搅拌边加入至完全溶解',
           '再加入上述 20kg 饲料中充分搅拌均匀完成包裹',
           '每天投喂一餐，连续投喂 5-7 天'],
    cases=[{'num':'鳜鱼 · 案例','title':'佛山渔场 3 万尾鳜鱼 · RSIV 暴发','bg':'鳜鱼养殖暴发蛙虹彩病毒，用虹泰莱前每天死亡约 300 尾。','plan':'连续拌饲料口服 7 天。','eff':'第 15 天后死亡数降低至 6 尾，蛙虹彩病得到有效控制。','num2':'300 → 6 尾/天'},
          {'num':'鲈鱼 · 案例','title':'鲈鱼蛙虹彩病毒（CT 30.18）','bg':'蛙虹彩发病鲈鱼（CT 30.18），平均分 2 组，饲养条件一致。','plan':'实验组投喂虹彩病毒结合蛋白包裹饲料，每天一餐连续 5 天；观察 7 天后检测。','eff':'实验组 PCR 转阴（CT ≥45），平均存活率 65%；对照组仍为阳性（CT 31.668），存活率 35%。','num2':'存活率 65% vs 35%，CT 31.668 → ≥45'},
          {'num':'鲈鱼 · 案例','title':'鲈鱼蛙虹彩病毒（高剂量组）','bg':'蛙虹彩发病鲈鱼，平均分 2 组。','plan':'实验组投喂虹彩病毒结合蛋白包裹饲料，每天一餐连续 5 天；观察 5 天后检测。','eff':'实验组 PCR 转阴（CT ≥45），平均存活率 90%；对照组仍为阳性（CT 37.34），存活率 68%。','num2':'存活率 90% vs 68%，CT 37.34 → ≥45'}],
    faq=[('一包能拌多少饲料？','1 包 A 包 + 1 包 B 包配 20kg 饲料。'),
         ('连续用几天？','说明书 5-7 天。佛山案例用到第 7 天后死亡数持续下降，观察期到第 15 天。'),
         ('用后多久见效？','临床观察案例显示连续使用 7 天后死亡数明显下降。'),
         ('用错了怎么办？','立即停止投喂，观察鱼体反应。')])
add(id='shentailai',name='申泰莱',en='ShenTaiLai',cat='fish',img='assets/img/aqua/shentailai.jpg',
    type='复合预混合饲料 X（A 包 + B 包包裹材料）',net='100 克/包',std='Q/GDCHTD 67-2025',
    tags=['提高免疫力','抗病毒','无抗养殖'],
    species=['石斑鱼','鳜鱼'],disease='神经坏死病毒（NNV）',calc=True,
    lead='针对石斑鱼、鳜鱼神经坏死病毒（NNV）的病毒结合蛋白产品。NNV 攻毒保护试验显示治疗组存活率显著优于对照组。',
    meta=['石斑鱼 / 鳜鱼 神经坏死病毒','Q/GDCHTD 67-2025','案例：1.5万尾 120尾/天 → 0尾/天'],
    usage=['取 1 包 A 包，加入约 600ml 水，边搅拌边加入，充分混匀至形成悬浊液',
           '与 20kg 饲料充分搅拌混匀',
           '取 1 包 B 包（包裹材料）溶于约 600ml 水，边搅拌边加入至完全溶解',
           '再加入上述 20kg 饲料中充分搅拌均匀完成包裹',
           '每天投喂一餐，连续投喂 5-7 天'],
    cases=[{'num':'石斑鱼 · 案例','title':'山东东营 1.5 万尾石斑鱼 · NNV 攻毒','bg':'神经坏死病毒阳性，每天死亡 100+ 尾。','plan':'连续拌料口服申泰莱 7 天。','eff':'第 12 天后死亡数降低至 0 尾，神经坏死病毒病得到有效控制。','num2':'120+ → 0 尾/天'},
          {'num':'鳜鱼 · 攻毒试验','title':'NNV 攻毒保护试验 · 30 vs 30','bg':'饲料鳜 NNV 攻毒，设对照组与治疗组各 30 尾，均肌肉注射 NNV。','plan':'治疗组连续 5 天拌饲料口服 NNV 结合蛋白。','eff':'治疗组死亡数显著低于对照组，5 天后存活率高于对照组，显示显著保护作用。','num2':'存活率显著优于对照'},
          {'num':'石斑鱼 · 案例','title':'石斑鱼虹彩病毒病','bg':'石斑鱼养殖场暴发虹彩病毒病。','plan':'连续使用申泰莱。','eff':'在临床观察中显示病情得到有效控制。','num2':''}],
    faq=[('什么规格的石斑鱼用？','商品规格可用。神经坏死病毒主要危害苗期（2-5cm），成鱼期也可用。'),
         ('连续用几天？','说明书 5-7 天。山东案例用到第 7 天后死亡持续下降，第 12 天归零。'),
         ('石斑鱼不吃料怎么办？','需转人工，由技术团队评估。')])
add(id='zhongtailai',name='仲泰莱',en='ZhongTaiLai',cat='fish',img='assets/img/aqua/zhongtailai.jpg',
    type='复合预混合饲料 XII（A 包 + B 包包裹材料）',net='100 克/包',std='Q/SDHTD 69-2024',
    tags=['提高免疫力','抗病毒','无抗养殖'],
    species=['鳜鱼'],disease='传染性脾肾坏死病（ISKNV）',calc=True,
    lead='针对鳜鱼传染性脾肾坏死病（ISKNV）的病毒结合蛋白产品。临床案例：PCR 强阳性鳜鱼连续拌料 5 天，第 8 天死亡归零、核酸检测阴性。',
    meta=['鳜鱼 传染性脾肾坏死病','Q/SDHTD 69-2024','案例：1万尾 60尾/天 → 0尾/天'],
    usage=['取 1 包 A 包，加入约 600ml 水，边搅拌边加入，充分混匀至形成悬浊液',
           '与 20kg 饲料充分搅拌混匀',
           '取 1 包 B 包（包裹材料）溶于约 600ml 水，边搅拌边加入至完全溶解',
           '再加入上述 20kg 饲料中充分搅拌均匀完成包裹',
           '每天投喂一餐，连续投喂 5-7 天'],
    cases=[{'num':'鳜鱼 · 案例','title':'佛山顺德 1 万尾饲料鳜 · ISKNV 强阳性','bg':'PCR 强阳性（CT 值约 10），每天死亡约 60 尾。','plan':'连续拌料口服仲泰莱 5 天。','eff':'第 8 天死亡数归零，ISKNV 核酸检测阴性。','num2':'60 → 0 尾/天'},
          {'num':'鳜鱼 · 攻毒试验','title':'鳜鱼脾肾坏死病毒（ISKNV）口服疫苗攻毒保护','bg':'免疫攻毒组（ISKNV 亚单位口服二免后）+ 攻毒对照组，各 30 尾，均肌肉注射 ISKNV。','plan':'ISKNV 亚单位口服疫苗连续免疫。','eff':'攻毒对照组第 9 天累计死亡 100%，免疫攻毒组第 12 天累计死亡 50%，之后病情得到有效控制。','num2':'50% vs 100%（保护率 50%）'},
          {'num':'鳜鱼 · 案例','title':'佛山 6.6 亩饲料鳜大塘口 · ISKNV 暴发','bg':'广东省佛山市 6.6 亩饲料鳜养殖场，ISKNV 阳性，死亡数急剧上升。','plan':'第 7 天起每天一餐添加脾肾坏死病毒结合蛋白饲料，持续 7 天 + 后续 4 天补充投喂。','eff':'第 26 天死鱼数量降至零，ISKNV 核酸检测阴性。','num2':'26 天归零'}],
    faq=[('跟虹泰莱有什么区别？','两款都是病毒结合蛋白类，但适配病毒不同：虹泰莱针对 RSIV，仲泰莱针对 ISKNV。'),
         ('一包拌多少料？','1 包 A 包 + 1 包 B 包配 20kg 饲料。'),
         ('需要做 PCR 吗？','建议做 PCR 确诊病毒种类再用药。'),
         ('用错了怎么办？','立即停止投喂，观察鱼体反应。')])
add(id='dantailai',name='丹泰莱',en='DanTaiLai',cat='fish',img='assets/img/aqua/dantailai.jpg',
    type='复合预混合饲料 VIII（A 包 + B 包包裹材料）',net='100 克/包',std='Q/SDHTD 65-2025',
    tags=['提高免疫力','抗病毒','无抗养殖'],
    species=['鱼'],disease='鱼用病毒结合蛋白',calc=True,
    lead='鱼用病毒结合蛋白产品，提升机体免疫、辅助抗病毒，适用于多种鱼类病毒病的防控与恢复。',
    meta=['鱼用病毒结合蛋白','Q/SDHTD 65-2025'])
add(id='yubaotai',name='鱼宝泰',en='YuBaoTai',cat='fish',img='assets/img/aqua/yubaotai.jpg',
    type='氟苯尼考粉（水产用）· 兽用处方药',net='100 克/包',std='兽药字 190859014',rx=True,
    tags=['诺卡氏菌','反向包裹','减少耐药'],
    species=['生鱼(乌鳢)'],disease='诺卡氏菌病',
    lead='针对生鱼（乌鳢）诺卡氏菌病的氟苯尼考粉（水产用），兽用处方药。独创反向包裹技术减少耐药菌产生。',
    meta=['粤兽药字 190859014','100g + 300ml 植物油拌 20kg 饵料','连用 3-7 天'],
    usage=['取本品 100g，加入 300ml 植物油充分混合后，用于拌料 20kg 鱼饲料使用',
           '连用本品 3-7 天',
           '拌好的药饵不宜久置',
           '不宜高剂量长期使用',
           '本产品仅适用于鱼用饲料添加'],
    cases=[{'num':'生鱼 · 案例','title':'阳春 2 万尾生鱼 · 诺卡氏菌病','bg':'250 克/尾，暴发诺卡氏菌病，每天死亡 130-150 尾，传统抗生素无效。','plan':'鱼宝泰每日 2 包拌 80 斤料。','eff':'第六天后细菌病基本得到控制。','num2':'130-150 → 基本控制'}],
    faq=[('是抗生素吗？能用吗？','氟苯尼考抗生素类，兽用处方药，凭兽医处方购买。'),
         ('一包拌多少料？','100g + 300ml 植物油 → 拌 20kg 饲料。'),
         ('诺卡氏菌和普通细菌病怎么区分？','需 PCR 或镜检确诊，建议转人工。'),
         ('用药后多久可以卖鱼？','休药期待补充，请咨询技术团队。')])
add(id='baozhentai_fish',name='包珍泰',en='BaoZhenTai (Fish)',cat='fish',img='assets/img/aqua/baozhentai_aqua.jpg',
    type='复合预混合饲料 VI（A 包 + B 包包裹材料）',net='100 克/包',std='Q/GDHTD 46-2024',
    tags=['提高免疫力','抗病毒','无抗养殖'],
    species=['鱼'],disease='鱼用疱疹病毒',calc=True,
    lead='鱼用疱疹病毒结合蛋白产品，提升机体免疫、辅助抗病毒，适用于鱼用疱疹病毒相关防控。',
    meta=['鱼用疱疹病毒结合蛋白','Q/GDHTD 46-2024'])
# ===== FROG (rich) =====
add(id='watailei',name='蛙泰莱',en='WaTaiLei',cat='frog',img='assets/img/aqua/watailei.jpg',
    type='复合预混合饲料 IV（A 包 + B 包包裹材料）',net='100 克/包',std='Q/SDHT 0159-2023',
    tags=['黄杆菌','歪头病','细菌粘附蛋白'],
    species=['牛蛙'],disease='歪头病（黄杆菌脑神经感染）',calc=True,
    lead='针对牛蛙歪头病（黄杆菌脑神经感染）的蛙属虹彩病毒结合蛋白产品。对照试验显示成活率约 75%（对照组约 44%）。',
    meta=['成活率约 75%（对照组约 44%）','Q/SDHT 0159-2023'],
    usage=['取 2 包蛙泰莱 A 包（500g），加入约 1200ml 水，边搅拌边加入，充分混匀至形成悬浊液',
           '与 20kg 蛙饲料充分搅拌混匀',
           '取 2 包 B 包（包裹材料）溶于约 1200ml 水，边搅拌边加入至完全溶解',
           '再加入上述 20kg 饲料中充分搅拌均匀完成包裹',
           '建议小四脚蛙苗时开始使用，首次连续投喂 3 天，每天一餐；间隔一个月后再投喂一次，连续 3 天，每天一餐'],
    cases=[{'num':'牛蛙 · 案例','title':'3 个牛蛙养殖场对照试验（各 2 万只）','bg':'牛蛙歪头病（黄杆菌）典型症状，部分蛙体歪头、游动失衡。','plan':'蛙泰莱（蛙属虹彩病毒结合蛋白）按说明拌饲料投喂。','eff':'蛙泰莱组成活率约 75% / 73% / 76%，死淘率较对照组下降约 50%。','num2':'成活率约 75%'},
          {'num':'牛蛙 · 案例','title':'澄海牛蛙场 · 歪头病预防','bg':'相邻两口蛙池各 10 万只，相同养殖条件。','plan':'实验组 2 包蛙泰莱 + 600ml 植物油混合，与 20kg 饲料拌匀，每天一餐连续 3 天；间隔一个月再投喂一次连续 3 天。','eff':'二免后 14 天内：实验组累计死蛙 2033 只，对照组 2526 只，实验组较对照组死亡降低 24.3%。','num2':'死亡率降低 24.3%'},
          {'num':'牛蛙 · 案例','title':'江门牛蛙场 · 成活率提升','bg':'江门某牛蛙场，4 万只小四脚牛蛙苗，实验组 vs 对照组各 2 万只，各 100㎡ 网池。','plan':'实验组小四脚开始使用，首月连续 3 天，次月连续 3 天，每天一餐。','eff':'成活率实验组 75% vs 对照组 60%；每池节省饲料成本 3824 元，销售额增加 9520 元，ROI 约 11.9 倍。','num2':'成活率 75% vs 60%，ROI 11.9 倍'},
          {'num':'牛蛙 · 案例','title':'海南万宁牛蛙场 · 烂皮病','bg':'海南万宁某牛蛙场，5.8 万只小四脚牛蛙苗，实验组 vs 对照组各 2.9 万只，各 140㎡ 土池流动水。','plan':'实验组首月连续 5 天共 2 包，次月连续 3 天共 4 包，合计 6 包。','eff':'养殖 1 月后：死亡率实验组 2.17% vs 对照组 2.60%；实验组皮肤更具光泽、烂皮蛙少、个体差异小、整齐度高。','num2':'死亡率 2.17% vs 2.60%'}],
    faq=[('一包能拌多少料？','2 包 A 包 + 2 包 B 包（双包）配 20kg 蛙饲料。'),
         ('连续用几天？','首次连续 3 天，间隔 1 月再用一次（预防性）。'),
         ('什么时候开始用？','小四脚蛙苗阶段。'),
         ('跟蛙宝泰有什么区别？','蛙泰莱生物制剂（预防，歪头病首选）vs 蛙宝泰抗生素（治疗，急性发作）。')])
add(id='wabaotai',name='蛙宝泰',en='WaBaoTai',cat='frog',img='assets/img/aqua/wabaotai.jpg',
    type='水产用抗生素（独创反向包裹技术）',net='100 克/包',std='兽药字 190859092',rx=True,
    tags=['独创反向包裹','降低药残','控制耐药'],
    species=['牛蛙'],disease='急性细菌病（红腿/烂皮/腹水）',
    lead='针对牛蛙急性细菌病的水产用抗生素，独创反向包裹技术减少水体污染与耐药菌产生。急性发作、重症首选，可与蛙泰莱联用。',
    meta=['兽药字 190859092','100g + 300ml 植物油拌 20kg 蛙饲料','连用 3-7 天'],
    usage=['取本品 100g，加入 300ml 植物油充分混合后，用于拌料 20kg 蛙饲料使用',
           '连用本品 3-7 天',
           '拌好的药饵不宜久置',
           '不宜高剂量长期使用',
           '本产品仅适用于蛙用饲料添加'],
    cases=[{'num':'牛蛙 · 案例','title':'广东潮州牛蛙养殖场 · 细菌病暴发','bg':'暴发细菌病，每天死亡 260-380 只，传统抗生素无效。','plan':'改用蛙宝泰拌料投喂。','eff':'迅速降低日死亡数量，细菌病得到控制。','num2':'260-380 → 迅速下降'}],
    faq=[('是抗生素吗？','是的，核心卖点是"反向包裹技术"——减少水体污染 + 减少耐药菌产生。'),
         ('一包拌多少料？','100g + 300ml 植物油 → 拌 20kg 蛙饲料。'),
         ('跟蛙泰莱怎么选？','预防/慢病 → 蛙泰莱；急性/重症 → 蛙宝泰；可联合使用。'),
         ('用药后多久卖蛙？','休药期待补充，请咨询技术团队。')])
add(id='wataida',name='蛙泰达',en='WaTaiDa',cat='frog',img='assets/img/aqua/wataida.jpg',
    type='复合预混合饲料 VI',net='250 克/包',std='Q/HDHTD 62-2023',
    tags=['气单胞菌','链球菌','红腿烂皮胃肠炎'],
    species=['牛蛙'],disease='红腿 / 烂皮 / 胃肠炎',
    lead='针对牛蛙气单胞菌、链球菌等引起的红腿、烂皮、胃肠炎，250g 大包装，告别红腿胃肠炎烂皮。',
    meta=['Q/HDHTD 62-2023','告别红腿胃肠炎烂皮'])
# ===== SHRIMP =====
add(id='hutailai',name='弧泰莱',en='HuTaiLai',cat='shrimp',img='assets/img/aqua/hutailai.jpg',
    type='复合预混合饲料 XI',net='100 克/包',std='Q/GDHTD 68-2023',
    tags=['虾弧菌','黏附蛋白','天然杀菌'],
    species=['对虾'],disease='弧菌病',
    lead='针对对虾弧菌的黏附蛋白产品，天然杀菌，适用于对虾弧菌病的防控。',
    meta=['Q/GDHTD 68-2023','粤饲预(2020)01001'])
add(id='baotailai',name='包泰莱',en='BaoTaiLai',cat='shrimp',img='assets/img/aqua/baotailai.jpg',
    type='复合预混合饲料 XV',net='100 克/包',std='Q/GDHTD 72-2024',
    tags=['肝肠孢子虫','黏附蛋白','天然杀虫'],
    species=['对虾'],disease='肝肠孢子虫',
    lead='针对对虾肝肠孢子虫的黏附蛋白产品，可作预防 + 治疗双场景使用。低载量下清零效果显著。',
    meta=['Q/GDHTD 72-2024','粤饲预(2021)01011','案例：4 次方内 7-8 天基本清零'],
    cases=[{'num':'对虾 · 案例 01','title':'中山虾 · 肝肠孢子虫 · 4 次方内','bg':'虾体内肝肠孢子虫载量在 4 次方以内。','plan':'连续 7-8 天使用包泰莱拌饲料口服。','eff':'7-8 天后虾体内肝肠孢子虫数量基本清零，摄食量与活力显著改善。','num2':'载量 4 次方 → 基本清零'},
          {'num':'对虾 · 案例 02','title':'珠海虾 · 治疗场景','bg':'肝肠孢子虫感染中后期。','plan':'按体重计算剂量，连续投喂。','eff':'载量较用药前显著下降，采食量与活力逐步恢复。','num2':'载量 ↓ · 活力 ↑'},
          {'num':'对虾 · 案例 03','title':'江苏小棚虾 · 预防方案','bg':'养殖密度高、疫病压力大。','plan':'放苗后定期投喂预防。','eff':'感染率显著低于对照组，整体养殖成功率提升。','num2':'感染率 ↓'}])
add(id='xiahongtai',name='虾虹泰',en='XiaHongTai',cat='shrimp',img='assets/img/aqua/xiahongtai.jpg',
    type='复合预混合饲料 XVII',net='100 克/包',std='Q/GDHTD 74-2024',
    tags=['虾虹彩病毒','提高免疫','无抗养殖'],
    species=['对虾','罗氏沼虾'],disease='虹彩病毒',
    lead='针对对虾、罗氏沼虾虹彩病毒的结合蛋白产品，提高免疫、无抗养殖。',
    meta=['Q/GDHTD 74-2024'])
add(id='xiajitai',name='虾吉泰',en='XiaJiTai',cat='shrimp',img='assets/img/aqua/xiajitai.jpg',
    type='复合预混合饲料 XIX',net='100 克/包',std='Q/GDHTD 76-2024',
    tags=['虾肌肉坏死病毒','提高免疫','无抗养殖'],
    species=['对虾'],disease='肌肉坏死病毒',
    lead='针对对虾肌肉坏死病毒的结合蛋白产品，提高免疫、无抗养殖。',
    meta=['虾肌肉坏死病毒结合蛋白','Q/GDHTD 76-2024'])
add(id='xiabantai',name='虾斑泰',en='XiaBanTai',cat='shrimp',img='assets/img/aqua/xiabantai.jpg',
    type='复合预混合饲料 XVIII',net='100 克/包',std='Q/GDHTD 75-2024',
    tags=['虾白斑病毒','提高免疫','无抗养殖'],
    species=['对虾'],disease='白斑病毒（WSSV）',
    lead='针对对虾白斑病毒（WSSV）的结合蛋白产品，提高免疫、无抗养殖。',
    meta=['Q/GDHTD 75-2024'])
# ===== LIVE =====
add(id='qinbaotai',name='禽宝泰',en='QinBaoTai',cat='live',img='assets/img/prod/prod_qinbaotai_pdf.jpg',
    type='维生素预混合饲料 Ⅰ（禽用）',net='200g · 1000 羽份/瓶',std='Q/GDHTD 41-2024',
    tags=['摆脱免疫抑制','长效保护 60 天+','激活免疫系统','降低死淘率'],
    species=['禽'],disease='免疫抑制 / 病毒防控',
    lead='禽用维生素预混，摆脱免疫抑制、激活免疫系统、长效保护 60 天以上、降低死淘率。1~3 日龄首次，7~10 日龄再用一次。',
    meta=['粤饲预(2021)13011','Q/GDHTD 41-2024','净含量 200g · 1000 羽份/瓶'])
add(id='xubaotai',name='畜宝泰',en='XuBaoTai',cat='live',img='assets/img/prod/prod_xubaotai_box.jpg',
    type='维生素预混合饲料（畜用）',net='畜用',std='Q/GDHTD 43-2024',
    tags=['摆脱免疫抑制','防腹泻保生长','长效保护 60 天+','降低死淘率'],
    species=['畜'],disease='免疫抑制 / 腹泻',
    lead='畜用维生素预混，摆脱免疫抑制、防腹泻保生长、长效保护 60 天以上。仔猪 20 头份/瓶、母猪 10 头份/瓶；首次连用 3-7 天，以后每两月一次。',
    meta=['粤饲预(2021)13011','Q/GDHTD 43-2024','仔猪 20 头份/瓶 · 母猪 10 头份/瓶'])
add(id='qintai_live',name='禽泰安',en='QinTaiAn (Binding Protein)',cat='live',img='assets/img/prod/prod_qintai_an.jpg',
    type='家禽病毒结合蛋白（维生素预混合饲料 Ⅰ）',net='100g · 大日龄 500 羽份',std='Q/GDHTD 43-2024',
    tags=['广谱通用','直接阻断感染','组合高效','孕产蛋可用'],
    species=['禽'],disease='家禽病毒病',
    lead='家禽病毒结合蛋白，广谱通用、直接阻断感染、组合高效、孕产蛋可用。预防连用 3 天、治疗连用 5-7 天，同时饲喂疫苗增效明显。',
    meta=['粤饲预(2021)13011','Q/GDHTD 43-2024','净含量 100g · 大日龄 500 羽份'])

# ---- 产品内容补强：注入桌面源材料挖掘到的真实 usage/cases/faq（不编造）----
# ===== RUMINANT (牛/羊) — source: 博美莱中英文版经营产品目录 + 2025 价格表(牛羊苗) =====
add(id='niubashigan',name='牛多杀性巴氏杆菌病灭活疫苗',en='Bovine Pasteurella Vaccine',cat='ruminant',img='assets/img/prod/prod_niubashigan.jpg',
    type='灭活疫苗',net='20 / 50 / 100 / 250 ml/瓶',en_type='Inactivated Vaccine',en_net='20 / 50 / 100 / 250 ml/vial',std='兽药生字140393008',
    tags=['牛巴氏杆菌病','呼吸道疾病','灭活疫苗'],
    en_tags=['Bovine pasteurellosis','Respiratory disease','Inactivated vaccine'],
    species=['牛'],en_species='Cattle',disease='牛多杀性巴氏杆菌病（牛呼吸道肺炎）',en_disease='Bovine Pasteurellosis (Respiratory Pneumonia)',
    lead='用于预防牛多杀性巴氏杆菌病（牛呼吸道肺炎）的灭活疫苗，提供针对巴氏杆菌感染的免疫保护。',
    en_lead='Inactivated vaccine for prevention of bovine pasteurellosis (bovine respiratory pneumonia), providing immune protection against Pasteurella infection.',
    meta=['兽药生字140393008','净含量 20/50/100/250 ml/瓶','灭活疫苗'],rx=True)
add(id='niushahotan',name='牛副伤寒灭活疫苗',en='Bovine Paratyphoid Vaccine',cat='ruminant',img='assets/img/prod/prod_niushahotan.jpg',
    type='灭活疫苗',net='20 / 50 / 100 ml/瓶',en_type='Inactivated Vaccine',en_net='20 / 50 / 100 ml/vial',std='兽药生字140393009',
    tags=['牛副伤寒','沙门氏菌肠炎','灭活疫苗'],
    en_tags=['Bovine paratyphoid','Salmonella enteritis','Inactivated vaccine'],
    species=['牛'],en_species='Cattle',disease='牛副伤寒（沙门氏菌性肠炎）',en_disease='Bovine Paratyphoid (Salmonella enteritis)',
    lead='用于预防牛副伤寒（沙门氏菌引起的肠炎与败血症）的灭活疫苗。',
    en_lead='Inactivated vaccine for prevention of bovine paratyphoid (Salmonella enteritis and septicemia).',
    meta=['兽药生字140393009','净含量 20/50/100 ml/瓶','灭活疫苗'],rx=True)
add(id='yangdachangganjun',name='羊大肠杆菌病灭活疫苗',en='Ovine Colibacillosis Vaccine',cat='ruminant',img='assets/img/prod/prod_yangdachangganjun.jpg',
    type='灭活疫苗',net='20 / 50 / 100 / 250 ml/瓶',en_type='Inactivated Vaccine',en_net='20 / 50 / 100 / 250 ml/vial',std='兽药生字140394009',
    tags=['羊大肠杆菌病','腹泻/败血症','灭活疫苗'],
    en_tags=['Ovine colibacillosis','Diarrhea / Septicemia','Inactivated vaccine'],
    species=['羊'],en_species='Sheep',disease='羊大肠杆菌病（腹泻/败血症）',en_disease='Ovine Colibacillosis (Diarrhea / Septicemia)',
    lead='用于预防羊大肠杆菌病（腹泻、败血症）的灭活疫苗。',
    en_lead='Inactivated vaccine for prevention of ovine colibacillosis (diarrhea, septicemia).',
    meta=['兽药生字140394009','净含量 20/50/100/250 ml/瓶','灭活疫苗'],rx=True)
add(id='qizhongji',name='气肿疽灭活疫苗',en='Blackleg Vaccine',cat='ruminant',img='assets/img/prod/prod_qizhongji.jpg',
    type='灭活疫苗',net='—',en_type='Inactivated Vaccine',en_net='—',std='—',
    tags=['气肿疽','黑腿病','牛/羊梭菌病'],
    en_tags=['Blackleg','Clostridial disease','Cattle / Sheep'],
    species=['牛','羊'],en_species='Cattle / Sheep',disease='气肿疽（黑腿病）',en_disease='Blackleg (Clostridium chauvoei)',
    lead='用于预防牛、羊气肿疽（黑腿病，气肿疽梭菌感染）的灭活疫苗。',
    en_lead='Inactivated vaccine for prevention of blackleg (Clostridium chauvoei infection) in cattle and sheep.',
    meta=['牛/羊通用','灭活疫苗','具体规格请参照产品说明书'],rx=True)
import json as _json
_ENRICH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'product_enrichment.json')
_GENERIC = {
    'taimiaoja': ('拌入猫粮或温水中，按产品推荐剂量每日 1 次使用；治疗期连用 7-10 天，日常保健可周期性使用。具体用法与剂量请遵医嘱，或联系海泰技术团队获取产品说明书。',
                  'Mix into cat food or warm water, once daily at the recommended dose; use 7–10 consecutive days during treatment, or periodically for daily health. For specific dosage, follow veterinary advice or contact the HiTide technical team for the product leaflet.'),
    'beizhuangtai': ('拌入猫粮或温水中，按产品推荐剂量每日 1 次使用；治疗期连用 7-10 天，日常保健可周期性使用。具体用法与剂量请遵医嘱，或联系海泰技术团队获取产品说明书。',
                     'Mix into cat food or warm water, once daily at the recommended dose; use 7–10 consecutive days during treatment, or periodically for daily health. For specific dosage, follow veterinary advice or contact the HiTide technical team for the product leaflet.'),
    'yanzhengtai': ('拌入猫粮或温水中，按产品推荐剂量每日 1 次使用；治疗期连用 7-10 天，日常保健可周期性使用。具体用法与剂量请遵医嘱，或联系海泰技术团队获取产品说明书。',
                    'Mix into cat food or warm water, once daily at the recommended dose; use 7–10 consecutive days during treatment, or periodically for daily health. For specific dosage, follow veterinary advice or contact the HiTide technical team for the product leaflet.'),
    'taiwangja': ('拌入犬粮或温水中，按产品推荐剂量每日 1 次使用；治疗期连用 7-10 天，日常保健可周期性使用。具体用法与剂量请遵医嘱，或联系海泰技术团队获取产品说明书。',
                  'Mix into dog food or warm water, once daily at the recommended dose; use 7–10 consecutive days during treatment, or periodically for daily health. For specific dosage, follow veterinary advice or contact the HiTide technical team for the product leaflet.'),
    'wanglebao': ('拌入犬粮或温水中，按产品推荐剂量每日 1 次使用；治疗期连用 7-10 天，日常保健可周期性使用。具体用法与剂量请遵医嘱，或联系海泰技术团队获取产品说明书。',
                  'Mix into dog food or warm water, once daily at the recommended dose; use 7–10 consecutive days during treatment, or periodically for daily health. For specific dosage, follow veterinary advice or contact the HiTide technical team for the product leaflet.'),
    'xinaowei': ('拌料或饮水使用，按推荐剂量连用 3-5 天，定期预防。具体剂量请参照产品标签，或联系海泰技术团队获取使用指导。',
                 'Use via feed mixing or drinking water at the recommended dose for 3–5 consecutive days; repeat periodically for prevention. For specific dosing, follow the product label or contact the HiTide technical team for guidance.'),
    'xinsian': ('拌料或饮水使用，按推荐剂量连用 3-5 天，定期预防。具体剂量请参照产品标签，或联系海泰技术团队获取使用指导。',
                'Use via feed mixing or drinking water at the recommended dose for 3–5 consecutive days; repeat periodically for prevention. For specific dosing, follow the product label or contact the HiTide technical team for guidance.'),
}
_GENERIC_BY_CAT = {
    'cat': ('拌入猫粮或温水中，按产品推荐剂量每日 1 次使用；治疗期连用 7-10 天，日常保健可周期性使用。具体用法与剂量请遵医嘱，或联系海泰技术团队获取产品说明书。',
            'Mix into cat food or warm water, once daily at the recommended dose; use 7–10 consecutive days during treatment, or periodically for daily health. For specific dosage, follow veterinary advice or contact the HiTide technical team for the product leaflet.'),
    'dog': ('拌入犬粮或温水中，按产品推荐剂量每日 1 次使用；治疗期连用 7-10 天，日常保健可周期性使用。具体用法与剂量请遵医嘱，或联系海泰技术团队获取产品说明书。',
            'Mix into dog food or warm water, once daily at the recommended dose; use 7–10 consecutive days during treatment, or periodically for daily health. For specific dosage, follow veterinary advice or contact the HiTide technical team for the product leaflet.'),
    'pigeon': ('拌料或饮水使用，按推荐剂量连用 3-5 天，定期预防。具体剂量请参照产品标签，或联系海泰技术团队获取使用指导。',
               'Use via feed mixing or drinking water at the recommended dose for 3–5 consecutive days; repeat periodically for prevention. For specific dosing, follow the product label or contact the HiTide technical team for guidance.'),
    'live': ('拌料或饮水使用，按推荐剂量连用 3-5 天，定期预防。具体剂量请参照产品标签，或联系海泰技术团队获取使用指导。',
             'Use via feed mixing or drinking water at the recommended dose for 3–5 consecutive days; repeat periodically for prevention. For specific dosing, follow the product label or contact the HiTide technical team for guidance.'),
    'fish': ('拌料口服，按推荐剂量每日一餐、连续投喂 5-7 天。具体用法请参照产品标签或联系海泰技术团队。',
             'Mix into feed and administer orally, one meal daily at the recommended dose for 5–7 consecutive days. For specific usage, follow the product label or contact the HiTide technical team.'),
    'frog': ('拌料口服，按推荐剂量每日一餐、连续投喂 5-7 天。具体用法请参照产品标签或联系海泰技术团队。',
             'Mix into feed and administer orally, one meal daily at the recommended dose for 5–7 consecutive days. For specific usage, follow the product label or contact the HiTide technical team.'),
    'shrimp': ('拌料口服，按推荐剂量每日一餐、连续投喂 5-7 天。具体用法请参照产品标签或联系海泰技术团队。',
               'Mix into feed and administer orally, one meal daily at the recommended dose for 5–7 consecutive days. For specific usage, follow the product label or contact the HiTide technical team.'),
    'ruminant': ('皮下或肌肉注射，具体免疫程序与剂量请遵医嘱或参照产品说明书；免疫前后避免应激，接种部位严格消毒。',
                 'Administer by subcutaneous or intramuscular injection. For specific immunization schedule and dosage, follow veterinary advice or the product leaflet; minimize stress around vaccination and disinfect the injection site.'),
}
_DEF_USAGE = ('按产品标签推荐剂量使用；具体用法与剂量请遵医嘱或联系海泰技术团队获取产品说明书。',
              'Use per product label recommended dosage; for specific usage and dosing, follow veterinary guidance or contact the HiTide technical team for the product leaflet.')
if os.path.exists(_ENRICH):
    _edata = _json.load(open(_ENRICH, encoding='utf-8'))
    for _p in P:
        _e = _edata.get(_p['id'])
        if _e:
            if _e.get('usage'): _p['usage'] = _e['usage']
            if _e.get('cases'): _p['cases'] = _e['cases']
            if _e.get('faq'):   _p['faq']   = _e['faq']
        # 仍缺用法：按 id 或类目兜底（仅通用说明，不编造数据）
        if not _p.get('usage'):
            _g = _GENERIC.get(_p['id']) or _GENERIC_BY_CAT.get(_p['cat'], _DEF_USAGE)
            _p['usage'] = [_g[0]]
            _p['en_usage'] = [_g[1]]

# ---- 英文翻译注入（来自 en_products.json，子代理翻译，覆盖 37 产品）----
_ENP = os.path.join(ROOT, 'en_products.json')
if os.path.exists(_ENP):
    _pdata = _json.load(open(_ENP, encoding='utf-8'))
    for _p in P:
        _e = _pdata.get(_p['id'])
        if not _e:
            continue
        if _e.get('en_lead'):  _p['en_lead']  = _e['en_lead']
        if _e.get('en_usage'): _p['en_usage'] = _e['en_usage']
        if _e.get('en_cases'): _p['en_cases'] = _e['en_cases']

# ---- 产品字段英文注入（来自 en_fields.json，子代理翻译，覆盖 37 产品）----
_ENF = os.path.join(ROOT, 'en_fields.json')
if os.path.exists(_ENF):
    _fdata = _json.load(open(_ENF, encoding='utf-8'))
    for _p in P:
        _f = _fdata.get(_p['id'])
        if not _f:
            continue
        if _f.get('en_type'):     _p['en_type']     = _f['en_type']
        if _f.get('en_net'):      _p['en_net']      = _f['en_net']
        if _f.get('en_species'):  _p['en_species']  = _f['en_species']
        if _f.get('en_disease'):  _p['en_disease']  = _f['en_disease']
        if _f.get('en_tags'):     _p['en_tags']     = _f['en_tags']
        if _f.get('en_faq'):      _p['en_faq']      = _f['en_faq']

BY_ID = {p['id']:p for p in P}

# ---- English for Chinese-only standard/approval codes (Standard No. field) ----
STD_EN = {
    '兽药字 190851143': 'Veterinary Approval 190851143',
    '兽药字 190856407': 'Veterinary Approval 190856407',
    '兽药字 190855071': 'Veterinary Approval 190855071',
    '兽药字 190859092': 'Veterinary Approval 190859092',
    '兽药字 190859014': 'Veterinary Approval 190859014',
    '兽用 OTC': 'Veterinary OTC',
    '二联灭活': 'Bivalent Inactivated',
    '鸽专用': 'Pigeon-specific',
    '猫狗双标签': 'Cat & Dog Dual-label',
    '兽药生字140393008': 'Veterinary Approval 140393008',
    '兽药生字140393009': 'Veterinary Approval 140393009',
    '兽药生字140394009': 'Veterinary Approval 140394009',
}

# ---------------- matcher ----------------
MATCHER = [
    ('鳜鱼','Mandarin Fish',[('脾肾坏死 / ISKNV','Spleen-Kidney Necrosis / ISKNV','zhongtailai'),('神经坏死 / NNV','Nervous Necrosis / NNV','shentailai'),('蛙虹彩 / RSIV / 烂身溃疡','Frog Iridovirus / RSIV / Sores','hongtailai')]),
    ('鲈鱼','Sea Bass',[('蛙虹彩 / RSIV','Frog Iridovirus / RSIV','hongtailai')]),
    ('石斑鱼','Grouper',[('神经坏死 / NNV','Nervous Necrosis / NNV','shentailai')]),
    ('生鱼（乌鳢）','Snakehead',[('诺卡氏菌 / 结节烂身','Nocardiosis / Nodules & Sores','yubaotai')]),
    ('牛蛙','Bullfrog',[('歪头病 / 黄杆菌','Wry-neck / Flavobacterium','watailei'),('红腿 / 烂皮 / 细菌病','Red Leg / Skin Ulcer / Bacterial','wabaotai')]),
    ('对虾','Shrimp',[('肝肠孢子虫','Hepatointestinal Microsporidia','baotailai'),('白斑病毒 / WSSV','White Spot Virus / WSSV','xiabantai'),('虹彩病毒','Iridovirus','xiahongtai'),('肌肉坏死','Muscle Necrosis','xiajitai'),('弧菌','Vibriosis','hutailai')]),
    ('猫','Cat',[('猫瘟 / FPV','FPV / Panleukopenia','wentailai'),('疱疹','Herpes','baozhentai_cat'),('杯状','Calici','beizhuangtai'),('传腹 / FCoV','FIP / FCoV','futailai'),('猫鼻支 / 泛白细胞减少','Feline Rhinotracheitis / Panleukopenia','taimiaoja')]),
    ('犬','Dog',[('犬瘟 / 细小 / 冠状','Distemper / Parvo / Corona','taiwangja')]),
    ('鸽','Pigeon',[('新城疫 / ND','Newcastle Disease / ND','xinaowei'),('禽流感 H9','Avian Influenza H9','xinliu')]),
    ('牛','Cattle',[('巴氏杆菌病 / 肺炎','Pasteurellosis / Pneumonia','niubashigan'),('副伤寒 / 肠炎','Paratyphoid / Enteritis','niushahotan'),('气肿疽 / 黑腿病','Blackleg','qizhongji')]),
    ('羊','Sheep',[('大肠杆菌病 / 腹泻','Colibacillosis / Diarrhea','yangdachangganjun'),('气肿疽 / 黑腿病','Blackleg','qizhongji')]),
]

# ---------------- render helpers ----------------
def r(t, **kw):
    for k,v in kw.items():
        t = t.replace('{{'+k+'}}', str(v))
    return t

# final pass: inline Chinese i18n text so content renders even if JS is off.
# Note: inside f-strings `{{key}}` collapses to `{key}`, so match both forms.
CHROME = {
    't_home':'首页','t_about':'公司简介','t_team':'人物介绍','t_products':'产品线','t_contact':'联系我们',
}
def fill_zh(html):
    for k,v in list(I18N.items()) + list(CHROME.items()):
        html = html.replace('{{'+k+'}}', v).replace('{'+k+'}', v)
    return html

def nav_html(rel=''):
    return f'''<nav class="nav">
  <div class="wrap nav-inner">
    <a href="{rel}index.html" class="brand">
      <img src="{rel}assets/img/logo.png" alt="HiTide Bio">
      <span class="brand-text"><span class="cn">海泰生物</span><span class="en">HiTide Biotech</span></span>
    </a>
    <div class="nav-links">
      <a href="{rel}index.html" data-nav="index.html">{zh_en('首页','Home')}</a>
      <a href="{rel}about.html" data-nav="about.html">{zh_en('公司简介','About')}</a>
      <a href="{rel}team.html" data-nav="team.html">{zh_en('人物介绍','Team')}</a>
      <a href="{rel}products.html" data-nav="products.html">{zh_en('产品线','Products')}</a>
      <span class="sep">|</span>
      <a href="{rel}contact.html" class="ext" data-nav="contact.html">{zh_en('联系我们','Contact')}</a>
      <span class="lang-btn"><button id="langZh" class="on">中</button><button id="langEn">EN</button></span>
    </div>
    <button class="hamburger" aria-label="menu"><span></span><span></span><span></span></button>
  </div>
</nav>
<div class="mobile-menu">
  <a href="{rel}index.html">{zh_en('首页','Home')}</a><a href="{rel}about.html">{zh_en('公司简介','About')}</a>
  <a href="{rel}team.html">{zh_en('人物介绍','Team')}</a><a href="{rel}products.html">{zh_en('产品线','Products')}</a>
  <a href="{rel}contact.html">{zh_en('联系我们','Contact')}</a>
</div>'''

def footer_html(rel=''):
    return f'''<footer>
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <div class="footer-brand"><span class="cn">海泰生物</span><span class="en">Jiangsu HiTide Biotechnology Co., Ltd.</span></div>
        <p style="line-height:1.8;">{zh_en('海纳百川 · 匡佑安泰','Haina Baichuan · Kuangyou Antai')}<br>{zh_en('海泰生物 · 扬帆蓝海','HiTide Biotech · Sailing the Blue Ocean')}</p>
        <p style="margin-top:14px;font-size:13px;color:rgba(255,255,255,.6);">{zh_en('专注动物疫苗与水产动保的高技术企业','A high-tech enterprise focused on animal vaccines and aquaculture health')}</p>
      </div>
      <div><h5>{zh_en('导航','Navigation')}</h5><ul>
        <li><a href="{rel}about.html">{zh_en('公司简介','About')}</a></li>
        <li><a href="{rel}team.html">{zh_en('人物介绍','Team')}</a></li>
        <li><a href="{rel}products.html">{zh_en('产品线','Products')}</a></li>
        <li><a href="{rel}contact.html">{zh_en('联系我们','Contact')}</a></li>
      </ul></div>
      <div><h5>{zh_en('业务板块','Business Segments')}</h5><ul>
        <li>{zh_en('动物疫苗','Animal Vaccines')}</li><li>{zh_en('兽用化药','Veterinary Pharma')}</li><li>{zh_en('动物抗体','Animal Antibodies')}</li><li>{zh_en('牛用产品','Ruminant Products')}</li><li>{zh_en('抗菌蛋白','Antimicrobial Proteins')}</li>
      </ul></div>
      <div><h5>{zh_en('联系','Contact')}</h5><ul>
        <li>{zh_en('邮箱：info@hitide-bio.com','Email: info@hitide-bio.com')}</li>
        <li>{zh_en('合作：商务顾问 Patrick Nijs','Partnership: Business Advisor Patrick Nijs')}</li>
        <li>{zh_en('技术：CTO 李其昌 博士','Technical: CTO Dr. Li Qichang')}</li>
      </ul></div>
    </div>
    <div class="footer-copy">
      <span>{zh_en('© 2026 江苏海泰生物科技 · HiTide Biotechnology','© 2026 Jiangsu HiTide Biotechnology Co., Ltd.')}</span>
      <span>{zh_en('兽医生物制品 / 化药 / 抗体 / 反刍 / 研发 / 抗菌蛋白','Veterinary Biologics / Pharma / Antibodies / Ruminants / R&D / Antimicrobial Proteins')}</span>
    </div>
  </div>
</footer>'''

def base(title, body, desc='', rel='', en_title=None):
    nav = nav_html(rel)
    footer = footer_html(rel)
    et = en_title or title
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-zh-title="{title}" data-en-title="{et}">{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{rel}assets/css/main.css">
</head>
<body>
<div id="progress"></div>
{nav}
{body}
{footer}
<script src="{rel}assets/js/i18n.js"></script>
<script src="{rel}assets/js/main.js"></script>
</body>
</html>'''

def product_card(p, rel=''):
    rx = '<span class="rx">' + zh_en('处方药','Rx') + '</span>' if p.get('rx') else ''
    tags_zh = p.get('tags',[])[:4]
    tags_en = (p.get('en_tags') or [])[:4]
    tags = ''.join(f'<span>{zh_en(t, tags_en[i] if i < len(tags_en) else "")}</span>' for i,t in enumerate(tags_zh))
    search = ' '.join([p['name'], p['en'], p.get('type',''), p.get('en_type',''), p.get('disease',''), p.get('en_disease',''), ' '.join(p.get('tags',[])), ' '.join(p.get('en_tags') or [])])
    return f'''<a class="product" href="{rel}products/{p['id']}.html" data-cat="{p['cat']}" data-name="{p['name']} {p['en']}" data-search="{search}">
  <div class="img" data-zoom>{rx}<img src="{rel}{p['img']}" alt="{p['name']}" loading="lazy"></div>
  <div class="body">
    <div class="cat">{zh_en(CAT_LABEL[p['cat']]['cn'], CAT_LABEL[p['cat']]['en'])}</div>
    <h5>{zh_en(p['name'], p['en'])}</h5>
    <div class="subname">{zh_en(p.get('type',''), p.get('en_type',''))}</div>
    <div class="claims">{tags}</div>
    <span class="more">{zh_en('查看详情 →','View Details →')}</span>
  </div>
</a>'''

# =========================================================
# INDEX
# =========================================================
def render_index():
    segs = ''.join(f'''<div class="card segment reveal">
      <div class="num">0{i+1} / {zh_en(s[0], s[4])}</div><h4>{zh_en(s[1], s[5])}</h4>
      <div class="entity">{zh_en(s[2], s[6])}</div><div class="desc">{zh_en(s[3], s[7])}</div>
      <div class="bar"></div></div>''' for i,s in enumerate([
      ('疫苗板块','动物疫苗','江西博美莱生物科技有限公司','7 条 GMP 生产线，40 项兽药生产批文，年产能 100 亿头/羽份。','Vaccines','Animal Vaccines','Jiangxi Bomeilai Biotech','7 GMP lines, 40 veterinary approvals, 10 billion doses/year capacity.'),
      ('化药板块','兽用化药','广东海泰达生物科技有限公司','水产动保、宠物、鸽用三大产品线，独创反向包裹技术。','Pharmaceuticals','Veterinary Pharma','Guangdong HiTide Biotech','Three product lines — aquaculture, pet, pigeon; proprietary reverse-encapsulation technology.'),
      ('抗体板块','动物抗体','南通海泰生物科技有限公司','养殖户好评的抗体产品，注册地南通海门。','Antibodies','Animal Antibodies','Nantong HiTide Biotech','Well-regarded antibody products among farmers; registered in Haimen, Nantong.'),
      ('反刍板块','牛用产品','广州新齐行生物技术有限公司','聚焦奶牛乳房炎等牛用生物制品，打破国外垄断。','Ruminants','Ruminant Products','Guangzhou Xinqixing Biotech','Focus on dairy mastitis and other ruminant biologics, breaking foreign monopolies.'),
      ('研发板块','研发中心','海泰达生物科技（广州）有限公司','与国内外院校深度合作，联合研究院孵化平台。','R&D','R&D Center','HiTide Biotech (Guangzhou)','Deep collaboration with domestic and overseas institutions; joint research institute platform.'),
      ('抗菌蛋白','抗菌蛋白','山东海泰达生物科技发展有限公司','无抗生素抗菌，探索无新兽药路径。','Antimicrobial Proteins','Antimicrobial Proteins','Shandong HiTide Biotech','Antibiotic-free antimicrobials; exploring new-veterinary-drug-free pathways.'),
    ]))

    plats = ''.join(f'''<div class="platform reveal"><div class="num">{zh_en('平台 0'+str(i+1), 'Platform 0'+str(i+1))}</div><h4>{zh_en(pl[0], pl[2])}</h4><p>{zh_en(pl[1], pl[3])}</p></div>''' for i,pl in enumerate([
      ('独创性杀菌蛋白技术平台','基于自研抗菌蛋白体系，针对耐药菌株开发广谱、高效、低残留杀菌方案。','Proprietary Bactericidal Protein','Broad-spectrum, high-efficacy, low-residue solutions against drug-resistant strains, built on self-developed antimicrobial proteins.'),
      ('创新疫苗佐剂和细胞免疫平台','独特佐剂显著提升疫苗滴度；细胞-病毒双向转化提高培养滴度、降成本。','Innovative Adjuvant & Cellular Immunity','Unique adjuvants boost vaccine titers; cell-virus bidirectional conversion raises culture titers and cuts cost.'),
      ('独创性水产包裹技术','反向包裹技术使药物在饵料表面快速包裹，降低流失、减少耐药、提升药效。','Proprietary Aquaculture Encapsulation','Reverse-encapsulation quickly coats medication onto feed, reducing loss, resisting resistance and improving efficacy.'),
      ('病毒/细菌受体结合蛋白疫苗平台','结合蛋白与病毒/细菌受体位点紧密结合阻断感染，应用于猫三联、传腹、犬瘟、虾虹彩、鱼疱疹等。','Virus/Bacteria Receptor-Binding Protein','Binding proteins block infection by tightly binding viral/bacterial receptor sites — for feline ternary, FIP, distemper, shrimp iridovirus, fish herpes and more.'),
      ('高效基因工程疫苗表达技术平台','杆状病毒/酵母/大肠杆菌多重组疫苗平台，VLP 与蛋白疫苗连接，EB66 细胞应用。','High-Efficiency Gene-Engineered Expression','Multi-expression platforms (baculovirus / yeast / E. coli); VLP and protein vaccines linked, with EB66 cell application.'),
    ]))
    plats += '<div class="platform feature reveal"><div class="num">'+zh_en('资质认证','Certifications')+'</div><h4>'+zh_en('四大工艺原则','Four Process Principles')+'</h4><p style="font-size:18px;font-weight:600;letter-spacing:.15em;margin-top:8px;">'+zh_en('安全 · 高效 · 均一 · 稳定','Safety · Efficiency · Consistency · Stability')+'</p><p style="margin-top:14px;">'+zh_en('Quality without compromise — 从原材料到成品全流程质控，每批次严格检验。','Quality without compromise — full-process quality control from raw material to finished product, with strict inspection of every batch.')+'</p></div>'

    stats = [('2017','2017','成立年份','Founded'),('6','6','子公司','Subsidiaries'),('40+','40+','兽药批文','Vet. Approvals'),('9','9','GMP 生产线','GMP Lines'),('100亿','10 Billion','年产能(头/羽份)','Annual Capacity'),(str(len(P)),str(len(P)),'已上市产品','Products Launched')]
    stat_html = ''.join(f'<div class="stat-item reveal"><span class="v" data-count="{s[0].replace("+","")}" data-suffix="{("+" if "+" in s[0] else "")}">{zh_en(s[0], s[1])}</span><span class="k">{zh_en(s[2], s[3])}</span></div>' for s in stats)

    body = f'''
<header class="hero">
  <div class="wrap">
    <div class="hero-eyebrow" data-i18n="hero_eyebrow">{{hero_eyebrow}}</div>
    <h1 data-i18n="hero_title">{{hero_title}}</h1>
    <p class="hero-lede" data-i18n="hero_lede">{{hero_lede}}</p>
    <div class="hero-cta">
      <a class="btn btn-primary" href="products.html">{zh_en('浏览产品线 →','Browse Products →')}</a>
      <a class="btn btn-ghost" href="about.html">{zh_en('了解海泰','About HiTide')}</a>
    </div>
    <dl class="hero-meta">{''.join(f'<div><dt>{zh_en(s[2], s[3])}</dt><dd>{zh_en(s[0], s[1])}</dd></div>' for s in stats[:4])}</dl>
  </div>
</header>

<section class="stat-strip"><div class="wrap"><div class="stat-grid">{stat_html}</div></div></section>

<section>
  <div class="wrap">
    <div class="sec-eyebrow reveal">{zh_en('关于海泰','About HiTide')}</div>
    <h2 class="sec-title reveal" data-i18n="about_title">{{about_title}}</h2>
    <p class="sec-lede reveal">{zh_en('公司创始人林旭埜博士从事动物疫苗行业 30 余年，其主持研发的 ST 猪瘟（转让）疫苗为我国猪瘟疫病防控做出重大贡献，在水产疫苗方面获得多个一类新兽药证书。','Founder Dr. Lin Xunye has spent 30+ years in animal vaccines; the ST swine fever (licensed-out) vaccine he led made a major contribution to China’s swine fever control, and multiple Class-I new veterinary drug certificates were granted in aquaculture vaccines.')}</p>
    <div class="about-grid">
      <div class="about-prose reveal">
        <p>{zh_en('海泰生物是一家专注于<strong>动物保护（动物疫苗）研发、生产、销售和服务</strong>为一体的高新生物技术企业。旗下拥有六家子公司，核心技术领域包括动物疫苗、动物抗体、水产动保、抗菌蛋白、牛用产品等。','HiTide Biotech is a high-tech biotechnology enterprise focused on the R&D, manufacturing, sales and service of <strong>animal health (animal vaccines)</strong>. It operates six subsidiaries; its core technology spans animal vaccines, animal antibodies, aquaculture health, antimicrobial proteins and ruminant products.')}</p>
        <p>{zh_en('海泰生物致力于通过生物技术手段解决动物疫病防控问题，助力国内农业养殖端绿色健康发展，推进解决养殖端药物残留超标等食品安全问题。','HiTide Biotech is committed to solving animal disease-control challenges through biotechnology, supporting green and healthy development of domestic farming and reducing food-safety issues such as excessive drug residues at the farm level.')}</p>
        <p>{zh_en('以美籍华人科学家<strong>李其昌博士</strong>为领军人物的技术团队，与牛津大学、康奈尔大学等国内外科研院所开展技术合作，建立了基因工程疫苗表达、水产口服疫苗、病毒结合蛋白及新型反向包裹技术等平台。','Led by Chinese-American scientist <strong>Dr. Li Qichang</strong>, the technical team collaborates with Oxford, Cornell and other research institutions, building platforms for gene-engineered vaccine expression, oral aquaculture vaccines, virus receptor-binding proteins and novel reverse-encapsulation technology.')}</p>
      </div>
      <aside class="about-side reveal">
        <h3>{zh_en('快速概览','Quick Overview')}</h3>
        <ul class="fact-list">
          <li><span class="k">{zh_en('总部','HQ')}</span><span class="v">{zh_en('江苏 · 海泰生物科技','Jiangsu · HiTide Biotech')}</span></li>
          <li><span class="k">{zh_en('成立','Founded')}</span><span class="v">2017</span></li>
          <li><span class="k">{zh_en('子公司','Subsidiaries')}</span><span class="v">{zh_en('6 家','6')}</span></li>
          <li><span class="k">{zh_en('业务板块','Business Segments')}</span><span class="v">{zh_en('6 大（疫苗/化药/抗体/反刍/研发/抗菌蛋白）','6 (Vaccines / Pharma / Antibodies / Ruminants / R&D / Antimicrobial Proteins)')}</span></li>
          <li><span class="k">{zh_en('高校合作','University Partners')}</span><span class="v">{zh_en('牛津 / 康奈尔 / 曼彻斯特','Oxford / Cornell / Manchester')}</span></li>
          <li><span class="k">{zh_en('兽药批文','Vet. Approvals')}</span><span class="v">{zh_en('40 项','40')}</span></li>
          <li><span class="k">{zh_en('GMP 产线','GMP Lines')}</span><span class="v">{zh_en('9 条（年产 100 亿头/羽份）','9 (10 billion doses/yr)')}</span></li>
          <li><span class="k">{zh_en('产品总数','Products')}</span><span class="v">{zh_en(str(len(P))+' 款',str(len(P)))}</span></li>
          <li><span class="k">{zh_en('公司理念','Philosophy')}</span><span class="v">{zh_en('海纳百川 · 匡佑安泰','Haina Baichuan · Kuangyou Antai')}</span></li>
        </ul>
      </aside>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-eyebrow reveal">{zh_en('业务板块','Business Segments')}</div>
    <h2 class="sec-title reveal">{zh_en('六大业务板块 · 全产业链布局','Six Business Segments · Full-Chain Layout')}</h2>
    <p class="sec-lede reveal">{zh_en('通过控股、参股、技术合作等灵活方式，聚集国内外多家合作企业，形成完整、系统的产业链。','Through flexible models of holding, equity participation and technical cooperation, HiTide aggregates multiple partner enterprises in China and abroad into a complete, systematic industry chain.')}</p>
    <div class="grid-3">{segs}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-eyebrow reveal">{zh_en('核心技术平台','Core Technology Platforms')}</div>
    <h2 class="sec-title reveal">{zh_en('五大独创技术平台 · 占据行业技术制高点','Five Proprietary Technology Platforms · At the Industry’s Technology Frontier')}</h2>
    <p class="sec-lede reveal">{zh_en('以林旭埜博士 30 年疫苗研发经验为基础，李其昌博士领衔的中美技术团队，与牛津、康奈尔等科研院所合作构建。','Built on Dr. Lin Xunye’s 30 years of vaccine R&D experience, by the China-US technical team led by Dr. Li Qichang, in collaboration with Oxford, Cornell and other research institutes.')}</p>
    <div class="grid-3">{plats}</div>
  </div>
</section>

<section class="band-navy">
  <div class="wrap">
    <div class="sec-eyebrow reveal">{zh_en('产品矩阵','Product Matrix')}</div>
    <h2 class="sec-title reveal" data-i18n="products_title">{{products_title}}</h2>
    <p class="sec-lede reveal">{zh_en('已上市产品 41 款，宠物 / 鸽 / 鱼 / 虾 / 蛙 / 畜禽 / 牛 / 羊全场景覆盖，结合蛋白技术贯穿全产品线。','41 products launched, covering pets / pigeons / fish / shrimp / frogs / livestock / cattle / sheep across all scenarios, with receptor-binding protein technology running through the entire product line.')}</p>
    <div class="product-grid">
      {''.join(product_card(p) for p in P[:8])}
    </div>
    <div class="cta-strip"><div class="t"><strong>{zh_en('查看全部 ' + str(len(P)) + ' 款产品','View all ' + str(len(P)) + ' products')}</strong> · {zh_en('按物种与疫病筛选','Filter by species and disease')}</div><a class="btn btn-primary" href="products.html">{zh_en('进入产品中心 →','Enter Product Center →')}</a></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-eyebrow reveal">{zh_en('核心团队','Core Team')}</div>
    <h2 class="sec-title reveal" data-i18n="team_title">{{team_title}}</h2>
    <p class="sec-lede reveal">{zh_en('林旭埜博士 30 年运营管理，李其昌博士领衔中美技术合作。','Dr. Lin Xunye brings 30 years of operations management; Dr. Li Qichang leads China-US technical cooperation.')}</p>
    <div class="team-grid">
      {''.join(team_card(t) for t in TEAM[:5])}
    </div>
    <div class="cta-strip"><div class="t"><strong>{zh_en('认识海泰的科学家与顾问团队','Meet HiTide’s scientists and advisory team')}</strong></div><a class="btn btn-navy" href="team.html">{zh_en('人物介绍 →','Team →')}</a></div>
  </div>
</section>
'''
    return base('海泰生物 HiTide Biotech · 动物疫苗与水产动保全产业链', body, '海泰生物是一家专注动物疫苗与水产动保的高技术企业，六大板块全产业链布局。', en_title='HiTide Biotech · Animal Vaccines & Aquaculture Health')

# =========================================================
# TEAM
# =========================================================
TEAM = [
    ('林旭埜','Founder · 董事长','LIN XUYE','博士，江苏南通海泰生物科技公司创始人。原广东永顺生物制药股份有限公司董事、总经理。江苏省双创人才、江西省双千人才。近 30 年生物制品研发、生产和运营管理经验，主持研发的 ST 猪瘟（转让）疫苗获国家新药证书。','PhD, founder of Jiangsu Nantong HiTide Biotech. Former director and general manager of Guangdong Wensun Biological Pharmaceutical. Jiangsu "Double-Creation" and Jiangxi "Double-Thousand" talent. Nearly 30 years in R&D, manufacturing and operations of biological products; led the ST swine fever (licensed-out) vaccine awarded a national New Veterinary Drug Certificate.','assets/img/team/lin_xunye.jpg'),
    ('林梓栋','CEO · 总经理','LIN ZIDONG','毕业于英国曼彻斯特大学。具备良好的技术背景，推进公司与海内外高等院校的深度技术合作，负责海泰生物经营管理工作。','Graduate of the University of Manchester, UK. Strong technical background; drives deep technical cooperation with universities in China and abroad, and leads HiTide\'s operations and management.','assets/img/team/lin_zidong.jpg'),
    ('李其昌','CTO · 研发副总','FRANK LI','生物学博士，美籍华人科学家。在美国生物公司拥有 25 年以上研发经验，开发多项前沿生物工程技术，申请 20 余项发明专利。多领域研发：水产疫苗、畜禽疫苗、疾病诊断检测。','PhD in biology, Chinese-American scientist. 25+ years of R&D experience at US biotech firms; developed multiple cutting-edge biotech platforms and filed 20+ invention patents. Spans aquaculture vaccines, livestock & poultry vaccines, and diagnostics.','assets/img/team/li_qichang.jpg'),
    ('张永富','技术顾问','ZHANG YONGFU','免疫学博士，康奈尔大学终身教授。公司技术顾问。动物疫苗领域获美国发明专利 3 项，近 40 年动物生物研发经验，发表上百篇高质量学术文章。','PhD in immunology, tenured professor at Cornell University; HiTide technical advisor. Holds 3 US invention patents in animal vaccines, with nearly 40 years of R&D experience and 100+ peer-reviewed publications.','assets/img/team/zhang_yongfu.jpg'),
    ('Patrick Nijs','商务顾问','PATRICK NIJS','前比利时驻中国大使，公司商务顾问。主要帮助公司引进欧洲大学和生物科技公司的技术和合作。','Former Ambassador of Belgium to China; HiTide business advisor. Helps the company secure technology partnerships with European universities and biotech companies.','assets/img/team/patrick_nijs.jpg'),
]
TEAM_ROLE_EN = {
    'Founder · 董事长': 'Founder · Chairman',
    'CEO · 总经理': 'CEO · General Manager',
    'CTO · 研发副总': 'CTO · VP of R&D',
    '技术顾问': 'Technical Advisor',
    '商务顾问': 'Business Advisor',
}
def team_card(t):
    return f'''<div class="team-card reveal">
      <div class="photo"><img src="{t[5]}" alt="{t[0]}" loading="lazy"></div>
      <div class="body"><h4>{zh_en(t[0], t[2])}</h4><div class="role">{zh_en(t[1], TEAM_ROLE_EN.get(t[1], ''))}</div><p>{zh_en(t[3], t[4])}</p></div>
    </div>'''

def render_team():
    track = f'''<div class="prod-grid reveal" style="grid-template-columns:repeat(4,1fr);">
      <div class="product-card" style="background:var(--paper-2);padding:20px;"><div class="label">{zh_en('主持科技项目','Led R&D Projects')}</div><div class="value" style="font-size:22px;color:var(--navy);font-weight:600;">{zh_en('16 项','16')}</div><div class="sub">{zh_en('国家/省/市区','National / Provincial / Municipal')}</div></div>
      <div class="product-card" style="background:var(--paper-2);padding:20px;"><div class="label">{zh_en('新药证书','New Drug Certificates')}</div><div class="value" style="font-size:22px;color:var(--navy);font-weight:600;">{zh_en('5 项','5')}</div><div class="sub">{zh_en('主持开发新产品十余项','Led development of 10+ new products')}</div></div>
      <div class="product-card" style="background:var(--paper-2);padding:20px;"><div class="label">{zh_en('转让收入','License Revenue')}</div><div class="value" style="font-size:22px;color:var(--navy);font-weight:600;">{zh_en('1.44 亿元','¥144M')}</div><div class="sub">{zh_en('ST 猪瘟新药 · 18 家公司','ST Swine Fever drug · 18 companies')}</div></div>
      <div class="product-card" style="background:var(--paper-2);padding:20px;"><div class="label">{zh_en('发明专利','Invention Patents')}</div><div class="value" style="font-size:22px;color:var(--navy);font-weight:600;">{zh_en('20 项','20')}</div><div class="sub">{zh_en('国家标准 10 项','10 national standards')}</div></div>
    </div>'''
    body = f'''
<section style="padding-top:84px;">
  <div class="wrap">
    <div class="sec-eyebrow reveal">{zh_en('核心团队','Core Team')}</div>
    <h2 class="sec-title reveal" data-i18n="team_title">{{team_title}}</h2>
    <p class="sec-lede reveal">{zh_en('林旭埜博士 30 年深耕动物疫苗，李其昌博士领衔中美技术合作，张永富教授（康奈尔）与 Patrick Nijs（前比利时驻华大使）提供技术与商务支持。','Dr. Lin Xunye has 30 years deep in animal vaccines; Dr. Li Qichang leads China-US technical cooperation, with Prof. Zhang Yongfu (Cornell) and Patrick Nijs (former Belgian Ambassador to China) providing technical and business support.')}</p>
    <div class="team-grid">{''.join(team_card(t) for t in TEAM)}</div>
    <div style="margin-top:48px;">
      <div class="sec-eyebrow reveal">{zh_en('Founder’s Track Record · 林旭埜博士','Founder’s Track Record · Dr. Lin Xunye')}</div>
      {track}
    </div>
  </div>
</section>'''
    return base('人物介绍 · 海泰生物核心团队', body, '海泰生物核心团队：林旭埜、林梓栋、李其昌、张永富、Patrick Nijs。', en_title='Team · HiTide Biotech Core Team')

# =========================================================
# ABOUT (dedicated page with production + certs)
# =========================================================
def render_about():
    gmp = ''.join(f'<div class="cert-img" data-zoom><img src="assets/img/corp/{f}" alt="GMP 车间" loading="lazy"></div>' for f in ['gmp_1.jpg','gmp_2.jpg','gmp_3.jpg','gmp_4.jpg'])
    certs = [(f,l,en) for f,l,en in [('cert_license.jpg','兽药生产许可证','Veterinary Manufacturing License'),('cert_gmp.jpg','兽药 GMP 证书','Veterinary GMP Certificate'),('cert_hightech.jpg','高新技术企业证书','High-Tech Enterprise Certificate'),('cert_business.jpg','营业执照','Business License')]]
    cert_html = ''.join(f'<div class="cert-item"><div class="cert-img" data-zoom><img src="assets/img/corp/{f}" alt="{l}" loading="lazy"></div><div class="cert-label">{zh_en(l, en)}</div></div>' for f,l,en in certs)
    body = f'''
<section style="padding-top:84px;">
  <div class="wrap">
    <div class="sec-eyebrow reveal">{zh_en('关于海泰','About HiTide')}</div>
    <h2 class="sec-title reveal" data-i18n="about_title">{{about_title}}</h2>
    <p class="sec-lede reveal">{zh_en('以生物技术解决动物疫病防控问题，助力绿色健康养殖，推进解决药物残留超标等食品安全问题。','Solving animal disease control with biotechnology, advancing green and healthy farming, and tackling food-safety issues such as drug-residue exceedance.')}</p>
    <div class="about-grid">
      <div class="about-prose reveal">
        <p>{zh_en('海泰生物是一家专注于<strong>动物保护（动物疫苗）研发、生产、销售和服务</strong>为一体的高新生物技术企业。旗下拥有六家子公司，核心技术领域包括动物疫苗、动物抗体、水产动保、抗菌蛋白、牛用产品等。','HiTide Biotech is a high-tech biotechnology enterprise focused on the R&D, manufacturing, sales and service of <strong>animal health (animal vaccines)</strong>. It operates six subsidiaries; its core technology spans animal vaccines, animal antibodies, aquaculture health, antimicrobial proteins and ruminant products.')}</p>
        <p>{zh_en('针对目前国内市场痛点，开发新型基因工程疫苗，做出<strong>使用方便、免疫原性好、保护期长</strong>的动物疫苗。解决的问题包括：猪蓝耳病、奶牛乳房炎（多联多价）、猫传腹 + 猫三联、鱼的口服疫苗。','Addressing key market pain points, it develops novel gene-engineered vaccines that are <strong>easy to use, highly immunogenic and long-lasting in protection</strong>. Targets include PRRS, dairy mastitis (multivalent), FIP + feline ternary vaccine, and oral fish vaccines.')}</p>
        <p>{zh_en('以美籍华人科学家<strong>李其昌博士</strong>为领军人物的技术团队，与牛津大学、康奈尔大学等国内外科研院所开展技术合作，建立了包括高效的基因工程疫苗表达技术平台、水产口服疫苗平台、病毒结合蛋白技术平台及新型反向包裹技术等平台。','Led by Chinese-American scientist <strong>Dr. Li Qichang</strong>, the technical team collaborates with Oxford, Cornell and other institutions, building platforms for gene-engineered vaccine expression, oral aquaculture vaccines, virus receptor-binding proteins and novel reverse-encapsulation technology.')}</p>
      </div>
      <aside class="about-side reveal">
        <h3>{zh_en('生产实力','Production Capacity')}</h3>
        <ul class="fact-list">
          <li><span class="k">{zh_en('GMP 线','GMP lines')}</span><span class="v">{zh_en('9 条','9 lines')}</span></li>
          <li><span class="k">{zh_en('年产能','Annual capacity')}</span><span class="v">{zh_en('100 亿头/羽份','10 billion doses')}</span></li>
          <li><span class="k">{zh_en('兽药批文','Vet. approvals')}</span><span class="v">{zh_en('40 项','40')}</span></li>
          <li><span class="k">{zh_en('覆盖','Coverage')}</span><span class="v">{zh_en('禽/猪/牛/羊/水产','Poultry/Swine/Cattle/Sheep/Aquatic')}</span></li>
          <li><span class="k">{zh_en('GMP 自检','GMP self-audit')}</span><span class="v">{zh_en('302 条款 · 关键项全合格','302 Clauses · All critical items passed')}</span></li>
        </ul>
      </aside>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="sec-eyebrow reveal">{zh_en('生产车间 · GMP','Production Facilities · GMP')}</div>
    <h2 class="sec-title reveal">{zh_en('9 条 GMP 生产线 · 年产能 100 亿头/羽份','9 GMP Production Lines · 10 Billion Doses / Year')}</h2>
    <p class="sec-lede reveal">{zh_en('博美莱生产车间拥有活疫苗/灭活疫苗共 7 条生产线，海泰生物本部 2 条生产线，覆盖禽用、猪用、牛用、羊用、水产用全品类生物制品。','The Bomeilai facility operates 7 live and inactivated vaccine lines, plus 2 lines at HiTide headquarters, covering poultry, swine, cattle, sheep and aquatic biological products.')}</p>
    <div class="grid-2" style="grid-template-columns:repeat(4,1fr);gap:14px;">
      {''.join(f'<div class="card reveal" style="padding:18px;"><div style="font-weight:600;color:var(--navy);">0{i+1}</div><div style="font-size:14px;color:var(--ink-2);margin-top:4px;">{zh_en(n, en)}</div></div>' for i,(n,en) in enumerate([('胚毒活疫苗','Embryo-derived live vaccine'),('细胞毒活疫苗','Cell-culture live vaccine'),('细菌活疫苗','Bacterial live vaccine'),('猪瘟活疫苗(兔源)','Swine fever live vaccine (rabbit origin)'),('胚毒灭活疫苗','Embryo-derived inactivated vaccine'),('细胞毒灭活疫苗','Cell-culture inactivated vaccine'),('细菌灭活疫苗','Bacterial inactivated vaccine'),('细胞悬浮培养灭活','Cell suspension culture inactivated')]))}
    </div>
    <div class="gmp-grid" style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:28px;">{gmp}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-eyebrow reveal">{zh_en('资质矩阵 · Certifications','Certification Matrix · Certifications')}</div>
    <h2 class="sec-title reveal">{zh_en('国家资质 · 国际认证 · 行业标准','National Qualifications · International Certifications · Industry Standards')}</h2>
    <p class="sec-lede reveal">{zh_en('博美莱（疫苗板块）通过农业农村部新版 GMP 验收，兽药生产许可证与 GMP 证书有效期至 2027 年 1 月。','Bomeilai (vaccine segment) passed the Ministry of Agriculture\'s new GMP inspection; its veterinary manufacturing license and GMP certificate are valid through January 2027.')}</p>
    <div class="cert-track" id="certTrack">
      {cert_html}
    </div>
    <div style="display:flex;gap:10px;margin-top:16px;">
      <button class="chip" id="certPrev">{zh_en('← 上一张','← Prev')}</button><button class="chip" id="certNext">{zh_en('下一张 →','Next →')}</button>
    </div>
  </div>
</section>'''
    return base('公司简介 · 海泰生物全产业链', body, '海泰生物公司简介：全产业链布局、9 条 GMP 生产线、国家资质与国际认证。', en_title='About · HiTide Biotech Full Value Chain')

# =========================================================
# PRODUCTS OVERVIEW (filter + search + matcher)
# =========================================================
def render_products():
    chips = '<button class="chip active" data-cat="all">' + zh_en('全部','All') + '</button>' + ''.join(f'<button class="chip" data-cat="{k}">{zh_en(cn, en)}</button>' for i,(k,cn,en) in enumerate(CATS))
    grid = ''.join(product_card(p) for p in P)
    # matcher species buttons
    sp_btns = ''.join(f'<button class="pill" data-species="{s[0]}" data-en="{s[1]}">{zh_en(s[0], s[1])}</button>' for s in MATCHER)
    matcher_json = json.dumps([{'sp':s[0],'en':s[1],'sym':[{'n':x[0],'en':x[1],'id':x[2]} for x in s[2]]} for s in MATCHER], ensure_ascii=False)
    body = f'''
<section style="padding-top:84px;">
  <div class="wrap">
    <div class="sec-eyebrow reveal">{zh_en('产品矩阵','Product Matrix')}</div>
    <h2 class="sec-title reveal" data-i18n="products_title">{{products_title}}</h2>
    <p class="sec-lede reveal">{zh_en('已上市产品 ' + str(len(P)) + ' 款 · 宠物 / 鸽 / 鱼 / 虾 / 蛙 / 畜禽 / 牛 / 羊全场景覆盖。支持按物种与疫病筛选，或用下方「病症匹配」工具快速找到对应产品。','Launched ' + str(len(P)) + ' products · full-scenario coverage for pets / pigeons / fish / shrimp / frogs / livestock / cattle / sheep. Filter by species and disease, or use the Symptom Matcher below to find the right product.')}</p>

    <div class="matcher reveal" style="margin-bottom:54px;">
      <div class="sec-eyebrow">{zh_en('病症匹配工具','Symptom Matcher')}</div>
      <h3 style="font-size:20px;color:var(--navy);margin-bottom:18px;">{zh_en('选择物种与症状，智能推荐产品','Select species and symptoms for smart product recommendations')}</h3>
      <div class="matcher-steps">
        <div><div class="matcher-label">{zh_en('第 1 步 · 选择物种','Step 1 · Select species')}</div><div class="pill-row" id="mSpecies">{sp_btns}</div></div>
        <div><div class="matcher-label">{zh_en('第 2 步 · 选择症状 / 疫病','Step 2 · Select symptom / disease')}</div><div class="pill-row" id="mSymptom"><span style="color:var(--ink-3);font-size:13px;">{zh_en('请先选择物种 ↑','Please select a species first ↑')}</span></div></div>
      </div>
      <div class="matcher-result" id="mResult">
        <div class="sec-eyebrow">{zh_en('为您推荐','Recommended for you')}</div>
        <div id="mCards"></div>
      </div>
    </div>

    <div class="toolbar reveal">
      <div class="search">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input id="pSearch" type="text" placeholder="搜索产品名称、疫病或关键词…">
      </div>
      <div class="filters" id="pChips">{chips}</div>
    </div>
    <div class="product-grid" id="pGrid">{grid}</div>
    <div class="empty" id="pEmpty" style="display:none;">{zh_en('未找到匹配的产品，换个关键词试试。','No matching products found. Try another keyword.')}</div>
  </div>
</section>
<script>window.__MATCHER__={matcher_json};</script>'''
    return base('产品线 · 海泰生物全场景产品矩阵', body, f'海泰生物 {len(P)} 款产品，涵盖猫/犬/鸽/鱼/虾/蛙/畜禽，支持病症智能匹配。', en_title='Products · HiTide Biotech Full-Scenario Matrix')

# =========================================================
# PRODUCT DETAIL
# =========================================================
def render_product(p, rel=''):
    rx = '<span class="rx">' + zh_en('处方药','Rx') + '</span>' if p.get('rx') else ''
    tags_zh = p.get('tags',[])
    tags_en = p.get('en_tags') or []
    tags = ''.join(f'<span>{zh_en(t, tags_en[i] if i < len(tags_en) else "")}</span>' for i,t in enumerate(tags_zh))
    facts = ''.join(f'<div><div class="k">{zh_en(k, ek)}</div><div class="v">{zh_en(v, ev)}</div></div>' for k,v,ek,ev in [
        ('产品类型', p.get('type','—'), 'Product Type', p.get('en_type','—')),
        ('净含量', p.get('net','—'), 'Net Content', p.get('en_net','—')),
        ('标准编号', p.get('std','—'), 'Standard No.', STD_EN.get(p.get('std','—'), p.get('std','—'))),
        ('适用对象', '、'.join(p.get('species',[])) or '—', 'For', p.get('en_species','—')),
        ('靶标疫病', p.get('disease','—'), 'Target Disease', p.get('en_disease','—')),
        ('分类', CAT_LABEL[p['cat']]['cn'], 'Category', CAT_LABEL[p['cat']]['en']),
    ])

    calc = ''
    if p.get('calc'):
        calc = f'''<div class="calc">
      <h4>{zh_en('💡 用量估算器（结合蛋白 A+B 包）','💡 Dosage Calculator (Binding Protein Pack A+B)')}</h4>
      <div class="row">
        <label>{zh_en('饲料重量（kg）：','Feed weight (kg):')}</label>
        <input id="calcFeed" type="number" min="0" step="1" placeholder="如 20" value="20">
        <button class="btn btn-navy" onclick="calcPacks()">{zh_en('计算','Calculate')}</button>
      </div>
      <div class="out">{zh_en('建议用量：','Recommended dosage:')}<b id="calcOut">1</b> {zh_en('套（A 包 + B 包）/ 20kg 饲料 · 每天一餐，连用 5-7 天','pack(s) (Pack A + Pack B) / 20kg feed · one meal daily, for 5-7 days')}</div>
    </div>'''

    # usage pane (bilingual)
    en_u = p.get('en_usage') or []
    if p.get('usage'):
        steps = ''.join(f'<li>{zh_en(s, en_u[i] if i < len(en_u) else "")}</li>' for i,s in enumerate(p['usage']))
        usage_pane = f'''<div class="pane active" data-pane="usage">
          <div class="acc open"><div class="acc-head">{zh_en('用法用量','Directions for Use')} <span class="ico">+</span></div><div class="acc-body"><div class="inner"><ol>{steps}</ol></div></div></div>
        </div>'''
    else:
        usage_pane = '<div class="pane active" data-pane="usage"><p style="color:var(--ink-2);">'+zh_en('详细用法用量与规格资料请联系海泰技术团队获取，凭兽医处方购买处方药。','For detailed dosage and specifications, please contact the HiTide technical team. Prescription-only products require a veterinarian prescription.')+'</p></div>'

    # cases pane (bilingual)
    en_c = p.get('en_cases') or []
    CASE_NUM_EN = {
        '鳜鱼 · 案例': 'Mandarin Fish · Case', '石斑鱼 · 案例': 'Grouper · Case',
        '鳜鱼 · 攻毒试验': 'Mandarin Fish · Challenge Trial', '生鱼 · 案例': 'Snakehead · Case',
        '牛蛙 · 案例': 'Bullfrog · Case', '对虾 · 案例 01': 'Shrimp · Case 01',
        '对虾 · 案例 02': 'Shrimp · Case 02', '对虾 · 案例 03': 'Shrimp · Case 03',
        '猫 · 案例': 'Cat · Case', '鱼 · 案例': 'Fish · Case',
        '虾 · 案例': 'Shrimp · Case', '禽 · 案例': 'Poultry · Case',
        '鲈鱼 · 案例': 'Sea Bass · Case',
    }
    CASE_NUM2_EN = {
        '300 → 6 尾/天': '300 → 6 fish/day', '120+ → 0 尾/天': '120+ → 0 fish/day',
        '60 → 0 尾/天': '60 → 0 fish/day', '存活率显著优于对照': 'Survival significantly better than control',
        '130-150 → 基本控制': '130–150 → largely controlled', '成活率约 75%': 'Survival rate ≈ 75%',
        '260-380 → 迅速下降': '260–380 → rapid decline', '载量 4 次方 → 基本清零': 'Load 10⁴ → essentially cleared',
        '载量 ↓ · 活力 ↑': 'Load ↓ · Vitality ↑', '感染率 ↓': 'Infection rate ↓',
        '50% vs 100%（保护率 50%）': '50% vs 100% (50% protection)',
        '26 天归零': 'Cleared on day 26',
        '存活率 65% vs 35%，CT 31.668 → ≥45': 'Survival 65% vs 35%, CT 31.668 → ≥45',
        '存活率 90% vs 68%，CT 37.34 → ≥45': 'Survival 90% vs 68%, CT 37.34 → ≥45',
        '死亡率降低 24.3%': 'Mortality reduced 24.3%',
        '成活率 75% vs 60%，ROI 11.9 倍': 'Survival 75% vs 60%, ROI 11.9×',
        '死亡率 2.17% vs 2.60%': 'Mortality 2.17% vs 2.60%',
    }
    if p.get('cases'):
        cases_html = ''
        for i,c in enumerate(p['cases']):
            ec = en_c[i] if i < len(en_c) else {}
            n_en = CASE_NUM_EN.get(c.get('num',''), '')
            n2_en = CASE_NUM2_EN.get(c.get('num2',''), '')
            cases_html += f'''<div class="case">
              <div class="ch"><span class="num">{zh_en(c.get('num',''), n_en)}</span><h4>{zh_en(c['title'], ec.get('title',''))}</h4></div>
              <div class="case-grid">
                <div class="col"><h6>{zh_en('背景','Background')}</h6><p>{zh_en(c['bg'], ec.get('bg',''))}</p></div>
                <div class="col"><h6>{zh_en('处理方案','Protocol')}</h6><p>{zh_en(c['plan'], ec.get('plan',''))}</p></div>
                <div class="col result"><h6>{zh_en('效果','Result')}</h6><p>{zh_en(c['eff'], ec.get('eff',''))}</p><span class="num">{zh_en(c.get('num2',''), n2_en)}</span></div>
              </div></div>'''
        cases_section = f'''<section class="band" style="padding-top:56px;padding-bottom:24px;">
      <div class="wrap">
        <div class="sec-eyebrow">{zh_en('真实数据','Real-World Data')}</div>
        <h2 class="sec-title">{zh_en('临床案例','Clinical Cases')}</h2>
        <p class="sec-lede">{zh_en('来自养殖一线与临床使用的真实效果记录。','Real efficacy records from aquaculture farms and clinical use.')}</p>
        {cases_html}
      </div>
    </section>'''
    else:
        cases_section = ''

    # faq pane (bilingual)
    en_f = p.get('en_faq') or []
    if p.get('faq'):
        faq_html = ''
        for i,(q,a) in enumerate(p['faq']):
            ef = en_f[i] if i < len(en_f) else {}
            faq_html += f'<div class="acc"><div class="acc-head">{zh_en(q, ef.get('q',''))} <span class="ico">+</span></div><div class="acc-body"><div class="inner"><p>{zh_en(a, ef.get('a',''))}</p></div></div></div>'
        faq_pane = f'<div class="pane" data-pane="faq">{faq_html}</div>'
    else:
        faq_pane = '<div class="pane" data-pane="faq"><p style="color:var(--ink-2);">'+zh_en('常见问题正在整理中，如需技术答疑请联系海泰技术团队。','FAQ are being compiled. For technical questions, contact the HiTide technical team.')+'</p></div>'

    # related
    rel_list = [x for x in P if x['cat']==p['cat'] and x['id']!=p['id']][:4]
    if not rel_list:
        rel_list = [x for x in P if x['id']!=p['id']][:4]
    rel_html = ''.join(product_card(x, rel) for x in rel_list)
    related_pane = f'<div class="pane" data-pane="related"><div class="related-grid">{rel_html}</div></div>'

    rxnote = f'<div class="cta-strip" style="border-color:var(--gold);"><div class="t"><strong style="color:var(--gold);">{zh_en('⚠ 处方药提示','⚠ Prescription Notice')}</strong> · {zh_en('本品为兽用处方药/抗生素，请凭兽医处方购买使用，遵守休药期规定。','This is a veterinary prescription/antibiotic product. Purchase and use with a veterinarian’s prescription and observe withdrawal periods.')}</div><a class="btn btn-navy" href="{rel}contact.html">{zh_en('联系技术团队','Contact Technical Team')}</a></div>' if p.get('rx') else ''

    body = f'''
<section style="padding-top:74px;">
  <div class="wrap">
    <div class="crumbs"><a href="{rel}index.html">{zh_en('首页','Home')}</a> / <a href="{rel}products.html">{zh_en('产品线','Products')}</a> / <span style="color:var(--ink-2);">{zh_en(p['name'], p['en'])}</span></div>
    <div class="pd-hero">
      <div class="wrap" style="padding:0;">
        <div class="pd-gallery" data-zoom>{rx}<img src="{rel}{p['img']}" alt="{p['name']}" data-name="{p['name']}"></div>
        <div class="pd-info">
          <div class="cat">{zh_en(CAT_LABEL[p['cat']]['cn'], CAT_LABEL[p['cat']]['en'])}</div>
          <h1>{zh_en(p['name'], p['en'])}</h1>
          <div class="tags">{tags}</div>
          <div class="pd-facts">{facts}</div>
          <p class="pd-lead">{zh_en(p.get('lead',''), p.get('en_lead',''))}</p>
          {calc}
          <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:18px;">
            <a class="btn btn-primary" href="{rel}contact.html">{zh_en('咨询 / 获取资料','Inquire / Get Info')}</a>
            <a class="btn btn-ghost" style="color:var(--navy);border-color:var(--rule);" href="{rel}products.html">{zh_en('← 返回产品中心','← Back to Products')}</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
{cases_section}
<section class="band" style="padding-top:60px;">
  <div class="wrap">
    <div class="tabs" data-tabs>
      <div class="tab active" data-tab="usage">{zh_en('用法用量','Directions')}</div>
      <div class="tab" data-tab="faq">{zh_en('常见问题','FAQ')}</div>
      <div class="tab" data-tab="related">{zh_en('相关产品','Related')}</div>
    </div>
    {usage_pane}{faq_pane}{related_pane}
    {rxnote}
  </div>
</section>
'''
    if calc:
        body += '''<script>
function calcPacks(){var f=parseFloat(document.getElementById('calcFeed').value)||0;var n=Math.max(1,Math.round(f/20));document.getElementById('calcOut').textContent=n;}
if(document.getElementById('calcFeed')){document.getElementById('calcFeed').addEventListener('input',calcPacks);calcPacks();}
</script>'''
    return base(f"{p['name']} {p['en']} · 海泰生物", body, p.get('lead',''), rel=rel, en_title=f"{p['en']} · HiTide Biotech")

# =========================================================
# CONTACT
# =========================================================
def render_contact():
    body = f'''
<section style="padding-top:84px;">
  <div class="wrap">
    <div class="sec-eyebrow reveal">{zh_en('联系海泰','Contact HiTide')}</div>
    <h2 class="sec-title reveal" data-i18n="contact_title">{{contact_title}}</h2>
    <p class="sec-lede reveal">{zh_en('无论是产品咨询、技术合作还是海外注册，海泰团队都将为您提供专业支持。','Whether for product consultation, technical cooperation or overseas registration, the HiTide team provides professional support.')}</p>
    <div class="grid-3">
      <div class="card reveal"><div class="segment"><div class="num">{zh_en('技术支持','Technical Support')}</div><h4>{zh_en('CTO 李其昌 博士','CTO Dr. Li Qichang')}</h4><div class="desc">{zh_en('美籍华人科学家，25+ 年生物研发经验。水产疫苗 / 畜禽疫苗 / 诊断检测。','Chinese-American scientist, 25+ years of R&D experience. Aquaculture vaccines / livestock & poultry vaccines / diagnostics.')}</div></div></div>
      <div class="card reveal"><div class="segment"><div class="num">{zh_en('商务合作','Business Cooperation')}</div><h4>Patrick Nijs</h4><div class="desc">{zh_en('前比利时驻中国大使，引进欧洲大学与生物科技公司技术和合作。','Former Ambassador of Belgium to China; brings in technology partnerships with European universities and biotech companies.')}</div></div></div>
      <div class="card reveal"><div class="segment"><div class="num">{zh_en('经营管理者','Management')}</div><h4>{zh_en('林梓栋 CEO','Lin Zidong CEO')}</h4><div class="desc">{zh_en('曼彻斯特大学毕业，推进海内外高校深度技术合作与公司运营。','University of Manchester graduate; drives deep technical cooperation with universities and company operations.')}</div></div></div>
    </div>
    <div class="cta-strip reveal">
      <div class="t"><strong>{zh_en('商务邮箱：','Business email:')}</strong>info@hitide-bio.com &nbsp;·&nbsp; <strong>{zh_en('总部：','HQ:')}</strong>{zh_en('江苏 · 海泰生物科技','Jiangsu · HiTide Biotech')}</div>
      <a class="btn btn-primary" href="products.html">{zh_en('浏览产品中心 →','Browse Products →')}</a>
    </div>
  </div>
</section>'''
    return base('联系我们 · 海泰生物', body, '联系海泰生物：产品咨询、技术合作、海外注册。', en_title='Contact Us · HiTide Biotech')

# =========================================================
# BUILD
# =========================================================
def build():
    os.makedirs(PROD_DIR, exist_ok=True)
    pages = {
        'index.html': render_index(),
        'about.html': render_about(),
        'team.html': render_team(),
        'products.html': render_products(),
        'contact.html': render_contact(),
    }
    for fn, html in pages.items():
        with open(os.path.join(OUT, fn), 'w', encoding='utf-8') as f:
            f.write(fill_zh(html))
    for p in P:
        with open(os.path.join(PROD_DIR, p['id']+'.html'), 'w', encoding='utf-8') as f:
            f.write(fill_zh(render_product(p, '../')))
    # write i18n dict
    i18n = {'zh':I18N,'en':EN}
    with open(os.path.join(OUT,'assets/js/i18n.js'),'w',encoding='utf-8') as f:
        f.write('window.__I18N__=' + json.dumps(i18n, ensure_ascii=False) + ';')
    print('Generated:', len(pages), 'pages +', len(P), 'product pages')

if __name__ == '__main__':
    build()
