"""
List of all current symbols `KRAKEN_SYMBOLS` and pairs `KRAKEN_PAIRS` on the Kraken Broker.
Data as of: 14/10/2024, Berlin, Germany.
"""


KRAKEN_SYMBOLS = [
    '1INCH',
	'AAVE',
	'ACA',
	'ACH',
	'ADA',
	'ADA.S',
	'ADX',
	'AED',
	'AED.HOLD',
	'AEVO',
	'AGLD',
	'AIR',
	'AKT',
	'ALCX',
	'ALGO',
	'ALGO.S',
	'ALICE',
	'ALPHA',
	'ALT',
	'ANKR',
	'ANT',
	'APE',
	'API3',
	'APT',
	'ARB',
	'ARKM',
	'ARPA',
	'ASTR',
	'ATLAS',
	'ATOM',
	'ATOM.S',
	'ATOM21.S',
	'AUCTION',
	'AUD',
	'AUD.HOLD',
	'AUDIO',
	'AVAX',
	'AVT',
	'AXS',
	'BADGER',
	'BAL',
	'BAND',
	'BAT',
	'BCH',
	'BEAM',
	'BICO',
	'BIGTIME',
	'BIT',
	'BLUR',
	'BLZ',
	'BNC',
	'BNT',
	'BOBA',
	'BODEN',
	'BOND',
	'BONK',
	'BRICK',
	'BSX',
	'BTC',
	'BTT',
	'C98',
	'CAD',
	'CAD.HOLD',
	'CELR',
	'CFG',
	'CHF',
	'CHF.HOLD',
	'CHR',
	'CHZ',
	'CLOUD',
	'COMP',
	'COTI',
	'CPOOL',
	'CQT',
	'CRV',
	'CSM',
	'CTSI',
	'CVC',
	'CVX',
	'CXT',
	'DAI',
	'DASH',
	'DENT',
	'DOGE',
	'DOT',
	'DOT.P',
	'DOT.S',
	'DOT28.S',
	'DRIFT',
	'DYDX',
	'DYM',
	'EGLD',
	'EIGEN',
	'ENA',
	'ENJ',
	'ENS',
	'EOS',
	'ETC',
	'ETH',
	'ETH2',
	'ETH2.S',
	'ETHFI',
	'ETHW',
	'EUL',
	'EUR',
	'EUR.HOLD',
	'EUR.M',
	'EURT',
	'EWT',
	'FARM',
	'FET',
	'FIDA',
	'FIL',
	'FIS',
	'FLOKI',
	'FLOW',
	'FLOW.S',
	'FLOW14.S',
	'FLOWH',
	'FLOWH.S',
	'FLR',
	'FLR.S',
	'FORTH',
	'FTM',
	'FXS',
	'GAL',
	'GALA',
	'GARI',
	'GBP',
	'GBP.HOLD',
	'GENS',
	'GFI',
	'GHST',
	'GLMR',
	'GMT',
	'GMX',
	'GNO',
	'GRT',
	'GRT.S',
	'GRT28.S',
	'GST',
	'GTC',
	'HDX',
	'HFT',
	'HNT',
	'HONEY',
	'ICP',
	'ICX',
	'IDEX',
	'IMX',
	'INJ',
	'INTR',
	'JASMY',
	'JPY',
	'JTO',
	'JUNO',
	'JUP',
	'KAR',
	'KAVA',
	'KAVA.S',
	'KAVA21.S',
	'KEEP',
	'KEY',
	'KILT',
	'KIN',
	'KINT',
	'KMNO',
	'KNC',
	'KP3R',
	'KSM',
	'KSM.P',
	'KSM.S',
	'KSM07.S',
	'KUJI',
	'L3',
	'LCX',
	'LDO',
	'LINK',
	'LIT',
	'LMWR',
	'LPT',
	'LRC',
	'LSK',
	'LTC',
	'LUNA',
	'LUNA.S',
	'LUNA2',
	'MANA',
	'MASK',
	'MATIC',
	'MATIC.S',
	'MATIC04.S',
	'MC',
	'MEME',
	'MEW',
	'MINA',
	'MINA.S',
	'MIR',
	'MKR',
	'MLN',
	'MNGO',
	'MNT',
	'MOG',
	'MOON',
	'MOVR',
	'MPL',
	'MSOL',
	'MULTI',
	'MV',
	'MXC',
	'NANO',
	'NEAR',
	'NMR',
	'NODL',
	'NOS',
	'NTRN',
	'NYM',
	'OCEAN',
	'OGN',
	'OMG',
	'ONDO',
	'OP',
	'ORCA',
	'OSMO',
	'OTP',
	'OXT',
	'OXY',
	'PARA',
	'PAXG',
	'PDA',
	'PENDLE',
	'PEPE',
	'PERP',
	'PHA',
	'PICA',
	'POL',
	'POLIS',
	'POLS',
	'POND',
	'POPCAT',
	'PORTAL',
	'POWR',
	'PRCL',
	'PRIME',
	'PSTAKE',
	'PUFFER',
	'PYTH',
	'PYUSD',
	'QNT',
	'QTUM',
	'RAD',
	'RARE',
	'RARI',
	'RAY',
	'RBC',
	'REN',
	'RENDER',
	'REP',
	'REPV2',
	'REQ',
	'REZ',
	'RLC',
	'ROOK',
	'RPL',
	'RUNE',
	'SAFE',
	'SAGA',
	'SAMO',
	'SAND',
	'SBR',
	'SC',
	'SCRT',
	'SCRT.S',
	'SCRT21.S',
	'SDN',
	'SEI',
	'SGB',
	'SHIB',
	'SKY',
	'SNX',
	'SOL',
	'SOL.S',
	'SOL03.S',
	'SPELL',
	'SRM',
	'STEP',
	'STG',
	'STORJ',
	'STRD',
	'STRK',
	'STX',
	'SUI',
	'SUPER',
	'SUSHI',
	'SXP',
	'SYN',
	'T',
	'TAO',
	'TBTC',
	'TEER',
	'TIA',
	'TLM',
	'TNSR',
	'TOKE',
	'TON',
	'TRAC',
	'TREMP',
	'TRIBE',
	'TRU',
	'TRX',
	'TRX.S',
	'TURBO',
	'TUSD',
	'TVK',
	'UMA',
	'UNFI',
	'UNI',
	'USD',
	'USD.HOLD',
	'USD.M',
	'USDC',
	'USDC.M',
	'USDS',
	'USDT',
	'USDT.M',
	'UST',
	'W',
	'WAVES',
	'WAXL',
	'WBTC',
	'WEN',
	'WETH',
	'WIF',
	'WOO',
	'XBT.M',
	'XCN',
	'XLM',
	'XMR',
	'XRP',
	'XRT',
	'XTZ',
	'XTZ.S',
	'YFI',
	'YGG',
	'ZEC',
	'ZETA',
	'ZEUS',
	'ZEX',
	'ZK',
	'ZRO',
	'ZRX',
]

