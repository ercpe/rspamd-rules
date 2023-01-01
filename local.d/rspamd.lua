local cnf = config['regexp']

cnf['FROM_MUNGAI'] = {
    re = 'From=/.*MUNGAI KIHANYA TRAINING.*/i{header}',
    score = 2.5,
}

local re_body_cryptobot = '/.*(crypto|auto|trader|new)bot.*/i{mime}'
local re_subject_cryptobot = 'Subject=/.*(crypto|auto|trader|new)bot.*/i{header}'
local re_body_tariff = '/.*tariff.*/i{mime}'
local re_body_initial_deposit = '/.*initial deposit.*/i{mime}'
cnf['BODY_CRYPTOBOT'] = {
    re = string.format('((%s) || (%s)) && ((%s) || (%s))', re_body_cryptobot, re_subject_cryptobot, re_body_tariff, re_body_initial_deposit),
    score = 1.0,
}
cnf['BODY_CRYPTOBOT_LAX'] = {
    re = string.format('((%s) || (%s))', re_body_cryptobot, re_subject_cryptobot),
    score = 1.0,
}

cnf['RECEIVED_BITCOIN'] = {
    re = 'Subject=/.*0\\.7495.*(Bitcoin|BTC).*/i{header}',
    score = 1.0,
}
