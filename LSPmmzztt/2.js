//学习网站：https://mmzztt.com/
//过当前debug
var _constructor = constructor;
Function.prototype.constructor = function(s){
   if (s === "debugger"){
       //console.log(s);
       return null;
  }
   return _constructor(s);
}
var CryptoJS = require('crypto-js')

function _0x30fe(_0x153f69, _0x3c2a58) {
    _0x1832f2 = _0x3c2a58["split"]("97cba" + '7c46d' + "fa9b8" + "8b62c" + "aa6b6" + '21d92' + "c4")[1],
        _0x19bb3d = '',
        _0x21cab2 = CryptoJS;
    for (i = 2; i < 18; i++) {
        _0x19bb3d += (_0x153f69 % i % 9)['toString']();
    }
    var _0x3a6afc = _0x21cab2['enc']["Hex"]['parse'](_0x1832f2),
        _0xcf383b = _0x21cab2["enc"]['Base64']['stringify'](_0x3a6afc),
        _0x1705e5 = _0x21cab2['MD5'](_0x21cab2['enc']["Utf8"]['parse'](_0x153f69 + ('d262d29cb702140' + "5dc1a" + "43c91" + '68043' + "b7") + _0x19bb3d))['toString']()['substr'](8, 16),
        _0x1705e5 = _0x21cab2['enc']['Utf8']['parse'](_0x1705e5),
        _0x5c0c92 = _0x21cab2['AES']['decrypt'](_0xcf383b, _0x1705e5, {
            "iv": _0x21cab2["enc"]['Utf8']["parse"](_0x19bb3d),
            "mode": _0x21cab2["mode"]["CBC"],
            "padding": _0x21cab2["pad"]["Pkcs7"]
        });
    return JSON["parse"](_0x5c0c92['toString'](_0x21cab2["enc"]["Utf8"]));
}

console.log(_0x30fe('39040', 'ad0f34a6e9ba5b2a9ee08a547de8f78d97cba7c46dfa9b88b62caa6b621d92c4b560ddceb5dbfb6f44949031f873bf6e9568827a841585c3219260560783fb6f3eda88b9d16cdfc31f9807c129095838323aa93a051cf14407c464a4401cac04e82d7a5db53b83c90aa62604bdb97f48a99d059174898a4f8cccaa495568345581b48b79c615f6dde27da5f2e8fe8eb89013553dd2cc08d843729488b32fdc22f43512cc18c61d0545a3e4f0fbfe72fb18bdccf910c58c5f12d03845f784018e6f066dbe679501a94a32efc937fb8311cc0b971a9c68b32d0e6edbb4a0f1497077291df40638d36bf42e77cfe9b54846b86837460daaad25f184f4169cf64add17844c55cf3c2a184f218f144855d7cb4a4915b3e8cedb83fd687d6cd5792c8fb1a8cb83d5ae3f1f03a8ed5fbec38409'));
