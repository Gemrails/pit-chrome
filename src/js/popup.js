import {
    signupOrLogin,
    getValidateEmail,
    getValidatePassword
} from './utils';

class Popup {
    constructor() {
        this._fetchUserInfo();
        this._signUp = this._signUp.bind(this);
        this._login = this._login.bind(this);
        this._submit = this._submit.bind(this);
    }

    initialDOM() {
        this._bindAction();
        return this;
    }

    _fetchUserInfo() {
        chrome.storage.sync.get('user', (result) => {
            if (result) {
                this._setPopDOM(result.user)
            }
        });
    }

    _bindAction() {
        // signup
        // document.getElementById('cliper_signup').onclick = () => {
        //     this._submit(this._signUp);
        // }
        // login
        document.getElementById('cliper_login').onclick = () => {
            this._submit(this._login);
        }
        // logout
        document.getElementById('cliper_logout').onclick = () => {
            this._logout();
        }
    }

    _submit(func) {
        const name = getValidateEmail('cliper_email');
        const password = getValidatePassword('cliper_password');
        if (name) {
            $('#cliper_email').removeClass('error');
        } else {
            $('#cliper_email').addClass('error');
            return;
        }
        if (password) {
            $('#cliper_password').removeClass('error');
        } else {
            $('#cliper_password').addClass('error');
            return;
        }
        this._toggleLoading(true);
        func(name, password);
    }

    _signUp(name, password) {
        const data = {
            name,
            password
        };
        this._userSignupOrLogin('', data, name);
    }

    _login(name, password) {
        const data = {
            name,
            password
        };
        this._userSignupOrLogin('user/loginSubmit', data, name);
    }

    _logout() {
        chrome.storage.sync.set({user: null}, () => {
            this._setPopDOM(null);
        });
    }

    _userSignupOrLogin(url, data, admin_name) {
        signupOrLogin(url, data).then((user) => {
            chrome.storage.sync.set({user: admin_name}, (result) => {
                this._setPopDOM(admin_name);
            });
            this._toggleLoading(true);
        }).catch((err) => {
            this._toggleLoading(false);
        });
    }

    _setPopDOM(admin_name) {
        console.log(admin_name)
        const userform = document.getElementById('cliper_userform');
        const userinfo = document.getElementById('cliper_userinfo');
        if (admin_name) {
            userform.className = "disabled";
            userinfo.className = "active";
            $('.user_name').text(admin_name);
        } else {
            userform.className = "active";
            userinfo.className = "disabled";
        }
        this._toggleLoading(false);
    }

    _toggleLoading(loading) {
        const cliperContainer = document.querySelector('.cliper_container');
        if (loading) {
            cliperContainer.className = 'cliper_container active';
        } else {
            cliperContainer.className = 'cliper_container';
        }
    }
}

export default Popup;
