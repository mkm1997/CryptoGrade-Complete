$( function() {
var names = [
    {
        'url': '/coins/BTC',
        'label': 'Bitcoin (BTC)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/btc.svg'
    },
    {
        'url': '/coins/ETH',
        'label': 'Ethereum (ETH)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/eth.svg'
    },
    {
        'url': '/coins/XRP',
        'label': 'Ripple (XRP)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/xrp.svg'
    },
    {
        'url': '/coins/BCH',
        'label': 'Bitcoin Cash (BCH)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/bch.svg'
    },
    {
        'url': '/coins/LTC',
        'label': 'Litecoin (LTC)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/ltc.svg'
    },
    {
        'url': '/coins/ADA',
        'label': 'Cardano (ADA)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/ada.svg'
    },
    {
        'url': '/coins/NEO',
        'label': 'NEO (NEO)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/neo.svg'
    },
    {
        'url': '/coins/XLM',
        'label': 'Stellar (XLM)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/xlm.svg'
    },
    {
        'url': '/coins/EOS',
        'label': 'EOS (EOS)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/eos.svg'
    },
    {
        'url': '/coins/MIOTA',
        'label': 'IOTA (MIOTA)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/miota.svg'
    },
    {
        'url': '/coins/DASH',
        'label': 'Dash (DASH)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/dash.svg'
    },
    {
        'url': '/coins/XEM',
        'label': 'NEM (XEM)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/xem.svg'
    },
    {
        'url': '/coins/XMR',
        'label': 'Monero (XMR)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/xmr.svg'
    },
    {
        'url': '/coins/LSK',
        'label': 'Lisk (LSK)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/lsk.svg'
    },
    {
        'url': '/coins/TRX',
        'label': 'TRON (TRX)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/trx.svg'
    },
    {
        'url': '/coins/ETC',
        'label': 'Ethereum Classic (ETC)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/etc.svg'
    },
    {
        'url': '/coins/VEN',
        'label': 'VeChain (VEN)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/ven.svg'
    },
    {
        'url': '/coins/QTUM',
        'label': 'Qtum (QTUM)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/qtum.svg'
    },
    {
        'url': '/coins/BTG',
        'label': 'Bitcoin Gold (BTG)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/btg.svg'
    },
    {
        'url': '/coins/USDT',
        'label': 'Tether (USDT)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/usdt.svg'
    },
    {
        'url': '/coins/ICX',
        'label': 'ICON (ICX)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/icx.svg'
    },
    {
        'url': '/coins/OMG',
        'label': 'OmiseGO (OMG)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/omg.svg'
    },
    {
        'url': '/coins/ZEC',
        'label': 'Zcash (ZEC)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/zec.svg'
    },
    {
        'url': '/coins/XRB',
        'label': 'Nano (XRB)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/xrb.svg'
    },
    {
        'url': '/coins/XVG',
        'label': 'Verge (XVG)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/xvg.svg'
    },
    {
        'url': '/coins/BNB',
        'label': 'Binance Coin (BNB)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/bnb.svg'
    },
    {
        'url': '/coins/STEEM',
        'label': 'Steem (STEEM)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/steem.svg'
    },
    {
        'url': '/coins/PPT',
        'label': 'Populous (PPT)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/ppt.svg'
    },
    {
        'url': '/coins/BCN',
        'label': 'Bytecoin (BCN)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/bcn.svg'
    },
    {
        'url': '/coins/SC',
        'label': 'Siacoin (SC)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/sc.svg'
    },
    {
        'url': '/coins/STRAT',
        'label': 'Stratis (STRAT)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/strat.svg'
    },
    {
        'url': '/coins/RHOC',
        'label': 'RChain (RHOC)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/rhoc.svg'
    },
    {
        'url': '/coins/SNT',
        'label': 'Status (SNT)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/snt.svg'
    },
    {
        'url': '/coins/DOGE',
        'label': 'Dogecoin (DOGE)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/doge.svg'
    },
    {
        'url': '/coins/WAVES',
        'label': 'Waves (WAVES)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/waves.svg'
    },
    {
        'url': '/coins/BTS',
        'label': 'BitShares (BTS)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/bts.svg'
    },
    {
        'url': '/coins/MKR',
        'label': 'Maker (MKR)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/mkr.svg'
    },
    {
        'url': '/coins/WTC',
        'label': 'Waltonchain (WTC)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/wtc.svg'
    },
    {
        'url': '/coins/ZRX',
        'label': '0x (ZRX)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/zrx.svg'
    },
    {
        'url': '/coins/DCR',
        'label': 'Decred (DCR)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/dcr.svg'
    },
    {
        'url': '/coins/AE',
        'label': 'Aeternity (AE)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/ae.svg'
    },
    {
        'url': '/coins/UCASH',
        'label': 'U.CASH (UCASH)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/ucash.svg'
    },
    {
        'url': '/coins/REP',
        'label': 'Augur (REP)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/rep.svg'
    },
    {
        'url': '/coins/VERI',
        'label': 'Veritaseum (VERI)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/veri.svg'
    },
    {
        'url': '/coins/HSR',
        'label': 'Hshare (HSR)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/hsr.svg'
    },
    {
        'url': '/coins/KMD',
        'label': 'Komodo (KMD)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/kmd.svg'
    },
    {
        'url': '/coins/ZCL',
        'label': 'ZClassic (ZCL)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/zcl.svg'
    },
    {
        'url': '/coins/KCS',
        'label': 'KuCoin Shares (KCS)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/kcs.svg'
    },
    {
        'url': '/coins/ETN',
        'label': 'Electroneum (ETN)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/etn.svg'
    },
    {
        'url': '/coins/ARDR',
        'label': 'Ardor (ARDR)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/ardr.svg'
    },
    {
        'url': '/coins/R',
        'label': 'Revain (R)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/r.svg'
    },
    {
        'url': '/coins/ARK',
        'label': 'Ark (ARK)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/ark.svg'
    },
    {
        'url': '/coins/DGD',
        'label': 'DigixDAO (DGD)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/dgd.svg'
    },
    {
        'url': '/coins/DRGN',
        'label': 'Dragonchain (DRGN)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/drgn.svg'
    },
    {
        'url': '/coins/GAS',
        'label': 'Gas (GAS)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/gas.svg'
    },
    {
        'url': '/coins/DGB',
        'label': 'DigiByte (DGB)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/dgb.svg'
    },
    {
        'url': '/coins/BAT',
        'label': 'Basic Attention Token (BAT)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/bat.svg'
    },
    {
        'url': '/coins/GBYTE',
        'label': 'Byteball Bytes (GBYTE)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/gbyte.svg'
    },
    {
        'url': '/coins/LRC',
        'label': 'Loopring (LRC)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/lrc.svg'
    },
    {
        'url': '/coins/ZIL',
        'label': 'Zilliqa (ZIL)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/zil.svg'
    },
    {
        'url': '/coins/GNT',
        'label': 'Golem (GNT)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/gnt.svg'
    },
    {
        'url': '/coins/BTM',
        'label': 'Bytom (BTM)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/btm.svg'
    },
    {
        'url': '/coins/KNC',
        'label': 'Kyber Network (KNC)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/knc.svg'
    },
    {
        'url': '/coins/MONA',
        'label': 'MonaCoin (MONA)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/mona.svg'
    },
    {
        'url': '/coins/PIVX',
        'label': 'PIVX (PIVX)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/pivx.svg'
    },
    {
        'url': '/coins/SYS',
        'label': 'Syscoin (SYS)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/sys.svg'
    },
    {
        'url': '/coins/ELF',
        'label': 'aelf (ELF)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/elf.svg'
    },
    {
        'url': '/coins/QASH',
        'label': 'QASH (QASH)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/qash.svg'
    },
    {
        'url': '/coins/CNX',
        'label': 'Cryptonex (CNX)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/cnx.svg'
    },
    {
        'url': '/coins/DCN',
        'label': 'Dentacoin (DCN)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/dcn.svg'
    },
    {
        'url': '/coins/AION',
        'label': 'Aion (AION)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/aion.svg'
    },
    {
        'url': '/coins/BTX',
        'label': 'Bitcore (BTX)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/btx.svg'
    },
    {
        'url': '/coins/NAS',
        'label': 'Nebulas (NAS)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/nas.svg'
    },
    {
        'url': '/coins/IOST',
        'label': 'IOStoken (IOST)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/iost.svg'
    },
    {
        'url': '/coins/ETHOS',
        'label': 'Ethos (ETHOS)',
        'img_url': 'https://cryptograde.io/static/coinviewer/logos/ethos.svg'
    }
];

var accentMap = {
  "á": "a",
  "ö": "o"
};
var normalize = function( term ) {
  var ret = "";
  for ( var i = 0; i < term.length; i++ ) {
    ret += accentMap[ term.charAt(i) ] || term.charAt(i);
  }
  return ret;
};

$( "#searchbar" ).autocomplete({
    source: function( request, response ) {
        var matcher = new RegExp( $.ui.autocomplete.escapeRegex( request.term ), "i" );
        response( $.grep( names, function( value ) {
            value = value.label || value.value || value;
            return matcher.test( value );
        }).slice(0, 8) );
    },
    open: function() { $('#div .ui-menu').width(300) },
    select: function( event, ui ) {
        window.open(ui.item.url, "_self")
    }
}).data( "ui-autocomplete" )._renderItem = function( ul, item ) {
    return $( "<li></li>" )
        .data( "item.autocomplete", item )
        .append( "<a>" +
            "<img style='width:20px;height:20px;margin-top:5px;margin-bottom:5px;' src='" + item.img_url + "' /> " +
            item.label +
            "</a>")
        .appendTo( ul );
};
} );
