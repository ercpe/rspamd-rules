local cnf = config['regexp']

cnf['FROM_MUNGAI'] = {
    re = 'From=/.*MUNGAI KIHANYA TRAINING.*/i{header}',
    score = 2.5,
}

cnf['SUBJECT_CRYPTOBOT'] = {
    re = 'Subject=/.*(crypto|auto|trader|new)bot.*/i{header}',
    score = 1.0,
}

cnf['BODY_CRYPTOBOT'] = {
    re = '/.*(crypto|auto|trader|new)bot.*/i{mime}',
    score = 1.0,
}

cnf['RECEIVED_BITCOIN'] = {
    re = 'Subject=/.*0.7495.*(Bitcoin|BTC).*/i{header}',
    score = 1.0,
}

cnf['FROM_COINBASE'] = {
    re = 'From=/.*coinbase.*/i{header}',
    score = 1.0,
}

cnf['BODY_COINBASE'] = {
    re = '/.*coinbase.*/i{mime}',
    score = 1.0,
}

cnf['SUBJECT_TESLA'] = {
    re = 'Subject=/.*tesla.*/i{header}',
    score = 0.5,
}

cnf['BODY_BITCOIN'] = {
    re = '/.*bitcoin.*/i{mime}',
    score = 1.0,
}

cnf['BODY_GOOGLE_DRIVE_LINK'] = {
    re = '/.*https:\\/\\/drive\\.google\\.com\\/file\\/.*/i{mime}',
    score = 1.0,
}