KRAKEN_PAIRS = [
	'1INCH/EUR',
	'1INCH/USD',
	'AAVE/BTC',
	'AAVE/ETH',
	'AAVE/EUR',
	'AAVE/GBP',
	'AAVE/USD',
	'ACA/EUR',
	'ACA/USD',
	'ACH/EUR',
	'ACH/USD',
	'ADA/AUD',
	'ADA/BTC',
	'ADA/ETH',
	'ADA/EUR',
	'ADA/GBP',
	'ADA/USD',
	'ADA/USDT',
	'ADX/EUR',
	'ADX/USD',
	'AEVO/EUR',
	'AEVO/USD',
	'AGLD/EUR',
	'AGLD/USD',
	'AIR/EUR',
	'AIR/USD',
	'AKT/EUR',
	'AKT/USD',
	'ALCX/EUR',
	'ALCX/USD',
	'ALGO/BTC',
	'ALGO/ETH',
	'ALGO/EUR',
	'ALGO/GBP',
	'ALGO/USD',
	'ALGO/USDT',
	'ALICE/EUR',
	'ALICE/USD',
	'ALPHA/EUR',
	'ALPHA/USD',
	'ALT/EUR',
	'ALT/USD',
	'ANKR/BTC',
	'ANKR/EUR',
	'ANKR/USD',
	'APE/EUR',
	'APE/USD',
	'APE/USDT',
	'API3/EUR',
	'API3/USD',
	'APT/EUR',
	'APT/USD',
	'ARB/EUR',
	'ARB/USD',
	'ARKM/EUR',
	'ARKM/USD',
	'ARPA/EUR',
	'ARPA/USD',
	'ASTR/EUR',
	'ASTR/USD',
	'ATLAS/EUR',
	'ATLAS/USD',
	'ATOM/BTC',
	'ATOM/ETH',
	'ATOM/EUR',
	'ATOM/GBP',
	'ATOM/USD',
	'ATOM/USDT',
	'AUCTION/EUR',
	'AUCTION/USD',
	'AUD/JPY',
	'AUD/USD',
	'AUDIO/EUR',
	'AUDIO/USD',
	'AVAX/EUR',
	'AVAX/USD',
	'AVAX/USDT',
	'AXS/EUR',
	'AXS/USD',
	'BADGER/EUR',
	'BADGER/USD',
	'BAL/BTC',
	'BAL/EUR',
	'BAL/USD',
	'BAND/EUR',
	'BAND/USD',
	'BAT/BTC',
	'BAT/ETH',
	'BAT/EUR',
	'BAT/USD',
	'BCH/AUD',
	'BCH/BTC',
	'BCH/ETH',
	'BCH/EUR',
	'BCH/GBP',
	'BCH/JPY',
	'BCH/USD',
	'BCH/USDT',
	'BEAM/EUR',
	'BEAM/USD',
	'BICO/EUR',
	'BICO/USD',
	'BIGTIME/EUR',
	'BIGTIME/USD',
	'BIT/EUR',
	'BIT/USD',
	'BLUR/EUR',
	'BLUR/USD',
	'BLZ/EUR',
	'BLZ/USD',
	'BNC/EUR',
	'BNC/USD',
	'BNT/EUR',
	'BNT/USD',
	'BOBA/EUR',
	'BOBA/USD',
	'BODEN/EUR',
	'BODEN/USD',
	'BOND/EUR',
	'BOND/USD',
	'BONK/EUR',
	'BONK/USD',
	'BRICK/EUR',
	'BRICK/USD',
	'BSX/EUR',
	'BSX/USD',
	'BTC/AUD',
	'BTC/CAD',
	'BTC/CHF',
	'BTC/DAI',
	'BTC/EUR',
	'BTC/GBP',
	'BTC/JPY',
	'BTC/PYUSD',
	'BTC/USD',
	'BTC/USDC',
	'BTC/USDT',
	'BTT/EUR',
	'BTT/USD',
	'C98/EUR',
	'C98/USD',
	'CELR/EUR',
	'CELR/USD',
	'CFG/EUR',
	'CFG/USD',
	'CHR/EUR',
	'CHR/USD',
	'CHZ/EUR',
	'CHZ/USD',
	'CLOUD/EUR',
	'CLOUD/USD',
	'COMP/BTC',
	'COMP/EUR',
	'COMP/USD',
	'COTI/EUR',
	'COTI/USD',
	'CPOOL/EUR',
	'CPOOL/USD',
	'CQT/EUR',
	'CQT/USD',
	'CRV/BTC',
	'CRV/EUR',
	'CRV/USD',
	'CSM/EUR',
	'CSM/USD',
	'CTSI/EUR',
	'CTSI/USD',
	'CVC/EUR',
	'CVC/USD',
	'CVX/EUR',
	'CVX/USD',
	'CXT/EUR',
	'CXT/USD',
	'DAI/EUR',
	'DAI/USD',
	'DAI/USDT',
	'DASH/BTC',
	'DASH/EUR',
	'DASH/USD',
	'DENT/EUR',
	'DENT/USD',
	'DOGE/AUD',
	'DOGE/BTC',
	'DOGE/EUR',
	'DOGE/GBP',
	'DOGE/USD',
	'DOGE/USDT',
	'DOT/BTC',
	'DOT/ETH',
	'DOT/EUR',
	'DOT/GBP',
	'DOT/JPY',
	'DOT/USD',
	'DOT/USDT',
	'DRIFT/EUR',
	'DRIFT/USD',
	'DYDX/EUR',
	'DYDX/USD',
	'DYM/EUR',
	'DYM/USD',
	'EGLD/EUR',
	'EGLD/USD',
	'EIGEN/EUR',
	'EIGEN/USD',
	'ENA/EUR',
	'ENA/USD',
	'ENJ/BTC',
	'ENJ/EUR',
	'ENJ/GBP',
	'ENJ/JPY',
	'ENJ/USD',
	'ENS/EUR',
	'ENS/USD',
	'EOS/BTC',
	'EOS/ETH',
	'EOS/EUR',
	'EOS/USD',
	'EOS/USDT',
	'ETC/BTC',
	'ETC/ETH',
	'ETC/EUR',
	'ETC/USD',
	'ETH/AUD',
	'ETH/BTC',
	'ETH/CAD',
	'ETH/CHF',
	'ETH/DAI',
	'ETH/EUR',
	'ETH/GBP',
	'ETH/JPY',
	'ETH/PYUSD',
	'ETH/USD',
	'ETH/USDC',
	'ETH/USDT',
	'ETHFI/EUR',
	'ETHFI/USD',
	'ETHW/ETH',
	'ETHW/EUR',
	'ETHW/USD',
	'EUL/EUR',
	'EUL/USD',
	'EUR/AUD',
	'EUR/CAD',
	'EUR/CHF',
	'EUR/GBP',
	'EUR/JPY',
	'EUR/USD',
	'EURT/EUR',
	'EURT/USD',
	'EURT/USDT',
	'EWT/BTC',
	'EWT/EUR',
	'EWT/GBP',
	'EWT/USD',
	'FARM/EUR',
	'FARM/USD',
	'FET/EUR',
	'FET/USD',
	'FIDA/EUR',
	'FIDA/USD',
	'FIL/BTC',
	'FIL/ETH',
	'FIL/EUR',
	'FIL/GBP',
	'FIL/USD',
	'FIS/EUR',
	'FIS/USD',
	'FLOKI/EUR',
	'FLOKI/USD',
	'FLOW/BTC',
	'FLOW/ETH',
	'FLOW/EUR',
	'FLOW/USD',
	'FLR/EUR',
	'FLR/USD',
	'FORTH/EUR',
	'FORTH/USD',
	'FTM/EUR',
	'FTM/USD',
	'FXS/EUR',
	'FXS/USD',
	'GAL/EUR',
	'GAL/USD',
	'GALA/EUR',
	'GALA/USD',
	'GARI/EUR',
	'GARI/USD',
	'GBP/USD',
	'GFI/EUR',
	'GFI/USD',
	'GHST/BTC',
	'GHST/EUR',
	'GHST/USD',
	'GLMR/EUR',
	'GLMR/USD',
	'GMT/EUR',
	'GMT/USD',
	'GMX/EUR',
	'GMX/USD',
	'GNO/EUR',
	'GNO/USD',
	'GRT/BTC',
	'GRT/EUR',
	'GRT/GBP',
	'GRT/USD',
	'GST/EUR',
	'GST/USD',
	'GTC/EUR',
	'GTC/USD',
	'HDX/EUR',
	'HDX/USD',
	'HFT/EUR',
	'HFT/USD',
	'HNT/EUR',
	'HNT/USD',
	'HONEY/EUR',
	'HONEY/USD',
	'ICP/EUR',
	'ICP/USD',
	'ICX/BTC',
	'ICX/ETH',
	'ICX/EUR',
	'ICX/USD',
	'IDEX/EUR',
	'IDEX/USD',
	'IMX/EUR',
	'IMX/USD',
	'INJ/EUR',
	'INJ/USD',
	'INTR/EUR',
	'INTR/USD',
	'JASMY/EUR',
	'JASMY/USD',
	'JTO/EUR',
	'JTO/USD',
	'JUNO/EUR',
	'JUNO/USD',
	'JUP/EUR',
	'JUP/USD',
	'KAR/EUR',
	'KAR/USD',
	'KAVA/BTC',
	'KAVA/ETH',
	'KAVA/EUR',
	'KAVA/USD',
	'KEEP/BTC',
	'KEEP/EUR',
	'KEEP/USD',
	'KEY/EUR',
	'KEY/USD',
	'KILT/EUR',
	'KILT/USD',
	'KIN/EUR',
	'KIN/USD',
	'KINT/EUR',
	'KINT/USD',
	'KMNO/EUR',
	'KMNO/USD',
	'KNC/ETH',
	'KNC/EUR',
	'KNC/USD',
	'KP3R/EUR',
	'KP3R/USD',
	'KSM/BTC',
	'KSM/DOT',
	'KSM/ETH',
	'KSM/EUR',
	'KSM/GBP',
	'KSM/USD',
	'KUJI/EUR',
	'KUJI/USD',
	'L3/EUR',
	'L3/USD',
	'LCX/EUR',
	'LCX/USD',
	'LDO/EUR',
	'LDO/USD',
	'LINK/AUD',
	'LINK/BTC',
	'LINK/ETH',
	'LINK/EUR',
	'LINK/GBP',
	'LINK/JPY',
	'LINK/USD',
	'LINK/USDT',
	'LIT/EUR',
	'LIT/USD',
	'LMWR/EUR',
	'LMWR/USD',
	'LPT/BTC',
	'LPT/EUR',
	'LPT/GBP',
	'LPT/USD',
	'LRC/EUR',
	'LRC/USD',
	'LSK/EUR',
	'LSK/USD',
	'LTC/AUD',
	'LTC/BTC',
	'LTC/ETH',
	'LTC/EUR',
	'LTC/GBP',
	'LTC/JPY',
	'LTC/USD',
	'LTC/USDT',
	'LUNA/EUR',
	'LUNA/USD',
	'LUNA2/EUR',
	'LUNA2/USD',
	'MANA/BTC',
	'MANA/EUR',
	'MANA/USD',
	'MANA/USDT',
	'MASK/EUR',
	'MASK/USD',
	'MATIC/BTC',
	'MATIC/EUR',
	'MATIC/GBP',
	'MATIC/POL',
	'MATIC/USD',
	'MATIC/USDT',
	'MC/EUR',
	'MC/USD',
	'MEME/EUR',
	'MEME/USD',
	'MEW/EUR',
	'MEW/USD',
	'MINA/BTC',
	'MINA/EUR',
	'MINA/GBP',
	'MINA/USD',
	'MIR/EUR',
	'MIR/USD',
	'MKR/BTC',
	'MKR/EUR',
	'MKR/USD',
	'MLN/BTC',
	'MLN/EUR',
	'MLN/USD',
	'MNGO/EUR',
	'MNGO/USD',
	'MNT/EUR',
	'MNT/USD',
	'MOG/EUR',
	'MOG/USD',
	'MOON/EUR',
	'MOON/USD',
	'MOVR/EUR',
	'MOVR/USD',
	'MPL/EUR',
	'MPL/USD',
	'MSOL/EUR',
	'MSOL/USD',
	'MULTI/EUR',
	'MULTI/USD',
	'MV/EUR',
	'MV/USD',
	'MXC/EUR',
	'MXC/USD',
	'NANO/BTC',
	'NANO/ETH',
	'NANO/EUR',
	'NANO/USD',
	'NEAR/EUR',
	'NEAR/USD',
	'NMR/EUR',
	'NMR/USD',
	'NODL/EUR',
	'NODL/USD',
	'NOS/EUR',
	'NOS/USD',
	'NTRN/EUR',
	'NTRN/USD',
	'NYM/BTC',
	'NYM/EUR',
	'NYM/USD',
	'OCEAN/BTC',
	'OCEAN/EUR',
	'OCEAN/GBP',
	'OCEAN/USD',
	'OGN/EUR',
	'OGN/USD',
	'OMG/BTC',
	'OMG/ETH',
	'OMG/EUR',
	'OMG/JPY',
	'OMG/USD',
	'ONDO/EUR',
	'ONDO/USD',
	'OP/EUR',
	'OP/USD',
	'ORCA/EUR',
	'ORCA/USD',
	'OSMO/EUR',
	'OSMO/USD',
	'OXT/EUR',
	'OXT/USD',
	'OXY/EUR',
	'OXY/USD',
	'PAXG/BTC',
	'PAXG/ETH',
	'PAXG/EUR',
	'PAXG/USD',
	'PDA/EUR',
	'PDA/USD',
	'PENDLE/EUR',
	'PENDLE/USD',
	'PEPE/EUR',
	'PEPE/USD',
	'PERP/EUR',
	'PERP/USD',
	'PHA/EUR',
	'PHA/USD',
	'POL/EUR',
	'POL/USD',
	'POLIS/EUR',
	'POLIS/USD',
	'POLS/EUR',
	'POLS/USD',
	'POND/EUR',
	'POND/USD',
	'POPCAT/EUR',
	'POPCAT/USD',
	'PORTAL/EUR',
	'PORTAL/USD',
	'POWR/EUR',
	'POWR/USD',
	'PRCL/EUR',
	'PRCL/USD',
	'PRIME/EUR',
	'PRIME/USD',
	'PSTAKE/EUR',
	'PSTAKE/USD',
	'PUFFER/EUR',
	'PUFFER/USD',
	'PYTH/EUR',
	'PYTH/USD',
	'PYUSD/EUR',
	'PYUSD/USD',
	'QNT/EUR',
	'QNT/USD',
	'QTUM/BTC',
	'QTUM/ETH',
	'QTUM/EUR',
	'QTUM/USD',
	'RAD/EUR',
	'RAD/USD',
	'RARE/EUR',
	'RARE/USD',
	'RARI/BTC',
	'RARI/EUR',
	'RARI/USD',
	'RAY/EUR',
	'RAY/USD',
	'RBC/EUR',
	'RBC/USD',
	'REN/EUR',
	'REN/USD',
	'RENDER/EUR',
	'RENDER/USD',
	'REP/EUR',
	'REP/USD',
	'REPV2/BTC',
	'REPV2/ETH',
	'REPV2/EUR',
	'REPV2/USD',
	'REQ/EUR',
	'REQ/USD',
	'REZ/EUR',
	'REZ/USD',
	'RLC/EUR',
	'RLC/USD',
	'ROOK/EUR',
	'ROOK/USD',
	'RPL/EUR',
	'RPL/USD',
	'RUNE/EUR',
	'RUNE/USD',
	'SAFE/EUR',
	'SAFE/USD',
	'SAGA/EUR',
	'SAGA/USD',
	'SAMO/EUR',
	'SAMO/USD',
	'SAND/BTC',
	'SAND/EUR',
	'SAND/GBP',
	'SAND/USD',
	'SBR/EUR',
	'SBR/USD',
	'SC/BTC',
	'SC/EUR',
	'SC/USD',
	'SCRT/EUR',
	'SCRT/USD',
	'SDN/EUR',
	'SDN/USD',
	'SEI/EUR',
	'SEI/USD',
	'SGB/EUR',
	'SGB/USD',
	'SHIB/EUR',
	'SHIB/USD',
	'SHIB/USDT',
	'SKY/EUR',
	'SKY/USD',
	'SNX/BTC',
	'SNX/ETH',
	'SNX/EUR',
	'SNX/USD',
	'SOL/AUD',
	'SOL/BTC',
	'SOL/ETH',
	'SOL/EUR',
	'SOL/GBP',
	'SOL/USD',
	'SOL/USDT',
	'SPELL/EUR',
	'SPELL/USD',
	'SRM/BTC',
	'SRM/EUR',
	'SRM/USD',
	'STEP/EUR',
	'STEP/USD',
	'STG/EUR',
	'STG/USD',
	'STORJ/BTC',
	'STORJ/EUR',
	'STORJ/USD',
	'STRD/EUR',
	'STRD/USD',
	'STRK/EUR',
	'STRK/USD',
	'STX/EUR',
	'STX/USD',
	'SUI/EUR',
	'SUI/USD',
	'SUPER/EUR',
	'SUPER/USD',
	'SUSHI/EUR',
	'SUSHI/USD',
	'SYN/EUR',
	'SYN/USD',
	'T/EUR',
	'T/USD',
	'TAO/EUR',
	'TAO/USD',
	'TBTC/BTC',
	'TBTC/EUR',
	'TBTC/USD',
	'TEER/EUR',
	'TEER/USD',
	'TIA/EUR',
	'TIA/USD',
	'TLM/EUR',
	'TLM/USD',
	'TNSR/EUR',
	'TNSR/USD',
	'TOKE/EUR',
	'TOKE/USD',
	'TON/EUR',
	'TON/USD',
	'TRAC/EUR',
	'TRAC/USD',
	'TREMP/EUR',
	'TREMP/USD',
	'TRU/EUR',
	'TRU/USD',
	'TRX/BTC',
	'TRX/ETH',
	'TRX/EUR',
	'TRX/USD',
	'TURBO/EUR',
	'TURBO/USD',
	'TUSD/EUR',
	'TUSD/USD',
	'TVK/EUR',
	'TVK/USD',
	'UMA/EUR',
	'UMA/USD',
	'UNFI/EUR',
	'UNFI/USD',
	'UNI/BTC',
	'UNI/ETH',
	'UNI/EUR',
	'UNI/USD',
	'USD/CAD',
	'USD/CHF',
	'USD/JPY',
	'USDC/AUD',
	'USDC/CAD',
	'USDC/CHF',
	'USDC/EUR',
	'USDC/GBP',
	'USDC/USD',
	'USDC/USDT',
	'USDS/EUR',
	'USDS/USD',
	'USDT/AUD',
	'USDT/CAD',
	'USDT/CHF',
	'USDT/EUR',
	'USDT/GBP',
	'USDT/JPY',
	'USDT/USD',
	'UST/EUR',
	'UST/USD',
	'UST/USDC',
	'UST/USDT',
	'W/EUR',
	'W/USD',
	'WAXL/EUR',
	'WAXL/USD',
	'WBTC/BTC',
	'WBTC/EUR',
	'WBTC/USD',
	'WEN/EUR',
	'WEN/USD',
	'WIF/EUR',
	'WIF/USD',
	'WOO/EUR',
	'WOO/USD',
	'XCN/EUR',
	'XCN/USD',
	'XLM/BTC',
	'XLM/EUR',
	'XLM/GBP',
	'XLM/USD',
	'XMR/BTC',
	'XMR/EUR',
	'XMR/USD',
	'XMR/USDT',
	'XRP/AUD',
	'XRP/BTC',
	'XRP/CAD',
	'XRP/ETH',
	'XRP/EUR',
	'XRP/GBP',
	'XRP/USD',
	'XRP/USDT',
	'XRT/EUR',
	'XRT/USD',
	'XTZ/BTC',
	'XTZ/EUR',
	'XTZ/USD',
	'XTZ/USDT',
	'YFI/EUR',
	'YFI/USD',
	'YGG/EUR',
	'YGG/USD',
	'ZEC/BTC',
	'ZEC/EUR',
	'ZEC/USD',
	'ZETA/EUR',
	'ZETA/USD',
	'ZEUS/EUR',
	'ZEUS/USD',
	'ZEX/EUR',
	'ZEX/USD',
	'ZK/EUR',
	'ZK/USD',
	'ZRO/EUR',
	'ZRO/USD',
	'ZRX/BTC',
	'ZRX/EUR',
	'ZRX/USD',
]