/**
 * 后台JS主入口
 */

var layer = layui.layer,
element = layui.element,
laydate = layui.laydate,
upload = layui.upload,
laytpl = layui.laytpl,
form = layui.form;

/**
 * jquery
 */
$(function() {
    /**
     * AJAX全局设置
     */
    $.ajaxSetup({
        type: 'post',
        dataType: 'json'
    });
    /**
     * 通用单图上传
     */
    if ($('.upload-cms').length > 0) {
        var upload_type = '';
        var uploadIndex;
        var uploadInit = upload.render({
            elem: '.upload-cms',
            before: function(obj) {
                uploadIndex = layer.load(2);
                var item = this.item;
                upload_type = $(item).data('type');
                uploadInit.config.data.fileType = upload_type;
                //console.log(upload_type);
            },
            url: '/index.php/user/upload/index/',
            done: function(json, index, upload) {
                layer.close(uploadIndex);
                var item = this.item;
                var path = $(item).attr('data-path');
                if (json.err == '') {
                    $('#' + path).val(json.msg.url);
                } else {
                    layer.msg(json.err);
                }
            },
            error: function(index, upload) {
                layer.close(uploadIndex);
            }
        });
    }
    /**
     * 通用日期时间选择
     */
    if ($('.datetime').length > 0) {
        lay('.datetime').each(function() {
            var format = $(this).data('format');
            var dateType = $(this).data('type');
            if (format == undefined) {
                format = 'yyyy-MM-dd HH:mm:ss';
            }
            if (dateType == undefined) {
                dateType = 'datetime';
            }
            laydate.render({
                elem: this,
                trigger: 'click',
                calendar: true,
                format: format,
                type: dateType,
                theme: 'grid'
            });
        });
    }
    /**
     * 通用颜色选择
     */
    if ($('.colorkey').length > 0) {
        $('.colorkey').colorpicker({
            fillcolor: true
        });
    }
    /**
     * 通用表单提交(AJAX方式)
     */
    form.on('submit(*)', function(data) {
        var formAjaxIndex;
        $.ajax({
            url: data.form.action,
            type: data.form.method,
            beforeSend: function() {
                formAjaxIndex = layer.msg('数据处理中', {
                    time: 0,
                    icon: 16,
                    shade: [0.3, '#393D49'],
                    scrollbar: false
                });
            },
            data: $(data.form).serialize(),
            success: function(json) {
                layer.close(formAjaxIndex);
                switch (json.code) {
                case 1:
                    layer.msg(json.msg, {
                        time: 2000
                    }, function() {
                        if (json.url == '' || json.url == null) {
                            location.reload();
                        } else {
                            location.href = json.url;
                        }
                    });
                    break;
                case 2:
                    parent.layer.closeAll();
                    break;
                case 3:
                    location.reload();
                    break;
                case 4:
                    parent.location.reload();
                    break;
                case 5:
                    layer_show('登录', json.url, 750, 500);
                    break;
                default:
                    layer.msg(json.msg);
                }
            }
        });
        return false;
    });

    /**
     * 通用Ajax执行
     */
    if ($('.ajax-exec').length > 0) {
        $('.ajax-exec').on('click', function() {
            var _href = $(this).attr('href');
            $.ajax({
                url: _href,
                type: 'get',
                success: function(json) {
                    //console.log(json);
                    //return;
                    switch (json.code) {
                    case 1:
                        layer.msg(json.msg, {
                            time: 2000
                        }, function() {
                            if (json.url == '' || json.url == null) {
                                location.reload();
                            } else {
                                location.href = json.url;
                            }
                        });
                        break;
                    case 2:
                        parent.layer.closeAll();
                        break;
                    case 3:
                        location.reload();
                        break;
                    case 4:
                        parent.location.reload();
                        break;
                    default:
                        layer.msg(json.msg);
                    }
                }
            });
            return false;
        });
    }

    /**
     * 通用批量处理（启用、推荐、置顶、删除）
     */
    if ($('.ajax-action').length > 0) {
        $('.ajax-action').on('click', function() {
            var _action = $(this).data('action');
            layer.open({
                shade: false,
                content: '确定执行此操作？',
                btn: ['确定', '取消'],
                yes: function(index) {
                    $.ajax({
                        url: _action,
                        data: $('.ajax-form').serialize(),
                        success: function(json) {
                            if (json.code == 0) {
                                layer.msg(json.msg);
                            } else {
                                layer.msg(json.msg, {
                                    time: 2000
                                },
                                function() {
                                    location.reload();
                                    //location.href = json.url;
                                });
                            }
                        }
                    });
                    layer.close(index);
                }
            });
            return false;
        });
    }
    /**
     * 通用批量处理（排序）
     */
    if ($('.ajax-post').length > 0) {
        $('.ajax-post').on('click', function() {
            var _action = $(this).data('action');
            $.ajax({
                url: _action,
                data: $('.ajax-form').serialize(),
                success: function(json) {
                    if (json.code == 0) {
                        layer.msg(json.msg);
                    } else {
                        layer.msg(json.msg, {
                            time: 2000
                        },
                        function() {
                            location.reload();
                            //location.href = json.url;
                        });
                    }
                }
            });
            return false;
        });
    }
    /**
     * 通用全选
     */
    form.on('checkbox(allChoose)', function(data) {
        var child = $(data.elem).parents('table').find('tbody input.chk-ids');
        child.each(function(index, item) {
            item.checked = data.elem.checked;
        });
        form.render('checkbox');
    });
    /**
     * 通用删除
     */
    if ($('.ajax-delete').length > 0) {
        $('.ajax-delete').on('click', function() {
            var _href = $(this).attr('href');
            layer.open({
                shade: false,
                content: '确定删除？',
                btn: ['确定', '取消'],
                yes: function(index) {
                    $.ajax({
                        url: _href,
                        type: 'get',
                        success: function(json) {
                            if (json.code == 0) {
                                layer.msg(json.msg);
                            } else {
                                layer.msg(json.msg, {
                                    time: 2000
                                },
                                function() {
                                    location.reload();
                                });
                            }
                            layer.msg(json.msg);
                        }
                    });
                    layer.close(index);
                }
            });
            return false;
        });
    }
});

