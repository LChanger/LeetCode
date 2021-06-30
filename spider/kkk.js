(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["chunk-common"], {
    3215: function(e, r, t) {},
    "3e09": function(module, __webpack_exports__, __webpack_require__) {
        "use strict";
        var core_js_modules_es6_regexp_match__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__("4917")
          , core_js_modules_es6_regexp_match__WEBPACK_IMPORTED_MODULE_0___default = __webpack_require__.n(core_js_modules_es6_regexp_match__WEBPACK_IMPORTED_MODULE_0__)
          , core_js_modules_es6_regexp_split__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__("28a5")
          , core_js_modules_es6_regexp_split__WEBPACK_IMPORTED_MODULE_1___default = __webpack_require__.n(core_js_modules_es6_regexp_split__WEBPACK_IMPORTED_MODULE_1__)
          , core_js_modules_es6_regexp_replace__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__("a481")
          , core_js_modules_es6_regexp_replace__WEBPACK_IMPORTED_MODULE_2___default = __webpack_require__.n(core_js_modules_es6_regexp_replace__WEBPACK_IMPORTED_MODULE_2__)
          , core_js_modules_es6_string_link__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__("b54a")
          , core_js_modules_es6_string_link__WEBPACK_IMPORTED_MODULE_3___default = __webpack_require__.n(core_js_modules_es6_string_link__WEBPACK_IMPORTED_MODULE_3__)
          , core_js_modules_es6_regexp_to_string__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__("6b54")
          , core_js_modules_es6_regexp_to_string__WEBPACK_IMPORTED_MODULE_4___default = __webpack_require__.n(core_js_modules_es6_regexp_to_string__WEBPACK_IMPORTED_MODULE_4__)
          , _home_biu_svnfile_h5_qq_node_modules_babel_runtime_corejs2_helpers_esm_typeof__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__("7618")
          , core_js_modules_es6_regexp_constructor__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__("3b2b")
          , core_js_modules_es6_regexp_constructor__WEBPACK_IMPORTED_MODULE_6___default = __webpack_require__.n(core_js_modules_es6_regexp_constructor__WEBPACK_IMPORTED_MODULE_6__)
          , vant_es_toast_style_less__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__("433b")
          , vant_es_toast__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__("d399")
          , underscore__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__("17fb")
          , underscore__WEBPACK_IMPORTED_MODULE_9___default = __webpack_require__.n(underscore__WEBPACK_IMPORTED_MODULE_9__)
          , axios__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__("bc3a")
          , axios__WEBPACK_IMPORTED_MODULE_10___default = __webpack_require__.n(axios__WEBPACK_IMPORTED_MODULE_10__)
          , _utils_userDC_js__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__("f928")
          , Kp = {};
        function Validation() {
            this.value = "",
            this.ruleName = "",
            this.param = "",
            this.errmsg = ""
        }
        Kp.Req = function(e) {
            var r = {
                method: "get",
                pathname: "/sc-api",
                url: "",
                data: {},
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "X-Requested-With": "XMLHttpRequest",
                    "X-Sc-Alias": ""
                },
                timeout: 5e3,
                responseType: "json",
                loadingText: "",
                message: "",
                finish: null,
                before: null,
                fail: null,
                success: null,
                callback: null,
                errorCallback: null
            };
            if (r = underscore__WEBPACK_IMPORTED_MODULE_9___default.a.extend(r, e),
            r.headers["X-Sc-Alias"] = COMMUNITY_INFO.alias_name,
            r.data.isIOS = Kp.Utils.isIOS(),
            "get" == r.method && r.data && (r.params = r.data),
            !underscore__WEBPACK_IMPORTED_MODULE_9___default.a.isEmpty(r.data)) {
                var t = new FormData;
                for (var _ in r.data)
                    t.append(_, r.data[_]);
                r.data = t
            }
            underscore__WEBPACK_IMPORTED_MODULE_9___default.a.isFunction(r.before) && r.before(r);
            var n = r.loadingText ? vant_es_toast__WEBPACK_IMPORTED_MODULE_8__["a"].loading({
                message: r.loadingText
            }) : null;
            return axios__WEBPACK_IMPORTED_MODULE_10___default()({
                method: r.method,
                url: r.pathname + r.url,
                data: r.data,
                params: r.params,
                headers: r.headers,
                timeout: r.timeout,
                responseType: r.responseType
            }).then((function(e) {
                var t = e.data || {};
                if (n && n.clear(),
                underscore__WEBPACK_IMPORTED_MODULE_9___default.a.isFunction(r.finish) && r.finish(t),
                r.success)
                    r.success(t);
                else if (0 == t.errno)
                    underscore__WEBPACK_IMPORTED_MODULE_9___default.a.isFunction(r.callback) && r.callback(t.data),
                    r.message && vant_es_toast__WEBPACK_IMPORTED_MODULE_8__["a"].success({
                        message: r.message,
                        duration: 1200
                    });
                else {
                    if (30 == t.errno)
                        return Object(vant_es_toast__WEBPACK_IMPORTED_MODULE_8__["a"])(t.errmsg),
                        _utils_userDC_js__WEBPACK_IMPORTED_MODULE_11__["a"].clearCommunityAlias(),
                        void setTimeout((function() {
                            window.location.href = "/com/select"
                        }
                        ), 1200);
                    if (20 == t.errno)
                        return Object(vant_es_toast__WEBPACK_IMPORTED_MODULE_8__["a"])(t.errmsg),
                        _utils_userDC_js__WEBPACK_IMPORTED_MODULE_11__["a"].clearUserToken(),
                        void setTimeout((function() {
                            window.location.href = "/qqlogin"
                        }
                        ), 800);
                    underscore__WEBPACK_IMPORTED_MODULE_9___default.a.isFunction(r.errorCallback) && r.errorCallback(t.data),
                    vant_es_toast__WEBPACK_IMPORTED_MODULE_8__["a"].fail(t.errmsg || "数据请求错误")
                }
            }
            )).catch((function(e) {
                console.log(e),
                n && n.clear(),
                underscore__WEBPACK_IMPORTED_MODULE_9___default.a.isFunction(r.finish) && r.finish(),
                underscore__WEBPACK_IMPORTED_MODULE_9___default.a.isFunction(r.fail) && r.fail(),
                vant_es_toast__WEBPACK_IMPORTED_MODULE_8__["a"].fail("网络异常，请稍后重试")
            }
            ))
        }
        ;
        var ruleExtends = {
            isNumber: function(e) {
                return /^-?(?:\d+|\d{1,3}(?:,\d{3})+)?(?:\.\d+)?$/.test(e)
            },
            isDigits: function(e) {
                return /^(-?[1-9]\d*|0)$/.test(e)
            },
            isAlnum: function(e) {
                return /^[0-9A-Za-z]+$/.test(e)
            },
            isAlpha: function(e) {
                return /^[A-Za-z]+$/.test(e)
            },
            isAlnumunder: function(e) {
                return /^[0-9A-Za-z_]+$/.test(e)
            },
            isCommaNum: function(e) {
                return /^(\d+[,])*(\d+)$/.test(e)
            },
            isEmail: function(e) {
                var r = /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)/
                  , t = /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(\]?)$/;
                return !r.test(e) && t.test(e)
            },
            isPhone: function(e) {
                return /^1\d{10}$/.test(e)
            },
            isTelephone: function(e) {
                return /^[0-9]{3,4}-[0-9]{7,8}$/.test(e)
            },
            isFax: function(e) {
                return /^[+]{0,1}(\d){1,3}[ ]?([-]?((\d)|[ ]){1,12})+$/.test(e)
            },
            isChinese: function(e) {
                return /^[\u4e00-\u9fa5]+$/.test(e)
            },
            isDate: function(e) {
                var r = /^(\d{4})-(\d{2})-(\d{2})$/;
                r.exec(e);
                return !(!r.test(e) && RegExp.$2 <= 12 && RegExp.$3 <= 31)
            },
            isDatetime: function(e) {
                return /^((\d){4})-((\d){2})-((\d){2}) ((\d){2}):((\d){2}):((\d){2})$/.test(e)
            },
            isUrl: function(e) {
                var r = new RegExp("^(?:(?:https?|ftp)://)?(?:\\S+(?::\\S*)?@)?(?:(?:[1-9]\\d?|1\\d\\d|2[01]\\d|22[0-3])(?:\\.(?:1?\\d{1,2}|2[0-4]\\d|25[0-5])){2}(?:\\.(?:[1-9]\\d?|1\\d\\d|2[0-4]\\d|25[0-4]))|(?:(?:[a-z\\u00a1-\\uffff0-9]-*)*[a-z\\u00a1-\\uffff0-9]+)(?:\\.(?:[a-z\\u00a1-\\uffff0-9]-*)*[a-z\\u00a1-\\uffff0-9]+)*(?:\\.(?:[a-z\\u00a1-\\uffff]{2,})))(?::\\d{2,5})?(?:/\\S*)?$","i");
                return r.test(e)
            }
        };
        underscore__WEBPACK_IMPORTED_MODULE_9___default.a.extend(Validation.prototype, {
            IsValid: function IsValid(value, rules, errors) {
                var _type = Object(_home_biu_svnfile_h5_qq_node_modules_babel_runtime_corejs2_helpers_esm_typeof__WEBPACK_IMPORTED_MODULE_5__["a"])(rules)
                  , that = this;
                if ("undefined" == _type)
                    return !0;
                if ("string" == _type && (rules = eval("(" + rules + ")")),
                that.value = value.toString(),
                Array.isArray(rules)) {
                    if (!rules.length)
                        return !0;
                    for (var tmpArr = [], i = 0, len = rules.length; i < len; i++) {
                        var item = rules[i];
                        for (var key in tmpArr[i] = 1,
                        item)
                            if (that.param = item[key],
                            that.ruleName = key.toLowerCase(),
                            !that.Validate()) {
                                tmpArr[i] = 0,
                                that.SetError(errors);
                                break
                            }
                    }
                    for (var k = 0, len = tmpArr.length; k < len; k++)
                        if (0 == tmpArr[k])
                            return !1;
                    return !0
                }
                for (var key in rules)
                    if (that.param = rules[key],
                    that.ruleName = key.toLowerCase(),
                    !that.Validate())
                        return that.SetError(errors),
                        !1;
                return that.ClearError(),
                !0
            },
            ClearError: function() {
                this.errmsg = ""
            },
            SetError: function SetError(errors) {
                if (errors)
                    try {
                        var _errors = eval("(" + errors + ")");
                        if (_errors[this.ruleName])
                            return void (this.errmsg = _errors[this.ruleName])
                    } catch (e) {
                        return void (this.errmsg = errors)
                    }
                switch (this.ruleName) {
                case "required":
                    this.errmsg = "此项不能为空";
                    break;
                case "number":
                    this.errmsg = "此项只能为数字";
                    break;
                case "alnumunder":
                    this.errmsg = "此项只能为数字、字母或下划线";
                    break;
                case "alnum":
                    this.errmsg = "此项只能为数字或字母";
                    break;
                case "alpha":
                    this.errmsg = "此项只能为字母";
                    break;
                case "digits":
                    this.errmsg = "此项只能为整数";
                    break;
                case "maxlength":
                    this.errmsg = "此项最大长度不能超过" + this.param + "位";
                    break;
                case "minlength":
                    this.errmsg = "此项最小长度不能少于" + this.param + "位";
                    break;
                case "rangelength":
                    this.errmsg = "此项长度必须介于" + this.param[0] + "位到" + this.param[1] + "位之间";
                    break;
                case "max":
                    this.errmsg = "请输入一个不大于" + this.param + "的数";
                    break;
                case "min":
                    this.errmsg = "请输入一个不小于" + this.param + "的数";
                    break;
                case "range":
                    this.errmsg = "请输入一个介于" + this.param[0] + "和" + this.param[1] + "之间的数";
                    break;
                case "commanum":
                    this.errmsg = "输入的格式不正确";
                    break;
                case "email":
                    this.errmsg = "请输入一个正确的电子邮件地址";
                    break;
                case "phone":
                    this.errmsg = "请输入一个正确的手机号码";
                    break;
                case "telephone":
                    this.errmsg = "请输入一个正确的座机号";
                    break;
                case "fax":
                    this.errmsg = "请输入一个正确的传真号码";
                    break;
                case "url":
                    this.errmsg = "请输入一个正确的网址";
                    break;
                case "chinese":
                    this.errmsg = "此项只能为汉字";
                    break;
                case "date":
                    this.errmsg = "此项只能为日期";
                    break;
                case "datetime":
                    this.errmsg = "此项只能为日期+时间";
                    break;
                default:
                    this.errmsg = "";
                    break
                }
            },
            GetError: function() {
                return this.errmsg || ""
            },
            GetRuleName: function() {
                return this.ruleName || ""
            },
            Validate: function() {
                switch (this.ruleName) {
                case "required":
                    if (this.param) {
                        var e = this.param ? this.value.trim().length > 0 : 0 == this.value.trim().length;
                        return e
                    }
                    return !0;
                case "number":
                    return ruleExtends.isNumber(this.value);
                case "alpha":
                    return ruleExtends.isAlpha(this.value);
                case "alnumunder":
                    return ruleExtends.isAlnumunder(this.value);
                case "alnum":
                    return ruleExtends.isAlnum(this.value);
                case "digits":
                    return ruleExtends.isDigits(this.value);
                case "maxlength":
                    var r = this.value.trim().length;
                    return r <= this.param;
                case "minlength":
                    r = this.value.trim().length;
                    return r >= this.param;
                case "rangelength":
                    r = this.value.trim().length;
                    return r >= this.param[0] && r <= this.param[1];
                case "max":
                    return this.value <= this.param;
                case "min":
                    return this.value >= this.param;
                case "range":
                    return this.value >= this.param[0] && this.value <= this.param[1];
                case "commanum":
                    return ruleExtends.isCommaNum(this.value);
                case "email":
                    return ruleExtends.isEmail(this.value);
                case "phone":
                    return ruleExtends.isPhone(this.value);
                case "telephone":
                    return ruleExtends.isTelephone(this.value);
                case "fax":
                    return ruleExtends.isFax(this.value);
                case "url":
                    return ruleExtends.isUrl(this.value);
                case "chinese":
                    return ruleExtends.isChinese(this.value);
                case "date":
                    return ruleExtends.isDate(this.value);
                case "datetime":
                    return ruleExtends.isDatetime(this.value);
                default:
                    return !0
                }
            }
        }),
        Kp.Validation = function() {
            return new Validation
        }
        ,
        Kp.Wechat = {
            sdkConfig: !1,
            shareConfig: !1,
            apiList: ["onMenuShareTimeline", "onMenuShareAppMessage", "onMenuShareQQ", "onMenuShareWeibo", "onMenuShareQZone", "startRecord", "stopRecord", "onVoiceRecordEnd", "playVoice", "pauseVoice", "stopVoice", "onVoicePlayEnd", "uploadVoice", "downloadVoice", "chooseImage", "previewImage", "uploadImage", "downloadImage", "openLocation", "getLocation", "translateVoice", "hideOptionMenu", "hideMenuItems", "closeWindow", "scanQRCode", "chooseWXPay"],
            inWechat: function() {
                return /micromessenger/i.test(navigator.userAgent)
            },
            inMiniProgram: function() {
                return "miniprogram" === window.__wxjs_environment
            },
            config: function(e, r) {},
            share: function(e) {
                function r(r) {
                    return e.apply(this, arguments)
                }
                return r.toString = function() {
                    return e.toString()
                }
                ,
                r
            }((function(r) {
                function t() {
                    if (share = window.SHARE = window.SHARE || {},
                    share.title = i.decodeEntity(window.SHARE.title || e("meta[property='og:title']").attr("content") || document.title),
                    share.desc = i.decodeEntity(window.SHARE.desc || e("meta[property='og:description']").attr("content")),
                    share.link = window.SHARE.link || location.href,
                    share.imgUrl = window.SHARE.imgUrl || e("meta[property='og:image']").attr("content"),
                    share.success = window.SHARE.success || e.noop,
                    window.CONFIG.uid) {
                        var r = e.cookie("partner_" + CONFIG.appid);
                        "undefined" != typeof r && r && (share.link += (-1 != share.link.indexOf("?") ? "&" : "?") + "pcode=" + r)
                    }
                    return e.each(window.SHARE, (function(r, t) {
                        -1 != e.inArray(r, ["success", "fail", "cancel", "complete"]) && function(e, r) {
                            share[e] = function() {
                                setTimeout(r, 100)
                            }
                        }(r, t)
                    }
                    )),
                    share
                }
                !this.inWechat() || !r && this.shareConfig || (this.shareConfig = !0,
                this.prepare((function(r) {
                    var _ = t();
                    i.wechat.inMiniProgram() ? (_.imgUrl = "undefined" == typeof _.largeImgUrl ? "" : _.largeImgUrl || e("meta[property='og:image-miniprogram']").attr("content"),
                    r.miniProgram.postMessage({
                        data: {
                            share: _
                        }
                    })) : r.ready((function() {
                        r.onMenuShareTimeline(_),
                        r.onMenuShareAppMessage(_),
                        r.onMenuShareQQ(_),
                        r.onMenuShareWeibo(_)
                    }
                    ))
                }
                )))
            }
            )),
            upload: function(r) {
                if (this.inWechat() && "function" == typeof r.success && r.from) {
                    r = e.extend({
                        count: 1,
                        sizeType: ["compressed"],
                        sourceType: ["album", "camera"],
                        progress: 1,
                        before: e.noop,
                        after: e.noop,
                        cancel: e.noop
                    }, r)
                }
            }
        },
        Kp.Cookie = {
            _IsValidKey: function(e) {
                return new RegExp('^[^\\x00-\\x20\\x7f\\(\\)<>@,;:\\\\\\"\\[\\]\\?=\\{\\}\\/\\u0080-\\uffff]+$').test(e)
            },
            GetRaw: function(e) {
                if (this._IsValidKey(e)) {
                    var r = new RegExp("(^| )" + e + "=([^;]*)(;|$)")
                      , t = r.exec(document.cookie);
                    if (t)
                        return t[2] || null
                }
                return null
            },
            Get: function(e) {
                var r = this.GetRaw(e);
                return "string" == typeof r ? (r = decodeURIComponent(r),
                r) : null
            },
            SetRaw: function(e, r, t) {
                if (this._IsValidKey(e)) {
                    t = t || {};
                    var _ = t.expires;
                    "number" == typeof t.expires && (_ = new Date,
                    _.setTime(_.getTime() + t.expires)),
                    document.cookie = e + "=" + r + (t.path ? "; path=" + t.path : "") + (_ ? "; expires=" + _.toGMTString() : "") + (t.domain ? "; domain=" + t.domain : "") + (t.secure ? "; secure" : "")
                }
            },
            Set: function(e, r, t) {
                this.SetRaw(e, encodeURIComponent(r), t)
            },
            Remove: function(e, r) {
                r = r || {},
                r.expires = new Date(0),
                this.SetRaw(e, "", r)
            }
        },
        Kp.Array = {
            inArray: function(e, r) {
                return underscore__WEBPACK_IMPORTED_MODULE_9___default.a.indexOf(r, e) > -1
            },
            intersect: function(e, r) {
                var t = this
                  , _ = [];
                return $(e).each((function(e, n) {
                    t.inArray(n, r) && _.push(n)
                }
                )),
                _
            },
            removeValue: function(e, r) {
                this.removeIndex(underscore__WEBPACK_IMPORTED_MODULE_9___default.a.indexOf(r, e), r)
            },
            removeIndex: function(e, r) {
                r.splice(e, 1)
            },
            movePre: function(e, r) {
                var t = $.inArray(e, r);
                return r.splice(t, 1),
                r.splice(t - 1, 0, e),
                r
            },
            moveNext: function(e, r) {
                var t = $.inArray(e, r);
                return r.splice(t, 1),
                r.splice(t + 1, 0, e),
                r
            }
        },
        Kp.String = {
            endWith: function(e, r) {
                var t = e.length - r.length;
                return t >= 0 && e.lastIndexOf(r) == t
            }
        },
        Kp.Object = {
            Clone: function(e) {
                var r = e.constructor === Array ? [] : {};
                if ("object" === Object(_home_biu_svnfile_h5_qq_node_modules_babel_runtime_corejs2_helpers_esm_typeof__WEBPACK_IMPORTED_MODULE_5__["a"])(e) || "function" === typeof e) {
                    for (var t in e)
                        r[t] = "object" === Object(_home_biu_svnfile_h5_qq_node_modules_babel_runtime_corejs2_helpers_esm_typeof__WEBPACK_IMPORTED_MODULE_5__["a"])(e[t]) ? Kp.Object.Clone(e[t]) : e[t];
                    return r
                }
            },
            DeepClone: function(e) {
                var r = JSON.stringify(e);
                return JSON.parse(r)
            }
        },
        Kp.Utils = {
            Guid: function() {
                return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, (function(e) {
                    var r = 16 * Math.random() | 0
                      , t = "x" === e ? r : 3 & r | 8;
                    return t.toString(16)
                }
                ))
            },
            UrlToJSON: function(e) {
                if (!e)
                    return {};
                var r, t, _, n = {}, a = e.split("&");
                for (r = 0,
                _ = a.length; r < _; r++)
                    t = a[r].split("="),
                    n[t[0]] = decodeURIComponent(t[1]);
                return n
            },
            JsonToUrl: function(e) {
                if (!e)
                    return "";
                var r, t = [];
                for (r in e)
                    e.hasOwnProperty(r) && t.push(r + "=" + encodeURIComponent(e[r]));
                return t.join("&")
            },
            dateFormat: function(e, r) {
                var t = e
                  , _ = {
                    "M+": t.getMonth() + 1,
                    "d+": t.getDate(),
                    "h+": t.getHours() % 12 == 0 ? 12 : t.getHours() % 12,
                    "H+": t.getHours(),
                    "m+": t.getMinutes(),
                    "s+": t.getSeconds(),
                    "q+": Math.floor((t.getMonth() + 3) / 3),
                    S: t.getMilliseconds()
                }
                  , n = {
                    0: "日",
                    1: "一",
                    2: "二",
                    3: "三",
                    4: "四",
                    5: "五",
                    6: "六"
                };
                for (var a in /(y+)/.test(r) && (r = r.replace(RegExp.$1, (t.getFullYear() + "").substr(4 - RegExp.$1.length))),
                /(E+)/.test(r) && (r = r.replace(RegExp.$1, (RegExp.$1.length > 1 ? RegExp.$1.length > 2 ? "星期" : "周" : "") + n[t.getDay() + ""])),
                _)
                    new RegExp("(" + a + ")").test(r) && (r = r.replace(RegExp.$1, 1 == RegExp.$1.length ? _[a] : ("00" + _[a]).substr(("" + _[a]).length)));
                return r
            },
            timestampFormat: function(e, r) {
                return e = new Date(1e3 * e),
                this.dateFormat(e, r)
            },
            curTimeFormat: function(e) {
                var r = new Date;
                return this.dateFormat(r, e)
            },
            getBaseUrl: function() {
                return window.location.origin + window.location.pathname
            },
            getCurUrl: function() {
                return window.location.href.split("#")[0]
            },
            isIOS: function() {
                var e = navigator.userAgent;
                return !!e.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/)
            },
            getScrollTop: function() {
                return document.documentElement.scrollTop || document.body.scrollTop || window.pageYOffset
            }
        },
        window._Kp = Kp,
        __webpack_exports__["a"] = Kp
    },
    f928: function(e, r, t) {
        "use strict";
        t("6b54");
        var _ = t("3e09")
          , n = "userToken"
          , a = "comAlias";
        r["a"] = {
            clearCommunityAlias: function(e) {
                localStorage.removeItem(a)
            },
            setCommunityAlias: function(e) {
                e && localStorage.setItem(a, e)
            },
            getCommunityAlias: function(e) {
                return localStorage.getItem(a) || ""
            },
            clearUserToken: function() {
                _["a"].Cookie.Remove(n)
            },
            getUserToken: function() {
                return _["a"].Cookie.Get(n)
            },
            isLogin: function() {
                var e = this.getUserToken();
                return !!e
            },
            isAuth: function() {
                return USER_INFO && USER_INFO.headimgurl.length > 10
            }
        }
    }
}]);
