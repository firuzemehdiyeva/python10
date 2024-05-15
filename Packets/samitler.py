def samitleri_al(cumlə):
    samitler = 'bcçdfgğhjklmnprsştvyz'
    return {hərif for hərif in cumlə.lower() if hərif in samitler}
