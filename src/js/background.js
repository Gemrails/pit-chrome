import { postCliper } from './utils';

class Background {
    constructor() {
        this.admin_name = '';
        this.selectionObj = null;
        this._handleMenuClick = this._handleMenuClick.bind(this);
    }

    initial() {
        chrome.storage.sync.get('user', (result) => {
            if(!!result){
                this.admin_name = result.user
            }
        });
        this._initialContextMenus();
        this._listenMessage();
        this._listenStorage();
    }

    _sendSuccessMessage(title) {
        chrome.tabs.query(
            {active: true, currentWindow: true},
            (tabs) => {
                chrome.tabs.sendMessage(tabs[0].id,
                    {
                        method: 'add_cliper_success',
                        data: title
                    }, (response) => {

                    });
            }
        );
    }

    _addTagBeforePostCliper() {
        return new Promise((resolve, reject) => {
            const message = {
                method: 'add_tag',
                data: {}
            }
            chrome.tabs.query(
                {active: true, currentWindow: true},
                (tabs) => {
                    chrome.tabs.sendMessage(tabs[0].id, message, (response) => {
                        resolve(response)
                    });
                }
            );
        })
    }

    _postCliper(pageData) {
        const cliper = {
            text: pageData.text,
            title: pageData.title,
            url: pageData.url,
            admin_name: this.admin_name || 'xxxxxx',
            tags: pageData.tags
        }

        postCliper({cliper}).then(res => {
            this._sendSuccessMessage(this.selectionObj.title)
            this.selectionObj = null;
        }, err => {
            console.error(err)
        });
    }

    _handleMenuClick(info) {
        if (info.menuItemId === 'save_page') {
            this._addTagBeforePostCliper().then(data => {
                this._postCliper(data);
            })
        }

        if(info.menuItemId === 'save_selection') {
            this._postCliper(this.selectionObj);
        }
    }

    _initialContextMenus() {
        chrome.runtime.onInstalled.addListener(() => {
            chrome.contextMenus.create({
                type: 'normal',
                title: 'save page',
                id: 'save_page'
            });
            chrome.contextMenus.create({
                type: 'normal',
                title: 'save selection',
                id: 'save_selection',
                contexts: ['selection']
            });
        });
        chrome.contextMenus.onClicked.addListener(this._handleMenuClick);
    }

    _listenStorage() {
        chrome.storage.onChanged.addListener((changes, namespace) => {
            Object.keys(changes).forEach((key) => {
                if (key === 'user') {
                    // do nothing
                }
            });
        });
    }

    _listenMessage() {
        chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
            if (message.method === 'get_selection') {
                this.selectionObj = message.data;
            }
        });
    }
}

export default Background;
