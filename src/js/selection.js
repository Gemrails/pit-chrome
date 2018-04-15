import keyboardJS from 'keyboardjs';

class Selection {
  _getSelectedText() {
    if (window.getSelection) {
      return window.getSelection().toString();
    } else if (document.getSelection) {
      return document.getSelection();
    } else if (document.selection) {
      return document.selection.createRange().text;
    }
  }

  _getSelectionMessage() {
    const text = this._getSelectedText();
    const title = document.title;
    const url = window.location.href;
    const data = {
      text: this._base64Encode(text),
      title: this._base64Encode(title),
      url: this._base64Encode(url)
    };
    let message = {
      method: 'get_selection',
      data: data
    }
    if (!text) {
      message['method'] = 'get_page';
      data.text = $("html").html();
    }
    return message;
  }

  _base64Encode(text) {
    // var b = new Buffer(text)
    // return b.toString('base64');
    return text
  }

  _sendSelectionMessage(message) {
    chrome.runtime.sendMessage(message, (response) => {});
  }

  listenKeyDown() {
    keyboardJS.bind('command + shift + s', (e) => {
      const message = this._getSelectionMessage();
      message['method'] = 'save_cliper';
      this._sendSelectionMessage(message);
    });
    return this;
  }

  listenMouseUp() {
    window.onmouseup = (e) => {
      if (!e.button === 2) {
        return;
      }
      const message = this._getSelectionMessage();
      this._sendSelectionMessage(message);
    };
    return this;
  }
}

export default Selection;
