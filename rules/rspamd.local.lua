local cnf = config['regexp']

cnf['FROM_MUNGAI'] = {
    re = 'From=/.*MUNGAI KIHANYA TRAINING.*/i{header}',
    score = 2.5,
}

-- local kinetic1 = 'From=/KINETIC (ENTERPRISES|TECHNOLOGIEZ)/i{header}'
-- local kinetic2 = 'From=/\\s+KINETIC TECH/i{header}'
--
-- cnf['KINETIC_SCREAMING'] = {
--     re = string.format('((%s) || (%s)) && (SUBJ_ALL_CAPS)', kinetic1, kinetic2),
--     score = 2.5
-- }
