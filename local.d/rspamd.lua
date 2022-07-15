local cnf = config['regexp']

cnf['FROM_MUNGAI'] = {
    re = 'From=/.*MUNGAI KIHANYA TRAINING.*/i{header}',
    score = 2.5,
}

local re_body_cryptobot = '/.*(crypto|auto|trader|new)bot.*/i{mime}'
local re_body_tariff = '/.*tariff.*/i{mime}'
cnf['BODY_CRYPTOBOT'] = {
    re = string.format('(%s) && (%s)', re_body_cryptobot, re_body_tariff),
    score = 1.0,
}