function GoBack() {
    window.history.go(-1);
}
function layer_show(title, url, w, h) {
    if (title == null || title == '') {
        title = false;
    };
    if (w == null || w == '') {
        w = ($(window).width() - 50);
    };
    if (h == null || h == '') {
        h = ($(window).height() - 50);
    };
    var id = 'layer_' + w + '_' + h;
    layer.open({
        id: id,
        type: 2,
        area: [w + 'px', h + 'px'],
        scrollbar: false,
        shade: 0.4,
        title: title,
        content: url
    });
}
function getHits(id, objId, objInfo) {
    if ($('#' + objId).length > 0) {
        $.ajax({
            type: 'POST',
            url: '/api/content/hits',
            data: {
                id: id
            },
            dataType: 'json',
            success: function(json) {
                if (json.code == 1) {
                    var infoString = objInfo == '' ? json.hits: json.hits + objInfo;
                    $('#' + objId).html(infoString);
                }
            }
        });
    }
}
// id 内容ID
// answerCountId 回答ID
// commentCountId 评论ID
// showListId 显示列表ID
function getComment(isMobile, id, answerCountId, commentCountId, showListId) {
    if ($('#' + showListId).length > 0) {
        $.ajax({
            type: 'POST',
            url: '/api/comment/index',
            data: {
                id: id,
                isMobile: isMobile
            },
            dataType: 'json',
            success: function(json) {
                if (json.code == 1) {
                    if ($('#' + answerCountId).length > 0) {
                        $('#' + answerCountId).html(json.answer_count);
                    }
                    if ($('#' + commentCountId).length > 0) {
                        $('#' + commentCountId).html(json.comment_count);
                    }
                    $('#' + showListId).html(json.html);
                }
            }
        });
    }
}
function getPageName() {
    var a = location.href;
    var b = a.split("/");
    var c = b.slice(b.length - 1, b.length).toString(String).split(".");
    return c.slice(0, 1);
}