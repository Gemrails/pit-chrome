class Notification {
    constructor(){
        this.currentMsg = null;
        this.tags = []
    }

    listen() {
        chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
            if (message.method === 'add_cliper_success') {
                this._showNotification(message.data);
            }
            if (message.method === 'add_tag') {
                this._showTagAdder().then(res => {
                    if(res.length){
                        sendResponse(res)
                    }
                })
            }
            return true
        });
    }

    notificationTemplate(title) {
        return `<div class='cliper_notification active'><div class='notification_title'>成功添加摘记，收录在：</div><a class='notification_content' href="http://cliper.com.cn" target="_blank">${title}</a></div>`;
    }

    _showNotification(title) {
        const $notification = $(this.notificationTemplate(title));
        $('body').append($notification);
        $notification.addClass('active');
        setTimeout(() => {
            this._removeNotification($notification);
        }, 3500);
    }

    _removeNotification($target) {
        $target.removeClass('active');
        setTimeout(() => {
            $target.remove();
        }, 500);
    }

    tagTemplate() {
        return `<div id="tag_temp" class='cliper_notification'><input name="tags" id="tags" value="" /><div class="btn_con"><button id="confirm">确定</button><button id="cancel">取消</button></div></div>`
    }

    _showTagAdder() {
        const query = document.getElementById('tags');
        if(!query){
            const $tagTemp = $(this.tagTemplate());
            $('body').append($tagTemp);
            $tagTemp.addClass('active');
            $('#tags').tagsInput({
                onAddTag: (res) => {
                    this.tags.push(res)
                },
                onRemoveTag: (res) => {
                    this.tags.splice(this.tags.indexOf(res), 1)
                }
            });
            $('#confirm').click(() => {
                this._AdderCallBack('confirm')
            })
            $('#cancel').click(() => {
                this._AdderCallBack('cancel')
            })
        }
        return new Promise((resolve, reject) => {
            this.currentMsg = {
                resolve,
                reject
            }
        })
    }

    _AdderCallBack(action) {
        console.log(`action is ${action}`)
        if (action === 'confirm') {
            this.currentMsg.resolve(this.tags)
            this.tags = []
        } else {
            this.currentMsg.resolve(false)
        }
    }

    _removeTagAdder() {
        $('#tag_temp').removeClass('active');
        setTimeout(() => {
            $('#tag_temp').remove();
        }, 500);
    }
}

export default Notification;
